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
b = (0, 0, 0) # Black
p = (255, 0, 164) #Pink

for i in range(27):
    rgb = sense.color # get the colour from the sensor
    x = (rgb.red, rgb.green, rgb.blue)

    image = [
      x, p, x, x, x, x, p, x,
      p, p, p, x, x, p, p, p,
      x, p, p, p, p, p, p, x,
      x, p, p, p, p, p, p, x,
      x, x, p, p, p, p, x, x,
      x, x, x, p, p, x, x, x,
      x, x, x, p, p, x, x, x,
      x, x, x, x, x, x, x, x]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

    sense.clear(b)
