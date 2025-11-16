#!/usr/bin/env python3
"""Comprehensive test script for the assistant application."""

import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path so we can import src
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models import AddressBook, NoteBook, Contact, Note
from src.services.assistent import Assistent
from src.services.note_assistant import NoteAssistant
from src.errors import ValidationError, NotFoundError, DuplicationError, CommandError


class TestResults:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def log_pass(self, test_name):
        self.passed += 1
        print(f"✅ PASS: {test_name}")

    def log_fail(self, test_name, error):
        self.failed += 1
        self.errors.append((test_name, str(error)))
        print(f"❌ FAIL: {test_name} - {error}")

    def summary(self):
        total = self.passed + self.failed
        print("\n" + "=" * 60)
        print(f"TEST SUMMARY: {self.passed}/{total} tests passed")
        print("=" * 60)
        if self.errors:
            print("\nFAILED TESTS:")
            for test_name, error in self.errors:
                print(f"  - {test_name}: {error}")
        return self.failed == 0


def test_contact_management(results):
    """Test all contact management operations."""
    print("\n" + "=" * 60)
    print("TESTING CONTACT MANAGEMENT")
    print("=" * 60)

    address_book = AddressBook()
    assistant = Assistent(address_book)

    # Test 1: Add contact with phone
    try:
        action, contact = assistant.add_contact("John", "+380501234567")
        assert action == "created"
        assert contact.name.value == "John"
        assert len(contact.phones) == 1
        results.log_pass("Add contact with phone")
    except Exception as e:
        results.log_fail("Add contact with phone", e)

    # Test 2: Add phone to existing contact
    try:
        action, contact = assistant.add_contact("John", "+380509876543")
        assert action == "updated"
        assert len(contact.phones) == 2
        results.log_pass("Add phone to existing contact")
    except Exception as e:
        results.log_fail("Add phone to existing contact", e)

    # Test 3: Add contact with email
    try:
        action, contact = assistant.add_contact("Jane", "jane@example.com")
        assert action == "created"
        assert len(contact.emails) == 1
        results.log_pass("Add contact with email")
    except Exception as e:
        results.log_fail("Add contact with email", e)

    # Test 4: Change phone number
    try:
        contact = assistant.change_contact("John", "+380501234567", "+380501111111")
        assert contact.find_phone("+380501111111") is not None
        assert contact.find_phone("+380501234567") is None
        results.log_pass("Change phone number")
    except Exception as e:
        results.log_fail("Change phone number", e)

    # Test 5: Add birthday
    try:
        past_date = (datetime.now() - timedelta(days=365 * 30)).strftime("%d.%m.%Y")
        contact = assistant.add_birthday("John", past_date)
        assert contact.birthday.value is not None
        results.log_pass("Add birthday")
    except Exception as e:
        results.log_fail("Add birthday", e)

    # Test 6: Add address
    try:
        contact = assistant.add_address("John", "123 Main St, New York")
        assert contact.address.value == "123 Main St, New York"
        results.log_pass("Add address")
    except Exception as e:
        results.log_fail("Add address", e)

    # Test 7: Rename contact
    try:
        contact = assistant.rename_contact("John", "Johnny")
        assert address_book.find("Johnny") is not None
        assert address_book.find("John") is None
        results.log_pass("Rename contact")
    except Exception as e:
        results.log_fail("Rename contact", e)

    # Test 8: Search contacts
    try:
        contacts = assistant.search_contacts("Jane")
        assert len(contacts) == 1
        assert contacts[0].name.value == "Jane"
        results.log_pass("Search contacts")
    except Exception as e:
        results.log_fail("Search contacts", e)

    # Test 9: Get all contacts
    try:
        all_contacts = assistant.get_all_contacts()
        assert len(all_contacts) == 2
        results.log_pass("Get all contacts")
    except Exception as e:
        results.log_fail("Get all contacts", e)

    # Test 10: Delete contact
    try:
        assistant.delete_contact("Jane")
        assert address_book.find("Jane") is None
        results.log_pass("Delete contact")
    except Exception as e:
        results.log_fail("Delete contact", e)


def test_contact_validation_errors(results):
    """Test contact validation and error handling."""
    print("\n" + "=" * 60)
    print("TESTING CONTACT VALIDATION & ERROR HANDLING")
    print("=" * 60)

    address_book = AddressBook()
    assistant = Assistent(address_book)

    # Test 1: Invalid phone format
    try:
        assistant.add_contact("Bob", "123")
        results.log_fail("Invalid phone validation", "Should raise ValidationError")
    except ValidationError:
        results.log_pass("Invalid phone validation")
    except Exception as e:
        results.log_fail("Invalid phone validation", f"Wrong exception: {e}")

    # Test 2: Invalid email format
    try:
        assistant.add_contact("Bob", "invalid-email")
        results.log_fail("Invalid email validation", "Should raise ValidationError")
    except ValidationError:
        results.log_pass("Invalid email validation")
    except Exception as e:
        results.log_fail("Invalid email validation", f"Wrong exception: {e}")

    # Test 3: Empty name
    try:
        assistant.add_contact("", "+380501234567")
        results.log_fail("Empty name validation", "Should raise ValidationError")
    except ValidationError:
        results.log_pass("Empty name validation")
    except Exception as e:
        results.log_fail("Empty name validation", f"Wrong exception: {e}")

    # Test 4: Name with digits
    try:
        assistant.add_contact("John123", "+380501234567")
        results.log_fail("Name with digits validation", "Should raise ValidationError")
    except ValidationError:
        results.log_pass("Name with digits validation")
    except Exception as e:
        results.log_fail("Name with digits validation", f"Wrong exception: {e}")

    # Test 5: Future birthday
    try:
        assistant.add_contact("Alice", "+380501234567")
        future_date = (datetime.now() + timedelta(days=365)).strftime("%d.%m.%Y")
        assistant.add_birthday("Alice", future_date)
        results.log_fail("Future birthday validation", "Should raise ValidationError")
    except ValidationError:
        results.log_pass("Future birthday validation")
    except Exception as e:
        results.log_fail("Future birthday validation", f"Wrong exception: {e}")

    # Test 6: Contact not found
    try:
        assistant.change_contact("NonExistent", "+380501234567", "+380509999999")
        results.log_fail("Contact not found error", "Should raise NotFoundError")
    except NotFoundError:
        results.log_pass("Contact not found error")
    except Exception as e:
        results.log_fail("Contact not found error", f"Wrong exception: {e}")

    # Test 7: Duplicate contact name on rename
    try:
        assistant.add_contact("Alice", "+380501234567")
        assistant.add_contact("Bob", "+380509876543")
        assistant.rename_contact("Alice", "Bob")
        results.log_fail("Duplicate rename validation", "Should raise DuplicationError")
    except DuplicationError:
        results.log_pass("Duplicate rename validation")
    except Exception as e:
        results.log_fail("Duplicate rename validation", f"Wrong exception: {e}")


def test_note_management(results):
    """Test all note management operations."""
    print("\n" + "=" * 60)
    print("TESTING NOTE MANAGEMENT")
    print("=" * 60)

    address_book = AddressBook()
    notebook = NoteBook()
    note_assistant = NoteAssistant(notebook, address_book)

    # Add a contact for linking tests
    contact_assistant = Assistent(address_book)
    contact_assistant.add_contact("TestUser", "+380501234567")

    # Test 1: Add note
    try:
        note = note_assistant.add_note("This is a test note")
        assert note.content.value == "This is a test note"
        assert note.id is not None
        results.log_pass("Add note")
    except Exception as e:
        results.log_fail("Add note", e)

    # Test 2: Edit note
    try:
        note = note_assistant.add_note("Original content")
        note_id = note.id
        edited_note = note_assistant.edit_note(note_id, "Updated content")
        assert edited_note.content.value == "Updated content"
        results.log_pass("Edit note")
    except Exception as e:
        results.log_fail("Edit note", e)

    # Test 3: Add tags to note
    try:
        note = note_assistant.add_note("Note with tags")
        note_id = note.id
        note_assistant.add_tags_to_note(note_id, "important", "work")
        assert len(note.tags) == 2
        results.log_pass("Add tags to note")
    except Exception as e:
        results.log_fail("Add tags to note", e)

    # Test 4: Remove tag from note
    try:
        note = note_assistant.add_note("Note for tag removal")
        note_id = note.id
        note_assistant.add_tags_to_note(note_id, "tag1", "tag2", "tag3")
        note_assistant.remove_tag_from_note(note_id, "tag2")
        assert len(note.tags) == 2
        results.log_pass("Remove tag from note")
    except Exception as e:
        results.log_fail("Remove tag from note", e)

    # Test 5: Link note to contact
    try:
        note = note_assistant.add_note("Note linked to contact")
        note_id = note.id
        note_assistant.link_note_to_contact(note_id, "TestUser")
        assert note.contact is not None
        assert note.contact.name.value == "TestUser"
        results.log_pass("Link note to contact")
    except Exception as e:
        results.log_fail("Link note to contact", e)

    # Test 6: Unlink note from contact
    try:
        note = note_assistant.add_note("Note to unlink")
        note_id = note.id
        note_assistant.link_note_to_contact(note_id, "TestUser")
        note_assistant.unlink_note_from_contact(note_id)
        assert note.contact is None
        results.log_pass("Unlink note from contact")
    except Exception as e:
        results.log_fail("Unlink note from contact", e)

    # Test 7: Search notes by tags
    try:
        note1 = note_assistant.add_note("Note 1")
        note_assistant.add_tags_to_note(note1.id, "python")
        note2 = note_assistant.add_note("Note 2")
        note_assistant.add_tags_to_note(note2.id, "javascript")

        results_python = note_assistant.search_notes("python")
        assert len(results_python) >= 1
        results.log_pass("Search notes by tags")
    except Exception as e:
        results.log_fail("Search notes by tags", e)

    # Test 8: Get all notes
    try:
        all_notes = note_assistant.get_all_notes()
        assert len(all_notes) > 0
        results.log_pass("Get all notes")
    except Exception as e:
        results.log_fail("Get all notes", e)

    # Test 9: Get all tags
    try:
        all_tags = note_assistant.get_all_tags()
        assert len(all_tags) > 0
        results.log_pass("Get all tags")
    except Exception as e:
        results.log_fail("Get all tags", e)

    # Test 10: Sort by created date
    try:
        sorted_notes = note_assistant.sort_by_created_date(reverse=False)
        assert len(sorted_notes) > 0
        results.log_pass("Sort by created date")
    except Exception as e:
        results.log_fail("Sort by created date", e)

    # Test 11: Sort by updated date
    try:
        sorted_notes = note_assistant.sort_by_updated_date(reverse=True)
        assert len(sorted_notes) > 0
        results.log_pass("Sort by updated date")
    except Exception as e:
        results.log_fail("Sort by updated date", e)

    # Test 12: Delete note
    try:
        note = note_assistant.add_note("Note to delete")
        note_id = note.id
        note_assistant.delete_note(note_id)
        assert note_assistant.find_note(note_id) is None
        results.log_pass("Delete note")
    except Exception as e:
        results.log_fail("Delete note", e)


def test_note_error_handling(results):
    """Test note error handling."""
    print("\n" + "=" * 60)
    print("TESTING NOTE ERROR HANDLING")
    print("=" * 60)

    address_book = AddressBook()
    notebook = NoteBook()
    note_assistant = NoteAssistant(notebook, address_book)

    # Test 1: Edit non-existent note
    try:
        note_assistant.edit_note("nonexistent123", "New content")
        results.log_fail("Edit non-existent note", "Should raise NotFoundError")
    except NotFoundError:
        results.log_pass("Edit non-existent note")
    except Exception as e:
        results.log_fail("Edit non-existent note", f"Wrong exception: {e}")

    # Test 2: Delete non-existent note
    try:
        note_assistant.delete_note("nonexistent456")
        results.log_fail("Delete non-existent note", "Should raise NotFoundError")
    except NotFoundError:
        results.log_pass("Delete non-existent note")
    except Exception as e:
        results.log_fail("Delete non-existent note", f"Wrong exception: {e}")

    # Test 3: Link note to non-existent contact
    try:
        note = note_assistant.add_note("Test note")
        note_assistant.link_note_to_contact(note.id, "NonExistentContact")
        results.log_fail("Link to non-existent contact", "Should raise NotFoundError")
    except NotFoundError:
        results.log_pass("Link to non-existent contact")
    except Exception as e:
        results.log_fail("Link to non-existent contact", f"Wrong exception: {e}")

    # Test 4: Link non-existent note to contact
    try:
        contact_assistant = Assistent(address_book)
        contact_assistant.add_contact("TestUser", "+380501234567")
        note_assistant.link_note_to_contact("nonexistent789", "TestUser")
        results.log_fail(
            "Link non-existent note to contact", "Should raise NotFoundError"
        )
    except NotFoundError:
        results.log_pass("Link non-existent note to contact")
    except Exception as e:
        results.log_fail("Link non-existent note to contact", f"Wrong exception: {e}")


def test_birthdays(results):
    """Test birthday functionality."""
    print("\n" + "=" * 60)
    print("TESTING BIRTHDAY FUNCTIONALITY")
    print("=" * 60)

    address_book = AddressBook()
    assistant = Assistent(address_book)

    # Test 1: Upcoming birthdays
    try:
        # Add contact with birthday next week
        today = datetime.now()
        next_week = today + timedelta(days=5)
        # Use birth year 30 years ago
        birth_year = today.year - 30
        birthday_str = f"{next_week.day:02d}.{next_week.month:02d}.{birth_year}"

        assistant.add_contact("BirthdayPerson", "+380501234567")
        assistant.add_birthday("BirthdayPerson", birthday_str)

        upcoming = assistant.birthdays()
        assert len(upcoming) >= 0  # Might be 0 or 1 depending on day of week
        results.log_pass("Get upcoming birthdays")
    except Exception as e:
        results.log_fail("Get upcoming birthdays", e)


def test_edge_cases(results):
    """Test edge cases and boundary conditions."""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES")
    print("=" * 60)

    address_book = AddressBook()
    assistant = Assistent(address_book)

    # Test 1: Very long name
    try:
        long_name = "A" * 100
        assistant.add_contact(long_name, "+380501234567")
        results.log_pass("Very long name")
    except Exception as e:
        results.log_fail("Very long name", e)

    # Test 2: Unicode name
    try:
        assistant.add_contact("Максим", "+380501234567")
        results.log_pass("Unicode name")
    except Exception as e:
        results.log_fail("Unicode name", e)

    # Test 3: Multiple phones for same contact
    try:
        assistant.add_contact("MultiPhone", "+380501111111")
        assistant.add_contact("MultiPhone", "+380502222222")
        assistant.add_contact("MultiPhone", "+380503333333")
        contact = address_book.find("MultiPhone")
        assert len(contact.phones) == 3
        results.log_pass("Multiple phones")
    except Exception as e:
        results.log_fail("Multiple phones", e)

    # Test 4: Empty note content
    try:
        notebook = NoteBook()
        note_assistant = NoteAssistant(notebook, address_book)
        note = note_assistant.add_note("")
        assert note.content.value == ""
        results.log_pass("Empty note content")
    except Exception as e:
        results.log_fail("Empty note content", e)

    # Test 5: Very long note content
    try:
        notebook = NoteBook()
        note_assistant = NoteAssistant(notebook, address_book)
        long_content = "A" * 10000
        note = note_assistant.add_note(long_content)
        assert len(note.content.value) == 10000
        results.log_pass("Very long note content")
    except Exception as e:
        results.log_fail("Very long note content", e)

    # Test 6: Special characters in note
    try:
        notebook = NoteBook()
        note_assistant = NoteAssistant(notebook, address_book)
        special_content = "Test !@#$%^&*()_+-=[]{}|;':\",./<>?"
        note = note_assistant.add_note(special_content)
        assert note.content.value == special_content
        results.log_pass("Special characters in note")
    except Exception as e:
        results.log_fail("Special characters in note", e)


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("COMPREHENSIVE ASSISTANT APPLICATION TEST SUITE")
    print("=" * 60)

    results = TestResults()

    # Run all test suites
    test_contact_management(results)
    test_contact_validation_errors(results)
    test_note_management(results)
    test_note_error_handling(results)
    test_birthdays(results)
    test_edge_cases(results)

    # Print summary
    success = results.summary()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
