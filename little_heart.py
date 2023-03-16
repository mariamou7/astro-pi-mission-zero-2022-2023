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
b=(0,0,0) #black
w=(255,255,255)#white
p=(245,67,254)#pink
g=(38,117,120)#dark green
r=(255,0,0) #red

for i in range(28):
    rgb= sense. color #get the color
    x=(rgb.red,rgb.green,rgb.blue)

    image=[
        x,x,x,x,x,x,x,x,
        x,x,r,x,x,x,r,x,
        x,r,r,r,x,r,r,r,    
        x,x,r,r,r,r,r,x,
        x,x,x,r,r,r,x,x,
        x,x,x,x,r,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x]

# Display the image
sense.set_pixels(image)
sleep(i)

sense.clear(b)
