import customtkinter as ctk
from customtkinter import *
from tkinter import *


root = CTk()

class colors:
    def __init__(self):
        self.fgcolor = "#363334"
        self.titlecolor = "#5dc7fc"
        
cor = colors()

class app:
    def __init__(self):
        
        self.x = 10
        self.y = 65
        self.acc = 1
        
        self.root = root
        self.screen()
        self.myappscreen()
        self.root.mainloop()
        
    def screen(self):
        
        self.root.title("Software de demonstração")
        self.root.geometry("1080x720")
        ctk.set_appearance_mode("dark-blue")
        ctk.set_default_color_theme("dark-blue")
        self.root.resizable(False, False)
        
    def myappscreen(self):
        
    # My main frame
    
        self.window = CTkFrame(
            master=self.root,
            fg_color=cor.fgcolor,
            width=1080,
            height=720
        ).place(x = 0, y = 0)
    
        self.screenframe = CTkFrame(
            master=self.window,
            width=1060,
            height=700,
            corner_radius=10,
            bg_color=cor.fgcolor,
            fg_color="#242424"
            ).place(anchor = CENTER, relx = 0.5, rely = 0.5)
    
    # Title
    
        self.title = CTkLabel(
            master=self.screenframe,
            text="Software de demonstração",
            text_color=cor.titlecolor,
            font=("Roboto", 25),
        ).place(anchor = CENTER, relx = 0.5, y = 40)
        
    # Footer
    
        self.footer = CTkLabel(
            master=self.screenframe,
            text="© Desenvolvido por João Pedro Pina Coelho",
            text_color=cor.titlecolor,
            font = ("Roboto", 12)
        ).place(anchor=CENTER, rely = 0.96, relx = 0.5)
        
    # Main applications
    
        self.button = CTkButton(
            master=self.screenframe,
            text="click me",
            width=93,
            height=40,
            command=self.animation
        ).place(anchor = CENTER, relx = 0.5, rely = 0.5)
    
    def animation(self):
        
        self.point = CTkFrame(
            master=self.screenframe,
            width=self.x,
            height=1,
            corner_radius=50,
            fg_color="#FFFFFF",
            bg_color="#FFFFFF"
        ).place(x = 10, y = self.y)
                
        if self.x > 1059:
            self.acc = 0
            self.x = 1060
        else:
            self.x += self.acc
            self.root.after(1, self.animation)
        
app()