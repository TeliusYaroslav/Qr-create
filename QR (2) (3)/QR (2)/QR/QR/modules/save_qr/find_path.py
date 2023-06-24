import customtkinter as ctk
import os

def find_path(filename):
    find_path = __file__
    find_path = find_path.split("/")
    del find_path[-1]
    find_path = "/".join(find_path)
    find_path = os.path.join(find_path, filename)
    return find_path