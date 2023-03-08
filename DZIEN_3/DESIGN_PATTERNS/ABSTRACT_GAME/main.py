#ForgWorld
class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.action()
        msg = f'{self} Żaba spotyka {obstacle} i {act}'
        print(msg)
        
class Bug:
    def __str__(self):
        return 'robak'
    
    def action(self):
        return "zjada go"
    
class FrogWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name
        
    def __str__(self):
        return '\n\n\t------------- Frog World --------------'
    
    def make_character(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        return Bug()
    
    
#Warlock World

class Warlock:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f'{self} Czarnoksiężnik spotyka {obstacle} i {act}'
        print(msg)
        
class Ork:

    def __str__(self):
        return 'ork'

    def action(self):
        return "zabija go"
        
class WarlockWorld:       
    
    def __str__(self,name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------------- Warlock World --------------'

    def make_character(self):
        return Warlock(self.player_name)

    def make_obstacle(self):
        return Ork()

