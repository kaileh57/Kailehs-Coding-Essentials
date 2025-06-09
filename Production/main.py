# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Define your pins here! Based on the schematic:
# SW1 (left) is on GPIO27, which is board.A1 on the XIAO RP2040
# SW2 (middle) is on GPIO28, which is board.A2
# SW3 (right) is on GPIO29, which is board.A3
PINS = [board.A1, board.A2, board.A3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    # When the switch is pressed, it connects the pin to ground.
    value_when_pressed=False,
    # We need to enable the internal pull-up resistors on the pins.
    pull=True,
)

# Here you define the buttons corresponding to the pins
# Left: Ctrl, Middle: C, Right: V
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
keyboard.keymap = [
    [KC.LCTL, KC.C, KC.V],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
