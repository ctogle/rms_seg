from rms_seg import rms_segmentation
import numpy as np


def test_segmentation():
    sample_rate = 8000
    window_size = 0.5
    threshold = 0.02
    duration = 120
    hz = 440 # an A note

    # make a dummy audio signal
    x = np.linspace(0, duration, duration * sample_rate)
    y = np.sin(2 * np.pi * x * sample_rate / hz)
    # mask the signal as if silent in the middle
    y *= (np.cos(2 * np.pi * x / duration) > 0).astype(int)
    # produce segmentation
    segments, rms = rms_segmentation(y, sample_rate, window_size, threshold)

    # ensure 3 segments, the middle of which is below the threshold
    assert (len(segments) == 3)
    assert (segments[0][0] == segments[2][0] == 1)
    assert (segments[1][0] == 0)
    # ensure segments cover the input
    assert (segments[0][1] == 0)
    assert (segments[0][2] == segments[1][1])
    assert (segments[1][2] == segments[2][1])
    assert (segments[-1][2] == duration)
