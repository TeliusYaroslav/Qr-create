import customtkinter as ctk
import modules.Qrcreate.create_sreen as nw_app
import modules.Qrcreate.frame as m_frm

from PIL import Image
import modules.save_qr.find_path as path
import qrcode 
import modules.Qrcreate.datadb as data
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer 
from qrcode.image.styles.colormasks import RadialGradiantColorMask


colors = ["qr color", 'red', 'green', 'blue', 'yellow',"white","black","violet","palegreen","aqua","darkred","orange"]
back_colors = ["back color",'red', 'green', 'blue', 'yellow',"white","black","violet","palegreen","aqua","darkred","orange"]
text = ctk.StringVar()
text2 = ctk.StringVar()
text3 = ctk.StringVar()
#
a = 0
img = qrcode.make()
#
qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L, 
                   box_size=10,
                   border=4)
qr.add_data('Розробники:Богдан Рубанов та Ярослав Теліус')
qr.make(True)
img = qr.make_image(fill_color="black", back_color="white")

#def picture_in_qrcode():
#    img = qr.make_image(image_factory=StyledPilImage, 
#                          embeded_image_path="qr_code1.png")
#    img.save("qrcode2.png")
#picture_in_qrcode()

a = 0
fill_c = "green"
#
def create_qrcode():
    global a, img
    a += 1
    # qr.add_data(text.get())
    # qr.make(True)
    # img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"qr_code{a}.png")
    qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
    label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
    label.place(rely= 0.03, relx=0.22)
# #
def text_input(): 
    font_size = ctk.CTkFont(
                        family= "Arial",
                        size= 20,
                        weight= "bold")
    text_input = ctk.CTkEntry(
    master= nw_app.app,
    width= 250,
    height= 50,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text
    )
    text_input.place(rely = 0.15, relx = 0.2)
#
b = 0
text_input()
label = ctk.CTkLabel(master= nw_app.app, text = "Name")
label.place(rely= 0.1, relx=0.1)
label = ctk.CTkLabel(master= nw_app.app, text = "Password")
label.place(rely= 0.5, relx=0.1)
def text_input2(): 
    font_size = ctk.CTkFont(
                        family= "Arial",
                        size= 20,
                        weight= "bold")
    text_input = ctk.CTkEntry(
    master= nw_app.app,
    width= 250,
    height= 50,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text3
    )
    text_input.place(rely = 0.6, relx = 0.2)
#
text_input2()
def new_w(resizable = False):
    global new_ww
    #data.data.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (text.get(), text3.get()))
    data.connect.commit()
    # data.connect.close()
    new_ww = ctk.CTkToplevel(width = 450, height = 600,fg_color= "darkblue" )
    new_ww.title("Qr create")
    text_name = text.get()
    FRAME1 = m_frm.Frame(master = new_ww, width = 270, height = 270, border_width = 0, border_color = "black", fg_color = "gray", bg_color= "gray")
    FRAME1.place(relx = 0.22, rely = 0.03)
    nw_app.app.withdraw()
    def save_qr(extension):
        global img
        img.save(f"qr_code{a}.{extension}")
    def profile_wind():
        global text, prfil
        prfil = ctk.CTkToplevel(width = 350, height = 400,fg_color="darkblue")
        prfil.title("Profile")
        
        label = ctk.CTkLabel(master= prfil, text = text_name)
        label.place(rely= 0.1, relx=0.6)
        # FRAME2 = ctk.CTkFrame(master = prfil, width = 330, height = 135, border_width = 0, border_color = "black", fg_color = "gray", bg_color= "gray")
        # FRAME2.place(relx = 0, rely= 0.5)
        FRAME2 = ctk.CTkFrame(master = prfil, width = 170, height = 170, border_width = 0, border_color = "black", fg_color = "gray", bg_color= "gray")
        FRAME2.place(relx = 0, rely= 0)
        def add_picture():
            image_name = ctk.filedialog.askopenfile(mode = "r", filetypes= [('Jpg Files', '*.jpg'), ("Png Files","*.png")])
            image_1 = Image.open(path.find_path(image_name.name))
        # image_1 = image_1.resize((100,100), resample= Image.LANCZOS)  
        
            qr1 = ctk.CTkImage(light_image = image_1, size= (170,170))
            label = ctk.CTkLabel(master= prfil, image = qr1, text = "")
            label.place(rely= 0, relx=0)
        def papka_qr():
            path1 = os.path.dirname(os.path.abspath(__file__))
            path1 = path1.split("/")
            del path1[-1]
            # del path1[-1]
            path1 = "/".join(path1)
            os.startfile(path1)
        button_im = ctk.CTkButton(master = prfil, width=50, height=50, fg_color="white",text_color="black", text="Avatar", command = add_picture)
        button_im.place(relx = 0.8, rely = 0.3)
        
        button_qr = ctk.CTkButton(master = prfil, width=50, height=50, fg_color="white",text_color="black", text="History", command = papka_qr)
        button_qr.place(relx = 0.6, rely = 0.3)
        
    def text_generate():
        global img, qr, b  
        b += 0.13
        qr = qrcode.QRCode(version=1, 
                   error_correction=qrcode.constants.ERROR_CORRECT_L, 
                   box_size=10,
                   border=4)  
        qr.add_data(text2.get())
        qr.make(True)
#
        try:
            img = qr.make_image(fill_color=combo_box_color.get(), back_color =combo_back_color.get())
        except:
            try:
                img = qr.make_image(fill_color="black", back_color =combo_back_color.get())
            except:
                try:
                    img = qr.make_image(fill_color=combo_box_color.get(), back_color ="white")
                except:
                    img = qr.make_image(fill_color="black", back_color ="white")
        img.save(f"qr_code{a}.png")
        qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
        label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
        label.place(rely= 0.03, relx=0.22)
        try:
            qr2 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (50,50))
            label = ctk.CTkLabel(master= prfil, image = qr2, text = "")
            label.place(rely= 0.38 + b, relx=0.1)
            label = ctk.CTkLabel(master= prfil, text = text2.get())
            label.place(rely= 0.38 + b, relx=0.4)
        except:
            pass
#
    
    def change_qr_color(color):
        try:
            global img

            # color = combo_box_color.get()
            img = qr.make_image(fill_color=color, back_color=combo_back_color.get())
            img.save(f"qr_code{a}.png")
            qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
            label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
            label.place(rely= 0.03, relx=0.22)
        except:
            pass
#
    def add_logo():
        global img
        image_name = ctk.filedialog.askopenfile(mode = "r", filetypes= [('Jpg Files', '*.jpg'), ("Png Files","*.png")])
        # image_1 = Image.open(path.find_path(image_name.name))
        # image_1 = image_1.resize((100,100), resample= Image.LANCZOS)
        try:
            img = qr.make_image(image_factory=StyledPilImage, embeded_image_path= image_name.name, fill_color=combo_box_color.get(), back_color =combo_back_color.get())
        except:
            try:
                img = qr.make_image(image_factory=StyledPilImage, embeded_image_path= image_name.name, fill_color="black", back_color =combo_back_color.get())
            except:
                try:
                    img = qr.make_image(image_factory=StyledPilImage, embeded_image_path= image_name.name, fill_color=combo_box_color.get(), back_color = "white")
                except:
                    img = qr.make_image(image_factory=StyledPilImage, embeded_image_path= image_name.name, fill_color = "black", back_color = "white")
        img.save(f"qr_code{a}.png")
        qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
        label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
        label.place(rely= 0.03, relx=0.22)
        
    def change_back_color(back_colors):
        global img
        try:
            img = qr.make_image(fill_color=combo_box_color.get(), back_color=back_colors)
            img.save(f"qr_code{a}.png")
            qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
            label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
            label.place(rely= 0.03, relx=0.22)
        except:
            img = qr.make_image(fill_color="white", back_color=back_colors)
            img.save(f"qr_code{a}.png")
            qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
            label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
            label.place(rely= 0.03, relx=0.22)
#
    def text_input2(): 
        font_size = ctk.CTkFont(
                            family= "Arial",
                            size= 20,
                            weight= "bold")
        text_input2 = ctk.CTkEntry(
        master= new_ww,
        width= 200,
        height= 50,
        fg_color= "white",
        text_color= "black",
        font= font_size,
        textvariable= text2
        )
        text_input2.place(rely = 0.9, relx = 0.12)
    text_input2()
    #
    combo_box_color = ctk.CTkComboBox(master=new_ww,values=colors, border_width=3,border_color="black", width = 200, height = 50, fg_color="white", text_color="black",command = change_qr_color)
    combo_box_color.place(relx = 0.04, rely = 0.63)
    #
    combo_back_color = ctk.CTkComboBox(master=new_ww,values=back_colors,border_width=3,border_color="black", width = 200, height = 50, fg_color="white",text_color="black", command = change_back_color)
    combo_back_color.place(relx = 0.53, rely = 0.63)
    #
    button2 = ctk.CTkButton(master = new_ww, width=200,border_width=3,border_color="black", height=50, fg_color="white",text_color="black", text="new-Qr", command = create_qrcode)
    button2.place( relx = 0.04, rely = 0.49)
    #
    button5 = ctk.CTkButton(master = new_ww, width=200, height=50,border_width=3,border_color="black", fg_color="white",text_color="black", text="add-logo", command = add_logo)
    button5.place(relx = 0.53, rely = 0.49)
    #
    def qr_mask():
        global img
        img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(), color_mask=RadialGradiantColorMask())

        img.save(f"qr_code{a}.png")
        qr1 = ctk.CTkImage(light_image = Image.open(f"qr_code{a}.png"), size= (270,270))
        label = ctk.CTkLabel(master= new_ww, image = qr1, text = "")
        label.place(rely= 0.03, relx=0.22)
    button6 = ctk.CTkButton(master = new_ww, width=200, height=50,border_width=3,border_color="black",  fg_color="white",text_color="black", text="variable", command = qr_mask)
    button6.place(relx = 0.04, rely = 0.78)
    #
    combo_box_save = ctk.CTkComboBox(master=new_ww,values=["png","svg","jpg"],border_width=3,border_color="black",  width = 200, height = 50, fg_color="white",text_color= "black", command = save_qr)
    combo_box_save.place(relx = 0.53, rely = 0.78)
    #
    button7 = ctk.CTkButton(master = new_ww, width=50, height=50, border_width=3,border_color="black", fg_color="white",text_color="black", text="create", command = text_generate)
    button7.place(relx = 0.6, rely = 0.9)
    #
    button_open_account = ctk.CTkButton(master = new_ww, width=50,border_width=3,border_color="black", height=50,  fg_color="white",text_color="black", text="Profile", command = profile_wind)
    button_open_account.place(relx = 0.88, rely = 0.01)
    return new_w

button_input = ctk.CTkButton(master = nw_app.app, width=75, height=50,  fg_color="white",text_color="black", text="registration", command = new_w)
button_input.place(relx = 0.4, rely = 0.8)
#