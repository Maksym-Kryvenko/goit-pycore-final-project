# Default filename for storing the address book data
DEFAULT_ADDRESSBOOK_FILENAME = "data/addressbook.pkl"
DEFAULT_NOTEBOOK_FILENAME = "data/notebook.pkl"

# Number of days to look ahead for upcoming birthdays
UPCOMING_BIRTHDAYS_DAYS = 7


GENERAL_COMMANDS = {
    "hello": {
        "description": "Greet the user",
        "example": "hello",
    },
    "help": {
        "description": "Show all commands",
        "example": "help",
    },
    "quit": {
        "description": "Exit the application",
        "example": "'exit'",
        "controller_route": "cmd_exit",
    },
    "exit": {
        "description": "Exit the application",
        "example": "'exit'",
    },
}
CONTACT_COMMANDS = {
    "add": {
        "description": "Add a contact with phone number or email",
        "example": "add <name> <phone/email>",
    },
    "change": {
        "description": "Modify a contact number or email",
        "example": "change <name> <phone/email>",
        "second_arg_contact_name": True,
    },
    "delete": {
        "description": "Delete a contact",
        "example": "delete <name>",
        "second_arg_contact_name": True,
    },
    "phone": {
        "description": "Show the contact's phones numbers",
        "example": "phone <name>",
        "second_arg_contact_name": True,
        "controller_route": "cmd_show_phone",
    },
    "all": {
        "description": "Show all contacts",
        "example": "all",
        "controller_route": "cmd_show_all",
    },
    "add-birthday": {
        "description": "Add/change contact's birthday",
        "example": "add-birthday <name> <birthday>",
        "second_arg_contact_name": True,
    },
    "show-birthday": {
        "description": "Show a contact's birthday",
        "example": "show-birthday <name>",
        "second_arg_contact_name": True,
    },
    "birthdays": {
        "description": "Sow upcoming birthdays",
        "example": "birthdays",
    },
    "search": {
        "description": "Search for a contact",
        "example": "search <name>",
        "second_arg_contact_name": True,
    },
    "add-address": {
        "description": "Add or edit contact's address",
        "example": "add-address <name> <address>",
        "second_arg_contact_name": True,
    },
    "rename": {
        "description": "Rename existing contact",
        "example": "rename <name> <new_name>",
        "second_arg_contact_name": True,
    },
}
NOTE_COMMANDS = {
    "add-note": {
        "description": "Add a note",
        "example": "add-note <text>",
    },
    "edit-note": {
        "description": "Edit a note",
        "example": "edit-note <note_id> <text>",
        "second_arg_note_id": True,
    },
    "delete-note": {
        "description": "Delete a note",
        "example": "delete-note <note_id>",
        "second_arg_note_id": True,
    },
    "search-notes": {
        "description": "Search for a note",
        "example": "search-notes <text>",
        "second_arg_note_id": True,
    },
    "all-notes": {
        "description": "Show all notes",
        "example": "all-notes",
    },
    "add-tag": {
        "description": "Add a tag for a note",
        "example": "add-tag <note_id> <tag>",
        "second_arg_note_id": True,
    },
    "remove-tag": {
        "description": "Remove a note's tag",
        "example": "remove-tag <note_id> <tag>",
        "second_arg_note_id": True,
        "third_arg_tag_name": True,
    },
    "get-tags": {
        "description": "Get all unique tags",
        "example": "get-tags",
        "second_arg_note_id": True,
    },
    "link-contact": {
        "description": "Link note to a contact",
        "example": "link-contact <note_id> <contact_id>",
        "second_arg_contact_name": True,
        "third_arg_note_id": True,
    },
    "unlink-contact": {
        "description": "Unlink note from a contact",
        "example": "unlink-contact <note_id>",
        "second_arg_contact_name": True,
        "third_arg_note_id": True,
    },
    "sort-created": {
        "description": "Sort notes by created date",
        "example": "sort-created",
    },
    "sort-updated": {
        "description": "Sort notes by updated date",
        "example": "sort-updated",
    },
}
COMMANDS = {
    **GENERAL_COMMANDS,
    **CONTACT_COMMANDS,
    **NOTE_COMMANDS,
}
