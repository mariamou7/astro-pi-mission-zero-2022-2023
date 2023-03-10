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
y = (255, 255, 0) # Yellow
p = (255, 0, 164) #Pink

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    x = (rgb.red, rgb.green, rgb.blue)

    image = [
      x, x, x, y, y, x, x, x,
      x, x, y, y, y, y, x, x,
      x, y, b, y, y, b, y, x,
      y, y, y, y, y, y, y, y,
      y, y, p, y, y, p, y, y,
      x, y, y, p, p, y, y, x,
      x, x, y, y, y, y, x, x,
      x, x, x, y, y, x, x, x]

    # Display the image
    sense.set_pixels(image)
    sleep(1)

    sense.clear(b)
