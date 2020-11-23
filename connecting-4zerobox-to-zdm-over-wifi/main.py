###############################################################################
# 4ZeroBox meets ZDM
#
# Created: 2020-09-10 15:45:48.789211
#
###############################################################################

from bsp.drivers import wifi
import streams
from zdm import zdm
import threading as th
import sfw
import mcu
from fourzerobox import fourzerobox

fzbox = None
d1 = 0
d2 = 1

def publish_handler():
    global d1
    global d2
    try:
        print(" --- Data to send ---")
        # Calculate fibonacci number
        num = d1 + d2
        d1 = d2
        d2 = num
        print("fibonacci:", num)
        to_send = {}
        to_send["fibonacci"] = num
        # Publish data to ZDM cloud service
        device.publish(to_send, "data" )
        print("... DONE")
    except Exception as e:
        print('Publish exception: ', e)
        fzbox.error_cloud()
        mcu.reset()

# Initialize system
sfw.watchdog(0, 60000)
streams.serial()
print("Serial init\r\n... DONE")
try:
    print("FourZerobox init")
    fzbox = fourzerobox.FourZeroBox()
    print("... DONE")
except Exception as e:
    print('Init exception: ', e)
    mcu.reset()

# Setup connection
try:
    print("Network init")
    fzbox.net_init()
    print("... DONE")
    print("Connecting to wifi ...")
    fzbox.net_connect("houseNET","house123")
    print("... DONE")
    print("Connecting to ZDM ...")
    device = zdm.Device()
    device.connect()
    print("... DONE")
except Exception as e:
    print('Connect exception: ', e)
    fzbox.pulse('R', 10000)
    mcu.reset()
    
# Main Loop
try:
    print("Start Main")
    while True:
        publish_handler()
        sfw.kick()
        sleep(10000)
except Exception as e:
    print('Run exception: ', e)
    fzbox.pulse('R', 10000)
    mcu.reset()
    