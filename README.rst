=========
rms_seg
=========

`rms_seg` provides a simple function to compute a segmentation of an audio signal based on
where its RMS level exceeds a specified threshold value (i.e. very crude silence segmentation).

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

