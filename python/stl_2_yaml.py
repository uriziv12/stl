
import os
import sys
import io
import re

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

# Functions
def string_2_yaml_line(string_i, prefix_for_text=None):
    regex_pttr = "(^\s*)(.*$)"
    regex_result = re.search(regex_pttr, decoded_line_i)
    leading_spaces_i = regex_result.group(1)
    rest_of_line_i = regex_result.group(2)
    ret_val = "{}\"{}\":\n".format(leading_spaces_i, rest_of_line_i)
    if prefix_for_text is not None:
        ret_val = "{}\"{}{}\":\n".format(leading_spaces_i, prefix_for_text, rest_of_line_i)
    return ret_val


# Write yaml file based on stl file
yaml_f = open(yaml_filepath, "w+")
with io.open(stl_filepath, 'rb') as stl_f:
    for line_num_i, line_i in enumerate(stl_f):
        decoded_line_i = line_i.decode("utf-8")
        line_num_formatted_i = '{:>04d}> '.format(line_num_i)
        yaml_line_i = string_2_yaml_line(decoded_line_i, prefix_for_text=line_num_formatted_i)
        yaml_f.write(yaml_line_i)
yaml_f.close()

print("File {} written.".format(yaml_filepath))
