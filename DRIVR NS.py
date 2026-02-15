print("Importing programs")
print("TKINTER")
import tkinter as tk
print("SUCCESS")
print("TIKINTER - TTK")
from tkinter import ttk
print("SUCCESS")
print("PILLOW")
from PIL import Image, ImageTk
print("SUCCESS")
print("PYFIGLET")
from pyfiglet import Figlet
print("SUCCESS")
print("OS")
import os
print("SUCCESS")
print("WEBBROWSER")
import webbrowser
print("SUCCESS")
print("pywinstyles")
import pywinstyles
print("SUCCESS")

#WARNING: you must run "pip install pygame, pillow, pyfiglet, pywinstyles" for this program to work.
#WARNING: this program will only work on python v3.12 and under, this can be found here(CTRL + Click): https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe
#make sure python interpritor is set to 3.12 (SHIFT + CTRL + P)

#initialize pygame
print("Initilizing PYGAME")
print("PYGAME Launch successful")

#Global
print("Checking directories")
BASEDIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASEDIR, "Icons/DRIVR.ico")


#Tyre background
tyre_image_path = os.path.join(BASEDIR, "Icons/tyre.png")

#Volvo 
Volvo_V50_front_path = os.path.join(BASEDIR, "Cars/VOLVO V50/Volvo V50 Front.jpg")
Volvo_V50_rear_path = os.path.join(BASEDIR, "Cars/VOLVO V50/Volvo V50 Rear.jpg")
Volvo_V50_interior_path = os.path.join(BASEDIR, "Cars/VOLVO V50/VOLVO V50 Interior.jpg")
Volvo_V50_engine_path = os.path.join(BASEDIR, "Cars/VOLVO V50/VOLVO V50 Engine.jpg")

#Golf
Golf_GTI_front_path = os.path.join(BASEDIR, "Cars/Golf GTI/Golf GTI Front.jpg")
Golf_GTI_Rear_path = os.path.join(BASEDIR, "Cars/Golf GTI/Golf GTI Rear.jpg")
Golf_GTI_interior_path = os.path.join(BASEDIR, "Cars/Golf GTI/Golf GTI Interior.jpg")
Golf_GTI_engine_path = os.path.join(BASEDIR, "Cars/Golf GTI/Golf GTI Engine.png")

#Focus
Focus_RS_front_path = os.path.join(BASEDIR, "Cars/Focus RS/FocusRS Main.jpg")
Focus_RS_Rear_path = os.path.join(BASEDIR, "Cars/Focus RS/FocusRS Rear.jpg")
Focus_RS_interior_path = os.path.join(BASEDIR, "Cars/Focus RS/FocusRS Interior.jpg")
Focus_RS_engine_path = os.path.join(BASEDIR, "Cars/Focus RS/FocusRS Engine.jpg")

#Skyline_GTR
Skyline_GTR_front_path = os.path.join(BASEDIR, "Cars/Nissan Skyline/GTR Main.jpg")
Skyline_GTR_Rear_path = os.path.join(BASEDIR, "Cars/Nissan Skyline/GTR Rear.jpg")
Skyline_GTR_interior_path = os.path.join(BASEDIR, "Cars/Nissan Skyline/GTR Interior.png")
Skyline_GTR_engine_path = os.path.join(BASEDIR, "Cars/Nissan Skyline/GTR Engine.jpg")

#Tesla S
Tesla_S_front_path = os.path.join(BASEDIR, "Cars/Tesla S/Telsa S Main.jpg")
Tesla_S_Rear_path = os.path.join(BASEDIR, "Cars/Tesla S/Tesla S Rear.jpg")
Tesla_S_interior_path = os.path.join(BASEDIR, "Cars/Tesla S/Tesla S Interior.jpg")
Tesla_S_engine_path = os.path.join(BASEDIR, "Cars/Tesla S/Telsa S Frunk.jpg")

#Koenigsegg Jesko Absolut
Koenigsegg_Jesko_Absolut_front_path = os.path.join(BASEDIR, "Cars/Koenigsegg Jesko Absolut/Koenigsegg Jesko Absolut Main.jpg")
Koenigsegg_Jesko_Absolut_rear_path = os.path.join(BASEDIR, "Cars/Koenigsegg Jesko Absolut/Koenigsegg Jesko Absolut Rear.jpg")
Koenigsegg_Jesko_Absolut_interior_path = os.path.join(BASEDIR, "Cars/Koenigsegg Jesko Absolut/Koenigsegg Jesko Absolut Interior.jpg")
Koenigsegg_Jesko_Absolut_engine_path = os.path.join(BASEDIR, "Cars/Koenigsegg Jesko Absolut/Koenigsegg Jesko Absolut Engine.jpg")


print("Success")

#Variables
print("Initializing variables")
specs_visible = False
desc_label = None
interior_label = None
rear_label = None
Volvo_extras_frame = None

Golf_extras_frame = None
Golf_interior_label = None
Golf_rear_label = None

FocusRS_interior_label = None
FocusRS_rear_label = None

Skyline_GTR_interior_label = None
Skyline_GTR_rear_label = None

Tesla_S_interior_label = None
Tesla_S_rear_label = None

Koenigsegg_Jesko_Absolut_interior_label = None
Koenigsegg_Jesko_Absolut_rear_label = None 

#General controls
#Backgrounds
Golf_Frame_BG = "#7F7F7F"
Volvo_Frame_BG = "#998B74"
FocusRS_Frame_BG = "#3366BD"
Skyline_GTR_Frame_BG = "#708A8E"
Tesla_S_Frame_BG = "#CE1E1E"
Koenigsegg_Jesko_Absolut_Frame_BG = "#16BF3D"

#Padding
Home_padding_X = 20
Home_padding_Y = 10

#BorderWidth
Home_border_width = 4

#Image sizes
image_size_home = 400, 200
Image_size_car_screen = 350, 250

#Figlet
print("Initializing Figlet")
fig = Figlet(font="slant")
print("Success")
#music

print("Launching DRIVR")
#Creating home window
Home = tk.Tk()
Home.title("DRIVR - Digital Reference & Interactive Vehicle Registry")
Home.geometry("1920x1080")
Home.iconbitmap(icon_path)
pywinstyles.apply_style(Home, "dark") 
music_var = tk.BooleanVar(value=True)
rainbow_var = tk.BooleanVar(value=False)

#Creating Home Frame
Home_Frame = tk.Frame(Home, bg="#2D2D2D", padx=10, pady=10)
Home_Frame.pack(fill="both", expand=True)
print("DRIVR Launched!")
Home_Content_Frame = tk.Frame(Home_Frame, bg="#2D2D2D")

# Load tyre image
tyre_original = Image.open(tyre_image_path)
tyre_resized = tyre_original.resize((1920, 1920))  # Adjust size as needed
tyre_photo = ImageTk.PhotoImage(tyre_resized)

# Create tyre label with transparent background
tyre_label = tk.Label(
    Home_Content_Frame,
    image=tyre_photo,
    bg="#2D2D2D", 
    borderwidth=0
)
tyre_label.image = tyre_photo
tyre_label.place(x=-100, y=-500)
tyre_label.lower() 

Volvo_Frame = tk.Frame(Home_Frame, bg=Volvo_Frame_BG)
Golf_Frame = tk.Frame(Home_Frame, bg=Golf_Frame_BG)
FocusRS_Frame = tk.Frame(Home_Frame, bg=FocusRS_Frame_BG)
Skyline_GTR_Frame = tk.Frame(Home_Frame, bg=Skyline_GTR_Frame_BG)
Tesla_S_Frame = tk.Frame(Home_Frame, bg=Tesla_S_Frame_BG)
Koenigsegg_Jesko_Absolut_Frame = tk.Frame(Home_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG)

#clears any frames other than home when here
Home_Content_Frame.pack(fill="both", expand=True)
Volvo_Frame.pack_forget()
Golf_Frame.pack_forget()
FocusRS_Frame.pack_forget()
Skyline_GTR_Frame.pack_forget()
Tesla_S_Frame.pack_forget()
Koenigsegg_Jesko_Absolut_Frame.pack_forget()
# Dim overlay
dim_Frame = tk.Frame(Home, bg="#1a1a1a")

print("Loading cars")
print("VOLVO V50")

# Frames for Volvo
Volvo_image_Frame = tk.Frame(Volvo_Frame, bg=Volvo_Frame_BG)
Volvo_specs_Frame = tk.Frame(Volvo_Frame, bg=Volvo_Frame_BG)
Volvo_desc_Frame = tk.Frame(Volvo_Frame, bg=Volvo_Frame_BG)

Volvo_image_Frame.grid(row=0, column=0, padx=Home_padding_X, pady=20, sticky="nw")
Volvo_specs_Frame.grid(row=0, column=1, rowspan=2, padx=Home_padding_X, pady=20, sticky="n")
Volvo_desc_Frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")

#Images for Volvo
Volvo_V50_original = Image.open(Volvo_V50_front_path)
photo_small = ImageTk.PhotoImage(Volvo_V50_original.resize((Image_size_car_screen)))
photo_large = ImageTk.PhotoImage(Volvo_V50_original.resize((image_size_home)))

Volvo_Engine = Image.open(Volvo_V50_engine_path)
Volvo_engine_photo_small = ImageTk.PhotoImage(Volvo_Engine.resize((Image_size_car_screen)))
Volvo_engine_photo_large = ImageTk.PhotoImage(Volvo_Engine.resize((image_size_home)))

Volvo_V50_interior = Image.open(Volvo_V50_interior_path)
photo_interior_small = ImageTk.PhotoImage(Volvo_V50_interior.resize((Image_size_car_screen)))
photo_interior_large = ImageTk.PhotoImage(Volvo_V50_interior.resize((image_size_home)))

Volvo_V50_rear = Image.open(Volvo_V50_rear_path)
photo_rear_small = ImageTk.PhotoImage(Volvo_V50_rear.resize((Image_size_car_screen)))
photo_rear_large = ImageTk.PhotoImage(Volvo_V50_rear.resize((image_size_home)))

print("Volkswagen Golf GTI MK4")
#Fames for golf
Golf_image_Frame = tk.Frame(Golf_Frame, bg=Golf_Frame_BG)
Golf_specs_Frame = tk.Frame(Golf_Frame, bg=Golf_Frame_BG)
Golf_desc_Frame = tk.Frame(Golf_Frame, bg=Golf_Frame_BG)

Golf_image_Frame.grid(row=0, column=0, padx=Home_padding_X, pady=20, sticky="nw")
Golf_specs_Frame.grid(row=0, column=1, rowspan=2, padx=Home_padding_X, pady=20, sticky="n")
Golf_desc_Frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")

#Images for golf
Golf_original = Image.open(Golf_GTI_front_path)
Golf_small = Golf_original.resize((Image_size_car_screen))
golf_photo_small = ImageTk.PhotoImage(Golf_small)

Golf_photo_large = Golf_original.resize((image_size_home))
Golf_photo_large = ImageTk.PhotoImage(Golf_photo_large)

Golf_Engine_photo = Image.open(Golf_GTI_engine_path)
Golf_engine_small = Golf_Engine_photo.resize((Image_size_car_screen))
Golf_engine_photo_small = ImageTk.PhotoImage(Golf_engine_small)

Golf_interior = Image.open(Golf_GTI_interior_path)
Golf_interior_small = Golf_interior.resize((Image_size_car_screen))
golf_photo_interior_small = ImageTk.PhotoImage(Golf_interior_small)

Golf_rear = Image.open(Golf_GTI_Rear_path)
Golf_rear_small = Golf_rear.resize((Image_size_car_screen))
golf_photo_rear_small = ImageTk.PhotoImage(Golf_rear_small)

print("Ford Focus RS")
#Frames for Focus
FocusRS_image_Frame = tk.Frame(FocusRS_Frame, bg=FocusRS_Frame_BG)
FocusRS_specs_Frame = tk.Frame(FocusRS_Frame, bg=FocusRS_Frame_BG)
FocusRS_desc_Frame = tk.Frame(FocusRS_Frame, bg=FocusRS_Frame_BG)
FocusRS_extras_frame = tk.Frame(FocusRS_Frame, bg=FocusRS_Frame_BG)

FocusRS_image_Frame.grid(row=0, column=0, padx=Home_padding_X, pady=20, sticky="nw")
FocusRS_specs_Frame.grid(row=0, column=1, rowspan=2, padx=Home_padding_X, pady=20, sticky="n")
FocusRS_desc_Frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")
FocusRS_extras_frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")

#Images for Focus
FocusRS_original = Image.open(Focus_RS_front_path)
FocusRS_small = FocusRS_original.resize((Image_size_car_screen))
FocusRS_photo_small = ImageTk.PhotoImage(FocusRS_small)

FocusRS_photo_large = FocusRS_original.resize((image_size_home))
FocusRS_photo_large = ImageTk.PhotoImage(FocusRS_photo_large)

FocusRS_Engine_photo = Image.open(Focus_RS_engine_path)
FocusRS_engine_small = FocusRS_Engine_photo.resize((Image_size_car_screen))
FocusRS_engine_photo_small = ImageTk.PhotoImage(FocusRS_engine_small)

FocusRS_interior = Image.open(Focus_RS_interior_path)
FocusRS_interior_small = FocusRS_interior.resize((Image_size_car_screen))
FocusRS_photo_interior_small = ImageTk.PhotoImage(FocusRS_interior_small)

FocusRS_rear = Image.open(Focus_RS_Rear_path)
FocusRS_rear_small = FocusRS_rear.resize((Image_size_car_screen))
FocusRS_photo_rear_small = ImageTk.PhotoImage(FocusRS_rear_small)

print("Nissan Skyline GTR")
#Frames for GTR
Skyline_GTR_image_Frame = tk.Frame(Skyline_GTR_Frame, bg=Skyline_GTR_Frame_BG)
Skyline_GTR_specs_Frame = tk.Frame(Skyline_GTR_Frame, bg=Skyline_GTR_Frame_BG)
Skyline_GTR_desc_Frame = tk.Frame(Skyline_GTR_Frame, bg=Skyline_GTR_Frame_BG)
Skyline_GTR_extras_frame = tk.Frame(Skyline_GTR_Frame, bg=Skyline_GTR_Frame_BG)

Skyline_GTR_image_Frame.grid(row=0, column=0, padx=Home_padding_X, pady=20, sticky="nw")
Skyline_GTR_specs_Frame.grid(row=0, column=1, rowspan=2, padx=Home_padding_X, pady=20, sticky="n")
Skyline_GTR_desc_Frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")
Skyline_GTR_extras_frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")

#Images for GTR
Skyline_GTR_original = Image.open(Skyline_GTR_front_path)
Skyline_GTR_small = Skyline_GTR_original.resize((Image_size_car_screen))
Skyline_GTR_photo_small = ImageTk.PhotoImage(Skyline_GTR_small)

Skyline_GTR_photo_large = Skyline_GTR_original.resize((image_size_home))
Skyline_GTR_photo_large = ImageTk.PhotoImage(Skyline_GTR_photo_large)

Skyline_GTR_Engine_photo = Image.open(Skyline_GTR_engine_path)
Skyline_GTR_engine_small = Skyline_GTR_Engine_photo.resize((Image_size_car_screen))
Skyline_GTR_engine_photo_small = ImageTk.PhotoImage(Skyline_GTR_engine_small)

Skyline_GTR_interior = Image.open(Skyline_GTR_interior_path)
Skyline_GTR_interior_small = Skyline_GTR_interior.resize((Image_size_car_screen))
Skyline_GTR_photo_interior_small = ImageTk.PhotoImage(Skyline_GTR_interior_small)

Skyline_GTR_rear = Image.open(Skyline_GTR_Rear_path)
Skyline_GTR_rear_small = Skyline_GTR_rear.resize((Image_size_car_screen))
Skyline_GTR_photo_rear_small = ImageTk.PhotoImage(Skyline_GTR_rear_small)

print("Tesla Model S")
#Frames for Tesla
Tesla_S_image_Frame = tk.Frame(Tesla_S_Frame, bg=Tesla_S_Frame_BG)
Tesla_S_specs_Frame = tk.Frame(Tesla_S_Frame, bg=Tesla_S_Frame_BG)
Tesla_S_desc_Frame = tk.Frame(Tesla_S_Frame, bg=Tesla_S_Frame_BG)
Tesla_S_extras_frame = tk.Frame(Tesla_S_Frame, bg=Tesla_S_Frame_BG)

Tesla_S_image_Frame.grid(row=0, column=0, padx=Home_padding_X, pady=20, sticky="nw")
Tesla_S_specs_Frame.grid(row=0, column=1, rowspan=2, padx=Home_padding_X, pady=20, sticky="n")
Tesla_S_desc_Frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")
Tesla_S_extras_frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")

#Images for Tesla
Tesla_S_original = Image.open(Tesla_S_front_path)
Tesla_S_small = Tesla_S_original.resize((Image_size_car_screen))
Tesla_S_photo_small = ImageTk.PhotoImage(Tesla_S_small)

Tesla_S_photo_large = Tesla_S_original.resize((image_size_home))
Tesla_S_photo_large = ImageTk.PhotoImage(Tesla_S_photo_large)

Tesla_S_Engine_photo = Image.open(Tesla_S_engine_path)
Tesla_S_engine_small = Tesla_S_Engine_photo.resize((Image_size_car_screen))
Tesla_S_engine_photo_small = ImageTk.PhotoImage(Tesla_S_engine_small)

Tesla_S_interior = Image.open(Tesla_S_interior_path)
Tesla_S_interior_small = Tesla_S_interior.resize((Image_size_car_screen))
Tesla_S_photo_interior_small = ImageTk.PhotoImage(Tesla_S_interior_small)

Tesla_S_rear = Image.open(Tesla_S_Rear_path)
Tesla_S_rear_small = Tesla_S_rear.resize((Image_size_car_screen))
Tesla_S_photo_rear_small = ImageTk.PhotoImage(Tesla_S_rear_small)

#Frames for Tesla
Koenigsegg_Jesko_Absolut_image_Frame = tk.Frame(Koenigsegg_Jesko_Absolut_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG)
Koenigsegg_Jesko_Absolut_specs_Frame = tk.Frame(Koenigsegg_Jesko_Absolut_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG)
Koenigsegg_Jesko_Absolut_desc_Frame = tk.Frame(Koenigsegg_Jesko_Absolut_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG)
Koenigsegg_Jesko_Absolut_extras_frame = tk.Frame(Koenigsegg_Jesko_Absolut_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG)

Koenigsegg_Jesko_Absolut_image_Frame.grid(row=0, column=0, padx=Home_padding_X, pady=20, sticky="nw")
Koenigsegg_Jesko_Absolut_specs_Frame.grid(row=0, column=1, rowspan=2, padx=Home_padding_X, pady=20, sticky="n")
Koenigsegg_Jesko_Absolut_desc_Frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")
Koenigsegg_Jesko_Absolut_extras_frame.grid(row=1, column=0, padx=Home_padding_X, pady=5, sticky="n")

#Images for Tesla
Koenigsegg_Jesko_Absolut_original = Image.open(Koenigsegg_Jesko_Absolut_front_path)
Koenigsegg_Jesko_Absolut_small = Koenigsegg_Jesko_Absolut_original.resize((Image_size_car_screen))
Koenigsegg_Jesko_Absolut_photo_small = ImageTk.PhotoImage(Koenigsegg_Jesko_Absolut_small)

Koenigsegg_Jesko_Absolut_photo_large = Koenigsegg_Jesko_Absolut_original.resize((image_size_home))
Koenigsegg_Jesko_Absolut_photo_large = ImageTk.PhotoImage(Koenigsegg_Jesko_Absolut_photo_large)

Koenigsegg_Jesko_Absolut_Engine_photo = Image.open(Koenigsegg_Jesko_Absolut_engine_path)
Koenigsegg_Jesko_Absolut_engine_small = Koenigsegg_Jesko_Absolut_Engine_photo.resize((Image_size_car_screen))
Koenigsegg_Jesko_Absolut_engine_photo_small = ImageTk.PhotoImage(Koenigsegg_Jesko_Absolut_engine_small)

Koenigsegg_Jesko_Absolut_interior = Image.open(Koenigsegg_Jesko_Absolut_interior_path)
Koenigsegg_Jesko_Absolut_interior_small = Koenigsegg_Jesko_Absolut_interior.resize((Image_size_car_screen))
Koenigsegg_Jesko_Absolut_photo_interior_small = ImageTk.PhotoImage(Koenigsegg_Jesko_Absolut_interior_small)

Koenigsegg_Jesko_Absolut_rear = Image.open(Koenigsegg_Jesko_Absolut_rear_path)
Koenigsegg_Jesko_Absolut_rear_small = Koenigsegg_Jesko_Absolut_rear.resize((Image_size_car_screen))
Koenigsegg_Jesko_Absolut_photo_rear_small = ImageTk.PhotoImage(Koenigsegg_Jesko_Absolut_rear_small)


# Main car labels
Volvo_V50_label = tk.Label(Home_Content_Frame, image=photo_large, bg=Volvo_Frame_BG, borderwidth=Home_border_width, relief="solid", cursor="hand2")
Volvo_V50_label.grid(row=3, column=0)

Golf_GTI_label = tk.Label(Home_Content_Frame, image=Golf_photo_large, bg=Volvo_Frame_BG, borderwidth=Home_border_width, relief="solid", cursor="hand2")
Golf_GTI_label.grid(row=4, column=0, pady=Home_padding_Y)

Focus_RS_label = tk.Label(Home_Content_Frame, image=FocusRS_photo_large, bg=Volvo_Frame_BG, borderwidth=Home_border_width, relief="solid", cursor="hand2")
Focus_RS_label.grid(row=3, column=1, pady=Home_padding_Y, padx=Home_padding_X)

Skyline_GTR_label = tk.Label(Home_Content_Frame, image=Skyline_GTR_photo_large, bg=Volvo_Frame_BG, borderwidth=Home_border_width, relief="solid", cursor="hand2")
Skyline_GTR_label.grid(row=4, column=1, pady=Home_padding_Y, padx=Home_padding_X)

Tesla_S_label = tk.Label(Home_Content_Frame, image=Tesla_S_photo_large, bg=Volvo_Frame_BG, borderwidth=Home_border_width, relief="solid", cursor="hand2")
Tesla_S_label.grid(row=3, column=2, pady=Home_padding_Y, padx=Home_padding_X)

Koenigsegg_Jesko_Absolut_label = tk.Label(Home_Content_Frame, image=Koenigsegg_Jesko_Absolut_photo_large, bg=Koenigsegg_Jesko_Absolut_Frame_BG, borderwidth=Home_border_width, relief="solid", cursor="hand2")
Koenigsegg_Jesko_Absolut_label.grid(row=4, column=2, pady=Home_padding_Y, padx=Home_padding_X)
#DRIVR Title

DRIVR_TITLE = ttk.Label(
    Home_Content_Frame,
    text="DRIVR",
    font=("Calibri", 36, "bold", "italic"),
    background="#1a1a1a",
    foreground="white"
)
DRIVR_TITLE.grid(row=0, column=0, pady=5, padx=0)
DRIVR_SUBTITLE = ttk.Label(
    Home_Content_Frame,
    text="Digital Reference & Interactive Vehicle Registry",
    font=("Calibri", 16, "italic"),
    background="#1a1a1a",
    foreground="white"
)
DRIVR_SUBTITLE.grid(row=1, column=0, pady=5)

settings_frame = tk.Frame(Home_Content_Frame, bg="#2D2D2D")
settings_frame.grid(row=2, column=0, pady=10)

print("Initilizing Functions")

#rainbow colours
rainbow_colors = ["red", "orange", "yellow", "green", "cyan", "teal", "lime",
 "indigo", "violet", "purple", "magenta", "pink", "gold", "white"]
rainbow_widgets = []
#rainbow function
def start_rainbow(root, i=0):
    if rainbow_var.get():  # Only run if rainbow is enabled
        colour = rainbow_colors[i]
        for widget in rainbow_widgets:
            try:
                widget.config(fg=colour)
            except:
                pass
        root.after(800, start_rainbow, root, (i+1) % len(rainbow_colors))
    else:
        # Reset to white when disabled
        for widget in rainbow_widgets:
            try:
                widget.config(fg="white")
            except:
                pass
        root.after(400, start_rainbow, root, i)  # Keep checking

#Show car spec fuctions
def show_volvo_specs(event:None):
        global specs_visible, desc_label, interior_label, rear_label, Volvo_extras_frame

    # hides home, goes to volvo screen
        Home_Content_Frame.pack_forget()
        Volvo_Frame.pack(fill="both", expand=True)
        if specs_visible:
            return

        #deletes previos image removing duplication
        for widget in Volvo_image_Frame.winfo_children():
            widget.destroy()

        # Enlarge main car image
        Volvo_V50_label.configure(image=photo_large, cursor="")
        Volvo_V50_label.image = photo_large

        # Dim background
        dim_Frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        Home_Frame.configure(bg=Volvo_Frame_BG)
        Volvo_image_Frame.configure(bg=Volvo_Frame_BG)
        Volvo_specs_Frame.configure(bg=Volvo_Frame_BG)
        Volvo_desc_Frame.configure(bg=Volvo_Frame_BG)
        Home_Frame.lift()
        
        # Clear previous specs
        for widget in Volvo_specs_Frame.winfo_children():
            widget.destroy()

        # Specs header
        tk.Label(Volvo_specs_Frame, text="SPECIFICATIONS:", font=("Calibri", 35, "bold", "italic"), bg=Volvo_Frame_BG, fg="white").pack(anchor="w")

        # Specs details
        v50_specs = {
            "Make": "Volvo",
            "Model": "V50",
            "Trim level": "SE",
            "Year": "2008",
            "Generation": "First Generation",
            "Body style": "Station Wagon",
            "Engine": "1.8L I4",
            "Horsepower": "125 hp",
            "Transmission": "5-speed manual / 5-speed automatic",
            "Torque": "160 Nm",
            "0-60 mph": "10.5 s",
            "Top Speed": "125 mph",
            "Fuel Economy": "25 mpg city / 32 mpg highway",
            "Seating Capacity": "5",
            "Drive Type": "FWD",
            "Suspension": "Independent front and rear",
            "Brakes": "Disc brakes all round",
            "Fuel Tank Capacity": "60 L",
            "Boot Space": "430 L (expandable with seats folded)",
            "Insurance cost like": "Cheap as chips"
            
        }

        for key, value in v50_specs.items():
            tk.Label(Volvo_specs_Frame, bg=Volvo_Frame_BG, fg="white", font=("Calibri", 16), text=f"{key}: {value}").pack(anchor="w")

        # Description label
        desc_label = tk.Label(Volvo_desc_Frame, text="'Slick grandad's car'", font=("Calibri", 45, "italic"), bg=Volvo_Frame_BG, fg="white")
        desc_label.grid(row=0, column=0, pady=0)

        desc_label = tk.Label(Volvo_desc_Frame, text="Shame they only drive at 20mph.", font=("Calibri", 22, "italic"), bg=Volvo_Frame_BG, fg="white")
        desc_label.grid(row=1, column=0, pady=0)

    # Extra images stacked horizontally under the main car
        Volvo_extras_frame = tk.Frame(Volvo_image_Frame, bg=Volvo_Frame_BG)
        Volvo_extras_frame.pack(side="bottom", padx=0, pady=5, anchor="w")

        Volvo_label = tk.Label(Volvo_image_Frame, image=photo_small, bg="#000", borderwidth=2, relief="solid", cursor="hand2")
        Volvo_label.image = photo_small
        Volvo_label.pack(side="left", padx=5, pady=0)

        Volvo_engine_label = tk.Label(Volvo_image_Frame, image=Volvo_engine_photo_small, bg="#000", borderwidth=2, relief="solid", cursor="hand2")
        Volvo_engine_label.image = Volvo_engine_photo_small
        Volvo_engine_label.pack(side="left", padx=5, pady=0)

        interior_label = tk.Label(Volvo_extras_frame, image=photo_interior_small, bg="#000", borderwidth=2, relief="solid", cursor="hand2")
        interior_label.image = photo_interior_small
        interior_label.pack(side="left", padx=5, pady=0)

        rear_label = tk.Label(Volvo_extras_frame, image=photo_rear_small, bg="#000", borderwidth=2, relief="solid", cursor="hand2")
        rear_label.image = photo_rear_small
        rear_label.pack(side="left", padx=5, pady=0)

        # Back button
        create_back_button(Volvo_specs_Frame, back_to_home)

        specs_visible = True

def show_golf_specs(event:None):
    global specs_visible, desc_label, interior_label, rear_label
    global Golf_extras_frame, FocusRS_interior_label, FocusRS_rear_label

    # hides home, goes to volvo screen
    Home_Content_Frame.pack_forget()
    Golf_Frame.pack(fill="both", expand=True)
    if specs_visible:
        return

    #deletes previos image removing duplication
    for widget in Golf_image_Frame.winfo_children():
        widget.destroy()

    # Enlarge main car image
    Golf_GTI_label.configure(image=Golf_photo_large, cursor="")
    Golf_GTI_label.image = Golf_photo_large

    # Dim background
    dim_Frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    Home_Frame.configure(bg=Golf_Frame_BG)
    Golf_image_Frame.configure(bg=Golf_Frame_BG)
    Golf_specs_Frame.configure(bg=Golf_Frame_BG)
    Golf_desc_Frame.configure(bg=Golf_Frame_BG)
    Home_Frame.lift()

    # Clear previous specs
    for widget in Golf_specs_Frame.winfo_children():
        widget.destroy()

    # Specs header
    tk.Label(Golf_specs_Frame, text="SPECIFICATIONS:", font=("Calibri", 35, "bold", "italic"), bg=Golf_Frame_BG, fg="white").pack(anchor="w")

    # Specs details
    Golf_GTI_specs = {
        "Make": "Volkswagen",
        "Model": "Golf GTI 1.8T 180",
        "Year": "2002",
        "Generation": "Mark 4",
        "Engine": "1.8L Turbocharged I4 20V",
        "Horsepower": "180 hp @ 5800 rpm",
        "Torque": "235 Nm @ 1800–5000 rpm",
        "Transmission": "5-speed manual / 6-speed manual (some markets)",
        "0–60 mph": "6.9 s",
        "Top Speed": "140 mph",
        "Drive Type": "FWD",
        "Body Style": "3-door or 5-door Hatchback",
        "Fuel Economy": "25 mpg city / 33 mpg highway",
        "Seating Capacity": "5",
        "Suspension": "Independent front, torsion beam rear",
        "Brakes": "Disc brakes all round",
        "Fuel Tank Capacity": "55 L",
        "Boot Space": "330 L",
        "Insurance cost like": "Moderate",
    }

    for key, value in Golf_GTI_specs.items():
        tk.Label(Golf_specs_Frame, bg=Golf_Frame_BG, fg="white", font=("Calibri", 16), text=f"{key}: {value}").pack(anchor="w")

    # Description label
    Golf_desc_label = tk.Label(Golf_desc_Frame, text="'Old but gold.'", font=("Calibri", 45, "italic"), bg=Golf_Frame_BG, fg="white")
    Golf_desc_label.grid(row=0, column=0, pady=0)

    Golf_desc_label = tk.Label(Golf_desc_Frame, text="Great time with a great car.", font=("Calibri", 22, "italic"), bg=Golf_Frame_BG, fg="white")
    Golf_desc_label.grid(row=1, column=0, pady=0)

    # Extra images stacked horizontally under the main car
    Golf_extras_frame = tk.Frame(Golf_image_Frame, bg=Golf_Frame_BG)
    Golf_extras_frame.pack(side="bottom", padx=0, pady=5, anchor="w")

    Golf_main_label = tk.Label(Golf_image_Frame, image=golf_photo_small, bg=Golf_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Golf_main_label.image = golf_photo_small
    Golf_main_label.pack(side="left", padx=5, pady=0)

    Golf_engine_label = tk.Label(Golf_image_Frame, image=Golf_engine_photo_small, bg=Golf_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Golf_engine_label.image = Golf_engine_photo_small
    Golf_engine_label.pack(side="left", padx=5, pady=0)

    Golf_interior_label = tk.Label(Golf_extras_frame, image=golf_photo_interior_small, bg=Golf_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Golf_interior_label.image = golf_photo_interior_small
    Golf_interior_label.pack(side="left", padx=5, pady=0)

    Golf_rear_label = tk.Label(Golf_extras_frame, image=golf_photo_rear_small, bg=Golf_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Golf_rear_label.image = golf_photo_rear_small
    Golf_rear_label.pack(side="left", padx=5, pady=0)

    # Back button
    create_back_button(Golf_specs_Frame, back_to_home)

    specs_visible = True

def show_focus_specs(event:None):
    global specs_visible, desc_label, interior_label, rear_label
    global FocusRS_extras_frame, FocusRS_interior_label, FocusRS_rear_label

    # hides home, goes to volvo screen
    Home_Content_Frame.pack_forget()
    FocusRS_Frame.pack(fill="both", expand=True)
    if specs_visible:
        return

    #deletes previos image removing duplication
    for widget in FocusRS_image_Frame.winfo_children():
        widget.destroy()

    # Enlarge main car image
    Focus_RS_label.configure(image=FocusRS_photo_large, cursor="")
    Focus_RS_label.image = FocusRS_photo_large

    # Dim background
    dim_Frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    Home_Frame.configure(bg=FocusRS_Frame_BG)
    FocusRS_image_Frame.configure(bg=FocusRS_Frame_BG)
    FocusRS_specs_Frame.configure(bg=FocusRS_Frame_BG)
    FocusRS_desc_Frame.configure(bg=FocusRS_Frame_BG)
    Home_Frame.lift()

    # Clear previous specs
    for widget in FocusRS_specs_Frame.winfo_children():
        widget.destroy()

    # Specs header
    header = tk.Label(
        FocusRS_specs_Frame,
        text="SPECIFICATIONS:",
        font=("Calibri", 35, "bold", "italic"),
        bg=FocusRS_Frame_BG,
        fg="white"
    )
    header.pack(anchor="w")
    rainbow_widgets.append(header)

    # Specs details
    FocusRS_specs = {
        "Make": "Ford",
        "Model": "Focus RS",
        "Year": "2016",
        "Generation": "3rd Gen (Mk3)",
        "Engine": "2.3L Turbocharged EcoBoost I4",
        "Horsepower": "350 hp @ 6000 rpm",
        "Torque": "440 Nm (470 Nm overboost) @ 2000–4500 rpm",
        "Transmission": "6-speed manual",
        "0–60 mph": "4.7 s",
        "Top Speed": "165 mph",
        "Drive Type": "AWD (Dynamic Torque Vectoring)",
        "Body Style": "5-door Hatchback",
        "Fuel Economy": "22 mpg city / 30 mpg highway (approx.)",
        "Seating Capacity": "5",
        "Suspension": "Independent front and rear with selectable drive modes",
        "Brakes": "Brembo ventilated discs (350mm front)",
        "Fuel Tank Capacity": "52 L",
        "Boot Space": "260 L",
        "Insurance cost like": "Through the roof!",
    }

    for key, value in FocusRS_specs.items():
        lbl = tk.Label(
            FocusRS_specs_Frame,
            bg=FocusRS_Frame_BG,
            fg="white",
            font=("Calibri", 16),
            text=f"{key}: {value}"
        )
        lbl.pack(anchor="w")
        rainbow_widgets.append(lbl)

    # Description labels
    
    FocusRS_desc_label = tk.Label(
        FocusRS_desc_Frame,
        text="'Boy racers drive this car.'",
        font=("Calibri", 45, "italic"),
        bg=FocusRS_Frame_BG,
        fg="white"
    )
    FocusRS_desc_label.grid(row=0, column=0, pady=0)
    rainbow_widgets.append(FocusRS_desc_label)


    FocusRS_desc_label2 = tk.Label(
        FocusRS_desc_Frame,
        text="'Thats all I'll Say.'",
        font=("Calibri", 22, "italic"),
        bg=FocusRS_Frame_BG,
        fg="white"
    )
    FocusRS_desc_label2.grid(row=1, column=0, pady=0)
    rainbow_widgets.append(FocusRS_desc_label2)
    # Extra images stacked horizontally under the main car
    FocusRS_extras_frame = tk.Frame(FocusRS_image_Frame, bg=FocusRS_Frame_BG)
    FocusRS_extras_frame.pack(side="bottom", padx=0, pady=5, anchor="w")

    FocusRS_main_label = tk.Label(FocusRS_image_Frame, image=FocusRS_photo_small, bg=FocusRS_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    FocusRS_main_label.image = FocusRS_photo_small
    FocusRS_main_label.pack(side="left", padx=5, pady=0)

    FocusRS_engine_label = tk.Label(FocusRS_image_Frame, image=FocusRS_engine_photo_small, bg=FocusRS_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    FocusRS_engine_label.image = FocusRS_engine_photo_small
    FocusRS_engine_label.pack(side="left", padx=5, pady=0)

    FocusRS_interior_label = tk.Label(FocusRS_extras_frame, image=FocusRS_photo_interior_small, bg=FocusRS_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    FocusRS_interior_label.image = FocusRS_photo_interior_small
    FocusRS_interior_label.pack(side="left", padx=5, pady=0)

    FocusRS_rear_label = tk.Label(FocusRS_extras_frame, image=FocusRS_photo_rear_small, bg=FocusRS_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    FocusRS_rear_label.image = FocusRS_photo_rear_small
    FocusRS_rear_label.pack(side="left", padx=5, pady=0)

    # Back button
    create_back_button(FocusRS_specs_Frame, back_to_home)

    start_rainbow(Home)

    specs_visible = True

def show_Skyline_GTR_specs(event:None):
    global specs_visible, desc_label, interior_label, rear_label
    global Skyline_GTR_extras_frame, Skyline_GTR_interior_label, Skyline_GTR_rear_label

    # hides home, goes to volvo screen
    Home_Content_Frame.pack_forget()
    Skyline_GTR_Frame.pack(fill="both", expand=True)
    if specs_visible:
        return

    #deletes previos image removing duplication
    for widget in Skyline_GTR_image_Frame.winfo_children():
        widget.destroy()

    # Enlarge main car image
    Skyline_GTR_label.configure(image=Skyline_GTR_photo_large, cursor="")
    Skyline_GTR_label.image = Skyline_GTR_photo_large

    # Dim background
    dim_Frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    Home_Frame.configure(bg=Skyline_GTR_Frame_BG)
    Skyline_GTR_image_Frame.configure(bg=Skyline_GTR_Frame_BG)
    Skyline_GTR_specs_Frame.configure(bg=Skyline_GTR_Frame_BG)
    Skyline_GTR_desc_Frame.configure(bg=Skyline_GTR_Frame_BG)
    Home_Frame.lift()

    # Clear previous specs
    for widget in Skyline_GTR_specs_Frame.winfo_children():
        widget.destroy()

    # Specs header
    tk.Label(Skyline_GTR_specs_Frame, text="SPECIFICATIONS:", font=("Calibri", 35, "bold", "italic"), bg=Skyline_GTR_Frame_BG, fg="white").pack(anchor="w")

    # Specs details
    Skyline_GTR_specs = {
        "Make": "Nissan",
        "Model": "Skyline GT-R",
        "Year": "1999",
        "Generation": "R34",
        "Engine": "2.6L Twin-Turbocharged RB26DETT Inline-6",
        "Horsepower": "320 hp @ 6800 rpm",
        "Torque": "392 Nm @ 4400 rpm",
        "Transmission": "6-speed manual",
        "0–60 mph": "4.9 s",
        "Top Speed": "155 mph",
        "Drive Type": "AWD (ATTESA E-TS Pro)",
        "Body Style": "2-door Coupe",
        "Fuel Economy": "16 mpg city / 23 mpg highway (approx.)",
        "Seating Capacity": "4",
        "Suspension": "Independent multi-link front and rear",
        "Brakes": "Brembo ventilated discs all round",
        "Fuel Tank Capacity": "65 L",
        "Boot Space": "300 L",
        "Insurance cost like": "Ridiculous",
    }
    for key, value in Skyline_GTR_specs.items():
        tk.Label(Skyline_GTR_specs_Frame, bg=Skyline_GTR_Frame_BG, fg="white", font=("Calibri", 16), text=f"{key}: {value}").pack(anchor="w")

    # Description label
    Skyline_GTR_desc_label = tk.Label(Skyline_GTR_desc_Frame, text="'Fast And Furiuos''", font=("Calibri", 45, "italic"), bg=Skyline_GTR_Frame_BG, fg="white")
    Skyline_GTR_desc_label.grid(row=0, column=0, pady=0)

    Skyline_GTR_desc_label2 = tk.Label(Skyline_GTR_desc_Frame, text="This car has a hell of a legacy!", font=("Calibri", 22, "italic"), bg=Skyline_GTR_Frame_BG, fg="white")
    Skyline_GTR_desc_label2.grid(row=1, column=0, pady=0)

# Extra images stacked horizontally under the main car
    Skyline_GTR_extras_frame = tk.Frame(Skyline_GTR_image_Frame, bg=Skyline_GTR_Frame_BG)
    Skyline_GTR_extras_frame.pack(side="bottom", padx=0, pady=5, anchor="w")

    Skyline_GTR_main_label = tk.Label(Skyline_GTR_image_Frame, image=Skyline_GTR_photo_small, bg=Skyline_GTR_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Skyline_GTR_main_label.image = Skyline_GTR_photo_small
    Skyline_GTR_main_label.pack(side="left", padx=5, pady=0)

    Skyline_GTR_engine_label = tk.Label(Skyline_GTR_image_Frame, image=Skyline_GTR_engine_photo_small, bg=Skyline_GTR_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Skyline_GTR_engine_label.image = Skyline_GTR_engine_photo_small
    Skyline_GTR_engine_label.pack(side="left", padx=5, pady=0)

    Skyline_GTR_interior_label = tk.Label(Skyline_GTR_extras_frame, image=Skyline_GTR_photo_interior_small, bg=Skyline_GTR_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Skyline_GTR_interior_label.image = Skyline_GTR_photo_interior_small
    Skyline_GTR_interior_label.pack(side="left", padx=5, pady=0)

    Skyline_GTR_rear_label = tk.Label(Skyline_GTR_extras_frame, image=Skyline_GTR_photo_rear_small, bg=Skyline_GTR_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Skyline_GTR_rear_label.image = Skyline_GTR_photo_rear_small
    Skyline_GTR_rear_label.pack(side="left", padx=5, pady=0)

    # Back button
    create_back_button(Skyline_GTR_specs_Frame, back_to_home)

    specs_visible = True

def show_Tesla_S_specs(event:None):
    global specs_visible, desc_label, interior_label, rear_label
    global Tesla_S_extras_frame, Tesla_S_interior_label, Tesla_S_rear_label

    # hides home, goes to volvo screen
    Home_Content_Frame.pack_forget()
    Tesla_S_Frame.pack(fill="both", expand=True)
    if specs_visible:
        return

    #deletes previos image removing duplication
    for widget in Tesla_S_image_Frame.winfo_children():
        widget.destroy()

    # Enlarge main car image
    Tesla_S_label.configure(image=Tesla_S_photo_large, cursor="")
    Tesla_S_label.image = Tesla_S_photo_large

    # Dim background
    dim_Frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    Home_Frame.configure(bg=Tesla_S_Frame_BG)
    Tesla_S_image_Frame.configure(bg=Tesla_S_Frame_BG)
    Tesla_S_specs_Frame.configure(bg=Tesla_S_Frame_BG)
    Tesla_S_desc_Frame.configure(bg=Tesla_S_Frame_BG)
    Home_Frame.lift()

    # Clear previous specs
    for widget in Tesla_S_specs_Frame.winfo_children():
        widget.destroy()

    # Specs header
    tk.Label(Tesla_S_specs_Frame, text="SPECIFICATIONS:", font=("Calibri", 35, "bold", "italic"), bg=Tesla_S_Frame_BG, fg="white").pack(anchor="w")

    # Specs details
    Tesla_S_specs = {
        "Make": "Tesla",
        "Model": "Model S",
        "Year": "2026",
        "Generation": "Latest Refresh",
        "Engine": "Dual Electric Motors (AWD)",
        "Horsepower": "670 hp",
        "Torque": "755 Nm ",
        "Transmission": "Single‑speed automatic (electric)",
        "0–60 mph": "3.1 s",
        "Top Speed": "155 mph",
        "Drive Type": "All‑Wheel Drive",
        "Body Style": "5‑door Liftback Sedan",
        "Battery Capacity": "100 kWh",
        "Range": "410 mi",
        "Charging": "Up to 250 kW DC fast charging",
        "Seating Capacity": "5",
        "Suspension": "Multilink independent",
        "Brakes": "Vented disc brakes all round",
        "Curb Weight": "≈4560–4827 lb",
        "Insurance cost like": "'High‑end' 'luxury' EV",
    }
    for key, value in Tesla_S_specs.items():
        tk.Label(Tesla_S_specs_Frame, bg=Tesla_S_Frame_BG, fg="white", font=("Calibri", 16), text=f"{key}: {value}").pack(anchor="w")

    # Description label
    Tesla_S_desc_label = tk.Label(Tesla_S_desc_Frame, text="'It's a piece of sh**''", font=("Calibri", 45, "italic"), bg=Tesla_S_Frame_BG, fg="white")
    Tesla_S_desc_label.grid(row=0, column=0, pady=0)

    Tesla_S_desc_label2 = tk.Label(Tesla_S_desc_Frame, text="WARNING: This is just to annoy Thomas Fairgrieve", font=("Calibri", 22, "italic"), bg=Tesla_S_Frame_BG, fg="white")
    Tesla_S_desc_label2.grid(row=1, column=0, pady=0)

# Extra images stacked horizontally under the main car
    Tesla_S_extras_frame = tk.Frame(Tesla_S_image_Frame, bg=Tesla_S_Frame_BG)
    Tesla_S_extras_frame.pack(side="bottom", padx=0, pady=5, anchor="w")

    Tesla_S_main_label = tk.Label(Tesla_S_image_Frame, image=Tesla_S_photo_small, bg=Tesla_S_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Tesla_S_main_label.image = Tesla_S_photo_small
    Tesla_S_main_label.pack(side="left", padx=5, pady=0)

    Tesla_S_engine_label = tk.Label(Tesla_S_image_Frame, image=Tesla_S_engine_photo_small, bg=Tesla_S_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Tesla_S_engine_label.image = Tesla_S_engine_photo_small
    Tesla_S_engine_label.pack(side="left", padx=5, pady=0)

    Tesla_S_interior_label = tk.Label(Tesla_S_extras_frame, image=Tesla_S_photo_interior_small, bg=Tesla_S_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Tesla_S_interior_label.image = Tesla_S_photo_interior_small
    Tesla_S_interior_label.pack(side="left", padx=5, pady=0)

    Tesla_S_rear_label = tk.Label(Tesla_S_extras_frame, image=Tesla_S_photo_rear_small, bg=Tesla_S_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Tesla_S_rear_label.image = Tesla_S_photo_rear_small
    Tesla_S_rear_label.pack(side="left", padx=5, pady=0)
    # Back button
    create_back_button(Tesla_S_specs_Frame, back_to_home)
    print("button")

    specs_visible = True

def show_Koenigsegg_Jesko_Absolut_specs(event:None):
    global specs_visible, desc_label, interior_label, rear_label
    global Koenigsegg_Jesko_Absolut_extras_frame, Koenigsegg_Jesko_Absolut_interior_label, Koenigsegg_Jesko_Absolut_rear_label

    # hides home, goes to car screen
    Home_Content_Frame.pack_forget()
    Koenigsegg_Jesko_Absolut_Frame.pack(fill="both", expand=True)
    if specs_visible:
        return

    #deletes previos image removing duplication
    for widget in Koenigsegg_Jesko_Absolut_image_Frame.winfo_children():
        widget.destroy()

    # Enlarge main car image
    Koenigsegg_Jesko_Absolut_label.configure(image=Koenigsegg_Jesko_Absolut_photo_large, cursor="")
    Koenigsegg_Jesko_Absolut_label.image = Koenigsegg_Jesko_Absolut_photo_large

    # Dim background
    dim_Frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    Home_Frame.configure(bg=Koenigsegg_Jesko_Absolut_Frame_BG)
    Koenigsegg_Jesko_Absolut_image_Frame.configure(bg=Koenigsegg_Jesko_Absolut_Frame_BG)
    Koenigsegg_Jesko_Absolut_specs_Frame.configure(bg=Koenigsegg_Jesko_Absolut_Frame_BG)
    Koenigsegg_Jesko_Absolut_desc_Frame.configure(bg=Koenigsegg_Jesko_Absolut_Frame_BG)
    Home_Frame.lift()

    # Clear previous specs
    for widget in Koenigsegg_Jesko_Absolut_specs_Frame.winfo_children():
        widget.destroy()

    # Specs header
    tk.Label(Koenigsegg_Jesko_Absolut_specs_Frame, text="SPECIFICATIONS:", font=("Calibri", 35, "bold", "italic"), bg=Koenigsegg_Jesko_Absolut_Frame_BG, fg="white").pack(anchor="w")

    # Specs details
    Koenigsegg_Jesko_Absolut_specs = {
    "Make": "Koenigsegg",
    "Model": "Jesko Absolut",
    "Year": "2024",
    "Generation": "Jesko platform",
    "Engine": "5.0L Twin-Turbocharged V8",
    "Horsepower": "1600 hp on E85, 1280 hp on petrol",
    "Torque": "1500 Nm",
    "Transmission": "9-speed Light Speed Transmission (LST)",
    "0–60 mph": "≈2.5 s",
    "Top Speed": "330 mph+",
    "Drive Type": "RWD",
    "Body Style": "2-door Hypercar",
    "Fuel Economy": "Irrelevant",
    "Seating Capacity": "2",
    "Suspension": "Double wishbone front & rear with Triplex damper system",
    "Brakes": "Carbon-ceramic discs with multi-piston calipers",
    "Fuel Tank Capacity": "≈72 L",
    "Boot Space": "Minimal",
    "Insurance cost like": "You don’t ask, you sign"
    }
    for key, value in Koenigsegg_Jesko_Absolut_specs.items():
        tk.Label(Koenigsegg_Jesko_Absolut_specs_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG, fg="white", font=("Calibri", 16), text=f"{key}: {value}").pack(anchor="w")

    # Description label
    Koenigsegg_Jesko_Absolut_desc_label = tk.Label(Koenigsegg_Jesko_Absolut_desc_Frame, text="'Fastest car in the world''", font=("Calibri", 45, "italic"), bg=Koenigsegg_Jesko_Absolut_Frame_BG, fg="white")
    Koenigsegg_Jesko_Absolut_desc_label.grid(row=0, column=0, pady=0)

    Koenigsegg_Jesko_Absolut_desc_label2 = tk.Label(Koenigsegg_Jesko_Absolut_desc_Frame, text="Don't beleve me, search it up!", font=("Calibri", 22, "italic"), bg=Koenigsegg_Jesko_Absolut_Frame_BG, fg="white")
    Koenigsegg_Jesko_Absolut_desc_label2.grid(row=1, column=0, pady=0)

# Extra images stacked horizontally under the main car
    Koenigsegg_Jesko_Absolut_extras_frame = tk.Frame(Koenigsegg_Jesko_Absolut_image_Frame, bg=Koenigsegg_Jesko_Absolut_Frame_BG)
    Koenigsegg_Jesko_Absolut_extras_frame.pack(side="bottom", padx=0, pady=5, anchor="w")

    Koenigsegg_Jesko_Absolut_main_label = tk.Label(Koenigsegg_Jesko_Absolut_image_Frame, image=Koenigsegg_Jesko_Absolut_photo_small, bg=Koenigsegg_Jesko_Absolut_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Koenigsegg_Jesko_Absolut_main_label.image = Koenigsegg_Jesko_Absolut_photo_small
    Koenigsegg_Jesko_Absolut_main_label.pack(side="left", padx=5, pady=0)

    Koenigsegg_Jesko_Absolut_engine_label = tk.Label(Koenigsegg_Jesko_Absolut_image_Frame, image=Koenigsegg_Jesko_Absolut_engine_photo_small, bg=Koenigsegg_Jesko_Absolut_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Koenigsegg_Jesko_Absolut_engine_label.image = Koenigsegg_Jesko_Absolut_engine_photo_small
    Koenigsegg_Jesko_Absolut_engine_label.pack(side="left", padx=5, pady=0)

    Koenigsegg_Jesko_Absolut_interior_label = tk.Label(Koenigsegg_Jesko_Absolut_extras_frame, image=Koenigsegg_Jesko_Absolut_photo_interior_small, bg=Koenigsegg_Jesko_Absolut_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Koenigsegg_Jesko_Absolut_interior_label.image = Koenigsegg_Jesko_Absolut_photo_interior_small
    Koenigsegg_Jesko_Absolut_interior_label.pack(side="left", padx=5, pady=0)

    Koenigsegg_Jesko_Absolut_rear_label = tk.Label(Koenigsegg_Jesko_Absolut_extras_frame, image=Koenigsegg_Jesko_Absolut_photo_rear_small, bg=Koenigsegg_Jesko_Absolut_Frame_BG, borderwidth=2, relief="solid", cursor="hand2")
    Koenigsegg_Jesko_Absolut_rear_label.image = Koenigsegg_Jesko_Absolut_photo_rear_small
    Koenigsegg_Jesko_Absolut_rear_label.pack(side="left", padx=5, pady=0)

    # Back button
    create_back_button(Koenigsegg_Jesko_Absolut_specs_Frame, back_to_home)
    print("button")

    specs_visible = True


# Back button function
def back_to_home():
    global specs_visible, desc_label
    global interior_label, rear_label, Volvo_extras_frame
    global Golf_extras_frame, Golf_interior_label, Golf_rear_label

    Volvo_Frame.pack_forget()
    Golf_Frame.pack_forget()
    FocusRS_Frame.pack_forget()
    Tesla_S_Frame.pack_forget()
    Skyline_GTR_Frame.pack_forget()
    Koenigsegg_Jesko_Absolut_Frame.pack_forget()

    Home_Content_Frame.pack(fill="both", expand=True)

    dim_Frame.place_forget()

    # Hide description
    if desc_label:
        desc_label.grid_forget()
        desc_label = None

    # Reset main car image
    Volvo_V50_label.configure(image=photo_large, cursor="hand2")
    Volvo_V50_label.image = photo_small

    Golf_GTI_label.configure(image=Golf_photo_large, cursor="hand2")
    Golf_GTI_label.image = Golf_photo_large

    Focus_RS_label.configure(image=FocusRS_photo_large, cursor="hand2")
    Focus_RS_label.image = FocusRS_photo_large
    
    Tesla_S_label.configure(image=Tesla_S_photo_large, cursor="hand2")
    Tesla_S_label.image = Tesla_S_photo_large

    Skyline_GTR_label.configure(image=Skyline_GTR_photo_large, cursor="hand2")
    Skyline_GTR_label.image = Skyline_GTR_photo_large

    Koenigsegg_Jesko_Absolut_label.configure(image=Koenigsegg_Jesko_Absolut_photo_large, cursor="hand2")
    Koenigsegg_Jesko_Absolut_label.image = Koenigsegg_Jesko_Absolut_photo_large

    # Reset background colors
    Home_Frame.configure(bg="#2D2D2D")
    Volvo_image_Frame.configure(bg="#2D2D2D")
    Volvo_specs_Frame.configure(bg="#2D2D2D")
    Volvo_desc_Frame.configure(bg="#2D2D2D")

    # Remove specs
    for widget in Volvo_specs_Frame.winfo_children():
        widget.destroy()

    for lbl in [Golf_interior_label, Golf_rear_label]:
        if lbl:
            lbl.destroy()
    Golf_interior_label = None
    Golf_rear_label = None

    if Golf_extras_frame:
        Golf_extras_frame.destroy()
        Golf_extras_frame = None

    # Destroy Volvo_extras_frame if it exists
    if Volvo_extras_frame:
        Volvo_extras_frame.destroy()
        Volvo_extras_frame = None

    specs_visible = False

# Function to create a back button
def create_back_button(parent_frame, command):
    back_btn = tk.Button(parent_frame, text="Back To Home", font=("Calibri", 14), command=command)
    back_btn.pack(pady=10, anchor="w")
    return back_btn



print("Functions initilized successfully")

# Bind main car image click
Volvo_V50_label.bind("<Button-1>", show_volvo_specs)
Golf_GTI_label.bind("<Button-1>", show_golf_specs)
Focus_RS_label.bind("<Button-1>", show_focus_specs)
Skyline_GTR_label.bind("<Button-1>", show_Skyline_GTR_specs)
Tesla_S_label.bind("<Button-1>", show_Tesla_S_specs)
Koenigsegg_Jesko_Absolut_label.bind("<Button-1>", show_Koenigsegg_Jesko_Absolut_specs)



def toggle_rainbow():
    if rainbow_var.get():
        start_rainbow(Home)  # Start rainbow effect
    else:
        # Reset all widgets to white
        for widget in rainbow_widgets:
            try:
                widget.config(fg="white")
            except:
                pass

def Open_github():
    webbrowser.open_new("https://github.com/Hatter135")
    print("Opened Link")
def open_settings():
    settings_window = tk.Toplevel(Home)
    settings_window.title("Settings")
    settings_window.geometry("400x300")
    settings_window.configure(bg="#2D2D2D")
    
    # Title
    tk.Label(
        settings_window,
        text="SETTINGS",
        font=("Calibri", 24, "bold"),
        bg="#2D2D2D",
        fg="white"
    ).pack(pady=20)
    
    # Add more settings here as needed
    creator_label = tk.Button(settings_window, text="Who made this?", command=Open_github)
    creator_label.pack(pady=20)
    # In your open_settings() function, add before the Close button:
    rainbow_check = tk.Checkbutton(
        settings_window,
        text="Enable Rainbow Effect (Focus RS)",
        variable=rainbow_var,
        bg="#2D2D2D",
        fg="white",
        selectcolor="#222",
        font=("Calibri", 14),
        command=toggle_rainbow
)
    rainbow_check.pack(pady=10)
    # Close button
    tk.Button(
        settings_window,
        text="Close",
        font=("Calibri", 12),
        command=settings_window.destroy,
    ).pack(pady=20)

settings_button = tk.Button(
    Home_Content_Frame,
    text="⚙ Settings",
    font=("Calibri", 12),
    bg="#3D3D3D",
    fg="white",
    command=open_settings
)

settings_button.grid(row=2, column=0, pady=10, sticky="w")
print("App Fully Launched. No errors!")
print(fig.renderText("DRIVR"))
print("HATTER135 - 2026")
print("Github: https://github.com/Hatter135")

Home.mainloop()
print("APP EXITED BY USER")
