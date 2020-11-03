from flask import Flask, render_template, Response
from Object_detection_webcam import VideoCamera 

# Flask application

app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def index():
    #return "Hello"
    return render_template('index.html')
    
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed', methods=['POST', 'GET'])
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
                    
#to use IP webcam comment lines from 21 to 24 and remove commenting from lines 26 to 30.
#@app.route('/video_feed/<address>', methods=['POST', 'GET'])
#def video_feed(address):
#return Response(gen(VideoCamera(address)),
#                mimetype='multipart/x-mixed-replace; boundary=frame')

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug=True)
