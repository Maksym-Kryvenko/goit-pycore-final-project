#!/usr/bin/env python3
"""CLI command integration test script."""

import sys
import os
from io import StringIO
from datetime import datetime, timedelta

# Add parent directory to path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models import AddressBook, NoteBook
from src.services.assistent import Assistent
from src.services.note_assistant import NoteAssistant
from src.view.console_view import ConsoleView
from src.controllers.app_controller import AppController


class MockView(ConsoleView):
    """Mock view that doesn't use prompt_toolkit."""

    def __init__(self):
        # Don't call super().__init__() to avoid prompt_toolkit initialization
        from rich.console import Console

        self.console = Console()
        self.outputs = []
        self.contacts_data = []
        self.notes_data = []

    def prompt(self, contacts, notes):
        """Mock prompt - not used in automated tests."""
        return ""

    def render_welcome(self):
        self.outputs.append("WELCOME")

    def render_help_proposal(self):
        self.outputs.append("HELP_PROPOSAL")

    def render_error(self, data):
        self.outputs.append(f"ERROR: {data.get('error', 'Unknown error')}")

    def invalid_command(self):
        self.outputs.append("INVALID_COMMAND")

    def update_data(self, contacts, notes):
        self.contacts_data = contacts
        self.notes_data = notes


def test_cli_commands():
    """Test CLI command routing and error handling."""
    print("\n" + "=" * 60)
    print("TESTING CLI COMMAND ROUTING")
    print("=" * 60)

    passed = 0
    failed = 0

    # Create fresh instances
    address_book = AddressBook()
    notebook = NoteBook()
    assistant = Assistent(address_book)
    note_assistant = NoteAssistant(notebook, address_book)
    view = MockView()
    controller = AppController(view, assistant, note_assistant)

    # Test commands
    commands_to_test = [
        # Contact commands
        ("add John +380501234567", "Add contact"),
        ("add Jane jane@example.com", "Add contact with email"),
        ("all", "List all contacts"),
        ("search John", "Search contacts"),
        ("phone John", "Show phone"),
        ("change John +380501234567 +380509999999", "Change phone"),
        ("add-address John 123 Main St", "Add address"),
        (
            f"add-birthday John {(datetime.now() - timedelta(days=365*25)).strftime('%d.%m.%Y')}",
            "Add birthday",
        ),
        ("show-birthday John", "Show birthday"),
        ("birthdays", "Show upcoming birthdays"),
        ("rename John Johnny", "Rename contact"),
        # Note commands
        ("add-note This is a test note", "Add note"),
        ("all-notes", "List all notes"),
        # Invalid commands
        ("add", "Insufficient args - add"),
        ("change John", "Insufficient args - change"),
        ("delete", "Insufficient args - delete"),
        ("add-birthday John", "Insufficient args - add-birthday"),
        ("nonexistent-command", "Invalid command"),
    ]

    for cmd, description in commands_to_test:
        try:
            # Parse command
            parts = cmd.split()
            cmd_name = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            # Clear previous outputs
            view.outputs = []

            # Get handler
            handler = controller.command_routes.get(cmd_name.lower())

            if handler:
                try:
                    handler(args)
                    # Check for errors in output
                    has_error = any("ERROR" in out for out in view.outputs)
                    if description.startswith(
                        "Insufficient args"
                    ) or description.startswith("Invalid"):
                        if has_error:
                            print(f"✅ PASS: {description}")
                            passed += 1
                        else:
                            print(
                                f"❌ FAIL: {description} - Expected error but succeeded"
                            )
                            failed += 1
                    else:
                        if not has_error:
                            print(f"✅ PASS: {description}")
                            passed += 1
                        else:
                            print(f"❌ FAIL: {description} - {view.outputs}")
                            failed += 1
                except Exception as e:
                    if description.startswith("Insufficient args"):
                        print(f"✅ PASS: {description}")
                        passed += 1
                    else:
                        print(f"❌ FAIL: {description} - {e}")
                        failed += 1
            else:
                if description == "Invalid command":
                    print(f"✅ PASS: {description}")
                    passed += 1
                else:
                    print(f"❌ FAIL: {description} - Command not found in routes")
                    failed += 1

        except Exception as e:
            print(f"❌ FAIL: {description} - {e}")
            failed += 1

    # Test note commands with IDs
    print("\nTesting note commands with IDs...")

    # Get a note ID
    notes = note_assistant.get_all_notes()
    if notes:
        note_id = notes[0].id

        note_commands = [
            (f"edit-note {note_id} Updated content", "Edit note"),
            (f"add-tag {note_id} important", "Add tag"),
            (f"get-tags {note_id}", "Get tags"),
            (f"remove-tag {note_id} important", "Remove tag"),
            (f"link-contact {note_id} Johnny", "Link contact"),
            (f"unlink-contact {note_id}", "Unlink contact"),
            (f"delete-note {note_id}", "Delete note"),
        ]

        for cmd, description in note_commands:
            try:
                parts = cmd.split()
                cmd_name = parts[0]
                args = parts[1:] if len(parts) > 1 else []

                view.outputs = []
                handler = controller.command_routes.get(cmd_name.lower())

                if handler:
                    handler(args)
                    has_error = any("ERROR" in out for out in view.outputs)
                    if not has_error:
                        print(f"✅ PASS: {description}")
                        passed += 1
                    else:
                        print(f"❌ FAIL: {description} - {view.outputs}")
                        failed += 1
                else:
                    print(f"❌ FAIL: {description} - Command not found")
                    failed += 1
            except Exception as e:
                print(f"❌ FAIL: {description} - {e}")
                failed += 1

    # Test sort commands
    print("\nTesting sort commands...")

    # Add some notes first
    note_assistant.add_note("Note 1")
    note_assistant.add_note("Note 2")

    sort_commands = [
        ("sort-created", "Sort by created date (asc)"),
        ("sort-created desc", "Sort by created date (desc)"),
        ("sort-updated", "Sort by updated date (asc)"),
        ("sort-updated reverse", "Sort by updated date (desc)"),
    ]

    for cmd, description in sort_commands:
        try:
            parts = cmd.split()
            cmd_name = parts[0]
            args = parts[1:] if len(parts) > 1 else []

            view.outputs = []
            handler = controller.command_routes.get(cmd_name.lower())

            if handler:
                handler(args)
                has_error = any("ERROR" in out for out in view.outputs)
                if not has_error:
                    print(f"✅ PASS: {description}")
                    passed += 1
                else:
                    print(f"❌ FAIL: {description} - {view.outputs}")
                    failed += 1
            else:
                print(f"❌ FAIL: {description} - Command not found")
                failed += 1
        except Exception as e:
            print(f"❌ FAIL: {description} - {e}")
            failed += 1

    # Summary
    total = passed + failed
    print("\n" + "=" * 60)
    print(f"CLI TEST SUMMARY: {passed}/{total} tests passed")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = test_cli_commands()
    sys.exit(0 if success else 1)
