from setup.configuration.variables \
    import \
    setup_of_default_variables, \
    clean

from jobs.workflows \
    import Workflow


class AutomationFramework:
    def __init__(self):
        setup_of_default_variables()
        self.workflow = Workflow()

    def __del__(self):
        clean()

    def setup(self):
        pass

    def execute(self):
        pass

    def finish(self):
        pass
