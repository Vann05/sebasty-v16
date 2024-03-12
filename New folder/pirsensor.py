# import RPi.GPIO as GPIO
# import time

# PIR_PIN = 18

# def setup():
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(PIR_PIN, GPIO.IN)

# def pir_motion_detected(channel):
#     if GPIO.input(PIR_PIN):
#         print("Motion detected!")
#     else:
#         print("Motion ended!")

# def main():
#     try:
#         setup()
#         GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=pir_motion_detected)
#         print("PIR sensor testing. Press Ctrl+C to exit.")
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Exiting...")
#     finally:
#         GPIO.cleanup()

# if __name__ == '__main__':
#     main()
