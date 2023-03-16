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
b =(0,0,0) #black
w =(255,255,255) #white          
p =(245,67,254) #pink
r =(255,0,0) #red
l =(0,100,255) #light blue

for i in range(28):
    rgb=sense.color # get the color
    x =(rgb.red,rgb.green,rgb.blue)
    image = [
    r,r,x,x,x,x,r,r,
    r,l,l,l,l,l,l,r,
    p,l,b,x,x,b,l,p,
    x,l,x,b,b,x,l,x,
    x,l,x,b,b,x,l,x,
    p,l,b,x,x,b,l,p,
    r,l,l,l,l,l,l,r,
    r,r,x,x,x,x,r,r,    
]

#display the image
sense.set_pixels(image)
