import random

class Drunk():

    def __init__(self, environment, drunks, house_number, House_Location):
        '''
        Sets the initial parameters for the Drunk class. The x and y values were calculated by converting the drunk.plan.txt file
        to excel, and then values of 1 which indicates the pub were recorded. the central point on the left side of the pub
        were chosen as the coordinates. For improvement, each drunk could be at any pub location in that case in the Drunk_Model.py
        the pubs locations can be found and appended similar to the house position, however the environment[j][i] value would be == 1
        '''
        self.environment = environment
        self.drunks = drunks
        self.width = len(environment) 
        self.height = len(environment[0])
        self._x = 129
        self._y = 149
        self.house_number = house_number
        self.House_Location = House_Location
        self.home = False

    '''
    This calculates and returns the distance between the x and y coords of the house location and the current x and y values 
    of the drunks.
    '''
    def distance_to_home(self, House_Location, x, y):
        return ((((House_Location[0] - x)**2) + ((House_Location[1] - y)**2))**0.5)
    
 
    def move(self):       
        '''
        Sets the distance between the current x and y values and the house location coords. The sober speed of each drunks is set to
        5. For improvement this value could be amended in the GUI interface so the reader chooses the sober speed. An alcohol_consumption
        parameter is created, where a random value between 1 to 5 is created. This assumes that drunks will have different alcohol consumption
        and that can enhibit the speed the drunk walks. This alcohol consumption idea could be improved where the higher alcohol consumption
        value, the drunks moves not randomly but the opposite direction to the house, or possibly pack to the pub, or even not make it home, i.e.
        collapses.
        '''
        Distancebetween = self.distance_to_home(self.House_Location, self._x, self._y)
        alcohol_consumption = random.randint(1,5)
        Sober_Speed = 5
      
        '''
        The if statements allows for the drunk to make either sober rational decisions or random alcohol driven decisions. If the random number is
        equal or less than 0.5, the potential distance the drunk moves in both directions are evaulated to drunks current distance to home. For instance,
        if the drunk wants to move south/down, and the distance is higher than the current position, then the drunk moves north/up where the home is 
        located. This is calculated for both x and y. However, if the random value was higher than 0.5 then, another random number is generated, so
        the drunk has an equal to chance to move in any random direction with a random alcohol_consumption
        '''        
        if random.random() <= 0.5:  
            Moves_Down = self._y - Sober_Speed
            new_y_distance = self.distance_to_home(self.House_Location, self._x, Moves_Down)
            if new_y_distance <= Distancebetween:
                self._y = (self._y - Sober_Speed)
            else: 
                self._y = (self._y + Sober_Speed)
        else:
            if random.random() < 0.5:
                self._y = (self._y + alcohol_consumption) 
            else: 
                self._y = (self._y + alcohol_consumption)
        
        if random.random() <= 0.5:  
            Moves_Right = self._x - 5
            new_x_distance = self.distance_to_home(self.House_Location, Moves_Right, self._y)
            if new_x_distance <= Distancebetween:
                self._x = (self._x - Sober_Speed)
            else: 
                self._x = (self._x + Sober_Speed)
        else:
            if random.random() < 0.5:
                self._x = (self._x + alcohol_consumption) 
            else:
                self._x = (self._x + alcohol_consumption)    
                
        '''
        These if statements help the model to run smoothly. When values were moving randomly, they moved to the end of the environment, causing errors
        and stopping the model. Therefore, to keep all the drunks within the limits of the environment, when the x or y values is less than 0 or greater
        than 299 (300 is the upper limit of the environment) then the new x and y values of 0 and 299 are appended. This means the drunks don't move past
        the limits of the environment. 
        '''
        if self._x < 0: 
            self._x = 0
        elif self._x > 299:
            self._x = 299
            
        if self._y < 0: 
            self._y = 0
        elif self._y > 299:
            self._y = 299

            
    '''
    These allow for the x and y to be more easily managed using the getter and setter methods in the property class.
    '''    
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    @property
    def y(self):
        """I'm the 'y' property."""
        return self._y
    
    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value
                

    
