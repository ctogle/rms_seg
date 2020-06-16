import numpy as np

def _windows(a, window):
    """Return windowed version of an array"""
    if a.shape[0] > window:
        shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
        strides = a.strides + (a.strides[-1], )
        return np.lib.stride_tricks.as_strided(a,
            shape=shape, strides=strides, writeable=False)
    else:
        return a.reshape(1, -1)

def _extend(x, w):
    """Pad array x with w zeros on each end"""
    left = (np.zeros((w, )) + x[0])
    right = (np.zeros((w - 1, )) + x[-1])
    return np.hstack((left, x, right))

def _segment(x):
    """Segment an array based on equality with adjacent elements"""
    state = x[0]
    segments = []
    i = 0
    for j in range(1, x.shape[0]):
        if not x[j] == state:
            segments.append((state, i, j))
            state = x[j]
            i = j
    j = x.shape[0]
    segments.append((state, i, j))
    return segments

def _rms(bucket):
    """Compute RMS level for a sample of values"""
    return np.sqrt((bucket ** 2).sum() / max(1, len(bucket)))

def rms_segmentation(wave, sample_rate,
                     window_secs=0.5, threshold=0.01, resample_rate=200):
    """Compute a sliding window of RMS over an audio signal and
    segment based on where the signal exceeds a threshold

    Args:
        wave (numpy.array): Audio signal as a 1D array
        sample_rate (int): Sample rate of the audio signal
        window_secs (float): Duration of sliding window for RMS value
        threshold (float): Threshold for RMS value to indicate transitions
        resample_rate (int): Sample rate the audio is resampled to for speed

    Returns:
        2-tuple containing a list of segments and the underlying RMS signal;
        segments are 3-tuples containing classification (1 for above threshold,
        0 for below), and the start and end time of the segment in seconds.
        Adjacent segments always differ in classification.

    """
    # down sample wave to make RMS calculation faster
    offset = sample_rate // resample_rate
    wave = wave[offset // 2::offset]
    # compute segmentation via sliding RMS value
    window_size = int(window_secs * resample_rate)
    frames = _windows(wave, window_size)
    rms = np.apply_along_axis(_rms, -1, frames)
    mask = (rms > threshold) * 1
    mask = _extend(mask, window_size // 2)
    rms = _extend(rms, window_size // 2)
    segments = _segment(mask)
    # convert units back to input time scale
    segments = [(c, i / resample_rate, j / resample_rate) for c, i, j in segments]
    return segments, rms
