#Andres Portillo
#3/26/2023
#COP3509

from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        super().__init__(name)
        self.image = image

    def can_breathe_fire(self):
        return True  # Returns True when the dragon can breathe fire

    def print(self, msg):
        assert self.image != None, "this cow was not initilized properly"
        # Asserts that the image attribute is not None, otherwise raises an AssertionError with the message 'this cow was not initilized properly'

        can_or_cannot = "can" if self.can_breathe_fire() else "cannot"
        # Conditionally assigns the string "can" or "cannot" to the variable 'can_or_cannot' based on the return value of 'can_breathe_fire()' method

        print(msg)  # Prints the argument 'msg'
        print(self.image)  # Prints the instance variable 'self.image'
        print(
            f"This dragon {can_or_cannot} breathe fire.")  # Prints a formatted string with the value of 'can_or_cannot'
