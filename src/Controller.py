class Controller:
    """Class Controller The controller class allows you 
    to interact with the sotrage object placed in it
    """

    def __init__(self, storage):
        self.__storage = storage

    def get_storage_about(self) -> str:
        """Return About from storage
        """

        return self.__storage.get_about()

    def get_storage_version(self) -> str:
        """Return Version from storage
        """
        return self.__storage.get_version()

    def get_storage_help(self) -> str:
        """Return Help from storage
        """
        return self.__storage.get_help()
