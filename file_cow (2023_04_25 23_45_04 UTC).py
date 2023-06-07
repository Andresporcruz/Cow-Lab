from cow import Cow

# assumes the filename is valid
def read_file_to_string_or_error(filename):
    try:
        with open(filename) as file_object:
            return file_object.read()
    except Exception:
        raise RuntimeError("MOOOOO!!!!!!")

class FileCow(Cow):
    def __init__(self, name, filename):
        super().__init__(name)
        self.image = read_file_to_string_or_error(filename)

    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow Image")