from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup the GPIO for the relay
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)

@app.route('/motor/forward', methods=['GET'])
def forward():
    GPIO.output(38, GPIO.HIGH)  # Turn on Relay 1
    GPIO.output(40, GPIO.LOW)  # Turn off Relay 2
    return 'Motor is moving forward', 200

@app.route('/motor/backward', methods=['GET'])
def backward():
    GPIO.output(38, GPIO.LOW)  # Turn off Relay 1
    GPIO.output(40, GPIO.HIGH)  # Turn on Relay 2
    return 'Motor is moving backward', 200

@app.route('/motor/stop', methods=['GET'])
def stop():
    GPIO.output(38, GPIO.LOW)  # Turn off Relay 1
    GPIO.output(40, GPIO.LOW)  # Turn off Relay 2
    return 'Motor has stopped', 200

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
