#!/usr/bin/env python3

from PIL import Image
import os

for name, depth in (('main', 5), ('miner_altercation', 4), ('secret_base', 4), ('dojo_temple', 4)):
    dst = 'tiles/{}/'.format(name)
    full = Image.open(name + ".png")

    for zoom in range(depth):
        zoom_dir = "{}/{}/".format(dst, zoom)
        if not os.path.exists(zoom_dir):
            os.makedirs(zoom_dir)
        width = pow(2, zoom)
        zoomed = full.resize((256 * width, 256 * width))
        for tile in range(pow(width, 2)):
            x = int(tile / width)
            y = tile % width
            print(zoom, x, y)
            x_dir = "{}/{}/".format(zoom_dir, x)
            if not os.path.exists(x_dir):
                os.makedirs(x_dir)
            zoomed.crop((256 * x, 256 * y, 256 * (x + 1), 256 * (y + 1))).save("{}/{}/{}.png".format(zoom_dir, x, y))
