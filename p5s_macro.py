import pyvjoy
import time
from joymapper import JOY_MAPPER

joy = JOY_MAPPER(pyvjoy.VJoyDevice(1))

print("Program will start in 3 seconds..")
time.sleep(3)

loopTimes = 10
currentLoops = 0


def DO_LOOP():
    global loopTimes, currentLoops

    print(f"CURRENT LOOP -> {currentLoops}")

    # SHINSEKAI SPAWN TO BILLIKEN STATUE
    joy.SET_TWO_AXIS(pyvjoy.HID_USAGE_Y, 0, pyvjoy.HID_USAGE_Z, 0.625, 1.5)
    joy.SET_AXIS(pyvjoy.HID_USAGE_Y, 0, 0.8)

    # BILLIKEN STATUE DIALOGUE
    joy.SET_BUTTON(3, 1, 0.25)
    joy.SET_BUTTON(4, 1)
    joy.SMASH_BUTTON(2, 0.25, 4.5)
    joy.SET_BUTTON(4, 0)

    # MAP CHANGE
    # IN SHINSEKAI
    joy.SET_BUTTON(5, 1, 0.1)
    time.sleep(.75)
    joy.SET_POV(0, 0.1)
    time.sleep(0.1)
    joy.SET_BUTTON(2, 1, 0.1)

    time.sleep(4)  # MAP LOAD

    # IN DONTONBORI
    joy.SET_BUTTON(5, 1, 0.1)
    time.sleep(.75)
    joy.SET_POV(2, 0.1)
    time.sleep(0.1)
    joy.SET_POV(2, 0.1)
    time.sleep(0.1)
    joy.SET_BUTTON(2, 1, 0.1)

    time.sleep(4)  # MAP LOAD

    if currentLoops < loopTimes:
        currentLoops += 1
        DO_LOOP()


DO_LOOP()
