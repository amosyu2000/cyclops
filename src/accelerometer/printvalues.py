import adafruit_adxl34x
import board
import busio
import datetime
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

x = []
y = []
z = []
t = []

xline, = plt.plot(t, x, 'r', label="x")
yline, = plt.plot(t, y, 'b', label="y")
zline, = plt.plot(t, z, 'g', label="z")
ax = plt.gca()
plt.legend(loc="upper left")
plt.title("Accelerometer readings")
plt.xlabel("Time")
plt.ylabel("Acceleration (m^2/s)")

while True:
	acceleration = accelerometer.acceleration

	if len(t) > 50:
		x.pop(0)
		y.pop(0)
		z.pop(0)
		t.pop(0)
	x.append(acceleration[0])
	y.append(acceleration[1])
	z.append(acceleration[2])
	t.append(datetime.datetime.now())

	xline.set_data(t, x)
	yline.set_data(t, y)
	zline.set_data(t, z)
	ax.relim()
	ax.autoscale_view()
	plt.draw()
	plt.pause(0.1)