#!/usr/bin/env python3

"""
Hijack cairosvg to load svg into our internal data structures.
"""

from cairosvg.parser import Tree
from cairosvg.surface import Surface

from bruhat.argv import argv
from bruhat.render import back
from bruhat.render.flatten import Flatten


class DummySurf(Surface):

    def __init__(self, tree, output, dpi):
    
        W, H = 600., 200. # point == 1/72 inch

        self.context = Flatten()

        self.dpi = dpi

        self._old_parent_node = self.parent_node = None
        self.output = output
        self.font_size = None

        self.context_width = W
        self.context_height = H

        self.cursor_position = [0, 0]
        self.cursor_d_position = [0, 0]
        self.text_path_width = 0
        self.stroke_and_fill = True

        self.tree_cache = {(tree.url, tree.get('id')): tree}

        self.markers = {}
        self.gradients = {}
        self.patterns = {}
        self.masks = {}
        self.paths = {}
        self.filters = {}

        self.map_rgba = None
        self.map_image = None

        self.draw(tree)
    
        #surface.finish()

        self.paths = self.context.paths


def loadsvg(name, dpi=72.):
    assert name.endswith(".svg")
    s = open(name).read()
    tree = Tree(bytestring=s)
    dummy = DummySurf(tree, None, dpi)
    item = back.Compound(dummy.paths)
    return item



if __name__ == "__main__":

    name = argv.next()
    s = open(name).read()
    tree = Tree(bytestring=s)
    my = DummySurf(tree, None, 72.)
    cvs = back.Canvas(my.paths)
    cvs.writePDFfile("output.pdf")





