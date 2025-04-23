# Spatial track matching

The "spatial track matching" plugin in Mastodon is a plugin for comparing two stereotypically developing embryo in Mastodon.
Usually datasets opened in Mastodon are completely independent, without interaction between them.
The "spatial track matching" plugin however allows to select two openend Mastodon datasets and compute the correspondance between the cells in both datasets.
Once the correspondance between cell has been computed, the plugin allows to perform various operations: starting at syncing the focused cell between two datasets,
copying cell names between datasets, copying "tag sets", sorting on datasets in Mastodon TrackScheme such that it matched the other dataset etc.. 

However the plugin doesn't support all types a datasets. The two Mastodon datasets need to show a stereotypically developing embryos of the same species.
Both datasets need to start at the same stage with at least 3 cells. The plugin also allows to skip initial frames of a datasets to match the stage.
At this "initial stage" all cells need to be named manually. At the names have to matche between the two datasets.
The plugin was sucessfully tested with Macrostumum embryo (starting at 4 cell stage), Platynereis embryies (starting at ~32 cell stage), an Phallusia mammillata (starting at ~64 cell stage).

## How does this work:

Lets assume we have Mastodon datasets for two embryos, lets call them embryo X and embryo Y. Both datasets start at a four cell stage. And these four initial cells have been labeled by an expert as A, B, C and D. So for the initial time point we know the correspondence between the four cells in the two dataset. Cell A of embryo X corresponds to Cell A of embryo Y, cell B of embryo X corresponds to cell B of embryo Y etc.

Now there's the question if when a cell divides, for example cell B divides in both datesets. How do the two daugther cells of cell B in embryo X correspond to the daughter cells of cell B in embryo Y?

![What is the correct correspondance between daugter cells](spatialtrackmatching/question.png)

To answer this question. Lets first for conveniance give names to the daugther cells X1 and X2 in embryo X and Y1 and Y2 in embryo Y:

![](spatialtrackmatching/explain1.png)

There are only two possible correspondences for the daugther cells. First option X1 corresponds to Y1 and X2 to Y2 or second option X1 corresponds to Y2 and X2 corresponds to Y1. Two find the right correspondance our strategy is to align the embryos with each other. For the is use the known correspondences A-A, B-B, C-C, D-D. And we find the rotation, translation and scaling of embryo Y that brings the cells A,B,C and D closest (sum of squared distances) two the cells of embryo X:

![](spatialtrackmatching/explain2.png)

Now that both embryos are in the same coordinate system, it is possible two compare directions in both datasets. The mastodon dataset contains the coordinates for all cells at all timepoints. So the vector (or direction) from daughter cell X1 to X2 (purple arrow) and Y1 to Y2 (green arrow) can be easily computed, as well as the angle between the two direction:

![](spatialtrackmatching/explain3.png)

The angle tells us which of the two correspondances is correct. If the angle is less than 90 degree then X1-Y1, X2-Y2 is correct. Otherwise X1-Y2 and X2-Y1 is the correct correpondence.

It's a simple idea. But we have seen how we find the correspondance for a cell division, if we have the correspondance for the parent cells. Repeating this step for all cell divisions in the mastodon datasets gives us the full set of correspondances in the two datasets.

But there is no garantie whether or not the found correspondence is biologically correct or relevant. The method however allows us to get an ideo of the quality of the found correspondencs. Having computed the angle between cell division direction, we know that an angle close to 0 or 180 degree cleary indicates a specivic correspondance while a angle close to 90 degree very vaguely distinguishes between the two option.

The spatial track matching plugin has the option to plot cell devision angles. Here is such a plot:
![](spatialtrackmatching/plot_cell_division_angle.png)

The plot shows the cell division angles the match cell division of two embryos. Until timepoint 300 there is allmost no cell division angle close to 90 degree. Indicating that the spatial track matching works well until timepoint 300. However there are two cell division angles close to 90 degree early on. They probably indicate a difference in the developement between the to embryos!


## Installation

This plugin is avaliable as part of the "Mastodon-Tomancak" collection of plugins for Mastodon. It is usually installed
within Fiji, be activating the two update sites "Mastodon" and "Mastodon-Tomancak". ([How to activate and update site.](https://imagej.net/update-sites/following))

## Usage

After completing the installation process, restart Fiji and open two Mastodon datasets of stereo typically developing embryos.
([Example datasets](https://github.com/mastodon-sc/mastodon-example-data/blob/master/astec/))
The recording in both datasets should show an embryo starting at same stage (for example 4, 8, 32 cells etc.) and the cells on the first timepoint must have the same names in both datasets.

(It is possible to select a "first timepoint for registration". This option can be used if the two datasets start at different stages. All timepoints before this "first timepoint" are ignored by the spatial track matching plugin. This option should also be used if the two datasets start with less than three dividing cells.)

From the Mastodon menu select `Plugins > Lineage analysis > Spatial Track Matching'. This will show a new dialog "Spatial Track Matching Across Two Mastodon Projects". The two Mastodon projects should be selected a "project A:" and "project B:".

The "Spatial Track Matching [...]" dialog allows to perform a variaty of operations with two linked dataset. You can copy tagsets from on dataset to the other. You can rename the cells in one dataset to match the names in the other dataset. Or you can sore the TrackSchemes accordingly, or plot angles between cell division directions.


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
