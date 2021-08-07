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
from tkcalendar import Calendar as tkc
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

import pandas as pd
import seaborn as sns

import os
from datetime import datetime as dt

import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
import nicexcel as nl

print("Loading TheMiceCounter application. This might take a minute.")

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

        self.label3 = ttk.Label(
            self.mainFrame1, text="Input: ", background="#F2f2f2"
        )
        self.label4 = ttk.Label(
            self.mainFrame1, text="Output:", background="#F2f2f2"
        )
        self.label5 = tk.Label(
            self.mainFrame1, text="Select Date Interval: ", background="#F2f2f2"
        )
        self.label6 = ttk.Label(
            self.mainFrame1, text="From:", background="#F2f2f2"
        )
        self.label7 = ttk.Label(
            self.mainFrame1, text="To:", background="#F2f2f2"
        )

        # Creating textboxes
        self.textbox1 = ttk.Entry(self.mainFrame1, width=80)
        self.textbox2 = ttk.Entry(self.mainFrame1, width=80)
        self.textbox3 = ttk.Entry(self.mainFrame1, width=20)
        self.textbox4 = ttk.Entry(self.mainFrame1, width=20)

        # Dropdown menu options
        self.options = [
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
        ]

        # datatype of menu text
        self.clicked = tk.StringVar()
        
        # initial menu text
        self.clicked.set( "All" )
        
        # Create Dropdown menu
        self.drop = tk.OptionMenu(self , self.clicked)

        # Creating and initializing buttons
        self.button1 = ttk.Button(
            self.mainFrame1, text="Select", command=lambda: [self.open_excel_file_location()]
        )
        self.button2 = ttk.Button(
            self.mainFrame1, text="Save", command=lambda: [self.save_results()]
        )
        self.button4 = ttk.Button(
            self, text="End date", command=self.grab_end_date
        )
        self.button5 = ttk.Button(
            self, text="Start date", command=self.grab_start_date
        )
        self.button_reset = ttk.Button(
            master=self, text="Reset", command=self.reset_app
        )
        self.button_quit = ttk.Button(
            master=self, text="Quit", command=self.quit
        )

        # Creating Canvas (where Histograms are going to be placed as matplotlib Figures)
        self.canvas01 = tk.Canvas(self.mainFrame2)
        self.canvas02 = tk.Canvas(self.mainFrame2)

    # Change the label text
    def show(self):
        try: 
            self.label_practice.destroy()

        except:
            self.label_practice.config( text = self.clicked.get() )
        
        

        

    def pack_all(self):

        self.mainFrame1.place(x=0, y=0, height=600, width=1950)
        self.mainFrame2.place(x=0, y=200, rely=0.05, height=1000, width=1950)

        self.label3.place(x=20, y=70, height=40, width=80)
        self.label4.place(x=20, y=140, height=40, width=80)
        self.label5.place(x=1300, y=30, height=30)
        self.label6.place(x=1250, y=80, height=30)
        self.label7.place(x=1250, y=150, height=30)

        self.textbox1.place(x=80, y=70, height=40, width=800)
        self.textbox2.place(x=80, y=140, height=40, width=800)
        self.textbox3.place(x=1300, y=70, height=40, width=99)
        self.textbox4.place(x=1300, y=140, height=40, width=99)

        self.button1.place(x=900, y=70, height=40, width=120)
        self.button2.place(x=900, y=140, height=40, width=120)
        self.button_reset.place(x=1090, y=140, height=40, width=120)
        self.button5.place(x=1450, y=70, height=40)
        self.button4.place(x=1450, y=140, height=40)
        self.button_quit.pack(side=tk.BOTTOM, pady=10)

        self.drop.place(x=0, y=0)
        # quit button not placed yet, just packed

        self.canvas01.place(x=100, y=40, height=600, width=800)
        self.canvas02.place(x=1000, y=40, height=600, width=800)

    def open_excel_file_location(self):
        """Open the File Explorer to select desired excel file
        """
        global filepath1
        if len(self.textbox1.get()) != 0:
            self.textbox1.delete(0, 'end')
            
        filepath1 = askopenfilename(filetypes=[(
            "xlsx Files", "*.xlsx"), ("csv Files", "*.csv"), ("All Files", "*.*")])
        try:
            with open(filepath1, "r"):
                self.textbox1.insert(tk.END, filepath1)
        
        except:
            if not filepath1:
                tk.messagebox.showwarning(title='No file selected.',
                    message='Please make sure a file has been chosen before running the program.')
                filepath1 = "../data/R403Q SoftMouse Export.xlsx"
                with open(filepath1, "r"):
                    self.textbox1.insert(tk.END, filepath1)

    def save_results(self):
        """Open the file Explorer to select desired location to save results
        """
        global filepath2
        if len(self.textbox2.get()) != 0:
            self.textbox2.delete(0, 'end')
        self.filepath2 = askdirectory()
        if not self.filepath2:
            tk.messagebox.showwarning(title='No folder selected',
                message='Please make sure a folder has been chosen before running the program.')
            self.filepath2 = "results/2021_monthly_results/plots_per_month"
        self.textbox2.insert(tk.END, self.filepath2)

    def import_excel_file(self):
        self.df = pd.read_excel(filepath1, sheet_name="Mouse List")

    def obtain_data_from_excel(self):
        self.import_excel_file()

        # Converting date format to compare with excel dates
        self.init_date = self.textbox3.get()
        self.init_date[::-1]
        self.final_date = self.textbox4.get()
        self.final_date[::-1]

        # Limit data from the excel file for the chosen period of time
        n_df = self.df[(self.init_date <= self.df.Date_of_birth) &
                       (self.df.Date_of_birth <= self.final_date)]

        # print(n_df)

        # Failed attempt to make the code underneath better

        # lage = []
        # for index, row in n_df.iterrows():
        #     a1 = str(self.final_date)
        #     aa = dt.strptime(a1, "%Y-%m-%d")
        #     b1 = str(n_df['Date_of_birth'])
        #     b1 = b1[5:15]
        #     print(b1)
        #     bb = dt.strptime(b1, "%Y-%m-%d")
        #     bd = abs((bb - aa).days)
        #     age_in_weeks = bd//7
        #     lage.append(age_in_weeks)
        # print(lage)

        # List of ages of the different type of mice 
        birth_MWt = []
        birth_FWt = []
        birth_MHet = []
        birth_FHet = []

# ***
# My BEST idea so far is to reorganize this code. If I calculate the birthday of all of the dataframe
# I can then just grab the dataframe of 'sex', 'Genotype' and 'status' and they will have the birthdays already
# ***

# Needs optimization. Too many lines for a simple part of the code
# There are 4 loops that are doing the same thing for example. There should be a way to reduce this
        # Selects data from the excel file for sex, genotype and status (only mice that are alive)
        df_MWt = pd.DataFrame(n_df.loc[(self.df['Sex'] == 'Male') & (
            n_df['Genotype'] == 'Null(-)') & (n_df['Status'] == 'Alive')])

        for index, rows in df_MWt.iterrows():
            a = str(n_df['Date_of_birth'][index])
            birth_MWt.append(a[:10])

        df_FWt = pd.DataFrame(n_df.loc[(self.df['Sex'] == 'Female') & (
            n_df['Genotype'] == 'Null(-)') & (n_df['Status'] == 'Alive')])

        for index, rows in df_FWt.iterrows():
            a = str(n_df['Date_of_birth'][index])
            birth_FWt.append(a[:10])

        df_MHet = pd.DataFrame(n_df.loc[(self.df['Sex'] == 'Male') & (
            n_df['Genotype'] == 'R403Q(+/-)') & (n_df['Status'] == 'Alive')])

        for index, rows in df_MHet.iterrows():
            a = str(n_df['Date_of_birth'][index])
            birth_MHet.append(a[:10])

        df_FHet = pd.DataFrame(n_df.loc[(self.df['Sex'] == 'Female') & (
            n_df['Genotype'] == 'R403Q(+/-)') & (n_df['Status'] == 'Alive')])

        for index, rows in df_FHet.iterrows():
            a = str(n_df['Date_of_birth'][index])
            birth_FHet.append(a[:10])

        dfappended = df_FHet.append([df_FWt,df_MHet, df_MWt], ignore_index=True)
        self.dfreduced = dfappended[['Sex', 'Genotype', 'Status','Date_of_birth']]

        birthday = [ birth_FHet, birth_FWt, birth_MHet, birth_MWt]

     

        # Adding a column in excel with the calculated age
        # self.dfreduced.loc[:,'Calculated Age'] = dd2

        self.create_excel_file()

    def create_excel_file(self):
        
        pass


if __name__ == "__main__":
    app = Application()
    app.geometry("1600x800+0+0")
    app.resizable(True, False)
    app.iconbitmap(r'../bucket_4.ico')
    app.mainloop()