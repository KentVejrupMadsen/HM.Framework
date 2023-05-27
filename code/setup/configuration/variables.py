from globals \
    import \
    set_path_to_library_folder, \
    set_path_to_output_folder,  \
    set_path_to_project_folder, \
    set_path_to_temporary_folder, \
    get_path_to_project_folder

from tempfile \
    import TemporaryDirectory

from constants \
    import zero

from os.path \
    import \
    split

from os \
    import listdir

from pathlib \
    import Path

temporary_directories = []


def get_temporary_directories() -> list:
    global temporary_directories
    return temporary_directories


def set_temporary_directories(
        value: list
) -> None:
    global temporary_directories
    temporary_directories = value


def search_for_project_recursively(
        current_dir: str
):
    current_location = Path(current_dir)
    found_dirs = listdir(current_dir)

    for f in found_dirs:
        if f == '__project__.py':
            return current_location

    return search_for_project_recursively(
        current_location.parent.absolute().__str__()
    )


def create_temp_directories():
    tmp_dirs = get_temporary_directories()

    output_folder = TemporaryDirectory()

    tmp_dirs.append(output_folder)
    set_path_to_output_folder(output_folder.name)

    temporary_folder = TemporaryDirectory()
    set_path_to_temporary_folder(temporary_folder.name)
    tmp_dirs.append(temporary_folder)


def search_for_library():
    project_location = Path(get_path_to_project_folder())
    set_path_to_library_folder(
        project_location.parent.absolute().__str__()
    )


def search_for_project():
    current_location = __file__
    current_location = split(current_location)[zero()]

    result = search_for_project_recursively(current_location)
    set_path_to_project_folder(result)


# use
def setup_of_default_variables():
    search_for_project()
    search_for_library()

    create_temp_directories()


def clean():
    directories = get_temporary_directories()

    for tmp_dir in directories:
        tmp_dir.cleanup()
