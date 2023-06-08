from abc \
    import ABC


class ConfigurationEntry(ABC):
    def __init__(self):
        self.identifier: str | None = None

    def __del__(self):
        del self.identifier

    def get_identifier(self) -> str:
        return self.identifier

    def set_identifier(
            self,
            value: str
    ) -> None:
        self.identifier = value

