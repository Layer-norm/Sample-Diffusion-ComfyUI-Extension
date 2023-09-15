import os
import importlib

NODE_CLASS_MAPPINGS = {}

for node in os.listdir(os.path.dirname(__file__) + os.sep + 'nodes'):
    if node.startswith('EXT_'):
        node = node.split('.')[0]
        node_import = importlib.import_module('custom_nodes.Sample-Diffusion-ComfyUI-Extension.nodes.' + node)
        print('Imported node: ' + node)
        # get class node mappings from py file
        NODE_CLASS_MAPPINGS.update(node_import.NODE_CLASS_MAPPINGS)

