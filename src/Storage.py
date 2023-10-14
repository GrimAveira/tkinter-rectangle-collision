class Storage:
    """Class Storage contains text header information
    """

    def __init__(self):
        self.__about = "A Python application with tkinter that allows you to look at the absolutely elastic collision of two rectangular bodies at a given mass and velocity"
        self.__version = "v0.0.3\n\nAdded\n\n- Working header menu with About, Version and Help\n- Test for function storage\n\n- All program logic is divided into several classes: Storage, Controller, Factory\n\nFixed\n\n- Formatting code for standarts\n- Same mass variable rectangle 1 and rectangle 2\n- RactangleCollision.py Tk parametr constructor\n\n\nRemoved\n\n- RactangleCollision.py unused variables\n\nv0.0.2\n\nAdded\n\n- Header menu (About, Version)\n- Entry and labels for mass and velocity relevant objects\n- Inputs validation\n- Start button collision\n- Test for function validation\n\nFixed\n\n- Formatting code for standarts\n- Renaming variables for readability"
        self.__help = "It is possible to enter data in 4 fields. The first 2 are responsible for the mass of objects, the second 2 are responsible for speed. To view the interaction of objects, click on the Start button. To exit the program, use Escape"

    def get_about(self) -> str:
        """Return About from storage
        """
        return self.__about

    def get_version(self) -> str:
        """Return Version
        """
        return self.__version

    def get_help(self) -> str:
        """Return Help
        """
        return self.__help
