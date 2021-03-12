import pyvjoy
import time

from pyvjoy.constants import HID_USAGE_POV


class JOY_MAPPER():
    def __init__(self, joy: pyvjoy.VJoyDevice) -> None:
        self.joy = joy
        self.axis_def = int(0x8000 * 0.5)

        self.reset()

    ###### HELPERS ######
    def map_toAxis(self, value):
        return int(value * 0x8000)

    def reset(self):
        half = int(0.5 * 0x8000)

        # RESET EVERYTHING
        self.joy.reset()
        self.joy.reset_buttons()
        self.joy.reset_data()
        self.joy.reset_povs()

        # APPLY RESETS
        self.joy.update()

        # RESTORE AXIS TO MIDDLE
        self.joy.set_axis(pyvjoy.HID_USAGE_X, half)
        self.joy.set_axis(pyvjoy.HID_USAGE_Y, half)

        self.joy.set_axis(pyvjoy.HID_USAGE_RX, half)
        self.joy.set_axis(pyvjoy.HID_USAGE_RY, half)

        self.joy.set_axis(pyvjoy.HID_USAGE_Z, half)
        self.joy.set_axis(pyvjoy.HID_USAGE_RZ, half)

    def inverse_state(self, state):
        if state == 1:
            return 0
        return 1

    ###### AXIS ######
    def SET_AXIS(self, axis, value, duration=0):
        print(
            f"SET_AXIS: AXIS '{axis}', VALUE '{value}', DURATION '{duration}' ")

        self.joy.set_axis(axis, self.map_toAxis(value))

        if duration > 0:
            time.sleep(duration)
            self.joy.set_axis(axis, self.axis_def)

    def SET_TWO_AXIS(self, axis_a, value_a, axis_b, value_b, duration=0):
        print(
            f"SET_TWO_AXIS: AXIS_A '{axis_a}' - VAL_A {value_a}, AXIS_B '{axis_b}' - VAL_B {value_b}, DURATION '{duration}' ")

        self.joy.set_axis(axis_a, self.map_toAxis(value_a))
        self.joy.set_axis(axis_b, self.map_toAxis(value_b))

        if duration > 0:
            time.sleep(duration)
            self.joy.set_axis(axis_a, self.axis_def)
            self.joy.set_axis(axis_b, self.axis_def)

    def SET_LSTICK(self, x_val, y_val, duration=0):
        print(
            f"SET_LSTICK: X_VAL '{x_val}', X_VAL '{y_val}', DURATION '{duration}' ")
        self.joy.set_axis(pyvjoy.HID_USAGE_X, self.map_toAxis(x_val))
        self.joy.set_axis(pyvjoy.HID_USAGE_Y, self.map_toAxis(y_val))

        if duration > 0:
            time.sleep(duration)
            self.joy.set_axis(pyvjoy.HID_USAGE_X, self.axis_def)
            self.joy.set_axis(pyvjoy.HID_USAGE_Y, self.axis_def)

    def SET_RSTICK(self, x_val, y_val, duration=0):
        print(
            f"SET_RSTICK: X_VAL '{x_val}', X_VAL '{y_val}', DURATION '{duration}' ")
        self.joy.set_axis(pyvjoy.HID_USAGE_RX, self.axis_def)
        self.joy.set_axis(pyvjoy.HID_USAGE_RY, self.axis_def)

        if duration > 0:
            time.sleep(duration)
            self.joy.set_axis(pyvjoy.HID_USAGE_RX, self.axis_def)
            self.joy.set_axis(pyvjoy.HID_USAGE_RY, self.axis_def)

    ###### BUTTONS ######
    def SET_BUTTON(self, buttonId, state, duration=0):
        print(
            f"SET_BUTTON ID '{buttonId}', STATE {state}, DURATION {duration}")
        self.joy.set_button(buttonId, state)

        if duration > 0:
            time.sleep(duration)
            self.joy.set_button(buttonId, self.inverse_state(state))

    def SMASH_BUTTON(self, buttonId, interval: float, duration: int):
        print(
            f"SMASH_BUTTON ID '{buttonId}', INTERVAL {interval}, DURATION {duration}")

        start = time.time()
        while time.time() - start < duration:
            self.joy.set_button(buttonId, 1)
            time.sleep(interval/2)
            self.joy.set_button(buttonId, 0)
            time.sleep(interval/2)

        self.joy.set_button(buttonId, 0)

    # only 4 DIRECTIONS POV !
    def SET_POV(self, state, duration: int):
        print(
            f"SET_POV STATE {state}, DURATION {duration}")
        self.joy.set_disc_pov(1, state)

        if duration > 0:
            time.sleep(duration)
            self.joy.set_disc_pov(1, -1)
