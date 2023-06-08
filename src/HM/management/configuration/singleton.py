from HM.management.configuration \
    import ConfigurationStore


singleton_configuration_store: ConfigurationStore | None = None


def initialise_on_call() -> None:
    global singleton_configuration_store

    if singleton_configuration_store is None:
        singleton_configuration_store = ConfigurationStore()


def get_configuration_store() -> ConfigurationStore:
    global singleton_configuration_store
    initialise_on_call()

    return singleton_configuration_store


def set_configuration_store(
        value: ConfigurationStore | None
) -> None:
    global singleton_configuration_store
    singleton_configuration_store = value
