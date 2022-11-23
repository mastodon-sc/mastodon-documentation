# Mastodon data structures.

Before we discuss how to extend Mastodon with your own plugins, we need to learn a little bit about how Mastodon stores and deal with the data it can visualize and edit.
This page will walk you through the data structure in Mastodon from a Java programmer perspective. 

## The data model.

All the data is aggregated in the [`MamutAppModel`](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/MamutAppModel.java) class. 
This is the class you will access for instance when you write a plugin, and it contains many things that relate to the image, the tracking data and the user-interface.
We document below its most important components.

### Image data.

The image data is stored in a special class [`SharedBigDataViewerData`](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/views/bdv/SharedBigDataViewerData.java). 
It aggregates several objects and information from the BDV ecosystem.
You can access the list of sources and the `SpimData` objects from it.
```java
SharedBigDataViewerData imageData = mamutAppModel.getSharedBigDataViewerData();
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
It is based on a special data structure to manage large graphs that we developed speically for Mastodon, and describe [elsewhere in this documentation](../partD/mastodon_graph_data_structure.md).
The graph instance can be obtained as follow:
```java
ModelGraph graph = model.getGraph();
```

This graph class if often required by Mastodon algorithms and plugins, but is not the first entry point to browse and navigate the data from a user point-of view. 
You can access the links of a spot directly with the spot class, and the collections of spots in a time-point via the index.

#### The index. The `SpatioTemporalIndex` class.

The model maintains an index of the spots that are presents in each time-point, in the [SpatioTemporalIndex](https://github.com/mastodon-sc/mastodon-graph/blob/master/src/main/java/org/mastodon/spatial/SpatioTemporalIndex.java) class and its implementation.
You can get the index from the model with
```java
SpatioTemporalIndex< Spot > index = model.getSpatioTemporalIndex();
```

The 


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

#### The track graph. The `ModelGraph` class.

#### 