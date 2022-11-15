# Mastodon data structures.

Before we discuss how to extend Mastodon with your own plugins, we need to learn a little bit about how Mastodon stores and deal with the data it can visualize and edit.
This page will walk you through the data structure in Mastodon from a Java programmer perspective. 

## The data model.

All the data is aggregated in the [MamutAppModel](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/MamutAppModel.java) class. 
This is the class you will access for instance when you write a plugin, and it contains many things that relate to the image, the tracking data and the user-interface.
We document below its most important components.

### Image data.

The image data is stored in a special class [SharedBigDataViewerData](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/views/bdv/SharedBigDataViewerData.java). 
It aggregates several objects and information from the BDV ecosystem.
You can access the list of sources and the `SpimData` objects from it.
```java
SharedBigDataViewerData imageData = mamutAppModel.getSharedBigDataViewerData();
AbstractSpimData< ? > spimData = imageData.getSpimData();
List< SourceAndConverter< ? > > imageData.getSources();
```

### Tracking data, the `Model` class.

The tracking data, including the graph, the feature values, tags, etc. are stored in the [Model](https://github.com/mastodon-sc/mastodon/blob/master/src/main/java/org/mastodon/mamut/model/Model.java) class.
This is the main class to focus on to interrogate and manipulate tracking data.
```java
Model model = mamutAppModel.getModel();
```
