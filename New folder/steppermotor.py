# import RPi.GPIO as GPIO
# import time

# # Set GPIO mode
# GPIO.setmode(GPIO.BOARD)

# # Define GPIO pins
# IN1 = 11
# IN2 = 12
# IN3 = 13
# IN4 = 15

# # Set up GPIO pins
# GPIO.setup(IN1, GPIO.OUT)
# GPIO.setup(IN2, GPIO.OUT)
# GPIO.setup(IN3, GPIO.OUT)
# GPIO.setup(IN4, GPIO.OUT)

# # Function to set stepper motor sequence
# def setStep(w1, w2, w3, w4):
#     GPIO.output(IN1, w1)
#     GPIO.output(IN2, w2)
#     GPIO.output(IN3, w3)
#     GPIO.output(IN4, w4)

# # Define stepper motor sequence
# # You may need to adjust the sequence according to your motor configuration
# seq = [[1,0,0,1],
#        [1,0,0,0],
#        [1,1,0,0],
#        [0,1,0,0],
#        [0,1,1,0],
#        [0,0,1,0],
#        [0,0,1,1],
#        [0,0,0,1]]

# # Define function to rotate stepper motor
# def rotate(degrees, delay):
#     steps_per_revolution = 512 # Change this value according to your motor specifications
#     steps = (degrees / 360) * steps_per_revolution
#     for _ in range(int(steps)):
#         for i in range(8):
#             setStep(seq[i][0], seq[i][1], seq[i][2], seq[i][3])
#             time.sleep(delay)

# # Example usage
# if __name__ == "__main__":
#     try:
#         while True:
#             degrees = float(input("Enter the degrees to rotate (e.g., 180, 90, 120): "))
#             delay = float(input("Enter the delay between steps (e.g., 0.01): "))
#             rotate(degrees, delay)
#     except KeyboardInterrupt:
#         GPIO.cleanup()
