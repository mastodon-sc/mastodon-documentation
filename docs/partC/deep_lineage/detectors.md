# Detectors and Linkers added to Mastodon

**It is highly recommended to use all detectors/linkers, added by Mastodon Deep Lineage, only on machines with a GPU (
ideally
NVIDIA). The detectors/linkers are very slow on machines without a GPU. Moreover, consider running these detectors on a
workstation and not on a typical consumer machine for better performance.**

* The detectors/linkers added to Mastodon are actually implemented in Python. They can be used in Fiji via
  the [Appose](https://apposed.org/) bridge between Java and Python.
* Each detector/linker needs a specific Python runtime environment with specific dependencies. These environments are
  automatically created and managed by Appose.
* There is a User Interface in Mastodon to install / update / delete these environments. The UI can be opened via
  `Plugins > Tracking > Python Environments for Detection/Linking`.
  ![python-environment-ui.png](detectors/python-environment-manager-menu.png)
* The dialog for managing the environments looks like
  this: ![python-environment-manager-dialog.png](detectors/python-environment-manager-dialog.png)
* It is recommended to use this dialog before using the detectors. However, the environments will also be installed
  automatically when using the detectors/linkers for the first time.
* In both case the installation process can be monitored using the Window `Console` in Fiji which can be accessed via
  `Window > Console` to monitor the progress of the installation.
  ![console.png](detectors/console.png)
* **Be aware that this installation processes may take some time and requires an internet connection. Depending on the
  detector, several gigabytes of data may be downloaded and installed to your system.**

## StarDist Detector

This detector uses StarDist for segmentation.

StarDist has been published in:

* [Cell Detection with Star-convex Polygons](https://link.springer.com/chapter/10.1007/978-3-030-00934-2_30), Uwe
  Schmidt, Martin Weigert, Coleman Broaddus, and Gene Myers, International
  Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI), Granada, Spain, 2018.

After the segmentation, spots are derived by fitting of ellipsoids to the pixel clouds of the detected objects.
The resulting spots are ellipsoids with the semi-axes computed from the variance covariance matrix of the pixel
positions of each segmented spot.

Parameters:

* Model: The StarDist model to use for segmentation. Depending on whether 2D or 3D data is processed, relevant models
  are shown.
    * Default Model (2D/3D): A pre-trained model for 2D and 3D segmentation. Has been trained on artificial data.
    * Plant Nuclei (3D): A pre-trained model for 3D segmentation of (plant) nuclei. Has been trained on real
      data: [10.5281/zenodo.8421755](https://bioimage.io/#/?tags=stardist&id=10.5281/zenodo.8421755)
    * Fluorescence Nuclei Segmentation (2D): A pre-trained model for 2D segmentation of fluorescence nuclei. Has
      been trained on real
      data: [10.5281/zenodo.6348084](https://bioimage.io/#/?tags=stardist&type=model&id=10.5281/zenodo.6348084)
    * SoSPIM (3D):A pre-trained model for 3D segmentation of cell nuclei imaged with SoSPIM. Has been trained on real
      data stained with DAPI and SOX2.
      labels: [https://doi.org/10.1101/2023.12.06.570366](https://doi.org/10.1101/2023.12.06.570366)
    * Confocal (3D): A pre-trained model for 3D segmentation of cell nuclei imaged with confocal microscopy. Has been
      trained on real data stained with the FUCCI
      label: [https://doi.org/10.1101/2023.12.06.570366](https://doi.org/10.1101/2023.12.06.570366)
    * Spinning Disk (3D): A pre-trained model for 3D segmentation of cell nuclei imaged with spinning disk
      microscopy. Has been trained on real data stained with DAPI
      label: [https://doi.org/10.1101/2023.12.06.570366](https://doi.org/10.1101/2023.12.06.570366)
* Probability/Score Threshold: Determine the number of object candidates to enter non-maximum suppression. Higher values
  lead to fewer segmented objects, but will likely avoid false positives.
* Overlap Threshold: Determine when two objects are considered the same during non-maximum suppression. Higher values
  allow segmented objects to overlap substantially.
* Estimated Object Diameters:
    * StarDist works best if object diameters estimates are given
    * Average diameter of the objects to be detected (in pixels) in X-Y plane.
    * Average diameter of the ojbects to be detected in Z direction (only for 3D data, in pixels).
    * Units are in pixels, so if your image has a pixel size of e.g. 0.5 µm, and you expect objects to be around 10 µm,
      enter 20 here.
    * If you do not know, enter 0 or -1 and StarDist will try to work without this info.
* **When this detection method is used for the first time, internet connection is needed, since an internal
  installation process is started. The installation consumes ~5GB hard disk space.**

## Cellpose3 Detector

This detector uses Cellpose3 for segmentation.

Cellpose3 has been published in:

* [Cellpose: a generalist algorithm for cellular segmentation](https://www.nature.com/articles/s41592-020-01018-x).
  Stringer et al., 2021, Nature Methods.

After the segmentation, spots are derived by fitting of ellipsoids to the pixel clouds of the detected objects.
The resulting spots are ellipsoids with the semi-axes computed from the variance covariance matrix of the pixel
positions of each segmented spot.

* Different Cellpose models can be used for different types of images. Cf.
  the [Cellpose documentation](https://cellpose.readthedocs.io/en/v3.1.1.1/models.html) for more information on the
  models.
* Cell probability threshold:
    * 0 ... more detections
    * 6 ... less detections (in dim regions)
* Flow threshold:
    * 0 ... viewer (ill-shaped) detections
    * 6 ... more detections
* Diameter:
    * Cellpose can exploit a priori knowledge on the size of cells.
    * If you have a rough estimate of the size of a typical cell, it can be entered, which will speed up the
      detection and improve the results.
    * Units are in pixels, so if your image has a pixel size of e.g. 0.5 µm, and you expect cells to be around 10 µm,
      enter 20 here.
    * If you do not know, enter 0 and cellpose will automatically determine the cell size estimate.
* GPU:
    * Select whether a GPU that should be used for processing. If no GPU is available, CPU processing will be used
      instead.
* Fraction of GPU memory to use:
    * Specify how much of the available GPU memory should be used for processing. If you are the only user of the GPU,
      you can set this value to 1.0 (100%). If you share the GPU with other users or applications, you may want to
      reduce this value.
* For 3D data, anisotropy can be respected. Respecting anisotropy may take significantly more time but can lead to
  better detection results.
* **When this detection method is used for the first time, internet connection is needed, since an internal
  installation process is started. The installation consumes ~7.5GB hard disk space.**

## Cellpose4 Detector

This detector uses Cellpose4 (Cellpose-SAM) for segmentation.

Cellpose4 has been published in:

* [Cellpose-SAM: superhuman generalization for cellular segmentation](https://www.biorxiv.org/content/10.1101/2025.04.28.651001v1).
  Pachitariu, M., Rariden, M., & Stringer, C. (2025). bioRxiv.

After the segmentation, spots are derived by fitting of ellipsoids to the pixel clouds of the detected objects.
The resulting spots are ellipsoids with the semi-axes computed from the variance covariance matrix of the pixel
positions of each segmented spot.

* Cell probability threshold:
    * 0 ... more detections
    * 6 ... less detections (in dim regions)
* Flow threshold:
    * 0 ... viewer (ill-shaped) detections
    * 6 ... more detections
* Diameter:
    * Cellpose can exploit an a priori knowledge on the size of cells.
    * If you have a rough estimate of the size of a typical cell, it can be entered, which will speed up the
      detection and improve the results.
    * Units are in pixels, so if your image has a pixel size of e.g. 0.5 µm, and you expect cells to be around 10 µm,
      enter 20 here.
    * If you do not know, enter 0 and cellpose will automatically determine the cell size estimate.
*
    * GPU:
        * Select whether a GPU that should be used for processing. If no GPU is available, CPU processing will be used
          instead.
* Fraction of GPU memory to use:
    * Specify how much of the available GPU memory should be used for processing. If you are the only user of the GPU,
      you can set this value to 1.0 (100%). If you share the GPU with other users or applications, you may want to
      reduce this value.
* **When this detection method is used for the first time, internet connection is needed, since an internal
  installation process is started. The installation consumes ~7.5GB hard disk space.**

## Which Cellpose version to use?

* Cellpose3 is the original Cellpose version, which is still widely used. It is a good choice for most applications. You
  have to choose a model that fits your data. Cyto3 seems to work for many different types of images, but it may happen
  that you have to try different models to find the best one for your data.
  For 3D applications, Cellpose3 is ~20 times faster than Cellpose4. For 2D applications the running time is similar.
* Cellpose4 is the latest version of Cellpose, which is based on the [SAM](https://segment-anything.com/) architecture.
  It does not require a model to be selected since it
  automatically adapts to the data. In 2D applications its running time is similar to Cellpose3, but in 3D applications
  it is ~20 times slower than Cellpose3.

## Example dataset:

* You can try the detectors on
  the [Mastodon example dataset](https://github.com/mastodon-sc/mastodon-example-data/tree/master/tgmm-mini)
* Cellpose3: ![mastodon-cellpose3.gif](detectors/mastodon-cellpose3.gif)
* Cellpose4: ![mastodon-cellpose4.gif](detectors/mastodon-cellpose4.gif)
* StarDist: ![mastodon-stardist.gif](detectors/mastodon-stardist.gif)

## Trackastra Linker

* This linker uses [TrackAstra](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/09819.pdf) for linking spots
  across timepoints.

Parameters:

* Link Threshold: Probability threshold for linking spots. Higher values lead to fewer links. Needs to be in the
  range [0, 1].
* Mode:
    * Greedy linking with divisions: Uses a greedy algorithm to link spots and allows for cell divisions.
    * Greedy linking without divisions: Uses a greedy algorithm to link spots and does not allow for cell divisions.
* Model (depends on dimensionality of data):
    * General Model (2D): Pre-trained model trained
      on [diverse 2D datasets](https://github.com/weigertlab/trackastra/blob/main/trackastra/model/pretrained.json).
      Recommended for 2D data.
    * Cell Tracking Challenge (2D+3D): Pre-trained model trained on data from the Cell Tracking Challenge.
* Source: The channel name of the source image that was used for detection.
* Resolution level: The resolution level of the source image. 0 is the full resolution, 1 is half resolution, etc.
* Window size: The size of the temporal window to consider for linking. Higher values lead to better linking results but
  also
  increase the running time. Must not be larger than the number of timepoints in the dataset.
