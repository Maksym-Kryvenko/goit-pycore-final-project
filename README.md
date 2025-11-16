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
- Dependencies listed in requirements.txt

## Installation
copy files into any directory
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py

## Usage
Once launched, the assistant accepts commands via the CLI. You can manage contacts and notes using commands like add contact, add_note note, search contact, show-birthdays contact, etc.

### Working with Notes

#### Quick Start
```python
from src.services import NoteAssistant
from src.models import Contact

# Initialize Assistant
assistant = NoteAssistant()

# Add note
my_note = assistant.add_note("Meeting notes", tags=("work", "important"))

# Add tags
assistant.add_tags_to_note(my_note.id, "project", "todo")

# Link to contact (requires Contact object)
contact = Contact("John Doe", phone="+38050-123-45-67")
assistant.link_note_to_contact(my_note.id, contact)

# Search
work_notes = assistant.search_by_tags("work")
john_notes = assistant.search_by_contact("John Doe")

# Sort
recent = assistant.sort_by_updated_date(reverse=True)
```

#### Available Note Operations
- `add_note(content, contact=None, tags=None)` - Add new note (contact must be Contact object)
- `delete_note(note_id)` - Delete note
- `find_note(note_id)` - Find note by ID
- `add_tags_to_note(note_id, *tags)` - Add tags
- `remove_tag_from_note(note_id, tag)` - Remove tag
- `link_note_to_contact(note_id, contact)` - Link to contact (contact must be Contact object)
- `unlink_note_from_contact(note_id)` - Unlink from contact
- `search_by_tags(*tags)` - Search by tags
- `search_by_contact(contact_name)` - Search by contact name (accepts string)
- `get_all_notes()` - Get all notes
- `get_all_tags()` - Get all unique tags
- `sort_by_created_date(reverse=False)` - Sort by creation date
- `sort_by_updated_date(reverse=False)` - Sort by update date

### Available Commands
General commands:
- help - Show available command list
- hello - Greet the user
- exit - Exit the application
- quit - Exit the application

Contact commands:
- add - Add a contact with phone number or email
- add-address - Add or edit contact's address
- add-birthday - Add/change contact's birthday
- change - Modify a contact number or email
- del - Delete a contact
- search - Search contact
- phone - Show the contact's phones numbers
- show-birthday - Show a contact's birthday
- all - Show all contacts
- birthdays - Show contact list with upcoming birthdays

Note commands:
- add_note - Add note
- edit_note - Edit note
- delete_note - Delete note
- search_notes - Search note
- all_notes - Show all notes
- add_tag - Add tag to note
- remove_tag - Remove tag from the note
- get_tags - Get tags
- link_contact - Create link from note to contact
- unlink_contact - Delete link from note to contact
- sort_created - Sort notes by creations date
- sort_updated - Sort notes by updating date

### Usage Examples
> add John +38050-123-45-67
> add John john@example.com
> add-birthday John 15.05.1990
> add note Presentation
> search_notes Presentation
> show-birthday John

# TODO update structure with new console
## Project Structure
```
goit-pycore-final-project/
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── fields.py          # Field, Name, Phone, Birthday
│   │   ├── contact.py         # Contact class # TODO (see contact.py)
│   │   └── address_book.py    # AddressBook class # TODO
│   ├── services/
│   │   ├── __init__.py
│   │   ├── storage.py         # save_data, load_data
│   │   └── contact_service.py # Business logic for contacts # TODO
│   ├── cli/
│   │   ├── __init__.py
│   │   ├── commands.py        # Command functions (add_contact, change_phone, etc.) # TODO
│   │   ├── parser.py          # parse_input function # TODO
│   │   └── interface.py       # main() function and user interaction # TODO
│   └── utils/
│       ├── __init__.py
│       ├── decorators.py      # input_error decorator # TODO
│       └── validators.py      # Validation utilities
├── data/                      # For storing .pkl files
│   └── .gitkeep
├── logs/                      # Application logs
│   └── .gitkeep
├── main.py                    # Entry point (minimal)
├── requirements.txt
├── .gitignore
├── README.md
└── config.py                  # Configuration constants
```

## Data Storage
All data is stored locally in .pkl files using Python’s pickle module. This ensures persistence between sessions without requiring a database.

## Configuration
TBD

## Logging
TBD

## Authors
Maksym Kryvenko
Yaroslav Zahoruiko
Viacheslav Zabolotnyi
Oleksandr Hrynenko
Oleksii Kocherhin