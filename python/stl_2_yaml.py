
import os
import sys
import io

# TODO: add argsparse

# Constants
SCR_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(SCR_DIR)
STL_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "stl")
YAML_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "yaml")

YAML_FILE_EXTENSION = ".yaml"
STL_FILE_EXTENSION = ".stl.txt"

# File names
filename = sys.argv[1]
stl_filepath = os.path.join(STL_ROOT_DIR, filename + STL_FILE_EXTENSION)
yaml_filepath = os.path.join(YAML_ROOT_DIR, filename + YAML_FILE_EXTENSION)

# Write yaml file based on stl file
# yaml_f = open(yaml_filepath, "w+")
yaml_f = open(yaml_filepath, "w+")

with io.open(stl_filepath, 'rb') as stl_f:
    for line_i in stl_f:
        decoded_line_i = line_i.decode("utf-8")
        yaml_f.write(decoded_line_i)

yaml_f.close()
