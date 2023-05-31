# Variables
debug_mode: bool = False


# Accessors
def get_debug_mode() -> bool:
    global debug_mode
    return debug_mode


def set_debug_mode(value: bool):
    global debug_mode
    debug_mode = value
