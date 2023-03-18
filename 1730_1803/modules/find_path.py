import os

# def find_path(file):
#     # path_file = __file__
#     path_file = __file__.split("/")
#     del path_file[-1]
#     # del path_file[-1]
#     path_file = "/".join(path_file)
#     path_file = os.path.join(path_file, file)
#     return path_file

def find_path(path):
    abs_path = __file__.split("/")
    del abs_path[-1]
    # del abs_path[-1]
    abs_path = "/".join(abs_path)
    abs_path = os.path.join(abs_path, path)
    return abs_path
