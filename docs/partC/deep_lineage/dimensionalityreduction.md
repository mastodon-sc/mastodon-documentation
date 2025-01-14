# Dimensionality reduction

For visualizing high-dimensional data, e.g. in two dimensions, potentially getting more insights into your data, you can
reduce the dimensionality of the measurements, using this algorithm:

* UMAP
  * [Uniform Manifold Approximation Projection (UMAP)](https://arxiv.org/abs/1802.03426)
  * [UMAP Python implementation](https://umap-learn.readthedocs.io/en/latest/)

## Usage

* Menu Location: `Plugins > Compute Feature > Dimensionality reduction`

Select the graph type whose features should be dimensionality reduced, either the Model Graph with Features for Spots
and Links or the Branch Graph with Features on BranchSpots and BranchLinks.
Next, select the feature + feature projections that should be dimensionality reduced. Prefer to select features, which
describe the phenotype (e.g. size, shape, velocity, number of neighbors, etc.).
Only select positional features (e.g. centroid, coordinates, timeframe, etc.), if the position of cells within
the image are descriptive for the phenotype. If you are unsure, you can select all features and then remove the
positional features later.

## Description

The available algorithms reduce the dimensionality of the selected features and adds the results as a new feature to the
table. In order to do so, the selected algorithm uses the data matrix from the spot or branch spot table, where each row
represents a spot or branch spot and each column represents a feature. The link and branch link features can be included
in the algorithm.

If they are selected, the algorithm will use the link feature value of its incoming edge or the average of all values of
all incoming edges, if there is more than one incoming edge.

The dialog will look like this:
![umap_dialog.png](dimensionalityreduction/umap_dialog.png)

By default, all measurements are selected in the box.

## Parameters

### Common Parameters

* Standardize: Whether to standardize the data before reducing the dimensionality. Standardization is recommended when
  the data has different scales / units.
  Further
  reading: [Standardization](https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling).
* Number of dimensions: The number of reduced dimensions to use. The default is 2, but 3 is also common.
  Further reading: [Number of Dimensions](https://umap-learn.readthedocs.io/en/latest/parameters.html#n-components).

### UMAP Parameters

* Number of neighbors: The size of the local neighborhood (in terms of number of neighboring sample points) used for
  manifold approximation.
  Larger values result in more global views of the manifold, while smaller values result in more local data being
  preserved.
  In general, it should be in the range 2 to 100.
  Further reading: [Number of Neighbors](https://umap-learn.readthedocs.io/en/latest/parameters.html#n-neighbors).
* Minimum distance: The minimum distance that points are allowed to be apart from each other in the low dimensional
  representation. This parameter controls how tightly UMAP is allowed to pack points together.
  Further reading: [Minimum Distance](https://umap-learn.readthedocs.io/en/latest/parameters.html#min-dist).

When you are done with the selection, click on `Compute`.
The resulting values will be added as additional columns to the selected table.

![umap_table.png](dimensionalityreduction/umap_table.png)

You can visualize the results using the `Grapher` View of Mastodon and selecting the newly added columns.

![umap_grapher.gif](dimensionalityreduction/umap_grapher.gif)

Visualization with the [Mastodon Blender View](https://github.com/mastodon-sc/mastodon-blender-view) is also possible.

![umap_blender.gif](dimensionalityreduction/umap_blender.gif)

## Example

The example above has been generated using the [
tgmm-mini](https://github.com/mastodon-sc/mastodon-example-data/tree/master/tgmm-mini) dataset, which is included in
the Mastodon repository.
