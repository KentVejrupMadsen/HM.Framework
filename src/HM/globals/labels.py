from HM.objects.labels.extensions.scripts \
    import get_python_label \
    as python_extension


def get_project_file_label() -> str:
    return '__project__' + python_extension()

