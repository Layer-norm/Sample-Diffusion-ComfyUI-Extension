import os
import importlib
import shutil
from pathlib import Path
import atexit

#####################
# copy playAudio.js #
#####################

CUR_PATH = os.path.join(Path(__file__).parent, 'playAudio.js')
DES_PATH = Path.joinpath(Path(__file__).parents[2], 'web','extensions', 'SampleDiff', 'playAudio.js')

if not os.path.exists(DES_PATH):
    os.makedirs(os.path.dirname(DES_PATH))

    try:
        shutil.copy(CUR_PATH, DES_PATH)
        print("JS File copied successfully.")
    except PermissionError:
        print("Permission denied.")
    except:
        print("Error occurred while copying file.")


############
# addnodes #
############

NODE_CLASS_MAPPINGS = {}

for node in os.listdir(os.path.dirname(__file__) + os.sep + 'nodes'):
    if node.startswith('EXT_'):
        node = node.split('.')[0]
        node_import = importlib.import_module('custom_nodes.Sample-Diffusion-ComfyUI-Extension.nodes.' + node)
        print('Imported node: ' + node)
        # get class node mappings from py file
        NODE_CLASS_MAPPINGS.update(node_import.NODE_CLASS_MAPPINGS)

####################
# remove audio_tmp #
####################

def cleartemp():
    audio_tmp_path = Path.joinpath(Path(__file__).parents[2], "audio_temp")
    
    try:
        os.remove(audio_tmp_path)
    except BaseException:
        ...

atexit.register(cleartemp)
