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
        self.cont = 60

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
            self.mainFrame1, text=" ", background="#F2f2f2"
        )

        # Dropdown menu options
        self.options = (
            "All",
            "Adjective",
            "Article",
            "City",
            "Color",
            "Country",
            "Kinship",
            "Noun",
            "Number",
            "Preposition",
            "Pronoun",
            "Verb",
            "Phrases",
            "Slang"
        )

        # datatype of menu text
        self.clicked = tk.StringVar(self)
        
     # option menu
        self.option_menu = ttk.OptionMenu(
            self,
            self.clicked,
            self.options[0],
            *self.options)

        # Creating and initializing buttons
        self.button1 = ttk.Button(
            self.mainFrame1, text="Select", command=lambda: [self.open_excel_file_location()]
        )
        self.button2 = ttk.Button(
            self.mainFrame1, text="Save", command=lambda: [self.save_results()]
        )
        self.button_reset = ttk.Button(
            master=self, text="Reset", command=self.restart_exercise()
        )
        self.button_quit = ttk.Button(
            master=self, text="Quit", command=self.quit
        )
        self.button_start_practice = ttk.Button(
            master=self , text="Start", command =lambda: [self.start_practice(), self.obtain_data_from_excel()]
        )

        
    def place_all(self):

        self.mainFrame1.place(x=0, y=0, height=600, width=1950)
        self.mainFrame2.place(x=0, y=200, rely=0.05, height=1000, width=1950)

        # self.output_label.place(x=200, y=40, height=40, width=200)
        self.option_menu.place(x=40, y=40, height=40, width=120)

        self.button_start_practice.place(x=190, y=40, height=40, width=120)
        
    def open_excel_file_location(self):
        """Open the File Explorer to select desired excel file
        """
        global filepath1            
        filepath1 = askopenfilename(filetypes=[(
            "xlsx Files", "*.xlsx"), ("csv Files", "*.csv"), ("All Files", "*.*")])

    def save_results(self):
        """Open the file Explorer to select desired location to save results
        """
        global filepath1  
        self.filepath2 = askdirectory()
       

    def start_practice(self):
        pass

    def import_excel_file(self):
        self.df = pd.read_excel(filepath1, sheet_name="Practice_words")

    def obtain_data_from_excel(self):
        self.import_excel_file()

        # Limit data from the excel file for the chosen category
        if self.df['Type'] == self.clicked:
            exercice_length = len(self.df['Type'])
            exercice_df = pd.DataFrame((self.df['Type'] == self.clicked))

        for index, rows in exercice_df.iterrows():
            random.randint(exercice_df.index)



        # Adding a column in excel with reviewed word
        # self.point_for_word.loc[:,'Reviewed word']

        self.create_excel_file()
    
        return exercice_length

    def create_excel_file(self):
        
        pass

    def restart_exercise(self):
        pass

if __name__ == "__main__":
    app = Application()
    app.geometry("1600x800+0+0")
    app.resizable(True, False)
    app.iconbitmap(r'../bucket_4.ico')
    app.mainloop()