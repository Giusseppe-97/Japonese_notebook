import tkinter as tk
from tkinter import ttk
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = tk.Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = ttk.Label(tkWindow, text="User Name").grid(row=0, column=0)
username = tk.StringVar()
usernameEntry = ttk.Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = ttk.Label(tkWindow,text="Password").grid(row=1, column=0)  
password = tk.StringVar()
passwordEntry = ttk.Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

# direction menu
lable_language = ttk.Label( text = "Choose language:")

# Create the list of options
options_list = ["English", "French", "Portuguese", "Japonese", "German", "Korean"]
  
# Variable to keep track of the option
# selected in OptionMenu
value_inside = tk.StringVar(tkWindow)
  
# Set the default value of the variable
value_inside.set("Select Language")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = tk.OptionMenu(tkWindow, value_inside, *options_list)
question_menu.grid(row=2, column=0)
  
# Function to print the submitted option-- testing purpose
  
  
def print_answers():
    print("Selected Option: {}".format(value_inside.get()))
    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tk.Button(tkWindow, text='Submit', command=print_answers)
submit_button.grid(row=3, column=0)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = ttk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()