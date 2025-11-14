# GoIT PyCore Final Project: Personal Assistant CLI Application

## Overview
TBD

## Features
TBD

## Requirements
TBD

## Installation
TBD

## Usage
TBD

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
TBD

### Usage Examples
TBD

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
TBD

## Configuration
TBD

## Logging
TBD

## Authors
TBD
