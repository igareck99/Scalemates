import math
from database.db import *
from PIL import Image

def compare(input_hex: str) -> str:
    colors = getAllColor()
    hexes = list(map(lambda x: x.color, colors))
    color_distance_list = []
    input_color = tuple(int(input_hex.upper().lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
    for i in range(len(hexes)):
        use_color = hexes[i]
        my_color = tuple(int(use_color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
        get_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(my_color, input_color)]))
        color_distance_list.append(get_distance)
    sorted_color_distance_list = min(color_distance_list)
    closest_hex = color_distance_list.index(sorted_color_distance_list)
    color = colors[closest_hex]
    return color

def createImage(hex: str):
    rgb = tuple(int(hex.upper().lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    img = Image.new('RGB', (200, 200), rgb)
    return img

def getCompany(value):
    if value == 1:
        return ProducerEnum.VALUE1.value
    if value == 2:
        return ProducerEnum.VALUE1.value
    if value == 3:
        return ProducerEnum.VALUE1.value


#compare('#905919')