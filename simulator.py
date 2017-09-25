##class trash_car
##class destination

class SimObject:
    def __init__(self, inst_time):
        self.my_time = inst_time
        print("current_object time:"+ str(self.my_time))
        
    def time_advance(self, advanced_time):
        self.my_time += advanced_time
        print("current_object time:"+ str(self.my_time))
        

class TrashCar(SimObject): 
    def __init__(self, id, time):
        SimObject.__init__(self,time)
        self.id = id;
    
def simulation_engine():
    a = TrashCar(0, 0)
    a.time_advance(10)
    
simulation_engine()