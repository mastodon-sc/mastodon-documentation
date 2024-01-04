# Mastodon data structures.

Before we discuss how to extend Mastodon with your own plugins, we need to learn a little bit about how Mastodon stores and deal with the data it can visualize and edit.
This page will walk you through the data structure in Mastodon from a Java programmer perspective. 

## The data model.

All the data is aggregated in the [`ProjectModel`](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/ProjectModel.java) class. 
This is the class you will access for instance when you write a plugin, and it contains many things that relate to the image, the tracking data and the user-interface.
We document below its most important components.

### Image data.

The image data is stored in a special class [`SharedBigDataViewerData`](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/views/bdv/SharedBigDataViewerData.java). 
It aggregates several objects and information from the BDV ecosystem.
You can access the list of sources and the `SpimData` objects from it.

```java
SharedBigDataViewerData imageData = projectModel.getSharedBdvData();
AbstractSpimData< ? > spimData = imageData.getSpimData();
List< SourceAndConverter< ? > > imageData.getSources();
```

### Tracking data, the `Model` class.

The tracking data, including the graph, the feature values, tags, etc. are stored in the [`Model`](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/model/Model.java) class.
This is the main class to focus on to interrogate and manipulate tracking data.

```java
Model model = mamutAppModel.getModel();
```

The `model` contains everything about the tracking data, from the individual objects, tracks, tags and numerical feature values. 
It also controls the undo / redo mechanisms.

### The tracking data. The `ModelGraph` class.

The tracks, that is the objects we follow, their shape and position, and how they evolve over time, are stored as a [mathematical graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)).
Precisely, the graph we use in Mastodon is a simple, directed graph: the edges have a direction, and there is at most one edge between two vertices. 
The vertices of the graph are the objects we track: cells or organelles, and they are represented by spots, described below.
One spot, of the `Spot` class represents one cell or one object at one time-point.
The edges of the graph link objects over time. 
They are represented by the `Link` class, also described below.
Two spots `s1` and `s2` that represent the same cell at time-points `t1` and `t2=t1+1` are linked together by an edge that goes from `s1` to `s2` labeled `l1=s1→s2`.
The direction of the edge important. 
In Mastodon, the edges are always oriented forward in time: the source spot of the edge is always in a time-points that is strictly lower than the target spot of the edge.
So there cannot be an edge oriented backward in time, and there cannot be an edge between two spots that are in the same time-point.

The class of the graph we use in Mastodon is [ModelGraph](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/model/ModelGraph.java).
It is based on a special data structure to manage large graphs that we developed specifically for Mastodon, and described [elsewhere in this documentation](../partE/mastodon_graph_data_structure.md).
The graph instance can be obtained as follow:
```java
ModelGraph graph = model.getGraph();
```

This graph class if often required by Mastodon algorithms and plugins, but is not the first entry point to browse and navigate the data from a user point-of view. 
You can access the links of a spot directly with the spot class, and the collections of spots in a time-point via the index.


#### The data objects. The `Spot` class.

The data objects are stored as spots with the [`Spot`](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/model/Spot.java) class. 
A spot is a 3D ellipsoid with a label and there methods in the `Spot` class to access all these properties:

The `Spot` class implements `ImgLib2` [`RealPositionable`](https://javadoc.scijava.org/ImgLib2/net/imglib2/RealPositionable.html) and [`RealLocalizable`](https://javadoc.scijava.org/ImgLib2/net/imglib2/RealLocalizable.html) interfaces, so you will find:
- all the methods to access the position: `localize(double[] pos)`, `getDoublePosition(int d)`. This refers to the center of the ellipsoid represented by the spot. 
- conversely, all the methods to set the position: `setPosition()`.

- The `setLabel(String label)` and / `getLabel()` are used for the spot label.
- `setCovariance(double[][] cov)` / `getCovariance()` to set or get the spot shape. As spots are ellipsoids, their shape is controlled by a covariance matrix that controls the ellipsoid size and orientation.
- `getTimepoint()` to return the timepoint this spot belongs to. The time-point of a spot is set at construction (see below) and cannot be changed.

Also, a spot is a vertex in the track graph (see below) and the `Spot` class has therefore methods to access the edges it is connected to in this graph:
- `edges()` return all the edges attached to this spot, regardless of their direction.
- `incomingEdges()` returns the collection of edges that are incoming to the spot (for which this spot is the _target_ vertex).
- `outgoingEdges()` is the converse: it returns the collection of edges that are outgoing, that is, for which this spot is the _source_ vertex).
The collection returned by `edges()` is the union of the collections returned by `incomingEdges()` and `outgoingEdges()`.

#### The `Link` class.


#### The index. The `SpatioTemporalIndex` and `SpatialIndex` classes.

The model maintains an index of the spots that are presents in each time-point, in the [SpatioTemporalIndex](https://github.com/mastodon-sc/mastodon-graph/blob/master/src/main/java/org/mastodon/spatial/SpatioTemporalIndex.java) class and its implementation.
You can get the index from the model with
```java
SpatioTemporalIndex< Spot > index = model.getSpatioTemporalIndex();
```

The index class has a generic parameter: `<Spot>`. 
This just indicates that for the data model we deal with in the Mastodon application, the objects we deal with are of the `Spot` class. 

The main use of the index is to retrieve all the spots at one specific time-point:
```java
// Retrieve all the spots in the 3rd time-point.
int tp = 2;
SpatialIndex< Spots > spatialIndex = index.getSpatialIndex( tp );
```

We get a `SpatialIndex` instance, which can be iterated over **all** the spots it contains:
```java
for (Spot spot : spatialIndex)
{
	// Do something with the spot.
}
```
The methods `isEmpty()` and `size()` methods can tell whether the collection is empty or its size. 
But the main interest of this `SpatialIndex` class is that it offers efficient methods to query the spots that are in specified volume, or the closest spots around a position.
The method:
```java
NearestNeighborSearch< Spot > nn = spatialIndex.getNearestNeighborSearch();
```
returns a class that can perform efficient nearest-neighbor search. 
Here is an example of its use:
```java
import net.imglib2.RealPoint;

// ...

// Get the NN instance for this time-point.
SpatioTemporalIndex< Spot > index = model.getSpatioTemporalIndex();
int tp = 2;
SpatialIndex< Spots > spatialIndex = index.getSpatialIndex( tp );
NearestNeighborSearch< Spot > nn = spatialIndex.getNearestNeighborSearch();

// Search the closest spot to a position.
// (We use a RealPoint. It could have been a Spot since a Spot is a RealLocalizable.)
RealLocalizable pos = new RealPoint(1.2, 5.6, 7.8);

// Perform the search 
nn.search( pos );

// Get search results.
Spot target = nn.getSampler().get();
double distance = nn.getDistance();
```

The `SpatialIndex` class can also return a `IncrementalNearestNeighborSearch`, which also perform nearest-neighbor search, but can be iterated to return the N closest spots to a position.

