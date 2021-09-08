import numpy as np
import scipy.fftpack

__AUTHOR__ = "Oscar Lundberg"

def ts_fft(signal, sample_rate):
    """Calculate the fft

    :param signal:
    :param sample_rate:
    :returns signal_fft:
    :returns freqs:
    """
    N = len(signal)
    T = sample_rate
    yf = scipy.fftpack.fft(signal)
    xf = np.linspace(0.0, 1.0/(2.0*T), int(N/2))
    yf = 2.0/N * np.abs(yf[:N//2])

    return yf, xf

