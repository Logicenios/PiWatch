from picamera2 import Picamera2
picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
picam2.title_fields = ["ExposureTime", "AnalogueGain"]