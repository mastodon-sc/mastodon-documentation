# Existing plugins

This part documents the functionalities of Mastodon that have been implemented as plugins.
They can typically be found in the _Plugins_ submenu. 
The page below lists them all and links to specific documentation page for each plugin.
Information on how to extend Mastodon yourself be creating such plugins can be found in the next part of this documentation. 

## Core plugins

The following plugins are available with the core of Mastodon.

### Importers

- [CSV importer](csv_import/csv-importer.md)
- [GraphML importer](graphml_import/graphml_importer.md)
- [Simi-BioCell importer](simi_bio_cell_import/simi_bio_cell_importer.md)
- [TGMM importer](tgmm_import/tgmm_import_importer.md)

### Image data

- [Export to CSV](track-image)

### Numerical feature operations

- [Statistics on nearest neighbors](stats-on-nearest-neighbors)

### Selection operations

<!-- - [Selection creator](selection-creator) -->


### Detection & Tracking

<!-- - [Semi-automatic tracking](semi-automatic-tracking) -->
<!-- - [Cell detection wizard](cell-detection-wizard) -->
<!-- - [Cell tracking wizard](cell-tracking-wizard) -->
<!-- - [Ellipsoid Fitting](ellipsoid-fitting) -->


## Extra plugins

### Track analysis, import and export add-ons (DeepLineage)

A collection of tools that extend Mastodon, e.g.:

* Additional features for spots and links
* Additional features for branches
* Hierarchical clustering of lineage trees
* Import of segmented images as tracks
* Export of ellipsoids to segmented images
* Export of TrackScheme branch view to GraphML
* Dimensionality reduction (UMAP, PCA, t-SNE)

* See [Deep Lineage](deep_lineage.rst).

### Track editing, analysis and export add-ons (Tomancak)

A collection of tools that extend Mastodon, e.g.:

* Spot renaming and transformation
* Sorting TrackScheme
* Advanced track editing
* Find, locate and edit tags
* Export tree measurements
* Merge projects
* Spatial track matching

* See [Tomancak](tomancak.rst).

### Visualization add-ons (Blender-View)

Allows to connect Mastodon to Blender for 3D visualization.

* See [Blender-View](blender_view.rst).
