import sys
sys.path.append('../src')
import pytest 
import numpy as np
import time
from accelerometer_thread.acceleration_plot import Acceleration_Plot


def test_data_points():
    acceleration_plot = Acceleration_Plot(data_points=50, average_of=3)
    assert len(acceleration_plot.avg_norm) == 0
    acceleration_plot.avg_norm.append(5)
    assert len(acceleration_plot.avg_norm) == 1

    acceleration_plot.avg_norm = np.arange(50).tolist()
    acceleration_plot.t = np.arange(50).tolist()
    assert len(acceleration_plot.avg_norm) == 50

def test_crash_detect():
    assert True