from HM.management.configuration \
    import ConfigurationEntry

from HM.management.configuration \
    import ConfigurationQueue


# todo: Global storage of application state
class ConfigurationStore:
    def __init__(self):
        self.queue = ConfigurationQueue()

    def __del__(self):
        del self.queue

    def get_queue(self) -> ConfigurationQueue:
        return self.queue

    def set_queue(self, value) -> None:
        self.queue = value


## Testing
test = ConfigurationStore()
