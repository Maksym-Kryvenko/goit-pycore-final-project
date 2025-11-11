
def parse_input(user_input):
    """Function for parsing input parameters"""
    if len(user_input) != 0:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    else:
        return False, ''
    return cmd, *args