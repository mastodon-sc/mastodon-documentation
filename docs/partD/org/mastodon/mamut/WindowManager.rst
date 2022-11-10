.. java:import:: java.awt Desktop

.. java:import:: java.awt Window

.. java:import:: java.awt.event WindowEvent

.. java:import:: java.io IOException

.. java:import:: java.lang.reflect InvocationTargetException

.. java:import:: java.net URI

.. java:import:: java.net URISyntaxException

.. java:import:: java.util ArrayList

.. java:import:: java.util Collections

.. java:import:: java.util HashMap

.. java:import:: java.util List

.. java:import:: java.util Map

.. java:import:: java.util Objects

.. java:import:: java.util.function Consumer

.. java:import:: javax.swing JDialog

.. java:import:: org.mastodon.feature FeatureSpecsService

.. java:import:: org.mastodon.feature.ui FeatureColorModeConfigPage

.. java:import:: org.mastodon.mamut.feature MamutFeatureProjectionsManager

.. java:import:: org.mastodon.mamut.model Model

.. java:import:: org.mastodon.mamut.model Spot

.. java:import:: org.mastodon.mamut.plugin MamutPlugin

.. java:import:: org.mastodon.mamut.plugin MamutPluginAppModel

.. java:import:: org.mastodon.mamut.plugin MamutPlugins

.. java:import:: org.mastodon.model.tag.ui TagSetDialog

.. java:import:: org.mastodon.ui SelectionActions

.. java:import:: org.mastodon.ui.coloring.feature FeatureColorModeManager

.. java:import:: org.mastodon.ui.keymap CommandDescriptionProvider

.. java:import:: org.mastodon.ui.keymap CommandDescriptions

.. java:import:: org.mastodon.ui.keymap CommandDescriptionsBuilder

.. java:import:: org.mastodon.ui.keymap KeyConfigContexts

.. java:import:: org.mastodon.ui.keymap Keymap

.. java:import:: org.mastodon.ui.keymap KeymapManager

.. java:import:: org.mastodon.ui.keymap KeymapSettingsPage

.. java:import:: org.mastodon.util RunnableActionPair

.. java:import:: org.mastodon.util ToggleDialogAction

.. java:import:: org.mastodon.views.bdv.overlay.ui RenderSettingsConfigPage

.. java:import:: org.mastodon.views.bdv.overlay.ui RenderSettingsManager

.. java:import:: org.mastodon.views.context ContextProvider

.. java:import:: org.mastodon.views.grapher.display.style DataDisplayStyleManager

.. java:import:: org.mastodon.views.grapher.display.style DataDisplayStyleSettingsPage

.. java:import:: org.mastodon.views.trackscheme ScreenTransform

.. java:import:: org.mastodon.views.trackscheme.display ColorBarOverlay.Position

.. java:import:: org.mastodon.views.trackscheme.display.style TrackSchemeStyleManager

.. java:import:: org.mastodon.views.trackscheme.display.style TrackSchemeStyleSettingsPage

.. java:import:: org.scijava Context

.. java:import:: org.scijava InstantiableException

.. java:import:: org.scijava.listeners Listeners

.. java:import:: org.scijava.plugin Plugin

.. java:import:: org.scijava.plugin PluginInfo

.. java:import:: org.scijava.plugin PluginService

.. java:import:: org.scijava.ui.behaviour KeyPressedManager

.. java:import:: org.scijava.ui.behaviour.util AbstractNamedAction

.. java:import:: org.scijava.ui.behaviour.util Actions

.. java:import:: org.scijava.ui.behaviour.util RunnableAction

.. java:import:: bdv.util InvokeOnEDT

.. java:import:: bdv.viewer ViewerPanel

.. java:import:: net.imglib2.realtransform AffineTransform3D

WindowManager
=============

.. java:package:: org.mastodon.mamut
   :noindex:

.. java:type:: public class WindowManager

   Main GUI class for the Mastodon Mamut application.

   It controls the creation of new views, and maintain a list of currently opened views. It has a \ :java:ref:`getProjectManager()`\  instance that can be used to open or create Mastodon projects. It has also the main app-model for the session.

   :author: Tobias Pietzsch, Jean-Yves Tinevez


Methods
-------


closeAllWindows
^^^^^^^^^^^^^^^

.. java:method:: public void closeAllWindows()
   :outertype: WindowManager

   Close all opened views and dialogs.

computeFeatures
^^^^^^^^^^^^^^^

.. java:method:: public void computeFeatures()
   :outertype: WindowManager

   Displays the feature computation dialog.

createBigDataViewer
^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutViewBdv createBigDataViewer()
   :outertype: WindowManager

   Creates and displays a new BDV view, with default display settings.

createBigDataViewer
^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutViewBdv createBigDataViewer(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new BDV view, using a map to specify the display settings.

   The display settings are specified as a map of strings to objects. The accepted key and value types are:

   ..

   * \ ``'FramePosition'``\  → an \ ``int[]``\  array of 4 elements: x, y, width and height.
   * \ ``'LockGroupId'``\  → an integer that specifies the lock group id.
   * \ ``'SettingsPanelVisible'``\  → a boolean that specifies whether the settings panel is visible on this view.
   * \ ``'BdvState'``\  → a XML Element that specifies the BDV window state. See \ :java:ref:`ViewerPanel.stateToXml()`\  and \ :java:ref:`ViewerPanel.stateFromXml(org.jdom2.Element)`\  for more information.
   * \ ``'BdvTransform'``\  → an \ :java:ref:`AffineTransform3D`\  that specifies the view point.
   * \ ``'NoColoring'``\  → a boolean; if \ ``true``\ , the feature or tag coloring will be ignored.
   * \ ``'TagSet'``\  → a string specifying the name of the tag-set to use for coloring. If not \ ``null``\ , the coloring will be done using the tag-set.
   * \ ``'FeatureColorMode'``\  → a String specifying the name of the feature color mode to use for coloring. If not \ ``null``\ , the coloring will be done using the feature color mode.
   * \ ``'ColorbarVisible'``\  → a boolean specifying whether the colorbar is visible for tag-set and feature-based coloring.
   * \ ``'ColorbarPosition'``\  → a \ :java:ref:`Position`\  specifying the position of the colorbar.

   :param guiState: the map of settings.

createBranchBigDataViewer
^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutBranchViewBdv createBranchBigDataViewer()
   :outertype: WindowManager

   Creates and displays a new Branch-BDV view, with default display settings. The branch version of this view displays the branch graph.

createBranchBigDataViewer
^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutBranchViewBdv createBranchBigDataViewer(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new Branch-BDV view, using a map to specify the display settings.

   :param guiState: the settings map.

   **See also:** :java:ref:`.createBigDataViewer(Map)`

createBranchTrackScheme
^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutBranchViewTrackScheme createBranchTrackScheme()
   :outertype: WindowManager

   Creates and displays a new Branch-TrackScheme view, with default display settings. The branch version of this view displays the branch graph.

createBranchTrackScheme
^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutBranchViewTrackScheme createBranchTrackScheme(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new Branch-TrackScheme view, using a map to specify the display settings.

   :param guiState: the settings map.

   **See also:** :java:ref:`.createTrackScheme(Map)`

createGrapher
^^^^^^^^^^^^^

.. java:method:: public MamutViewGrapher createGrapher()
   :outertype: WindowManager

   Creates and displays a new Grapher view, with default display settings.

createGrapher
^^^^^^^^^^^^^

.. java:method:: public MamutViewGrapher createGrapher(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new Grapher view, using a map to specify the display settings.

   The display settings are specified as a map of strings to objects. The accepted key and value types are:

   ..

   * \ ``'FramePosition'``\  → an \ ``int[]``\  array of 4 elements: x, y, width and height.
   * \ ``'LockGroupId'``\  → an integer that specifies the lock group id.
   * \ ``'SettingsPanelVisible'``\  → a boolean that specifies whether the settings panel is visible on this view.
   * \ ``'NoColoring'``\  → a boolean; if \ ``true``\ , the feature or tag coloring will be ignored.
   * \ ``'TagSet'``\  → a string specifying the name of the tag-set to use for coloring. If not \ ``null``\ , the coloring will be done using the tag-set.
   * \ ``'FeatureColorMode'``\  → a @link String specifying the name of the feature color mode to use for coloring. If not \ ``null``\ , the coloring will be done using the feature color mode.
   * \ ``'ColorbarVisible'``\  → a boolean specifying whether the colorbar is visible for tag-set and feature-based coloring.
   * \ ``'ColorbarPosition'``\  → a \ :java:ref:`Position`\  specifying the position of the colorbar.
   * \ ``'GrapherTransform'``\  → a \ :java:ref:`org.mastodon.views.grapher.datagraph.ScreenTransform`\  specifying the region to initially zoom on the XY plot.

   :param guiState: the map of settings.

createHierarchyTrackScheme
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutBranchViewTrackScheme createHierarchyTrackScheme()
   :outertype: WindowManager

   Creates and displays a new Hierarchy-TrackScheme view, with default display settings.

createHierarchyTrackScheme
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public MamutBranchViewTrackScheme createHierarchyTrackScheme(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new Hierarchy-TrackScheme view, using a map to specify the display settings.

   :param guiState: the settings map.

   **See also:** :java:ref:`.createTrackScheme(Map)`

createTable
^^^^^^^^^^^

.. java:method:: public MamutViewTable createTable(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new Table or a Selection Table view, using a map to specify the display settings.

   The display settings are specified as a map of strings to objects. The accepted key and value types are:

   ..

   * \ ``'TableSelectionOnly'``\  → a boolean specifying whether the table to create will be a selection table of a full table. If \ ``true``\ , the table will only display the current content of the selection, and will listen to its changes. If \ ``false``\ , the table will display the full graph content, listen to its changes, and will be able to edit the selection.
   * \ ``'FramePosition'``\  → an \ ``int[]``\  array of 4 elements: x, y, width and height.
   * \ ``'LockGroupId'``\  → an integer that specifies the lock group id.
   * \ ``'SettingsPanelVisible'``\  → a boolean that specifies whether the settings panel is visible on this view.
   * \ ``'NoColoring'``\  → a boolean; if \ ``true``\ , the feature or tag coloring will be ignored.
   * \ ``'TagSet'``\  → a string specifying the name of the tag-set to use for coloring. If not \ ``null``\ , the coloring will be done using the tag-set.
   * \ ``'FeatureColorMode'``\  → a @link String specifying the name of the feature color mode to use for coloring. If not \ ``null``\ , the coloring will be done using the feature color mode.
   * \ ``'ColorbarVisible'``\  → a boolean specifying whether the colorbar is visible for tag-set and feature-based coloring.
   * \ ``'ColorbarPosition'``\  → a \ :java:ref:`Position`\  specifying the position of the colorbar.

   :param guiState: the map of settings.

createTable
^^^^^^^^^^^

.. java:method:: public MamutViewTable createTable(boolean selectionOnly)
   :outertype: WindowManager

   Creates and display a new Table or Selection Table view with default settings.

   :param selectionOnly: if \ ``true``\ , the table will only display the current content of the selection, and will listen to its changes. If \ ``false``\ , the table will display the full graph content, listen to its changes, and will be able to edit the selection.
   :return: a new table view.

createTrackScheme
^^^^^^^^^^^^^^^^^

.. java:method:: public MamutViewTrackScheme createTrackScheme()
   :outertype: WindowManager

   Creates and displays a new TrackScheme view, with default display settings.

createTrackScheme
^^^^^^^^^^^^^^^^^

.. java:method:: public MamutViewTrackScheme createTrackScheme(Map<String, Object> guiState)
   :outertype: WindowManager

   Creates and displays a new BDV view, using a map to specify the display settings.

   The display settings are specified as a map of strings to objects. The accepted key and value types are:

   ..

   * \ ``'FramePosition'``\  → an \ ``int[]``\  array of 4 elements: x, y, width and height.
   * \ ``'LockGroupId'``\  → an integer that specifies the lock group id.
   * \ ``'SettingsPanelVisible'``\  → a boolean that specifies whether the settings panel is visible on this view.
   * \ ``'TrackSchemeTransform'``\  → a \ :java:ref:`ScreenTransform`\  that defines the starting view zone in TrackScheme.
   * \ ``'NoColoring'``\  → a boolean; if \ ``true``\ , the feature or tag coloring will be ignored.
   * \ ``'TagSet'``\  → a string specifying the name of the tag-set to use for coloring. If not \ ``null``\ , the coloring will be done using the tag-set.
   * \ ``'FeatureColorMode'``\  → a @link String specifying the name of the feature color mode to use for coloring. If not \ ``null``\ , the coloring will be done using the feature color mode.
   * \ ``'ColorbarVisible'``\  → a boolean specifying whether the colorbar is visible for tag-set and feature-based coloring.
   * \ ``'ColorbarPosition'``\  → a \ :java:ref:`Position`\  specifying the position of the colorbar.

   :param guiState: the map of settings.

editTagSets
^^^^^^^^^^^

.. java:method:: public void editTagSets()
   :outertype: WindowManager

   Displays the tag-set editor dialog.

forEachBdvView
^^^^^^^^^^^^^^

.. java:method:: public void forEachBdvView(Consumer<? super MamutViewBdv> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened BDV views.

   :param action: the action to execute.

forEachBranchTrackSchemeView
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public void forEachBranchTrackSchemeView(Consumer<? super MamutBranchViewTrackScheme> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened Branch-TrackScheme views.

   :param action: the action to execute.

forEachBranchView
^^^^^^^^^^^^^^^^^

.. java:method:: public void forEachBranchView(Consumer<? super MamutBranchView<?, ?, ?>> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened branch-graph views.

   :param action: the action to execute.

forEachGrapherView
^^^^^^^^^^^^^^^^^^

.. java:method:: public void forEachGrapherView(Consumer<? super MamutViewGrapher> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened Grapher views.

   :param action: the action to execute.

forEachTableView
^^^^^^^^^^^^^^^^

.. java:method:: public void forEachTableView(Consumer<? super MamutViewTable> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened Table views.

   :param action: the action to execute.

forEachTrackSchemeView
^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public void forEachTrackSchemeView(Consumer<? super MamutViewTrackScheme> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened TrackScheme views.

   :param action: the action to execute.

forEachView
^^^^^^^^^^^

.. java:method:: public void forEachView(Consumer<? super MamutView<?, ?, ?>> action)
   :outertype: WindowManager

   Executes the specified action for all the currently opened views.

   :param action: the action to execute.

getBdvWindows
^^^^^^^^^^^^^

.. java:method:: public List<MamutViewBdv> getBdvWindows()
   :outertype: WindowManager

   Exposes currently open BigDataViewer windows.

   :return: a \ :java:ref:`List`\  of \ :java:ref:`MamutViewBdv`\ .


openOnlineDocumentation
^^^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public void openOnlineDocumentation()
   :outertype: WindowManager

   Opens the online documentation in a browser window.
