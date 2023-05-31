from HM.automation.singleton   \
    import                     \
    get_automation_framework,  \
    delete_automation_framework


def main():
    automation = get_automation_framework()

    automation.setup()
    automation.execute()

    delete_automation_framework()


if __name__ == '__main__':
    main()
