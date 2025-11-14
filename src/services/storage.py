import pickle
from src.models.address_book import AddressBook
from src.models.notebook import NoteBook
from src.config import DEFAULT_ADDRESSBOOK_FILENAME, DEFAULT_NOTEBOOK_FILENAME


def _load_pkl_book(filename) -> object:
    """
    Load a serialized book object from a pickle file.

    Args:
        filename (str): The path to the pickle file to load.

    Returns:
        object: The deserialized book object (AddressBook or NoteBook).
                Returns an empty AddressBook if the file is not found.

    Raises:
        FileNotFoundError: Caught internally and returns empty AddressBook.
    """
    try:
        with open(filename, "rb") as f:
            obj_book = pickle.load(f)
            return obj_book
    except FileNotFoundError:
        return AddressBook()


def load_data(
    addressbook_filename=DEFAULT_ADDRESSBOOK_FILENAME,
    notebook_filename=DEFAULT_NOTEBOOK_FILENAME,
) -> tuple[AddressBook, NoteBook]:
    """
    Load both address book and notebook data from pickle files.

    Args:
        addressbook_filename (str, optional): Path to the address book file.
                                             Defaults to DEFAULT_ADDRESSBOOK_FILENAME.
        notebook_filename (str, optional): Path to the notebook file.
                                          Defaults to DEFAULT_NOTEBOOK_FILENAME.

    Returns:
        tuple[AddressBook, NoteBook]: A tuple containing the loaded AddressBook
                                      and NoteBook objects.
    """
    address_book = _load_pkl_book(addressbook_filename)
    note_book = _load_pkl_book(notebook_filename)
    return address_book, note_book


def save_pkl_book(book: object, filename):
    """
    Serialize and save a book object to a pickle file.

    Args:
        book (object): The book object to save (AddressBook or NoteBook).
        filename (str): The path to the file where the book will be saved.

    Returns:
        bool: True if the save was successful, False otherwise.
    """
    try:
        with open(filename, "wb") as f:
            pickle.dump(book, f)
        return True
    except Exception:
        return False
