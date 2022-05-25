# The selection creator. 

The automated detection process we use often generates a lot of spurious
detections.
In [TrackMate](https://imagej.net/plugins/trackmate/) we complemented it by adding *feature filters* just after the detection step.
In TrackMate UI it takes the shape of filter windows, where the user can specify a feature and a threshold above or below which spots are rejected. 
The filters can be stacked to generate a more stringent filtering. 
This approach is like fishing with a small-hole net, then throwing back unwanted fishes to sea.

In Mastodon we take a somewhat different approach. 
We don't have a filter interface, but instead work with the selection tool. 
To remove spurious spots, they are added to the selection based on criteria you define, then the selection content is deleted. 
The tool to create a selection is called the selection creator and we describe it here. 
It works differently from the interactive selection we have been presenting before.
Instead of manually clicking on spots or links, or drawing a selection rectangle in TrackScheme, you will enter an expression that will be parsed to generate a selection.

We thought this approach would be more convenient and powerful. 
First going through the selection allows to use the selection creator for other ends than filtering.
You can create a selection and assign a tag to it for instance.
Or use a selection as an input to the linking wizard.
Or have a BDV view that only shows the selection you just created.
