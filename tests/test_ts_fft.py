import numpy as np
import unittest
import matplotlib.pyplot as plt
from lib.ts_fft import ts_fft
import pandas as pd

__AUTHOR__ = "Oscar Lundberg"

class TestTFFT(unittest.TestCase):
    """Test"""

    def test_001_auto_cut(self):
        """"""
        N = 600
        T = 1.0/800.0
        x = np.linspace(0.0, N*T, N)
        y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

        signal_fft, freq = ts_fft(signal=y, sample_rate=T)

        assert len(signal_fft) == len(freq)

        fig, ax = plt.subplots()
        ax.plot(freq, signal_fft)
        plt.show()

    def test_002(self):
        df = pd.read_csv("data/Case option 3 - Data.csv", 
                         parse_dates=["tstamp"], dayfirst=True)

        signal = df["consumed_heat"].to_numpy()
        N = 1000
        signal =  np.convolve(signal, np.ones(N)/N, mode='valid')
        #signal = df["temp"].to_numpy()
        signal_fft, freq = ts_fft(signal, 1)

        fig, ax = plt.subplots(nrows=2, figsize=(20, 5))
        #ax[0].plot(1/freq[1:]/86400, signal_fft[1:])
        #ax[0].plot(freq[1:], signal_fft[1:])
        ax[0].plot(freq, signal_fft)
        ax[1].plot(signal)
        plt.show()
