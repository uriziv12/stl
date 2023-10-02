
import os
import sys

SCR_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(SCR_DIR)
STL_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "stl")
YAML_ROOT_DIR = os.path.join(PROJECT_ROOT_DIR, "yaml")

YAML_FILE_EXTENSION = ".yaml"
STL_FILE_EXTENSION = ".stl.txt"

filename = sys.argv[1]
stl_filepath = os.path.join(STL_ROOT_DIR, filename + STL_FILE_EXTENSION)
yaml_filepath = os.path.join(YAML_ROOT_DIR, filename + YAML_FILE_EXTENSION)

with open(stl_filepath, 'rb') as f:
    for line_i in f:
        print(line_i)
