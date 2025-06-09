# Sinquencer

![Image of Main Window of Sinquencer rendering all 7 waves/layers from the subwindows, plus 7 Subwindows representing layers, each with their own wave](/SinquencerSS-2025-06-08.png)

An experimental MIDI sequencer based on the intersections of waves built using Pygame-CE

1. Current Work:
  * Building a general UI
    * Complete: Main Window, Layers (sub windows)
    * Still Needed: Sequence Length Indicator, Sequence Length Divider Lines on Main Window, Channel/Instrument Indicators (to show which active layers/waves are defining the intersection)
      
2. TODO:
  * Implement Methods to select modify and : Frequency, Amplitude and Phase of Selected Waves/Layers (in whole or float increments) 
  * Create a step-divider to allow up to 64 subdivisions of the main window
  * Create Intersection calculation function
  * Create a "play head" to step through based on BPM using pygame timers
  * Implement MIDI Channel Triggering
  * Stay Poor
