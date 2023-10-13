from Controller import Controller
from Storage import Storage


class Factory():
    """Class Factory acts as a factory for creating an object 
    of the RectangleCollision class , implementing dependency injection 
    with a controller and storage
    """

    def create(application):
        """Create instance class variable application.

        Keyword arguments:
        application:class -- argument for creating an object of the specified class

        """

        storage = Storage()
        controller = Controller(storage)
        storage_about = controller.get_storage_about()
        storage_version = controller.get_storage_version()
        storage_help = controller.get_storage_help()

        return application(about=storage_about, version=storage_version, help=storage_help)
