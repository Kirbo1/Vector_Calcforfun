# Luke Williams

# Coding CHallenge: Vector Calc (2D and 3D) 

# #sigma_for_life!
#9/27/25

# importing libs needed for project
import numpy as np

import tkinter as tk

import calculator_funcs

# Title and size of gui window
root = tk.Tk()
root.geometry("500x550")
root.title("Vector Calculator")

root.iconphoto(False, tk.PhotoImage(file="Icon_mogged.png"))
# GUI icon cause why not lol 

# vector defining
vector_a = None
vector_b = None

#  variable for switching between 3D and 2D
is_2D = True

# Creating and displaying a frame for the display
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Label for the result from doing the calculations
vector_result_label = tk.Label(root, text="Result here", font=("Times New Roman", 20), fg="blue")
vector_result_label.pack(padx = 10, pady= 20)


# function for updating the calc if it's 2d or 3d and for recent operations
def updates():
    
    for widget in input_frame.winfo_children():
        widget.destroy()

    if is_2D == True:
        label = 'Enter your vector components with a space "x y": '

    else:
        label = 'Enter your vector components "x y z": '

    global vector_entry_A
    global vector_entry_B

    vector_entry_A = tk.Entry(input_frame, width=40)
    label_a = tk.Label(input_frame, text="Vector 1 " + label)
    label_a.pack()
    vector_entry_A.pack()
    
    vector_entry_B = tk.Entry(input_frame, width=40)
    label_b = tk.Label(input_frame, text="Vector 2 " + label)
    label_b.pack()
    vector_entry_B.pack()

# function for loading vectors

def loading():
    global vector_a
    global vector_b

    
    partA = vector_entry_A.get().split()
    
    partB = vector_entry_B.get().split()
    

    counting_for_a = 0
    counting_for_b = 0
    
    for num in partA:
        counting_for_a += 1

    for num in partB:
        counting_for_b += 1
    
    if is_2D == True:
        bare = 2
    else: 
        bare = 3
    

    if (counting_for_a != bare):
        return False
    
    

    try:
        # making the user input into floats cause they were strings 
        # also checking if the user put random junk into the calculator
        vector_a = np.array([
            float(component) for component in partA
        ])
        
    except ValueError:
        return False

    if len(partB) == bare:
        try:
            vector_b = np.array([

            float(component) for component in partB])
        except ValueError:
            return False
    else:
        vector_b = None

   
   
    return True

# Making the functions for the calc operations 

def calc_magnitude():
    if not loading():
        return 
    mg = calculator_funcs.magnitude(vector_a)

    vector_result_label.config(text=f"|A| = {mg}")

# Function that applies a scalar of 2 to the A vector
def calc_scal():
    if not loading():
        return
    scal_val = calculator_funcs.scalar_multiplication(2, vector_a)

    vector_result_label.config(text=f"A scaled by 2 = {scal_val}")



#Function for dot product 
def calc_dot_product():
    if not loading():
        return 
    if vector_b is None:
        return 
    dot = calculator_funcs.dot_product(vector_a, vector_b)
    vector_result_label.config(text=f"A dot B = {dot}")

# Function for cross product 
def calc_cross_product():
    if not loading():
        return 
    if vector_b is None:
        return
    cross = calculator_funcs.cross_product(vector_a, vector_b)
    vector_result_label.config(text=f"A cross B = {cross}")

# Function that finds the theta between two vectors( in rad)
def calc_theta_between_vectorsR():
    if not loading():
        return 
    if vector_b is None:
        return
    theta = calculator_funcs.theta_between_vectorsR(vector_a, vector_b)
    vector_result_label.config(text=f"theta (in radians) = {theta}")

# Function that finds the theta between two vectors (in deg)
def calc_theta_between_vectors_Deg():
    if not loading():
        return 
    if vector_b is None:
        return
    theta = calculator_funcs.theta_between_vectors_Deg(vector_a, vector_b)
    vector_result_label.config(text=f"theta (in degrees) = {theta}")


# Resultant vector function 
def calc_Resultant_Vector():
    if not loading():
        return 
    if vector_b is None:
        return
    Resultant = calculator_funcs.Resultant_Vector(vector_a, vector_b)
    vector_result_label.config(text=f" Resultant vector = {Resultant}")


# Difference function for vectors
def calc_Difference_Vector():
    if not loading():
        return 
    if vector_b is None:
        return
    Difference = calculator_funcs.Difference_Vector(vector_a, vector_b)
    vector_result_label.config(text=f" Difference vector = {Difference}")


# button functions for 2D or 3D

def func2D():
    global is_2D
    is_2D = True
    updates()

def func3D():
    global is_2D
    is_2D = False
    updates()
 
# creating the buttons for changing from 2D to 3D vectors

button_2D = tk.Button(root, text="2D Vector", command=func2D).place(relx=0.8, rely=0.9)
button_3D = tk.Button(root, text="3D Vector", command=func3D).place(relx=0.8, rely=0.8)


# buttons for operators

tk.Button(root, text="Magnitute of vector A", command=calc_magnitude).pack()
tk.Button(root, text="Vector A scaled by 2", command=calc_scal).pack()
tk.Button(root, text="A cross B", command=calc_cross_product).pack()
tk.Button(root, text="A dot B", command=calc_dot_product).pack()
tk.Button(root, text="theta between both vectors (rad)", command=calc_theta_between_vectorsR).pack()
tk.Button(root, text="theta between both vectors (deg)", command=calc_theta_between_vectors_Deg).pack()
tk.Button(root, text="Resultant", command=calc_Resultant_Vector).pack()
tk.Button(root, text="Difference", command=calc_Difference_Vector).pack()



updates()

root.mainloop()

