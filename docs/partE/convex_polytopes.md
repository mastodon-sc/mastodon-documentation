# Containment in Convex Polytopes using *k*-D trees.

Several important features of Mastodon rely on the fast retrieval of data items (spots and links) close to specific 3D positions. 
For instance we need to do so when you move the mouse close to the drawing of a spot in a view, to retrieve the spot in question. 
Or to determine what spots must to be painted in a BDV view, depending on the zoom level, position, rotation and field of view. 
There exists several well established algorithms and techniques to do that, in the case where the bounding-box in which we need to retrieve data items is a 3D rectangle aligned with the X, Y, Z axes of the dataset.

In our case it is not. 
In BDV you can rotate the view around an arbitrary angle. 
The XY view plane does not match an orthogonal plane of the dataset. 
Also the planes that make the bounds of the field of view are not aligned with these axes. 
In our case, the field of view is a [Convex Polytope](https://en.wikipedia.org/wiki/Convex_polytope). 
It is a portion of 3D space delimited by a set of planes. 
Think of an ideal diamond. 
Each facet of the diamond would be one of the planes. 
The interior of the diamond would be the convex polytope. 
Our goal is to know what are the points that are inside this volume so that we can paint them without losing time painting the ones not in the field of view.

At the time of the development of Mastodon, there was no published algorithm for the fast retrieval of points in a convex polytope. 
Tobias derived such an algorithm in 2016, and it is detailed in this chapter.
To the best of our knowledge this is unpublished:

[Containment in Convex Polytopes using kD trees](./TPietzschConvexPolytopes.pdf)