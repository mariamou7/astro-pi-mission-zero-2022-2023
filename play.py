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
b = (0, 0, 0)#black
w = (255, 255, 255)#white
p = (245, 67, 254)#pink
l = (236, 157, 238)#lila
g = (38, 117, 120)#dark green
G = (150, 150, 150)#gray

P = (103, 66, 103)#purple
y = (255, 255, 0)#yellow
r = (255, 0, 0)#red
bl = (0, 0, 255)#blue

for i in range (28):
    rgb = sense.color # get the colour
    B = (rgb.red, rgb.green, rgb.blue) 


    image = [
         B, B, B, B, B, B, B, B,
         B, r, r, B, r, r, B, B,
         B, r, r, r, r, r, B, B,
         B, B, r, r, r, B, B, B,
         B, B, B, r, B, B, B, B,
         B, y, B, y, B, y, B, B,
         B, y, y, y, B, y, B, B,
         B, y, B, y, B, y, B, B]   
  

    # Display the image
    sense.set_pixels(image)
    sleep(0.5)

    sense.clear(b)
