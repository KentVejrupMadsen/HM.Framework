from framework \
    import AutomationFramework

from globals.paths import get_path_to_user_directory


def main():
    automated = AutomationFramework()

    try:
        automated.setup()
        automated.execute()

    finally:
        automated.finish()


if __name__ == '__main__':
    main()
