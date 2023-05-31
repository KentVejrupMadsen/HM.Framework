# packages
from HM.automation.framework \
    import AutomationFramework

# variables
automation_singleton: None | AutomationFramework = None


# Accessors & State management
##
def is_automation_framework_initialised() -> None:
    global automation_singleton

    if automation_singleton is None:
        automation_singleton = AutomationFramework()


##
def get_automation_framework() -> AutomationFramework | None:
    global automation_singleton

    is_automation_framework_initialised()

    return automation_singleton


##
def set_automation_framework(
        variable: None | AutomationFramework
) -> None:
    global automation_singleton
    automation_singleton = variable

