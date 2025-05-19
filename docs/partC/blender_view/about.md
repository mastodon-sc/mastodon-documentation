# About Mastodon Blender View

The Mastodon Blender View is a plugin for the [Mastodon](https://github.com/mastodon-sc/mastodon/) cell tracking
software.
The plugin allows visualizing Mastodon cell tracking data in the [Blender](https://blender.org) 3d modeling software.
It adds a new menu entry `Window > Blender Views` to Mastodon.
There are two options available:

## New Blender View (Advanced Visuals)

* This option opens a new Blender window with the cell tracking data. The data in the Blender window is detached
  from the Mastodon data, i.e., there is no interaction with Mastodon possible, and data updated in Mastodon is not
      updated in the Blender View. It can handle large datasets efficiently. It is possible to modify the visualization
      in Blender.

### Geometry Nodes

* This Blender View uses
  Blender's [Geometry Nodes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/introduction.html) to
  visualize the data. For this purpose, Mastodon exports the data to a CSV file, which is then read by Blender.
* This option opens a new Blender window with the cell tracking data. The data in the Blender window is detached
  from the Mastodon data, i.e., there is no interaction with Mastodon possible, and data updated in Mastodon is not
  updated in the Blender View. It can handle large datasets efficiently. It is possible to modify the visualization
  in Blender.
* Preferred option for high-quality rendering of movies.
* The data can be rotated and shown from all angles.

## New Blender View (Linked to Mastodon)

* This option opens a new Blender window with the cell tracking data. Blender & Mastodon are linked. You may use Blender
  to select objects, just as if it's a part of Mastodon.
* How it works:
    * This View under the hood uses a bridge between Mastodon (Java) and Blender (Python).
    * [gRPC](https://grpc.io/) is used to communicate between Mastodon and Blender.
    * During the installation of the Mastodon Blender plugin, a gRPC server is installed into the Blender installation
      directory. This server is used to communicate between Mastodon and Blender.
    * The server is started when the Blender View is opened.
    * The server is stopped when the Blender View is closed.
    * The server has implemented methods to synchronize the data between Mastodon and Blender, e.g. synchronize the time
      point,
      synchronize the active spot, synchronize the selected spots, etc.
    * The Mastodon Blender plugin in Blender listens to commands from Mastodon and executes them in Blender.
    * The communication works in both directions.

## For both options

* The data can be rotated and shown from all angles.
* The plugin has been successfully tested with Blender 3.5, 3.6, 4.0, 4.1 and 4.2. It is recommended to use the latest
  version of Blender. However, the plugin is not guaranteed to work with future versions of Blender.

## Example of a visualization

* ![blender.gif](about/blender.gif)
* Tracking data of phallusia mammillata embryogenesis
  by [Guignard et a. (2020)](https://doi.org/10.1126/science.aar5663).
