import pickle
from src.models.address_book import AddressBook


def load_data(filename="data/addressbook.pkl"):
    """ 
    Function open saved data from file
    """
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 


def save_data(book, filename="data/addressbook.pkl"):
    """
    Function for save data to file
    """
    with open(filename, "wb") as f:
        pickle.dump(book, f)

