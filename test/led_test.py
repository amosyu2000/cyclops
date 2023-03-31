import sys
sys.path.append('../src')
import pytest 
from led_handler.test_led import Led_Handler

def test_led_init():
    led_handle = Led_Handler()
    assert led_handle.color_gradient == [[255, 0, 0], [252, 64, 0], [249, 128, 0], [245, 191, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0]]
    assert led_handle.num_pixels == 8

def test_startup():
    led_handle = Led_Handler()
    led_handle.startup_sequence()
    for i in range(8):
        assert led_handle.pixels[i] == ((0, 0, 0,))

def test_capture():
    led_handle = Led_Handler()
    led_handle.capture_sequence()
    for i in range(8):
        assert led_handle.pixels[i] == ((0, 0, 0,))

def test_poweroff():
    led_handle = Led_Handler()
    led_handle.poweroff_sequence()
    for i in range(8):
        assert led_handle.pixels[i] == ((0, 0, 0,))

def test_distance():
    led_handle = Led_Handler()
    led_handle.startup_sequence()
    for i in range(8):
        assert led_handle.pixels[i] == ((0, 0, 0,))

