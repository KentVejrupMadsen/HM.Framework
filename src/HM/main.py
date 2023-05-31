from HM.automation.singleton \
    import get_automation_framework


def main():
    automation = get_automation_framework()

    try:
        automation.setup()
        automation.execute()

    finally:
        automation.finish()


if __name__ == '__main__':
    main()
