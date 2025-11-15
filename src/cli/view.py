from abc import ABC, abstractmethod


class View(ABC):
    """
    Abstract base class for view implementations.
    Subclasses must implement all abstract methods.
    """

    @abstractmethod
    def prompt(self, message: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def invalid_command(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_error(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_welcome(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_help_proposal(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_help(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_hello(self) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_add(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_change(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_show_phone(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_all(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_add_birthday(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_show_birthday(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_birthdays(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_add_address(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_delete(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def render_rename(self, success: bool, data: dict) -> None:
        raise NotImplementedError("Subclasses must implement this method")