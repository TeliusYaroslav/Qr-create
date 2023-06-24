import customtkinter as ctk

SCREEN_HEIGHT = 400
SCREEN_WIDHT = 400

class Screen(ctk.CTk):
    def __init__(self, fg_color):
        super().__init__()
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDHT = SCREEN_WIDHT
        self.X = 200
        self.Y = 200
        self.resizable(False, False)
        self.geometry(f"{self.SCREEN_HEIGHT}x{self.SCREEN_WIDHT}+{self.X}+{self.Y}")
        self.COLOR = fg_color = "darkblue"
        self.title("authorization")
       # self.About()

app = Screen(fg_color="darkblue")

#class About(ctk.CTkToplevel):
#    def create_second_window():
#        about = About()
#        about.grab_set()
        
