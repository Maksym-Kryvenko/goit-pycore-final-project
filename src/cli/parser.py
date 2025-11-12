def parse_input(user_input: str) -> tuple:
    """
    Parse user input into command and arguments.
    :param user_input: str The raw input string from the user.

    Return: Tuple of command and list of arguments.
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    return command, *args
