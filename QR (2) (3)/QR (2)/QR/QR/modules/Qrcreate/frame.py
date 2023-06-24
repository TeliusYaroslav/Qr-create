import customtkinter as ctk

class Frame(ctk.CTkFrame):
    def __init__(self, master, width, height, border_width, border_color, fg_color, bg_color, **kwargs):
        super().__init__(master = master, width = width, height = height, border_width = border_width, border_color = border_color, fg_color = fg_color, bg_color = bg_color, **kwargs)