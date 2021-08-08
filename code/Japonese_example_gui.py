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
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

import pandas as pd
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
        self.pack_all()

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
            self.mainFrame1, text=" ", background="#F2f2f2"
        )
        self.output_label = ttk.Label(
            self, foreground='red'
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
            *self.options,
            command=self.option_changed)

        

        # Creating and initializing buttons
        # self.button1 = ttk.Button(
        #     self.mainFrame1, text="Select", command=lambda: [self.open_excel_file_location()]
        # )
        # self.button2 = ttk.Button(
        #     self.mainFrame1, text="Save", command=lambda: [self.save_results()]
        # )
        # self.button_reset = ttk.Button(
        #     master=self, text="Reset", command=self.reset_app
        # )
        # self.button_quit = ttk.Button(
        #     master=self, text="Quit", command=self.quit
        # )
        self.button_select_category = ttk.Button(
            master=self , text="click Me" , command = self.option_changed())

    # Change the label text

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.clicked.get()}'
        
    def pack_all(self):

        self.mainFrame1.place(x=0, y=0, height=600, width=1950)
        self.mainFrame2.place(x=0, y=200, rely=0.05, height=1000, width=1950)

        self.output_label.place(x=200, y=40, height=40, width=200)
        self.option_menu.place(x=40, y=40, height=40, width=120)

        self.button_select_category.place(x=1090, y=140, height=40, width=120)

        # self.drop.place(x=0, y=0)

        # quit button not placed yet, just packed

    # def open_excel_file_location(self):
    #     """Open the File Explorer to select desired excel file
    #     """
    #     global filepath1
    #     if len(self.textbox1.get()) != 0:
    #         self.textbox1.delete(0, 'end')
            
    #     filepath1 = askopenfilename(filetypes=[(
    #         "xlsx Files", "*.xlsx"), ("csv Files", "*.csv"), ("All Files", "*.*")])
    #     try:
    #         with open(filepath1, "r"):
    #             self.textbox1.insert(tk.END, filepath1)
        
    #     except:
    #         if not filepath1:
    #             tk.messagebox.showwarning(title='No file selected.',
    #                 message='Please make sure a file has been chosen before running the program.')
    #             filepath1 = "../data/R403Q SoftMouse Export.xlsx"
    #             with open(filepath1, "r"):
    #                 self.textbox1.insert(tk.END, filepath1)

    # def save_results(self):
    #     """Open the file Explorer to select desired location to save results
    #     """
    #     global filepath2
    #     if len(self.textbox2.get()) != 0:
    #         self.textbox2.delete(0, 'end')
    #     self.filepath2 = askdirectory()
    #     if not self.filepath2:
    #         tk.messagebox.showwarning(title='No folder selected',
    #             message='Please make sure a folder has been chosen before running the program.')
    #         self.filepath2 = "results/2021_monthly_results/plots_per_month"
    #     self.textbox2.insert(tk.END, self.filepath2)

    # def import_excel_file(self):
    #     self.df = pd.read_excel(filepath1, sheet_name="Mouse List")

    # def obtain_data_from_excel(self):
    #     self.import_excel_file()

    #     # Limit data from the excel file for the chosen period of time
    #     n_df = self.df[(self.init_date <= self.df.Date_of_birth) &
    #                    (self.df.Date_of_birth <= self.final_date)]

        # Selects data from the excel file for sex, genotype and status (only mice that are alive)
        # df_MWt = pd.DataFrame(n_df.loc[(self.df['Sex'] == 'Male') & (
        #     n_df['Genotype'] == 'Null(-)') & (n_df['Status'] == 'Alive')])

        # for index, rows in df_MWt.iterrows():
        #     a = str(n_df['Date_of_birth'][index])
        #     birth_MWt.append(a[:10])

        # df_FWt = pd.DataFrame(n_df.loc[(self.df['Sex'] == 'Female') & (
        #     n_df['Genotype'] == 'Null(-)') & (n_df['Status'] == 'Alive')])

     

        # Adding a column in excel with the calculated age
        # self.dfreduced.loc[:,'Calculated Age'] = dd2

        # self.create_excel_file()

    def create_excel_file(self):
        
        pass


if __name__ == "__main__":
    app = Application()
    app.geometry("1600x800+0+0")
    app.resizable(True, False)
    app.iconbitmap(r'../bucket_4.ico')
    app.mainloop()