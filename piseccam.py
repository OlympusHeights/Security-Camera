import imutils
import cv2
import time
import os
import datetime
import gmail1
import threading
import RPi.GPIO as GPIO
import time
import subprocess

class Camera():

	def __init__(self, email="starkilla818@gmail.com"):
		self.firstFrame = None
		self.sent = False
		self.timing = 0
		self.email = email
		self.found = False

	def startCapture(self):
		camera = cv2.VideoCapture(0)
		while True:
			(grabbed, frame) = camera.read()
			text = "Undetected"

			if not grabbed:
				break

			frame = imutils.resize(frame, width=500)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			gray = cv2.GaussianBlur(gray, (21,21), 0)

			if self.firstFrame is None:
				self.firstFrame = gray
				continue

			frameDelta = cv2.absdiff(self.firstFrame, gray)
			thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

			thresh = cv2.dilate(thresh, None, iterations=2)
			(_,cnts,_) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


			for c in cnts:
				self.found = True
				(x, y, w, h) = cv2.boundingRect(c)
				cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)
				text = "Detected"

			cv2.putText(frame, "Status: {}".format(text), (10, 20),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
			cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
				(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

			if self.found is True:
				if self.sent is False and self.timing == 0:
					imgname = 'footage.png'
					cv2.imwrite(imgname, frame)
					img_data = open(imgname, 'rb').read()
					gmail1.sendingImage(img_data, self.email, imgname)
					self.sent = True
					self.timing = time.time()

				elif self.sent is True and time.time() - self.timing >10:
					self.sent = False
					self.timing = 0

				else:
					continue
				self.found = False

			key = cv2.waitKey(1) & 0xFF
				# if the `q` key is pressed, break from the lop
			if key == ord("q"):
				break
		camera.release()
		cv2.destroyAllWindows()


def sess():
	cam = Camera()
	cam.startCapture()

def check():
	GPIO.setmode(GPIO.BCM)
	batpin = 17
	GPIO.setup(batPin, GPIO.IN)
	while True:
		if not GPIO.input(batpin):
			print("Low Battery")
			print("Shutting Down")
			subprocess.call(["sudo", "shutdown", "-h", "now"])
		time.sleep(60)






t = threading.Thread(target=sess)
t.start()
