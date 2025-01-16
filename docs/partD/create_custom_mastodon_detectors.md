# Creating custom detectors in Mastodon.

In this developer tutorial we will introduce how to create your own detectors in Mastodon.
Detectors are special Mastodon plugins that are used to detect objects of interest, typically cells, in an image. 
They will be used subsequently for linking and analysis, building cell trajectories and linages. 
Mastodon is like  [TrackMate](https://imagej.net/plugins/trackmate/) and can be extended with new detectors and linkers by third-parties.
It can serve as a platform for you to deploy a novel detection algorithm and benefit from the existing visualization, analysis and IO facilities of Mastodon.

Ideally you should have read the previous tutorial on creating generic [plugins](create_custom_mastodon_plugins.md) in Mastodon.
Custom detectors will use a similar mechanism. 
They are however specialized for the task at hand, which makes writing them a bit more guided.

## The code template.

We will use the same example repository as for the previous tutorial.
You can clone it from:

> [https://github.com/mastodon-sc/mastodon-plugin-example](https://github.com/mastodon-sc/mastodon-plugin-example)

The detector example we will use in this tutorial are in the package:
> `src/main/java/org/mastodon/mamut/example/detection/`

([Or online](https://github.com/mastodon-sc/mastodon-plugin-example/tree/main/src/main/java/org/mastodon/mamut/example/detection).)

You will find three classes there, the purpose of which we will explain shortly.
They implement a dummy detector that creates spots at random locations in the source image.

## The detector class hierarchies.

Two classes are needed for the detector itself:

> `RandomSpotDetectorOp`
> `RandomSpotDetectionExampleMamut`

The `RandomSpotDetectionExampleMamut` is almost empty, while the `RandomSpotDetectorOp` is quite fledged. 

The last class is used for the UI panel:
> `RandomSpotDetectorDescriptor`

We need first to explain why the two classes for one detector.
It is again to achieve some generality and facilitate reuse beyond Mastodon.

You may remember from the [previous dev tutorial](https://mastodon.readthedocs.io/en/latest/docs/partD/create_custom_mastodon_plugins.html#the-interface-to-implement) that we tend to separate code that is generic to the Mastodon API, and code that is specific to the Mastodon application (which is the one users see).
We suffixed everything specific to the Mastodon app with `Mamut`.
Normally we also put them in the package `org.mastodon.mamut`, while everything that is generic and not specific to tracking can live in `org.mastodon`.
Here we did the same: `RandomSpotDetectorOp` is generic and `RandomSpotDetectionExampleMamut` uses it to make it specific to the `Spot`s and `Link`s we use in the Mastodon app.

For the hierarchies, it works as follow:

### `DetectorOp`

`RandomSpotDetectorOp` implements `DetectorOp`.
It is a SciJava "op" that accepts:
- a `DetectionCreatorFactory`, which will be use to actually add the objects this detector will find in the source image,
- and a `List< SourceAndConverter< ? > > sources` which represents the input image. The list represents the possibly multiple channels or sources in BDV linguo.

### `SpotDetectorOp`

`RandomSpotDetectionExampleMamut` implements `SpotDetectorOp`.
It is also a SciJava op, but accepts:
- the `List< SourceAndConverter< ? > > sources`,
- and the `ModelGraph graph` which is the Mastodon app data structure to which the spots will be added. 

We will see later how to link the two. 
This is basically simply reusing the existing facilities in a nice base abstract class.
But for now let's focus on the main actor of the detection, the detector op.

## Writing a generic detector.

We will be writing the `RandomSpotDetectorOp` class. 
It is supposed to be generic, that is, be able to detect objects and add them to *any* kind of data structure. 
Which means that the code of this class is supposed to receive an image, and yield a list of coordinates.
In our example they will random.

It is simpler and faster to inherit from a convenient abstract class for the detectors you want to write: `AbstractDetectorOp`.
Hence, our detector class will start with:

```java
@Plugin( type = DetectorOp.class )
public class RandomSpotDetectorOp extends AbstractDetectorOp implements DetectorOp
{
	// ...
```

The `@Plugin( type = DetectorOp.class )` annotation will make the detector discoverable by Mastodon.
This inheritance leaves us with only one method to implement:

```java
	@Override
	public void mutate1( final DetectionCreatorFactory detectionCreatorFactory, final List< SourceAndConverter< ? > > sources )
	{
		// ...
```
The abstract class `AbstractDetectorOp` we inherit provides several useful fields that are used to store settings, communicate success or failure with an error message, or sends messages to the user interface.
The first one is the `ok` flag, that states whether the computation finished successfully. 
If not, a meaningful error message should be provided in the `errorMessage` field. The user interface will use them.

We start by settings the `ok` flag to false. 
If we break before the end, this will signal something wrong happened.

```java
		ok = false;
```

And we clear the status display.

``` java
		statusService.clearStatus();
```

### Reading the settings map, and check validity.

The parameters used to configure your detector will be stored in a `Map< String, Object > settings` map.
The keys of the map are strings containing a key to a parameter (e.g. `"N_SPOTS"`) and the values are the corresponding parameter value (e.g. `3`; `1.5`; `true`, etc.).
The first task is to check that these settings are present and valid:

The `settings` variable (stored in the mother abstract class) is such a map, that will be passed with all the settings the user will specify, either programmatically or in the wizard. 
For our dummy detector example, we have 5 parameters: 

1. the number of spots we will create,
2. their radius,
3. with respect to what source of channel, 
4. and 5. the min and max time-points we will process.

To check that they are present in the map and of the right class, we use a utility function defined in `LinkingUtils` that accepts the settings map, the key of the parameter to test, its desired class, and a holder to store error messages. It goes like this:

In the import list:
```java
import static org.mastodon.tracking.detection.DetectorKeys.KEY_MAX_TIMEPOINT;
import static org.mastodon.tracking.detection.DetectorKeys.KEY_MIN_TIMEPOINT;
import static org.mastodon.tracking.detection.DetectorKeys.KEY_RADIUS;
import static org.mastodon.tracking.detection.DetectorKeys.KEY_SETUP_ID;
import static org.mastodon.tracking.linking.LinkingUtils.checkParameter;
```

In the method:
```java
		final StringBuilder errorHolder = new StringBuilder();
		boolean good = true;
		good = good & checkParameter( settings, KEY_N_SPOTS, Integer.class, errorHolder );
		good = good & checkParameter( settings, KEY_RADIUS, Double.class, errorHolder );
		good = good & checkParameter( settings, KEY_SETUP_ID, Integer.class, errorHolder );
		good = good & checkParameter( settings, KEY_MIN_TIMEPOINT, Integer.class, errorHolder );
		good = good & checkParameter( settings, KEY_MAX_TIMEPOINT, Integer.class, errorHolder );
		if ( !good )
		{
			errorMessage = errorHolder.toString();
			return;
		}
		// Now we are sure that they are here, and of the right class.

		final int n = ( int ) settings.get( KEY_N_SPOTS );
		final int minTimepoint = ( int ) settings.get( KEY_MIN_TIMEPOINT );
		final int maxTimepoint = ( int ) settings.get( KEY_MAX_TIMEPOINT );
		final int setup = ( int ) settings.get( KEY_SETUP_ID );
		final double radius = ( double ) settings.get( KEY_RADIUS );

		// Extra checks.
		if ( n < 1 )
		{
			errorMessage = "The parameter " + KEY_N_SPOTS + " has a value lower than 1: " + n;
			return;
		}
		if ( radius <= 0 )
		{
			errorMessage = "Radius is equal to or smaller than 0: " + radius;
		}
		if ( setup < 0 || setup >= sources.size() )
		{
			errorMessage = "The parameter " + KEY_SETUP_ID + " is not in the range of available sources ("
					+ sources.size() + "): " + setup;
			return;
		}
		if ( maxTimepoint < minTimepoint )
		{
			errorHolder.append( "Min time-point should smaller than or equal to max time-point, be was min = "
					+ minTimepoint + " and max = " + maxTimepoint + "\n" );
			return;
		}
```

Now we are sure that the parameters we need are here, and of the right class.

### Loop over all time-points and detect objects.

Now we move on to the processing of the image. 
Not in our case actually, because the dummy detector we write creates spots randomly. 
You would normally need to use `imglib2` to process the image, and as such, know how to use `imglib2`. 
Here will just use it to get the size of the input image so that we create random spots within its bounds.

The detector interface we implement requires that we process the whole time-lapse. 
It is up to us to decide whether we want to process multiple time-points in parallel or not. 
In Mastodon case, I would humbly recommend processing one time-point at a time, and allocating all threads to this time-point.
Single time-point images can be very large in Mastodon, and you run the risk to saturate your computer RAM if you process them in parallel, as they are loaded lazily.

So in our case, the beginning of this section starts like this:

```java

		final Random ran = new Random();

		// The `statusService` can be used to show short messages.
		statusService.showStatus( "Creating random spots." );
		for ( int tp = minTimepoint; tp <= maxTimepoint; tp++ )
		{
			// We use the `statusServive to show progress.
			statusService.showProgress( tp - minTimepoint + 1, maxTimepoint - minTimepoint + 1 );

			/*
			 * The detection process can be canceled. For instance, if the user
			 * clicks on the 'cancel' button, this class will be notified via
			 * the `isCanceled()` method.
			 * 
			 * You can check if the process has been canceled as you wish (you
			 * can even ignore it), but we recommend checking every time-point.
			 */
			if ( isCanceled() )
				break; // Exit but don't fail.

			/*
			 * Important: With the image data structure we use, some time-points
			 * may be devoid of a certain source. We need to test for this, and
			 * should it be the case, to skip the time-point.
			 * 
			 * Again, there is a utility function to do this:
			 */
			if ( !DetectionUtil.isPresent( sources, setup, tp ) )
				continue;
```

Now let's move to the image processing part. 
We now that there is an image or a _source_ for the setup (or channel) and time-point we requested.
This source has possibly several resolution levels, as explained in the part A of the documentation.
And for your own real detector, it might be very interesting to work on a lower resolution (higher level). 
Check the [DogDetectorOp](https://github.com/mastodon-sc/mastodon-tracking/blob/master/src/main/java/org/mastodon/tracking/detection/DoGDetectorOp.java) code for instance.
For us, we don't even care for pixels, we just want to have the image boundary from the highest resolution (level 0).

```java
			final int level = 0;
			final RandomAccessibleInterval< ? > image = source.getSource( tp, level );
			/*
			 * This is the 3D image of the current time-point, specified
			 * channel. It always 3D. If the source is 2D, the 3rd dimension
			 * will have a size of 1.
			 */

			// The image bounds. It might be different for every time-point.
			final int[] mins = Intervals.minAsIntArray( image );
			final int[] maxs = Intervals.maxAsIntArray( image );
```

Now let's create N random points within these bounds.

``` java
			final List< double[] > points = new ArrayList<>( n );
			for ( int i = 0; i < n; i++ )
			{
				final double x = mins[ 0 ] + ran.nextDouble() * ( maxs[ 0 ] - mins[ 0 ] );
				final double y = mins[ 1 ] + ran.nextDouble() * ( maxs[ 1 ] - mins[ 1 ] );
				final double z = mins[ 2 ] + ran.nextDouble() * ( maxs[ 2 ] - mins[ 2 ] );
				final double[] pos = new double[] { x, y, z };
				points.add( pos );
			}
```

### The detection creator factory design.

We have now to create the `Spot` objects corresponding to these detections to the model.

To simplify doing so, the detection framework uses a factory, that can be configured elsewhere, and that provides facilities to add new spots in a safe way. 
It is the second argument of the `mutate1` method we implement. 
It has only one useful method, that creates a spot adder for the current time-point.

```java
			final DetectionCreator spotAdder = detectionCreatorFactory.create( tp );
```

This spot adder is actually important. It is the medium through which we offer *generalisability*.

Indeed, notice that we did not use any of the class specific to the _Mamut_ application in this class: there is no mention of the `Spot` class nor to the `Model` class. 
Yet we will need to create `Spot` objects from the detections and add them to the `Model`
instance of the data. 
This is what the `spotAdder` does.

The one we use in the Mamut application takes the detection, creates spots from them and add them to the model. 
We could have made another design devoid of the `spotAdder` and the `detectionCreatorFactory`, directly using the `Model` class. 
But we wanted to make it possible to reuse any of the detector we built for Mastodon with other application type.

For instance, if someone wants to make a new application with the Mastodon code, but that does not use the Mamut classes, they can reuse directly the all the code under the
`org.mastodon.tracking.detection` package for detection. 
They will have to implement a `DetectionCreatorFactory` specific to their application, that will know how to add detections to their specific model.
But the actual detector code can be reused as is with this design.

We already use the flexibility of this design in the Mamut application, with several implementations of the `DetectionCreatorFactory` interface.
The "Advanced DoG detector" offers a special option to configure the behavior of the
detector, when a spot is found where another already exists. 
The user can specify whether they want to add it on top of the existing one, skip adding the new spot, replace the existing one, or remove all existing spots before detection (the default). 
This is simply done with several implementations of `DetectionCreatorFactory` that know how to perform each of these behaviors.

Also: the detections are have now are just points. 
Their position is stored in pixel units, in the reference frame of the source.
But each source might be rotated, translated, etc. 
And this might change for every time-point and source. 
So before creating spots we need to transform these points in the global coordinate system.

This is done with an `AffineTransform3D`, also stored in the source. 
There is a utility method to extract it for the current source, time-point and level:

```java
			final AffineTransform3D transform = DetectionUtil.getTransform( sources, tp, setup, level );
```

Coming back to the `spotAdder`. 
Adding spots must be done within a block calling the following methods in order:

``` java
			spotAdder.preAddition();
			try {
					// Detect objects and transform their position.
					...
					spotAdder.createDetection( pos, radius, quality );
			}
			finally
			{
					spotAdder.postAddition();
			}
```

The `preAddition()` and `postAddition()` contain any task that must  be performed before and after adding detection to the model in batch. 
In our case implementing this results into:

```java
			spotAdder.preAddition();
			try
			{
				for ( final double[] point : points )
				{
					/*
					 * The transform "goes" from the pixel coordinate to the
					 * global coordinate system. We can get the "world"
					 * coordinates of our detection this way:
					 */
					final double[] worldCoords = new double[ 3 ];
					transform.apply( point, worldCoords );

					/*
					 * `worldCoords` now contains the coordinate of the
					 * detection, in physical units, in the global reference
					 * frame. We can now create the `Spot` object from these
					 * coordinates, using the `spotAdder` we created above. It
					 * requires a `quality` value, for which we use a dummy
					 * random value as well.
					 */
					final double quality = ran.nextDouble();
					spotAdder.createDetection( worldCoords, radius, quality );
				}
			}
			finally
			{
				spotAdder.postAddition();
			}
		}
```

We are done!
Gracefully exit, stating we are ok.

``` java
		ok = true;
	} // end of the mutate1 method.
```

That's it for the `RandomSpotDetectorOp` class.
This is enough to write a generic detector.

## Writing a detector for the Mastodon app.

Now we want to write the part specific to the Mastodon 'Mamut' app. 
This is done in the `RandomSpotDetectionExampleMamut` class, which has a separate hierarchy. 
But by implementing a convenient abstract class, the code can be made really short:

```java
@Plugin( SpotDetectorOp.class, priority = Priority.LOW, name = "Random detector",
		description = "<html>"
				+ "This example detector generates a fixed number of spots at random "
				+ "locations."
				+ "<p>"
				+ "It is only used as an example to show how to implement a custom "
				+ "detector in Mastodon."
				+ "</html>" )
public class RandomSpotDetectionExampleMamut extends AbstractSpotDetectorOp
```

We also have a `@Plugin` annotation, with a specific hierarchy (`type = SpotDetectorOp.class`).
By extending `AbstractSpotDetectorOp`, we just have two methods to implement:

```java
	@Override
	public void compute( final List< SourceAndConverter< ? > > sources, final ModelGraph graph )
```

Normally, we would need to write the content of this method, instantiating and calling the `RandomSpotDetectorOp` class we just wrote.
But  the mother class contains a convenience `exec` method that makes it simple:

```java
	@Override
	public void compute( final List< SourceAndConverter< ? > > sources, final ModelGraph graph )
	{
		exec( sources, graph, RandomSpotDetectorOp.class );
	}
```
This is enough to create a `RandomSpotDetectorOp` detector, run it on the source image with the configured parameters, and convert its output to `Spot`s. 

The second method is used to specify default settings. 
This is important for Mastodon to discover what parameters are needed, what name they have and what type they accept.
This is done via the method `getDefaultSettings()` method.
You should create a map with all the required parameters for your detectors (and only them) and set a default value of the right class. 
Ideally, if you have parameters that are the same that for the built-in detectors, you should re-use the parameter names and default values for them.

``` java
	@Override
	public Map< String, Object > getDefaultSettings()
	{
		final Map< String, Object > ds = new HashMap< String, Object >();
		ds.put( KEY_SETUP_ID, DEFAULT_SETUP_ID );
		ds.put( KEY_MIN_TIMEPOINT, DEFAULT_MIN_TIMEPOINT );
		ds.put( KEY_MAX_TIMEPOINT, DEFAULT_MAX_TIMEPOINT );
		ds.put( KEY_RADIUS, DEFAULT_RADIUS );
		ds.put( KEY_N_SPOTS, 30 );
		return ds;
	}
} // end of class RandomSpotDetectionExampleMamut
```

That's it.
This is sufficient to plug our detector in the Mastodon app.

The next (big) step is to write a config panel that can be shown in the detection wizard.
But we could also call this detector programmatically.




## Making a user interface for configuring the detector

In Mastodon the main way we run the detection is actually via the wizard UI, that users run with the _Plugins > Tracking > Detection..._ command.
In the third panel of this wizard, Mastodon lists all the detectors it found, _and_ that have a config panel.
For our dummy detector to appear in this list, we need to create such a config panel.
Let's do this.

For the wizard UI, we need to create a 'descriptor'. 
A descriptor is a class that represents a 'card' in the sequence of panels shown by the UI. 
The one we will make has only one responsibility: offer the user to configure the random spot detector, and pass these settings to the detection runner.
For this it creates a UI panel, specific to the detector.
It also has several methods to get and store setting values, and to inform Mastodon about the detector it relates to.

We don't have to go into details here, but it turns out that the class in charge of running the automated detection and linking processes is called [`TrackMate`](https://github.com/mastodon-sc/mastodon-tracking/blob/master/src/main/java/org/mastodon/tracking/mamut/trackmate/TrackMate.java).
It stores the detection and linking settings, and will modify the data model. 
We just have to worry about the detection settings, eveything else is taken care of.

The full class of this descriptor is in the example repository [here](https://github.com/mastodon-sc/mastodon-plugin-example/blob/main/src/main/java/org/mastodon/mamut/example/detection/RandomSpotDetectorDescriptor.java). 
We describe its content below.

First, your descriptor must extend the `SpotDetectorDescriptor` abstract class.
It has several fields and methods that simplify writing a custom one.
Second, the descriptor also uses the SciJava discovery mechanism, so it needs the `@Plugin` annotation, like the two other classes above. 
We will see soon how Mastodon associate a descriptor with the right detector it can configure.

```java
@Plugin( type = SpotDetectorDescriptor.class, name = "Random spot dummy detector configuration descriptor" )
public class RandomSpotDetectorDescriptor extends SpotDetectorDescriptor
{
```

Also this descriptor has only one specific field, the tracking settings to configure:

```java
	private Settings settings;
```

In the descriptor constructor, you need to specify a unique ID, and create the UI panel with the elements to configure the settings

```java
	public RandomSpotDetectorDescriptor()
	{
		/*
		 * A descriptor represents a 'card' in the wizard we have in Mastodon.
		 * For the wizard to run properly, you need to give it a unique
		 * identifier and a UI panel when you create it.
		 */

		this.panelIdentifier = "Configure random spot detector";
		this.targetPanel = new ConfigPanel(); // described just below.
	}
```

The UI panel can be anything you want (it must extend `JPanel`) but we recommend emulating the size, look and feel of the other ones.
For this example we copy / pasted an existing one and removed everything not needed. 
It contains only two `JFormattedTextField` to set the diameter and the number of random spots to create. 

Normally our detector requires more parameters to be configured: we need to tell what channel (setup ID) to run the detection on, the min and max time-point as well. 
But in the wizard, this is actually done in the first two panels, and we don't have to worry about them.

```java

	/*
	 * The UI part, stored as a private static class. We need to show only two
	 * controls that can configure the number of spots we want to generate and
	 * their diameter.
	 */
	private static class ConfigPanel extends JPanel
	{
		// ... see content in the file directly.
	}
```

After that comes the method to handle the wizard process, that is: the user 'moving' in the panel or leaving it.

```java
	@Override
	public void setTrackMate( final TrackMate trackmate )
	{
		/*
		 * This method is called when the panel is shown, when the user 'enters'
		 * the config panel. It receives the instance of TrackMate that will run
		 * the detection, and that this panel needs to configure. We use the
		 * method for two things:
		 * 
		 * 1/ Get the settings map to configure. The TrackMate instance stores
		 * the detector settings in a map. We will need to update it with the
		 * values set by the user on the panel when they 'leave' the panel, so
		 * we store a reference to it in the descriptor.
		 */

		this.settings = trackmate.getSettings();

		/*
		 * 2/ We want to display the detector settings values, either the
		 * default ones, or the one that were set previously. For this, we read
		 * these values from the TrackMate instance we receive.
		 */

		if ( null == settings )
			return;

		// Get the values.
		final Map< String, Object > detectorSettings = settings.values.getDetectorSettings();
		final double diameter;
		final Object objRadius = detectorSettings.get( KEY_RADIUS );
		if ( null == objRadius )
			diameter = 2. * DetectorKeys.DEFAULT_RADIUS;
		else
			diameter = 2. * ( double ) objRadius;

		final int nSpots;
		final Object nSpotsObj = detectorSettings.get( KEY_N_SPOTS );
		if ( null == nSpotsObj )
			nSpots = 30; // default
		else
			nSpots = ( int ) nSpotsObj;

		// Show them in the config panel.
		final ConfigPanel panel = ( ConfigPanel ) targetPanel;
		panel.diameter.setValue( diameter );
		panel.nSpots.setValue( nSpots );
		// Also the spatial units because we are nice.
		final String unit = DetectionUtil.getSpatialUnits( settings.values.getSources() );
		panel.lblDiameterUnit.setText( unit );
	}
```

and when the user click the 'Next' button:

```java

	@Override
	public void aboutToHidePanel()
	{
		/*
		 * This method is run when the user 'leaves' the panel going 'forward'.
		 * This is the step just before running the full detection. The only
		 * thing we have to do is to grab the setting values from the panel, and
		 * store them in the settings instance we got when we entered the panel.
		 */

		if ( null == settings )
			return;

		/*
		 * In the wizard, the settings map should already contain the parameter
		 * values for the target channel and min and max time-point to run the
		 * detector on (KEY_SETUP_ID, KEY_MIN_TIMEPOINT and KEY_MAX_TIMEPOINT).
		 * We just have to add the parameters specific to this detector.
		 */

		// Cast the panel field to the right class.
		final ConfigPanel panel = ( ConfigPanel ) targetPanel;
		// Update settings map for the detector.
		final Map< String, Object > detectorSettings = settings.values.getDetectorSettings();
		detectorSettings.put( KEY_RADIUS, ( ( Number ) panel.diameter.getValue() ).doubleValue() / 2. );
		detectorSettings.put( KEY_N_SPOTS, ( ( Number ) panel.nSpots.getValue() ).intValue() );
	}
```

Then there is a method to tell Mastodon what detector this descriptor can configure:

```java
	@Override
	public Collection< Class< ? extends SpotDetectorOp > > getTargetClasses()
	{
		/*
		 * This method is used to tell Mastodon what detectors this wizard
		 * descriptor can configure. This one is only suitable for our dummy
		 * detector, which yields:
		 */
		return Collections.singleton( RandomSpotDetectionExampleMamut.class );
	}
```

The last method is useful only if you want to do fancy things in your config panel:

```java
	@Override
	public void setAppModel( final ProjectModel appModel )
	{
		/*
		 * This method is used to receive the project model. Other detector
		 * descriptors use it to run a preview of the detection, or to display
		 * information about it.
		 * 
		 * In our case we don't do preview, so we don't need to keep a reference
		 * to the project model. This method does then nothing.
		 */
	}
} // end of class RandomSpotDetectorDescriptor
```

If you add this class, compile it and add the resulting jar to Fiji, this should be enough to have the custom detector appear and run in the wizard UI:

![](../imgs/Mastodon_ExampleDetector_10.png){align="center"}
![](../imgs/Mastodon_ExampleDetector_11.png){align="center"}
![](../imgs/Mastodon_ExampleDetector_12.png){align="center"}
![](../imgs/Mastodon_ExampleDetector_13.png){align="center"}

## Summary and stragegies

What we described here is a means to implement a detector that will work by finding spots on the image:

- `RandomSpotDetectorOp` does the main job of processing the image and generating a list of X,Y,Z coordinates per time-point.
- `RandomSpotDetectionExampleMamut` reuses it to convert these lists to create Mastodon `Spot` object and add them to the data model. It also specifies what parameters are needed to configure the detector.

This is enough the run the detector from scripts.

- `RandomSpotDetectorDescriptor` deals with the user interface and integration inside the tracking wizard.

Using a `DetectorOp` and `SpotDetectorOp` allows to make your detector general and seperate concers (first one performs generic detection, second one takes care about integration into Mastodon data structures).
However you can skip the generic part, and immediately make a detector that would work only for the Mastodon app data structures, by only implementing the `SpotDetectorOp` interface (of better extending the `AbstractSpotDetectorOp` abstract class).
In that case you would do the heavy lifting in the 
```java
public void compute( final List< SourceAndConverter< ? > > sources, final ModelGraph graph )
```
method, process the image and add the created `Spot`s object to the `ModelGraph`.
This would be particularly suitable if you want to use algorithms that do not work by finding X,Y,Z detections, as we did above. 
That would be the case for detectors based on StarDist for instance, that return the shape of objects, and that could be encoded in the `Spot` ellipsoids. 

To go further, do not hesitate to study the builtin detectors, such as the DoG detector to see [how we use imglib2 algorithms to build a detector ](https://github.com/mastodon-sc/mastodon-tracking/blob/master/src/main/java/org/mastodon/tracking/detection/DoGDetectorOp.java) and [how we put a preview button in the UI](https://github.com/mastodon-sc/mastodon-tracking/blob/master/src/main/java/org/mastodon/tracking/mamut/trackmate/wizard/descriptors/DoGDetectorDescriptor.java).

