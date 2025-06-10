# Mastodon file format and cell tracking on remote images.

The goal of Mastodon is to make tracking in large images feasible and convenient.
Given that image files can be very large, it makes sense to think about data management if you have a project with large images.
So far in this section of the documentation we have been dealing with images stored in a local file on your computer.
However Mastodon can visualize and analyze images stored remotely and stream them to your computer. 
Mastodon is compatible with two main technologies for handling large images stored remotely:
- BDV servers.
- OME-NGFF specifications, mainly OME-Zarr and N5 file formats.
We can use them transparently, along with the possibility to open local files, thanks to Mastodon file format separating the storage for tracking data and image data.

## The Mastodon file format

This is a brief explanation of the mastodon file format, to introduce how we implemented opening local and remove images. 
This can be useful to know if you need to change the image file a Mastodon project points to. 

A `.mastodon` file is actually a plain zip file. 
If you unzip it you will get a folder.
It contains a series of binary files with the tracking data (graph and feature values), as well as a `project.xml` file that mostly contain the physical units and the link to the image file:


![](../imgs/Mastodon_remote_img_02.png)

As explained in the [introduction tutorial](getting_started.md), we mainly use the BDV file format for local images files.
An image is represented by two files (a `xml` and a `h5`) that stores pixel data and spatial transformations, plus an optional `xml` file storing the display settings.

![](../imgs/Mastodon_remote_img_01.png)

It turns out that the `xml` file is very flexible and can harness a wide range of file format.
The first one we can use is the remote BDV server.


## Opening a remote BDV image.

The BDV image file format we described before make it possible to store the `h5` on a remote server.
This server can send the image chunks required by a local client, like Mastodon.
In the example below we will be browsing and tracking an image stored on a server in the Institut Pasteur, Paris. 
The data layout is schematically the following:

![](../imgs/Mastodon_remote_img_03.png)

Download the exemple datasets from here: TODO TODO XXXX

The `ParhyaleHawaiensis` folder contains the first 10 timepoints of the MaMuT dataset, published in [Wolff, Tinevez, Pietzsch et al, 2018](https://doi.org/10.7554/eLife.34410).
If you open the file `MaMuT_Parhyale_demo.xml`, you can see that the link to the image is different from what we had with a local file:

![](../imgs/Mastodon_remote_img_04.png)

The `<ImageLoader>` element changed and we now have a `bdv.remote` as format. 
And the URL points to a http server, which is actually hosted in Pasteur.
Compare to what we have for a local file:
```xml
    <ImageLoader format="bdv.hdf5">
      <hdf5 type="relative">datasethdf5.h5</hdf5>
```

Let's use this XML file to create a new Mastodon project.
Open the Mastodon launcher (_Plugins > Tracking > Mastodon > Mastodon launcher_) and select _new Mastodon project_.
In the panel that shows up, select _Browse to a BDV file_ and browse to where the `MaMuT_Parhyale_demo.xml` is stored.

![](../imgs/Mastodon_remote_img_05.png){width="400px" align="center"}

Then create the project. 
The Mastodon control window should open and you will be able to browse a large image stored elsewhere, thanks to a 43kB file.

![](../imgs/Mastodon_remote_img_06.png){width="500px" align="center"}

The Mastodon projects you save from these files will keep the link to the remote image. 
For instance you can open the Mastodon file `MaMuT_Parhyale_demo-mamut.mastodon` in the same folder and have the remote image and the tracking data:


![](../imgs/Mastodon_remote_img_07.gif){width="400px" align="center"}


Parenthetically, the tracking data stored in this file is the result of the TGMM tracking algorithm ([Amat et al 2014](https://doi.org/10.1038/nmeth.3036)).
Note also that the image is stored remotely, but all the tracking annotations are local only. 
They live in the `.mastodon` file on your computer.
