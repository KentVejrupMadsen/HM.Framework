from setup.configuration.variables \
    import setup_of_default_variables


class Setup:
    def __init__(self):
        self.startup()

    def startup(self):
        setup_of_default_variables()
