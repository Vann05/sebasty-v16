from flask import Flask, render_template, Response
import cv2
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO setup
left_motor_pin1 = 17
left_motor_pin2 = 18
right_motor_pin1 = 22
right_motor_pin2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_pin1, GPIO.OUT)
GPIO.setup(left_motor_pin2, GPIO.OUT)
GPIO.setup(right_motor_pin1, GPIO.OUT)
GPIO.setup(right_motor_pin2, GPIO.OUT)

# GPIO functions
def move_forward():
    GPIO.output(left_motor_pin1, GPIO.HIGH)
    GPIO.output(left_motor_pin2, GPIO.LOW)
    GPIO.output(right_motor_pin1, GPIO.HIGH)
    GPIO.output(right_motor_pin2, GPIO.LOW)
    pass

def move_backward():
    GPIO.output(left_motor_pin1, GPIO.LOW)
    GPIO.output(left_motor_pin2, GPIO.HIGH)
    GPIO.output(right_motor_pin1, GPIO.LOW)
    GPIO.output(right_motor_pin2, GPIO.HIGH)
    pass

def turn_left():
    GPIO.output(left_motor_pin1, GPIO.LOW)
    GPIO.output(left_motor_pin2, GPIO.HIGH)
    GPIO.output(right_motor_pin1, GPIO.HIGH)
    GPIO.output(right_motor_pin2, GPIO.LOW)
    pass

def turn_right():
    GPIO.output(left_motor_pin1, GPIO.HIGH)
    GPIO.output(left_motor_pin2, GPIO.LOW)
    GPIO.output(right_motor_pin1, GPIO.LOW)
    GPIO.output(right_motor_pin2, GPIO.HIGH)
    pass

def stop_robot():
    GPIO.output(left_motor_pin1, GPIO.LOW)
    GPIO.output(left_motor_pin2, GPIO.LOW)
    GPIO.output(right_motor_pin1, GPIO.LOW)
    GPIO.output(right_motor_pin2, GPIO.LOW)
    pass

# Camera setup
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    direction = request.form['direction']

    if direction == 'forward':
        move_forward()
    elif direction == 'backward':
        move_backward()
    elif direction == 'left':
        turn_left()
    elif direction == 'right':
        turn_right()
    elif direction == 'stop':
        stop_robot()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
