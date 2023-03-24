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
f = (232,222,123)
h = (222,111,0)

for i in range(28):
    rgb =sense.color # get the colour
    x = (rgb.red, rgb.green, rgb.blue)
    
    # Display the image

    image = [
    x, h, x, x, x, x, h, x, 
    x, h, h, h, h, h, h, h, 
    x, x, x, x, x, x, h, h, 
    x, h, x, h, x, h, x, h, 
    h, x, h, x, h, x, h, x,
    h, h, h, h, h, h, h, h,
    x, x, x, x, x, x, x, x,
    x, x, x, x, x, x, x, x]

     # Display the iwage
    sense.set_pixels(image)
    sleep(1)

    sense.clear(h)
