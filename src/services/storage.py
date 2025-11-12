import pickle
from src.models.address_book import AddressBook
from src.config import DEFAULT_STORAGE_FILENAME


def load_data(filename=DEFAULT_STORAGE_FILENAME):
    """
    Function open saved data from file.
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def save_data(book, filename=DEFAULT_STORAGE_FILENAME):
    """
    Function for save data to file.

    Args:
        - book (AddressBook): The address book object to save.
        - filename (str): The name of the file to save the address book to. Defaults to DEFAULT_STORAGE_FILENAME.
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)
