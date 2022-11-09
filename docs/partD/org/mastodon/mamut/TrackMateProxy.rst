.. java:import:: java.util ArrayList

.. java:import:: java.util Arrays

.. java:import:: java.util HashMap

.. java:import:: java.util List

.. java:import:: java.util Map

.. java:import:: org.apache.commons.lang WordUtils

.. java:import:: org.mastodon.tracking.detection DetectionUtil

.. java:import:: org.mastodon.tracking.linking LinkingUtils

.. java:import:: org.mastodon.tracking.mamut.detection SpotDetectorOp

.. java:import:: org.mastodon.tracking.mamut.linking KalmanLinkerMamut

.. java:import:: org.mastodon.tracking.mamut.linking SpotLinkerOp

.. java:import:: org.mastodon.tracking.mamut.trackmate PluginProvider

.. java:import:: org.mastodon.tracking.mamut.trackmate TrackMate

.. java:import:: org.scijava.log Logger

org.mastodon.mamut.TrackMateProxy
=================================

.. java:package:: org.mastodon.mamut
   :noindex:

.. java:type:: public class TrackMateProxy

   The tracking gateway used in scripting to configure and execute tracking in Mastodon scripts.

   :author: Jean-Yves Tinevez

Methods
-------
info
^^^^

.. java:method:: public void info()
   :outertype: TrackMateProxy

   Prints the current tracking configuration.

infoDetectors
^^^^^^^^^^^^^

.. java:method:: public void infoDetectors()
   :outertype: TrackMateProxy

   Prints information on the collection of detectors currently usable in Mastodon.

infoLinkers
^^^^^^^^^^^

.. java:method:: public void infoLinkers()
   :outertype: TrackMateProxy

   Prints information on the collection of linkers currently usable in Mastodon.

resetDetectorSettings
^^^^^^^^^^^^^^^^^^^^^

.. java:method:: public void resetDetectorSettings()
   :outertype: TrackMateProxy

   Resets the detection settings to their default values.

resetLinkerSettings
^^^^^^^^^^^^^^^^^^^

.. java:method:: public void resetLinkerSettings()
   :outertype: TrackMateProxy

   Resets the linking settings to their default values.

run
^^^

.. java:method:: public boolean run()
   :outertype: TrackMateProxy

   Executes the tracking with current configuration.

   :return: \ ``true``\  if tracking completed successful. An error message will be printed otherwise.

setDetectorSetting
^^^^^^^^^^^^^^^^^^

.. java:method:: public void setDetectorSetting(String key, Object value)
   :outertype: TrackMateProxy

   Configures one parameter of the current detector. The parameter key and value must be valid for the detector set with \ :java:ref:`useDetector(String)`\ , as shown in \ :java:ref:`infoDetectors()`\ .

   :param key: the key of the parameter.
   :param value: the value to set for this parameter.

setLinkerSetting
^^^^^^^^^^^^^^^^

.. java:method:: public void setLinkerSetting(String key, Object value)
   :outertype: TrackMateProxy

   Configures one parameter of the current link. The parameter key and value must be valid for the linkset with \ :java:ref:`useLinker(String)`\ , as shown in \ :java:ref:`infoLinkers())`\ .

   :param key: the key of the parameter.
   :param value: the value to set for this parameter.

useDetector
^^^^^^^^^^^

.. java:method:: public void useDetector(String detector)
   :outertype: TrackMateProxy

   Configures this tracking session to use the specified detector. Prints an error message if the name is unknown.

   :param detector: the name of the detector, as returned in \ :java:ref:`infoDetectors()`\ .

useLinker
^^^^^^^^^

.. java:method:: public void useLinker(String linker)
   :outertype: TrackMateProxy

   Configures this tracking session to use the specified linker. Prints an error message if the name is unknown.

   :param linker: the name of the linker, as returned in \ :java:ref:`infoLinkers()`\ .

