class Storage:
    """Class Storage contains text header information
    """

    def __init__(self):
        self.__about = "A Python application with tkinter that allows you to look at the collision of two rectangular bodies at a given mass and velocity"
        self.__version = "Version", "v0.0.2\n\nAdded\n\n- Header menu (About, Version)\n- Entry and labels for mass and velocity relevant objects\n- Inputs validation\n- Start button collision\n- Test for function validation\n\nFixed\n\n- Formatting code for standarts\n- Renaming variables for readability"
        self.__help = ""

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
