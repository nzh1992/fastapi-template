from enum import IntEnum, Enum


class Color(IntEnum):
    RED = 1
    GREEN = 2
    YELLOW = 3


for color in Color:
    print(color.value)



class ColorCut(Enum):
    RED = "a"
    GREEN = "b"
    YELLOW = "c"


for color_cut in ColorCut:
    print(color_cut.value)