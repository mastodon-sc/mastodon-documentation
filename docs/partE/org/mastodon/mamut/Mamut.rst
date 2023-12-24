.. java:import:: java.awt Color

.. java:import:: java.io File

.. java:import:: java.io IOException

.. java:import:: java.util ArrayList

.. java:import:: java.util Collection

.. java:import:: java.util Iterator

.. java:import:: java.util List

.. java:import:: java.util Map

.. java:import:: java.util Optional

.. java:import:: java.util Random

.. java:import:: java.util.concurrent.atomic AtomicInteger

.. java:import:: java.util.concurrent.locks ReentrantReadWriteLock

.. java:import:: org.mastodon.collection RefSet

.. java:import:: org.mastodon.feature Feature

.. java:import:: org.mastodon.feature FeatureModel

.. java:import:: org.mastodon.feature FeatureSpec

.. java:import:: org.mastodon.feature FeatureSpecsService

.. java:import:: org.mastodon.graph GraphIdBimap

.. java:import:: org.mastodon.graph.algorithm RootFinder

.. java:import:: org.mastodon.mamut.feature MamutFeatureComputer

.. java:import:: org.mastodon.mamut.feature MamutFeatureComputerService

.. java:import:: org.mastodon.mamut.model Link

.. java:import:: org.mastodon.mamut.model Model

.. java:import:: org.mastodon.mamut.model ModelGraph

.. java:import:: org.mastodon.mamut.model ModelUtils

.. java:import:: org.mastodon.mamut.model Spot

.. java:import:: org.mastodon.mamut.project MamutProject

.. java:import:: org.mastodon.mamut.project MamutProjectIO

.. java:import:: org.mastodon.mamut.selectioncreator SelectionParser

.. java:import:: org.mastodon.model SelectionModel

.. java:import:: org.mastodon.model.tag ObjTagMap

.. java:import:: org.mastodon.model.tag TagSetModel

.. java:import:: org.mastodon.model.tag TagSetStructure

.. java:import:: org.mastodon.model.tag TagSetStructure.Tag

.. java:import:: org.mastodon.model.tag TagSetStructure.TagSet

.. java:import:: org.mastodon.tracking.detection DetectionUtil

.. java:import:: org.mastodon.tracking.detection DetectorKeys

.. java:import:: org.mastodon.tracking.linking LinkerKeys

.. java:import:: org.mastodon.tracking.linking LinkingUtils

.. java:import:: org.mastodon.tracking.mamut.detection DoGDetectorMamut

.. java:import:: org.mastodon.tracking.mamut.linking SimpleSparseLAPLinkerMamut

.. java:import:: org.mastodon.tracking.mamut.trackmate Settings

.. java:import:: org.mastodon.tracking.mamut.trackmate TrackMate

.. java:import:: org.mastodon.views.bdv SharedBigDataViewerData

.. java:import:: org.scijava Context

.. java:import:: org.scijava.command CommandInfo

.. java:import:: org.scijava.command CommandService

.. java:import:: org.scijava.log AbstractLogService

.. java:import:: org.scijava.log LogLevel

.. java:import:: org.scijava.log LogMessage

.. java:import:: org.scijava.log Logger

.. java:import:: org.scijava.module ModuleItem

.. java:import:: loci.formats FormatException

.. java:import:: mpicbg.spim.data SpimDataException


Mamut
=====

.. java:package:: org.mastodon.mamut
   :noindex:

.. java:type:: public class Mamut

   Main gateway for scripting Mastodon.

   This should be the entry point to create a new project or open an existing one via the \ :java:ref:`open(String)`\  and \ :java:ref:`newProject(String)`\  static methods. Once an instance is obtained this way, a Mastodon project can be manipulated with the instance methods.

   The gateways used in scripting are called Mamut and TrackMate. We chose these names to underly that this application offer functionalities that are similar to that of the MaMuT and TrackMate software, but improved. Nonetheless, all the code used is from Mastodon and allows only dealing with Mastodon projects.

   :author: Jean-Yves Tinevez

Static methods
--------------

These methods need to be called on the class object `org.mastodon.mamut.Mamut` iself.
They return an instance that can be used to manipulate the associated Mastodon project.

newProject
^^^^^^^^^^

.. java:method:: public static final Mamut newProject(String bdvFile, Context context) throws IOException, SpimDataException, FormatException
   :outertype: Mamut

   Creates a new Mastodon project analyzing the specified image data.

   :param bdvFile: a path to a BDV XML file. It matters not whether the image data is stored locally or remotely.
   :param context: an existing, non-\ ``null``\  \ :java:ref:`Context`\  instance to use to open the project.
   :throws IOException: when an error occurs trying to locate and open the file.
   :throws SpimDataException: when an error occurs trying to open the image data.
   :throws FormatException: when an error occurs with the image file format.
   :return: a new \ :java:ref:`Mamut`\  instance.

newProject
^^^^^^^^^^

.. java:method:: public static final Mamut newProject(String bdvFile) throws IOException, SpimDataException, FormatException
   :outertype: Mamut

   Creates a new Mastodon project analyzing the specified image data.

   A new \ :java:ref:`Context`\  is created along this call.

   :param bdvFile: a path to a BDV XML file. It matters not whether the image data is stored locally or remotely.
   :throws IOException: when an error occurs trying to locate and open the file.
   :throws SpimDataException: when an error occurs trying to open the image data.
   :throws FormatException: when an error occurs with the image file format.
   :return: a new \ :java:ref:`Mamut`\  instance.

open
^^^^

.. java:method:: public static final Mamut open(String mamutProject) throws IOException, SpimDataException, FormatException
   :outertype: Mamut

   Opens an existing Mastodon project and returns a \ :java:ref:`Mamut`\  instance that can manipulate it.

   A new \ :java:ref:`Context`\  is created along this call.

   :param mamutProject: the path to the Mastodon file.
   :throws IOException: when an error occurs trying to locate and open the file.
   :throws SpimDataException: when an error occurs trying to open the image data.
   :throws FormatException: when an error occurs with the image file format.
   :return: a new \ :java:ref:`Mamut`\  instance.

open
^^^^

.. java:method:: public static final Mamut open(String mamutProject, Context context) throws IOException, SpimDataException, FormatException
   :outertype: Mamut

   Opens an existing Mastodon project and returns a \ :java:ref:`Mamut`\  instance that can manipulate it.

   :param mamutProject: the path to the Mastodon file.
   :param context: an existing, non-\ ``null``\  \ :java:ref:`Context`\  instance to use to open the project.
   :throws IOException: when an error occurs trying to locate and open the file.
   :throws SpimDataException: when an error occurs trying to open the image data.
   :throws FormatException: when an error occurs with the image file format.
   :return: a new \ :java:ref:`Mamut`\  instance.


Methods
-------

These methods manipulate a Mastodon project using an instance returned by the static methods above.

clear
^^^^^

.. java:method:: public void clear()
   :outertype: Mamut

   Clears the content of the data model. Can be undone.

computeFeatures
^^^^^^^^^^^^^^^

.. java:method:: public void computeFeatures(String... featureKeys)
   :outertype: Mamut

   Computes the specified features.

   :param featureKeys: the names of the feature computer to use for computation. It matters not whether the feature is for spots, links, ...

computeFeatures
^^^^^^^^^^^^^^^

.. java:method:: public void computeFeatures(boolean forceComputeAll, String... featureKeys)
   :outertype: Mamut

   Computes the specified features, possible forcing recomputation for all data items, regardless of whether they are in sync or not.

   :param forceComputeAll: if \ ``true``\ , will force recomputation for all data items. If \ ``false``\ , feature values that are in sync won't be recomputed.
   :param featureKeys: the names of the feature computer to use for computation. It matters not whether the feature is for spots, links, ...

createTag
^^^^^^^^^

.. java:method:: public void createTag(String tagSetName, String... labels)
   :outertype: Mamut

   Creates a new tag-set and several tags for this tag-set.

   :param tagSetName: the tag-set name.
   :param labels: the list of labels to create in this tag-set.

createTrackMate
^^^^^^^^^^^^^^^

.. java:method:: public TrackMateProxy createTrackMate()
   :outertype: Mamut

   Creates and returns a new \ :java:ref:`TrackMateProxy`\  instance. This instance can then be used to configure tracking on the image analyzed in this current \ :java:ref:`Mamut`\  instance.

   It is perfectly possible to create and configure separately several \ :java:ref:`TrackMateProxy`\  instances. Tracking results will be combined depending on the instances configuration.

   :return: a new \ :java:ref:`TrackMateProxy`\  instance.

deleteSelection
^^^^^^^^^^^^^^^

.. java:method:: public void deleteSelection()
   :outertype: Mamut

   Deletes all the data items (spots and tracks) currently in the selection.

detect
^^^^^^

.. java:method:: public void detect(double radius, double threshold)
   :outertype: Mamut

   Performs detection of spots in the image data with the default detection algorithm (the DoG detector).

   :param radius: the radius of spots to detect, in the physical units of the image data.
   :param threshold: the threshold on quality of detection below which to reject detected spots.

echo
^^^^

.. java:method:: public void echo()
   :outertype: Mamut

   Prints the content of the data model as two tables as text in the logger output.

echo
^^^^

.. java:method:: public void echo(int nLines)
   :outertype: Mamut

   Prints the first N data items of the content of the data model as two tables as text in the logger output.

   :param nLines: the number of data items to print.

getLogger
^^^^^^^^^

.. java:method:: public Logger getLogger()
   :outertype: Mamut

   Returns the logger instance to use to send messages and errors.

   :return: the logger instance.

getModel
^^^^^^^^

.. java:method:: public Model getModel()
   :outertype: Mamut

   Returns the data model manipulated by this \ :java:ref:`Mamut`\  instance.

   :return: the data model.

getSelectionModel
^^^^^^^^^^^^^^^^^

.. java:method:: public SelectionModel<Spot, Link> getSelectionModel()
   :outertype: Mamut

   Returns the selection model manipulated by this \ :java:ref:`Mamut`\  instance.

   :return: the selection model.

getWindowManager
^^^^^^^^^^^^^^^^

.. java:method:: public WindowManager getWindowManager()
   :outertype: Mamut

   Returns the \ :java:ref:`WindowManager`\  gateway used to create views of the data used in this \ :java:ref:`Mamut`\  instance.

   :return: the \ :java:ref:`WindowManager`\  gateway.

info
^^^^

.. java:method:: public void info()
   :outertype: Mamut

   Prints a summary information to the logger output.

infoFeatures
^^^^^^^^^^^^

.. java:method:: public void infoFeatures()
   :outertype: Mamut

   Prints summary information on the feature computers known to Mastodon to the logger output.

infoTags
^^^^^^^^

.. java:method:: public void infoTags()
   :outertype: Mamut

   Prints summary information on the tag-sets and tags currently present in the current Mastodon project.

link
^^^^

.. java:method:: public void link(double maxLinkingDistance, int maxFrameGap)
   :outertype: Mamut

   Performs linking of existing spots using the default linking algorithm (the Simple LAP linker).

   :param maxLinkingDistance: the max linking distance (in physical unit) beyond which to forbid linking.
   :param maxFrameGap: the max difference in frames for bridging gaps (missed detections).

redo
^^^^

.. java:method:: public void redo()
   :outertype: Mamut

   Redo the last changes. Can be called several times.

resetSelection
^^^^^^^^^^^^^^

.. java:method:: public void resetSelection()
   :outertype: Mamut

   Clears the current selection.

save
^^^^

.. java:method:: public boolean save()
   :outertype: Mamut

   Saves the Mastodon project of this instance to a Mastodon file.

   This method will return an error if a Mastodon file for the project has not been specified a first time with the \ :java:ref:`saveAs(String)`\  method.

   :return: \ ``true``\  if saving happened without errors. Otherwise an error message is sent to the \ :java:ref:`Logger`\  instance.

saveAs
^^^^^^

.. java:method:: public boolean saveAs(String mastodonFile)
   :outertype: Mamut

   Saves the Mastodon project of this instance to a new Mastodon file (it is recommended to use the \ ``.mastodon``\  file extension).

   The file specified will be reused for every following call to the \ :java:ref:`save()`\  method.

   :param mastodonFile: a path to a writable file.
   :return: \ ``true``\  if saving happened without errors. Otherwise an error message is sent to the \ :java:ref:`Logger`\  instance.

select
^^^^^^

.. java:method:: public void select(String expression)
   :outertype: Mamut

   Sets the current selection from a selection creator expression.

   Such an expression can be:

   .. code-block:: python

      mamut.select( "vertexFeature( 'Track N spots' ) < 10" )

   Check `the selection creator tutorial <../../../../partA/selection_creator.html>`_ to learn how to build such expressions.
   An error message is sent to the logger is there is a problem with the evaluation of the expression.

   :param expression: a selection creator expression.

setLogger
^^^^^^^^^

.. java:method:: public void setLogger(Logger logger)
   :outertype: Mamut

   Sets the logger instance to use to send messages and errors.

   :param logger: a logger instance.

setTagColor
^^^^^^^^^^^

.. java:method:: public void setTagColor(String tagSetName, String label, int R, int G, int B)
   :outertype: Mamut

   Sets the color associated with a tag in a tag-set. The color is specified as a RGB triplet from 0 to 255.

   :param tagSetName: the name of the tag-set containing the target tag.
   :param label: the tag to modify the color of.
   :param R: the red value of the RGB triplet.
   :param G: the green value of the RGB triplet.
   :param B: the blue value of the RGB triplet.

tagSelectionWith
^^^^^^^^^^^^^^^^

.. java:method:: public void tagSelectionWith(String tagSetName, String label)
   :outertype: Mamut

   Assigns the specified tag to the data items currently in the selection.

   :param tagSetName: the name of the tag-set to use.
   :param label: the name of the tag in the tag-set to use.

undo
^^^^

.. java:method:: public void undo()
   :outertype: Mamut

   Undo the last changes. Can be called several times.

