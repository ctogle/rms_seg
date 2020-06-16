=========
rms_seg
=========

`rms_seg` provides the function `rms_segmentation` to compute
a segmentation of an audio signal based on where its RMS level
exceeds a specified threshold value (i.e. very crude silence segmentation).
The function returns a 2-tuple containing a list of segments and the underlying RMS signal;
segments are 3-tuples containing classification (1 for above threshold, 0 for below),
and the start and end time of the segment in seconds.
Adjacent segments always differ in classification.

------------
Installation
------------

Installs via pip:

.. code-block:: bash

    git clone https://github.com/ctogle/rms_seg
    cd rms_seg
    pip install .

-----
Usage
-----

The variables `window_size` and `threshold` should be manually selected depending on the application.

.. code-block:: python

    from rms_seg import rms_segmentation
    from librosa.core import load

    window_size, threshold = 0.5, 0.02
    audio_signal, sample_rate = load(audio_path)
    segments, rms_signal = rms_segmentation(audio_signal, sample_rate, window_size, threshold)

