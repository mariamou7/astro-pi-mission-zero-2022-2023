# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

# Add colour variables and image
BL = (0, 0, 0)#BLACK
B = (0, 255, 0)#BLUE
S = (232, 233, 165)#SKIN
R = (225, 0, 0)#RED
BG = (0, 45, 65)#BACKGROUND
Y = (255, 255, 0)#YELLOW
G = (0, 255, 0)#GREEN

# Display the image

for i in range(28):
    rgb = sense.color # get the colour 
    BG = (rgb.red, rgb.green, rgb.blue)


image = [
    BG, BG, BG, BG, BG, BG, BG, BG,
    BG, Y, Y, Y, Y, Y, Y, BG,
    BG, S, S, Y, Y, S, S, BG,
    BG, S, BL, S, S, BL, S, BG,
    BG, S, S, S, S, S, S, BG,
    BG, R, S, S, S, S, R, BG,
    BG, S, R, R, R, R, S, BG,
    BG, BG, BG, BG, BG, BG, BG, BG,
]

sense.set_pixels(image)
sleep(1)

sense.clear(BL)
