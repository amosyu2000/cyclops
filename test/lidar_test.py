import sys
sys.path.append('../src')
import pytest 
from lidar_thread.lidar import Lidar

def test_lidar_init():
    lidar = Lidar(5, 115200)
    assert True