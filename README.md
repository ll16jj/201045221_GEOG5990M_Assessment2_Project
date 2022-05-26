# Assessment 2: Show me the way to go home... A Drunken Model
## Brief Introduction 
This document provides context of the project, the model development process, issues during model development, and any improvements that can be made. The project selected is “Show me the way to go home...”, which was developed for the second Assessment of GEOG5990M Programming for GIS Analysis: Core Skills module for the MSc GIS program. 
The project was produced using Python 3.7.6 in Anaconda Spyder. The project aims to simulate drunken individuals walk back home after drinking at the town pub. 

## Summary of the Model
The model for this project attempts to simulate drunken individuals find their way home after drinking at a local town pub. The density routes of the drunks are recorded therefore, a town planner can evaluate the model and ensure that all the drunks are able to safely get home, as well as how the rate of alcohol consumption can affect the density routes. This model is relatively simple, there are 25 drunks within an 300x300 environment, where the pub lies centrally in the environment and the houses are near-equidistant from each other and are situated mainly near the boundaries of the environment. The 25 drunks move towards their respective houses, stumbling as a result of a function randomly generating decisions; the function decides whether the drunks moves randomly or moves consciously towards their house. When moving in a random unconscious manner, alcohol consumption is randomly generated to reduce the drunken individuals speed. Although the model is simple and not complex enough to be applicable to real-world problems, it forms as a foundation model which can be constantly improved and engineered towards a particular real-world problem. 

To summarise, the model is separated into two python scripts, the first is the Drunk_ABM.py script, which determines how the drunks move. The second script is the Drunk_Model.py script, which sets the environment, finds the drunks house number and their relative position in the environment, animates the drunks moving, plots the model, plots density routes, and adds GUI functionality. The model overall can be broken down into five relatively simple steps: 
1.	Pulls in the drunk.plan text file using csv reader to append to the environment. Using the environment, the houses and pub locations are determined.
2.	Displays the environment with the houses and pub data onto a scatter graph.
3.	Creates a drunk class, where the house number and positions are appended to the drunk class. 
4.	Drunks move either consciously towards their house using Euclidean distances, or in an unconscious random behaviour, until the drunks reach to their respective homes. 
5.	Density of the routes taken by each drunk are recorded, plotted onto a scatter graph, and saved into a text file (Figure 2).

## Running the Model
Open both python scripts and run the Drunk_Model.py script. A GUI interface will appear, and select "Run the model" to begin the animation. The number of iterations
can be adjusted using the slider before running the model. When the button "Exit the model" is pressed, the model closes and a density plot should appear in the python
console, showing the route taken by the drunken individuals from the pub back to their house. 
