# Import the libraries
from sense_hat import SenseHat
from time import sleep

# Set up the Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# Set up the colour sensor
sense.color.gain = 60 # Set the sensitivity of the sensor
sense.color.integration_cycles = 64 # The interval at which the reading will be taken

b = (0, 0, 255)
w = (255, 255, 255)

for i in range(26):
    rgb = sense.color
    x = (rgb.red, rgb.green, rgb.blue)
    image = [
        x, x, x, x, x, x, x, x,
        x, x, x, b, b, x, x, x,
        x, x, b, b, b, b, x, x,
        x, b, b, b, b, b, b, x,
        x, b, b, b, b, b, b, x,
        x, x, b, b, b, b, x, x,
        x, x, x, b, b, x, x, x,
        x, x, x, x, x, x, x, x,
    ]    

    sense.set_pixels(image)
    sleep(1)

    sense.clear(w)
