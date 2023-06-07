#Andres Portillo
#3/26/2023
#COP3509

class Cow:
    # Define a class named "Cow"

    def __init__(self, name):
        # Define the constructor method with a parameter "name"

        # Set the name attribute to the input name
        self._name = name

        # Set the image attribute to None
        self._image = None

    # Getter method for the name attribute
    @property
    def name(self):
        # Define a getter method for the "name" attribute
        return self._name

    # Setter method for the name attribute
    @name.setter
    def name(self, name):
        # Define a setter method for the "name" attribute
        self._name = name

    # Getter method for the image attribute
    @property
    def image(self):
        # Define a getter method for the "image" attribute
        return self._image

    # Setter method for the image attribute
    @image.setter
    def image(self, image):
        # Define a setter method for the "image" attribute
        self._image = image

    # Method to print a message and the cow image if it exists
    def print(self, message):
        # Define a method to print a message and the cow image if it exists

        # Check if the cow image exists
        if self.image is None:
            # If there is no image, print only the message with the cow name
            print(f"{self.name}: {message}")
        else:
            # If there is an image, print the message above the cow image
            print(f"{message}\n{self.image}")

    # Method to print a message and the cow image. Asserts that the cow image exists
    def print_message(self, msg):
        # Define a method to print a message and the cow image, and asserts that the cow image exists

        assert self.image is not None, "This cow was not initialized properly"
        # Raise an error if the cow image is None

        print(msg)
        print(self.image)
