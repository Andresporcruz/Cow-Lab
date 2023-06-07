#Andres Portillo
#3/26/2023
#COP3509

from dragon import Dragon

class IceDragon(Dragon):
    def __init__(self, name, image):
        # Calls the __init__ method of the parent class, Dragon
        super().__init__(name, image)

    def can_breathe_fire(self):
        # Overrides the can_breathe_fire method of the parent class
        # Returns False to indicate that an IceDragon cannot breathe fire
        return False
