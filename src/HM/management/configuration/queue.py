from HM.globals \
    import negative_one

from HM.management.configuration \
    import ConfigurationEntry


class ConfigurationQueue:
    def __init__(self):
        self.entries: None | list = None

    def __del__(self):
        self.__event_delete_all_entries()
        del self.entries

    def get_element_at(
            self,
            index: int
    ):
        if self.__boundary_is_outside_entry_list_range(index):
            raise IndexError(
                'index out of bounds'
            )

        return self.entries[index]

    def append(
            self,
            value: ConfigurationEntry
    ):
        self.__event_initialise_on_call()
        self.entries.append(value)

    def remove_entry_at(
            self,
            index: int
    ):
        self.entries.pop(index)

    def remove_object(
            self,
            value: ConfigurationEntry
    ):
        self.entries.remove(value)

    def get_entries(self) -> None | list:
        return self.entries

    def set_entries(
            self,
            value: None | list
    ) -> None:
        self.entries = value

    def get_length(self) -> int:
        if self.entries is None:
            return negative_one()

        return len(
            self.entries
        )

    def __event_initialise_on_call(self):
        if self.entries is None:
            self.set_entries(
                []
            )

    def __event_delete_all_entries(self) -> None:
        size = self.get_length()

        if size == -1:
            return

        for index in range(self.get_length()):
            del self.entries[index]

    def __boundary_is_outside_entry_list_range(
            self,
            value: int
    ) -> bool:
        return value > self.get_length()
