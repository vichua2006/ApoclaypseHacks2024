import cv2
import numpy as np
from flask import Flask, Response

# Initialize the camera
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 30
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

app = Flask(__name__)

def generate_frames():
    while True:
        im = picam2.capture_array()
        
        # Optional: You can add any processing on the image here
        points = [(115, 200), (525, 200), (640, 370), (0, 370)]
        width = 640
        height = 480
        input_pts = np.float32(points)
        output_pts = np.float32([(0, 0), (width - 1, 0), (width - 1, height - 1), (0, height - 1)])

        # Display the resulting frame
        ret, buffer = cv2.imencode('.jpg', im)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Raspberry Pi Camera</title>
    </head>
    <body>
        <h1>Raspberry Pi Camera Feed</h1>
        <img src="/video_feed" width="640" height="480">
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)