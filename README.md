# GoIT PyCore Final Project: Personal Assistant CLI Application

## Overview
This is a command-line personal assistant designed to help users manage contacts and notes efficiently. It supports storing detailed contact information, tracking birthdays, validating input, and organizing notes with tags and links. The project demonstrates practical use of object-oriented programming, modular architecture, and CLI interaction.

## Features
- CLI interface with command parsing and error handling
- Persistent data storage using pickle serialization
- Input validation for names, phone numbers, emails and birthdays
- Birthday tracking and filtering
- Modular design with separation of models, services, and CLI logic

## Requirements
- Python 3.10+
- OS: Windows, macOS, or Linux
- Dependencies listed in `requirements.txt`

## Installation
1. Clone or copy the project into any directory.
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

## Usage
Once launched, the assistant accepts commands via an interactive CLI with autocompletion and a helpful toolbar.  
You can manage contacts and notes using commands like `add`, `add-note`, `search`, `birthdays`, `search-notes`, etc.

### Available Commands
**General commands**
- `hello` – Greet the user.
- `help` – Show the list of commands in the console.
- `exit`, `quit` – Save data and exit the application.

**Contact commands**
- `add <name> <phone/email>` – Add a contact with phone number or email.
- `change <name> <old_phone/email> <new_phone/email>` – Modify a contact phone or email.
- `rename <name> <new_name>` – Rename an existing contact.
- `delete <name>` – Delete a contact.
- `add-address <name> <address>` – Add or edit contact's address.
- `add-birthday <name> <dd.mm.yyyy>` – Add or change a contact's birthday.
- `show-birthday <name>` – Show a contact's birthday.
- `phone <name>` – Show the contact's phone numbers.
- `all` – Show all contacts.
- `search <query>` – Search contacts by name, phone, or email.
- `birthdays` – Show contacts with upcoming birthdays (within configured days).

**Note commands**
- `add-note <text>` – Add a note.
- `edit-note <note_id> <text>` – Edit a note.
- `delete-note <note_id>` – Delete a note.
- `search-notes <query>` – Search notes by tags or contact name.
- `all-notes` – Show all notes.
- `add-tag <note_id> <tag>` – Add a tag to a note.
- `remove-tag <note_id> <tag>` – Remove a tag from a note.
- `get-tags <note_id>` – Show tags for a specific note.
- `link-contact <note_id> <contact_name>` – Link a note to a contact.
- `unlink-contact <note_id>` – Unlink a note from a contact.
- `sort-created [desc]` – Sort notes by creation date (optional `desc`/`true`/`yes` for reverse).
- `sort-updated [desc]` – Sort notes by last update date (optional `desc`/`true`/`yes` for reverse).

### Usage Examples
```text
> add John +38050-123-45-67
> add John john@example.com
> add-birthday John 15.05.1990
> add-note Presentation
> search-notes Presentation
> show-birthday John
> birthdays
> all-notes
```

## Project Structure
```text
goit-pycore-final-project/
├── data/                      # Pickle storage for contacts and notes
│   ├── addressbook.pkl
│   └── notebook.pkl
├── logs/                      # Application logs (reserved, can be extended)
├── main.py                    # Entry point: initializes CLI, controller, and view
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── src/
    ├── __init__.py
    ├── config.py              # Command registry and configuration constants
    ├── controllers/
    │   ├── __init__.py
    │   └── app_controller.py  # Application controller, command dispatch and orchestration
    ├── errors/                # Custom exception types
    │   ├── __init__.py
    │   ├── command_error.py
    │   ├── duplication_error.py
    │   ├── not_found_error.py
    │   └── validation_error.py
    ├── helpers/
    │   └── is_birthday_within_next_days.py  # Birthday calculations
    ├── models/                # Domain models (contacts and notes)
    │   ├── __init__.py
    │   ├── address_book.py
    │   ├── contact.py
    │   ├── fields.py
    │   ├── note.py
    │   └── notebook.py
    ├── services/              # Business logic and persistence for contacts/notes
    │   ├── __init__.py
    │   ├── assistent.py       # Contact assistant (AddressBook operations)
    │   ├── note_assistant.py  # Note assistant (NoteBook operations)
    │   └── storage.py         # Pickle save/load helpers
    ├── utils/
    │   ├── __init__.py
    │   └── validators.py      # Validation utilities for fields
    └── view/                  # CLI views and rendering
        ├── __init__.py
        ├── view.py            # Base view abstraction
        └── console/
            ├── __init__.py
            ├── completer.py   # Autocompletion for commands, contacts, and notes
            ├── print_help.py  # Rich-powered help screen
            ├── tip_toolbar.py # Dynamic bottom toolbar with hints
            ├── contacts/      # Contact-specific console rendering
            ├── notes/         # Note-specific console rendering
            └── tags/          # Tag-specific console rendering

## Data Storage
All data is stored locally in `.pkl` files using Python’s `pickle` module:
- **Contacts**: `data/addressbook.pkl`
- **Notes**: `data/notebook.pkl`

The `src/services/storage.py` module contains helper functions to save and load these structures.

## Configuration
Core configuration and command metadata live in `src/config.py`:
- `DEFAULT_ADDRESSBOOK_FILENAME`, `DEFAULT_NOTEBOOK_FILENAME` – Paths to pickle files.
- `UPCOMING_BIRTHDAYS_DAYS` – Number of days ahead to scan for upcoming birthdays.
- `COMMANDS` – Combined registry of all CLI commands (general, contact, note) used by the controller and console to drive autocompletion and help output.

You can adjust these values to change storage paths or birthday lookahead behavior.

## Logging
The `logs/` directory is reserved for application logs.  
At the moment the core application does not write structured logs by default, but this folder can be used to add logging in future enhancements.

## Authors
Maksym Kryvenko
Yaroslav Zahoruiko
Viacheslav Zabolotnyi
Oleksandr Hrynenko
Oleksii Kocherhin