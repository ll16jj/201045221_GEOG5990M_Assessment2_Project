'''Step 1: Import all relevant modules'''
print("Step 1: Import Modules")

import Drunk_ABM
import random
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import tkinter
import os

'''Step 2: Initialises the starting parameters'''
print("Step 2: Intitialise parameters")

drunks = []
num_of_drunks = 25
environment = []
house_number = []
House_Location = []
data = []
density = []



'''Step 3: Initialises environment, which reads in csv environment data from a text document'''
print("Step 3: Read in Environment Data")

def read_raster(file):
    '''
    Desribe what the function does.
    Parameters
    ----------
    file : text
        The path to a file.
    Returns
    -------
    environment : list of lists
        Raster read in.
    '''
    f = open(file) 
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    environment = []
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
    f.close()
    #print(environment)
    return environment

environment = read_raster('drunk.plan.txt')


'''Step 4: Defines the x and y coordinates for each house and allocates each drunk their own house number'''
print("Step 4: Define house position and allocate drunks to each house")

def HousePosition(data):
    '''
    Creates an empty array of house positions. Then all the data for the houses in each 
    column and row in the environment are appended to the empty list. The size (width/height) of the houses
    can be calculated by printing the House_Position list, in which the the x and y coords of each house have 
    been appended to. Therefore, when examining the list, for each house there are 11 x and 11 y values (11 by 11
    squares). For each house the entrance will be randomised using the random function in the range of 1 to 11, meaning
    every house has a different entrance appended to the house position list. However, these entrances are not on the 
    outer edge of each house therefore, this fucntion could be improved where entrances are different for each house
    along the edge. Each drunk has their own house: drunk 1 is allocated to house number 10; drunk 2 to house number 
    20 and so fourth to house number 250.This is then appended to the house number list. For i in range of house_number
    --- this function looks through thehouse number list and appends the house position to an empty list.
    '''
    House_Position = []
    for i in range(0,len(environment)):
        for j in range(0, len(environment[0])):
            #if environment[j][i] == 1: ------- Possible function to allocate drunks to the pub position
            #    Pub_Position.append([i,j])
            if environment[j][i] == data: 
                House_Position.append([i,j])
                #print(House_Position)
                
    House_Position = House_Position[random.randint(1,11)]
    return House_Position;



for i in range(num_of_drunks):
    house_number_per_drunk = (i+1)*10
    house_number.append(house_number_per_drunk)
 

for i in house_number:
    House_Location.append(HousePosition(i))
    #print(HousePosition(i))
    #print(House_Location)
    


'''Step 5: Defines the density environment, which will show the denisty of the routes taken by each drunk to their house'''
print("Step 5: Defines the Density Environment")                     

density = []

for i in range(0,len(environment)):
    rowlist = []
    for j in range(0, len(environment[0])):
        rowlist.append(0)
    density.append(rowlist)


for i in range(num_of_drunks):
    drunks.append(Drunk_ABM.Drunk(environment, drunks, house_number[i], House_Location[i]))





'''Step 6: Initialise the GUI and initialises parameters for the stopping conditions'''
print("Step 6: Initialising GUI.")

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
carry_on = True
init = True
halted = False
rerunid = 0
total_ite = 0;
root = tkinter.Tk() 
root.wm_title("Show me the way to go home: A Drunken Model")
print("A GUI window should appear. Please select \"Run Model\" to run the model. The number of iterations can be manually altered by the sliding scale")


'''Step 7: Animating Drunks'''
print("Step 7: Animating Drunks")

'''
Updates the drunks in the animation. 
'''
def update(frame_number):
 
    global carry_on
    global init
    global halted
    global rerunid
    if (init == True):
        print("Step 7: Animate acting agents.")
        print("Start .", end='')
        init = False
    else:
        if (halted):
            rerunid += 1
            print("Continuing", rerunid, end='')
            halted = False
        else:
            print(" .", end='')
        
    fig.clear()
    '''
Initially sets amount of drunks home to 0, then add the value of 1 each time a drunk gets home (drunks[i].home == True).
This allows for a stopping condition (carry_on == False) of the model when all the drunks in the model arrive home (25 drunks).
A drunk is declared home when the x and y coordinates of that current drunk is equal to the house number they have been assigned.
If the x andy values are false, then the animation continues by declaring drunks[i].move(), which moves the drunks using
the imported drunk ABM module, which states each drunks takes either a sober conscious move or a random move. The density
can be appended a value of 1 each time the drunks move from their x and y coords.
    '''
    drunks_home = 0 
    
    for i in range (num_of_drunks): 
            if drunks[i].house_number == drunks[i].environment[drunks[i]._y][drunks[i]._x]:  
                drunks[i].home == True
                drunks_home += 1
                          
            else:
                drunks[i].home == False
                drunks[i].move()
                density[drunks[i].gety()][drunks[i].getx()] += 1
                
    if drunks_home == num_of_drunks:
            carry_on = False
            print('The Model has now finished, all drunks have found their way home')             
                
    '''
Plots the environment, where the the sequential colourmap chosen was the greenblues and a legend and grid are also added.
Plots the drunks onto the enviroment as a scattergraph, where drunks that are not home are assinged the color red however,
when the drunks x and y values is equal to their respective house number, the marker color changes to black.
    '''              
                     
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.ylim(0, len(environment[0]))
    matplotlib.pyplot.imshow(environment, matplotlib.pyplot.cm.get_cmap('GnBu'))
    matplotlib.pyplot.colorbar(label='Houses (different color for each house)')
    matplotlib.pyplot.grid(True)
    for i in range(num_of_drunks):
        matplotlib.pyplot.title("Show me the way to go home: A Drunken Model")
        matplotlib.pyplot.xlabel("X-Axis")
        matplotlib.pyplot.ylabel("Y-Axis")
        if drunks[i].house_number == drunks[i].environment[drunks[i]._y][drunks[i]._x]: 
            matplotlib.pyplot.scatter(drunks[i].getx(),drunks[i].gety(), c='black', marker = '*')    
        else:
            matplotlib.pyplot.scatter(drunks[i].getx(),drunks[i].gety(), c='red', marker = '*')
        

'''Step 8: Halting Function'''
print("Step 8: Halting Function")

'''
A stopping function for the animation. There are two stopping conditions, the first is when the number of iterations 
in the animation equals the number of iterations set. The number of iterations is changeable in the GUI using a slider
scale thus, the number of iterations is set to the value input by the reader using the slider scale. The second stopping
condition is when carry_on == False, which occurs when all the drunks arrive home. 
'''
def gen_function():
    a = 0
    num_of_iterations = Iteration_Slider.get()
    global carry_on
    global halted
    global total_ite
    
    while (a < num_of_iterations) & (carry_on):
        yield a			
        a = a + 1
        total_ite += 1
    halted = True
    if (a == num_of_iterations):
        print(" run stopped after", total_ite, "iterations.")
    else:
        print(total_ite, "iterations.")
    
    
'''Step 9: Run the Animation'''
print("Step 9: Run the Animation")  


def runanimation():
    
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

'''
The slider scale for number of iterations needs to be declared before the default values are set. The range for the 
number of iterations is set from 1 to 500, and this can be changed here by putting a different range of values. The default
value for number of iteration is set to 400, as some of the model tests range to ~320 iterations. 
'''
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
Iteration_Slider = tkinter.Scale(root, from_=1, to=500, orient=tkinter.HORIZONTAL,label='No. of Iterations')
Iteration_Slider.place(relx=0.01,rely=0.2)



def set_defaults():
    Iteration_Slider.set(400)
set_defaults()

'''Step 10: Exiting and Writing Density'''
print("Step 10: Exit and Prints Density")
'''
The density parameter is written to a density text file upon exiting the model. 
'''
def exiting():
    
    if halted == False:
        print(" run stopped after", total_ite, "iterations.")
        
    file = os.path.join('density.txt')
    with open(file, 'w', newline='') as f2:
        writer = csv.writer(f2, delimiter=',')
        for row in density:
            writer.writerow(row)
    
    root.quit()
    root.destroy()
    
    
'''Step 11: Final GUI and plotting density'''
print("Step 11: Final GUI and plotting density")
'''
Final GUI features are declared, with the run and exit command buttons which are padded and colourised. The tkinter.mainloop()
finishes the loop and exits the GUI. The density data is then plotted onto the python console using red colourmap to show the 
routes more clearly.   
'''

menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=runanimation)
model_menu.add_command(label="Exit", command=exiting)

button=tkinter.Button(root, command=runanimation, text="Run the Model", bg='green', fg='white')
button.pack(padx=30, pady=5)
button1=tkinter.Button(root, command=exiting, text="Exit the Model", bg='red', fg='white')
button1.pack(padx=30, pady=5)

tkinter.mainloop()
print("Thank you for running the model.")



fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

matplotlib.pyplot.xlim(0, len(environment)) 
matplotlib.pyplot.ylim(0, len(environment[0]))
matplotlib.pyplot.imshow(density, vmin=0, vmax=50)
matplotlib.pyplot.grid(True)
matplotlib.pyplot.title("Show me the way to go home: Density of Drunks")
matplotlib.pyplot.xlabel("X-Axis")
matplotlib.pyplot.ylabel("Y-Axis")
matplotlib.pyplot.imshow(density, matplotlib.pyplot.cm.get_cmap('Reds'))
matplotlib.pyplot.colorbar(label='Density of Drunks')
 

   
