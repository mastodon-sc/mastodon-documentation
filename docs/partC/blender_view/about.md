# About Mastodon Blender View

The Mastodon Blender View is a plugin for the [Mastodon](https://github.com/mastodon-sc/mastodon/) cell tracking
software.
The plugin allows visualizing Mastodon cell tracking data in the [Blender](https://blender.org) 3d modeling software.
It adds a new menu entry `Window > Blender Views` to Mastodon.
There are two options available:

* New Blender View (Advanced Visuals)
    * This option opens a new Blender window with the cell tracking data. The data in the Blender window is detached
      from the Mastodon data, i.e. there is no interaction with Mastodon possible and data updated in Mastodon is not
      updated in the Blender View. It can handle large datasets efficiently. It is possible to modify the visualization
      in Blender.
* New Blender View (Linked to Mastodon)
    * This option opens a new Blender window with the cell tracking data. Blender &
      Mastodon are linked. You may use Blender to select objects, just as if it's a part of Mastodon.

For both options:

* The data can be rotated and shown from all angles.
* High quality rendering of movies is possible.
* Example of a visualization:
    * ![blender.gif](about/blender.gif)
    * Tracking data of phallusia mammillata embryogenesis
      by [Guignard et a. (2020)](https://doi.org/10.1126/science.aar5663).

![about.mov](about/about.mov)
