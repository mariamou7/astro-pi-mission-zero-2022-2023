# Εισαγωγή βιβλιοθηκών
from sense_hat import SenseHat
from time import sleep

# Ρύθμιση του Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Ρύθμιση του αισθητήρα χρωμάτων
sense.color.gain = 60 # Ρύθμιση της ευαισθησίας του αισθητήρα
sense.color.integration_cycles = 64 # Το μεσοδιάστημα κατά το οποίο θα γίνεται η ανάγνωση

# Προσθήκη μεταβλητών χρωμάτων και εικόνας

# Εμφάνιση της εικόνας

# Προσθήκη μεταβλητών χρωμάτων και εικόνας
B = (0,0,0) #black
W = (255,255,255) #white
P =(245,67,254) #pink
l = (236,157,238) #lila
g = (150,150,150) #gray
b = (68,125,252) #light blue
p = (103,66,103) #purple

for i in range (28):
    rgb = sense.color # get the color
    x =(rgb.red, rgb.green, rgb.blue)

    image = [
         g ,g ,x ,x ,x ,x ,g ,g,
         g ,W ,p ,p ,p ,p ,W ,g,
         x ,b ,b ,b ,b ,b ,b ,x,
         x ,P ,B ,b ,b ,B ,P ,x,
         x ,P ,B ,b ,b ,B ,P ,x,
         x ,b ,b ,b ,b ,b ,b ,x,
         g ,W ,p ,p ,p ,p ,W ,g,
         g ,g ,x ,x ,x ,x ,g ,g]
 
     # Εμφάνιση της εικόνας
    sense.set_pixels(image)
    sleep(1)

    sense.clear(b)
