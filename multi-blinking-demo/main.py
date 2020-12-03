# multi-blinking-demo
# Created at 2020-11-06 13:52:17.023623

import streams                          # Import the streams module.
from fourzerobox import fourzerobox     # Import the FourZeroBox.

streams.serial()                        # Open the default serial port.
fzbox = fourzerobox.FourZeroBox()       # Create 4ZeroBox Object.

while True:                             # Loop through all available colors.
       fzbox.set_led('R')               # Set the LED color.
       print("Red")                     # Print the LED color.
       sleep(1000)                      # Delay one second.
       fzbox.set_led('G')
       print("Green")
       sleep(1000)
       fzbox.set_led('B')
       print("Blue")
       sleep(1000)
       fzbox.set_led('M')
       print("Magenta")
       sleep(1000)
       fzbox.set_led('Y')
       print("Yellow")
       sleep(1000)
       fzbox.set_led('C')
       print("Cyan")
       sleep(1000)
       fzbox.set_led('W')
       print("White")
       sleep(1000)
