from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(1, 100):
	sleep(1)

	camera.capture('/home/pi/lab/image%d.jpg'%(i))

camera.stop_preview()
