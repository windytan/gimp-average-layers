#!/usr/bin/env python

from gimpfu import *

def layer_average(img, drw):
  n = len(img.layers)
  for layer in img.layers:
    layer.opacity = 100.0/n
    n = n-1
  img.flatten()

register(
        "python_fu_layer_average",
        "Blend the layers together to create an average image",
        "Blend the layers together to create an average image",
        "Oona Raisanen",
        "Oona Raisanen",
        "2012",
        "<Image>/Image/Average Layers",
        "RGB*, GRAY*",
        [],
        [],
        layer_average)

main()

