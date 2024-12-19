# Spatial track matching

* This command allows comparing the lineages of two similarly developing embryos stored in two Mastodon projects.
* By analyzing the spindle directions, the plugin tries to find the corresponding cells in both embryos.

## Pre-conditions

The following conditions need to be met for the algorithm to work:

* Both projects should show stereotypically developing embryos.
* The first frame should show both the embryos at a similar developmental stage. The frame number that is considered
  the first frame can be set by the user.
* Root nodes must be labeled, and the labels should match between the two projects.
* There needs to be at least three tracks with cell divisions, that can be paired based on their names.
* Note: The plugin ignores tracks that have no cell divisions.

## Operations based on the correspondence information

The plugin allows performing various operations based on the correspondence information, such as:

* Couple projects:
    * Spot highlighting and focus are synchronized between the two projects.
    * Navigation to a clicked spot is synchronized for the selected `sync group`.
    * Synchronization works best between the TrackScheme Branch and TrackScheme Hierarchy windows.
    * Synchronization is only implemented for spots, not for links.
* Sort TrackScheme based on the correspondences
    * Orders the descendants in the TrackScheme of the chosen project such that their order matches the order in the
      other project.
* Copy cell names
    * The correspondences are on the level of cells. This is why all the spots that belong to the same cell will get
      the same label. Labels of individual spots can not be copied.
    * The label of the first spot of a cell is assumed to be the cell name.
    * This assumption is different from the TrackScheme Branch. Which actually shows the label of the last spot as
      the label of the branch.
* Copy tags between the corresponding cells in both embryos:
    * Use the found correspondences to copy a tag set from one project to the other.
    * The correspondences are on the level of cells / branches thus tags are only copied if the entire cell / branch
      is tagged. Tags on individual spots are not copied.
* Plot cell division angles
    * Show a plot of angles between paired cell division directions over time
* Add angles to table
    * Stores the angles between paired cell division directions as a feature in both projects.
* Color paired lineages
    * Creates a new tag set `lineages` in both projects. Lineages with the same root node label get a tag with the
      same color.

## Parameters and Track Matching Methods

* project A: the first project to compare
* project B: the second project to compare
* First frame: The first time point of a project to be used for the registration.
    * This is useful if
        * both projects start at different stages of development
            * e.g. one project starts at the 4-cell stage and the other at the 8-cell stage
            * in this case, the user can set the first frame of both projects to the same stage (i.e. the 8-cell stage)
        * there are less than three cells in the first time point
            * in this case, the user can set the first frame to a later time point where there are at least three cells
              in both projects.
* Spatial track matching method:
    * Fixed spatial registration based on root cells
        * Pairs of root cells with the same name are used to estimate the transformation between the two embryos.
    * Dynamic spatial registration based on root cells and their descendants
        * Pairs of root cells with the same name in both projects and respective descendants are used to estimate the
          transformation between
          the two embryos. The transformation is stabilized by averaging over the descendants of the root cells.
    * Dynamic spatial registration based on "landmarks" tag set
        * The user can define "landmark" spots in both projects. These spots need to be tagged with the same tag of a
          tag set called "landmarks" in both projects. The transformation is estimated based on the positions of the
          landmarks.

## Example

* project A (left
  side): [Phallusia mammillata](https://github.com/mastodon-sc/mastodon-example-data/blob/master/astec/Pm01.mastodon)
* project B (right
  side): [Phallusia mammillata](https://github.com/mastodon-sc/mastodon-example-data/blob/master/astec/Pm02.mastodon)
* Visualisation: ![spatial_track_matching.gif](spatialtrackmatching/spatial_track_matching.gif)
