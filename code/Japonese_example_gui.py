"""
Created on Fri Apr  2 15:18:14 2021

@author: josep
"""

# Executing the program as a HD window for windows and exception for running it on mac
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

import pandas as pd
import random
import seaborn as sns
import os

import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
import nicexcel as nl

print("Loading your study session. This might take a minute.")

class Application(tk.Tk):
    """[Creating a main App class where all the frames are going to be set upon]

    The main App class must inherit from tk.Tk which is the root or main window
    """

    def __init__(self, *args, **kwargs):
        """init is the method for setting default state of the object
        """

        super().__init__(*args, **kwargs)

        # Set style of the GUI
        # missing

        # Create Main Frames
        self.mainFrame1 = tk.Frame(
            self, background="#F2f2f2"
        )
        self.mainFrame2 = tk.Frame(
            self, background="#F2f2f2"
        )

        # Call methods
        self.configure_basic_tk_properties()
        self.place_all()

    def configure_basic_tk_properties(self):
        """This method configures the basic tkinter esthetic properties for the GUI
        """
        self.title("  My japonese notebook")

        # Setting the main App in the center regardless to the window's size chosen by the user
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Setting a background for the main App which will be divided in 2 different Frames
        self.configure(bg="light blue")

        # Creating and placing Lables for each Frame
        self.lable = tk.Label(
            self.mainFrame1, text="What are we reviewing?", foreground="white",
            background="#120597").place(x=0, width=1920
        )
        self.lable2 = tk.Label(
            self.mainFrame2, text="Answers", foreground="white",
            background="#120597").place(y=0, width=1920
        )
        
        # Creating labels
        self.label_practice = ttk.Label(
            self.mainFrame1, text= "", background="#F2f2f2"
        )
        # Initializing filepath to excel database
        self.filepath = "../data/Japonese_notebook.xlsx"

        # Dropdown menu practice options
        self.exercice = (
            "Type the answer" ,
            "Multiple choice" ,
            "Select from list",
            "All"
        )
        
        # Dropdown menu practice direction
        self.direction = (
            "Romanji -> Word"            ,
            "Word -> Romanji"            ,
            "Romanji -> Type"            ,
            "Hiragana & Katakana -> Word",
            "Word -> Hiragana & Katakana",
            "Hiragana & Katakana -> Type",
            "Kanji -> Word"              ,
            "Word -> Kanji"              ,
            "Kanji -> Type"              ,
            "Furigana -> Word"           ,
            "Word -> Furigana"           ,
            "Furigana -> Type"           ,
            "All"
        )

        # Dropdown menu practice options
        self.options = (
            "  All                      ",
            "  Adjective                ",
            "  Article                  ",
            "  City                     ",
            "  Color                    ",
            "  Country                  ",
            "  Kinship                  ",
            "  Noun                     ",
            "  Number                   ",
            "  Preposition              ",
            "  Pronoun                  ",
            "  Verb                     ",
            "  Phrases                  ",
            "  Slang                    "
        )

        # datatype of menu text
        self.clicked_op = tk.StringVar(self)
        self.clicked_ex = tk.StringVar(self)
        self.clicked_dir = tk.StringVar(self)
        
        # option menu
        self.option_menu = ttk.OptionMenu(
            self,
            self.clicked_op,
            self.exercice[0],
            *self.exercice
        )
     
        # exercice menu
        self.exercice_menu = ttk.OptionMenu(
            self,
            self.clicked_ex,
            self.options[0],
            *self.options
        )
     
        # direction menu
        self.direction_menu = ttk.OptionMenu(
            self,
            self.clicked_dir,
            self.direction[0],
            *self.direction
        )

        # Creating and initializing lables
        self.output_label = ttk.Label(self, text= "Old text")
        self.lable_op = ttk.Label(self, text = "Choose type of word/phrase:")
        self.lable_ex = ttk.Label(self, text = "Choose exercise:")
        self.lable_dir = ttk.Label(self,text = "Choose direction:") 

        # Creating and initializing buttons
        self.button_start_practice = ttk.Button(
            master=self , text="Start", command=lambda: [self.start_practice()]
        )
        self.button_save = ttk.Button(
            self.mainFrame1, text="Save", command=lambda: [self.save_results()]
        )
        self.button_reset = ttk.Button(
            master=self, text="Reset", command=self.restart_exercise()
        )
        self.button_quit = ttk.Button(
            master=self, text="Quit", command=self.quit
        )
        
    def place_all(self):

        self.mainFrame1.place(x=0, y=0, height=600, width=1950)
        self.mainFrame2.place(x=0, y=200, rely=0.05, height=1000, width=1950)

        self.output_label.place(x=700, y=40, height=300, width=800)

        self.exercice_menu.place(x=250, y=40, height=40, width=200)
        self.direction_menu.place(x=250, y=100, height=40, width=200)
        self.option_menu.place(x=250, y=160, height=40, width=200)

        self.button_save.place(x=500, y=40, height=40, width=120)
        self.button_reset.place(x=500, y=90, height=40, width=120)
        self.button_quit.place(x=500, y=140, height=40, width=120)
        self.button_start_practice.place(x=500, y=190, height=40, width=120)

        self.lable_op.place(x=40, y=40, height=40, width=200)
        self.lable_dir.place(x=40, y=100, height=40, width=200)
        self.lable_ex.place(x=40, y=160, height=40, width=200)

    def save_results(self):
        """Open the file Explorer to select desired location to save results
        """
        global filepath_save
        self.filepath_save = askdirectory()
       
    def import_excel_file(self):
        self.df = pd.read_excel(self.filepath, sheet_name="Practice_words")

    def start_practice(self):
        self.import_excel_file()
        the_list = []
        for index, rows in self.df.iterrows():
            the_list.append(rows['Word'])
        self.output_label.config(text=the_list[random.randint(0, index)])
        self.output_label.config(font=("Courier", 11))

    def obtain_data_from_excel(self):
        self.import_excel_file()

        # Limit data from the excel file for the chosen category
        if self.df.loc[self.df['Type']] == self.clicked_op:
            exercice_length = len(self.df['Type'])
            exercice_df = pd.DataFrame((self.df['Type'] == self.clicked_op))

        for index, rows in exercice_df.iterrows():
            random.randint(exercice_df.index)
    
        return exercice_length

    def restart_exercise(self):
        pass

if __name__ == "__main__":
    app = Application()
    app.geometry("1600x800+0+0")
    app.resizable(True, False)
    app.iconbitmap(r'../bucket_4.ico')
    app.mainloop()