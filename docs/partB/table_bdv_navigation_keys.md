# Navigating in the BDV views. 

| **Action**                      | **Key**  |
|---------------------------------|---------------|
| **_View._**                        ||
| Move in X & Y.                  | `Right-click` and `Drag`.    |
| Move in Z.                      | `Mouse-wheel`. <br>Press and hold `Shift` to move faster, `Control` to move slower. |
| Align with XY plane | `Shift Z` |
| Align with YZ plane | `Shift X` |
| Align with XZ plane | `Shift C` or `Shift A`. <br>For these 3 shortcuts, the view will rotate around the mouse position on the BDV. |
| Zoom / Unzoom.                  | `Control` + `Shift` + `Mouse-wheel` or `Command` + `Mouse-wheel`. <br>The view will zoom and unzoom around the mouse location. |
| **_Time-points_**.              |                    |
| Next time-point.                | `]` or `M`         |
| Previous time-point.            | `[` or `N`         |
| **_Bookmarks_.**                |                    |
| Store a bookmark.               | `Shift B` then press any key to store a bookmark with this key as label. <br>A bookmark stores the position, zoom and orientation in the view but not the time-point. Bookmarks are saved in display settings file. |
| Recall a bookmark.              | Press `B` then the key of the bookmark. |
| Recall a bookmark orientation.  | Press `O` then the key of the bookmark. Only the orientation of the bookmark will be restored. |
| **_Image display_.**            |                         |
| Select source 1, 2 ...          | Press `1` / `2` ...     |
| Brightness and color dialog.    | Press `S`. <br />In this dialog you can adjust the min & max for each source, select to what sources these min & max apply and pick a color for each source. |
| Toggle fused mode.              | Press `F`. <br /> In fused mode, several sources are overlaid. Press `Shift` + `1` / `Shift` + `2` ... to add / remove the source to the view. In single-source mode, only one source is shown.          |
| Visibility and grouping dialog. | Press `F6`.<br /> In this dialog you can define what sources are visible in fused mode, and define groups of sources for use in the grouping mode.         |
| Save / load display settings.   | `F11` / `F12`. <br />This will create a _XYZ_settings.xml_ file in which the display settings and bookmarks will be saved.                                               |
