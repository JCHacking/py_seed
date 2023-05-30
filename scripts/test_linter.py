"""Test linter Management.

This module provides the necessary methods to execute linter.
"""
import os.path
import shutil

DIRECTORY_REPORTS_ROOT: str = "reports"
DIRECTORY_LINTER: str = "reports/linter"
DIRECTORY_LINTER_JUNIT_XML: str = "reports/linter/junit.xml"
DIRECTORY_SRC: str = "src"
DIRECTORY_TEST: str = "tests"


def clean() -> None:
    """Removes linter reports."""
    print("=>CLEAN LINTER REPORT -> IN PROGRESS")

    try:
        if os.path.exists(DIRECTORY_LINTER):
            shutil.rmtree(DIRECTORY_LINTER)
        elif not os.path.exists(DIRECTORY_REPORTS_ROOT):
            os.mkdir(DIRECTORY_REPORTS_ROOT)

        os.mkdir(DIRECTORY_LINTER)
    except Exception as e:
        print(e)
        print("=>CLEAN LINTER REPORT -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN LINTER REPORT -> FINISH")


def execute() -> None:
    """Execute linter."""
    print("=>TEST LINTER -> IN PROGRESS")

    try:
        commands: tuple[str, ...] = (
            f"flake8 {DIRECTORY_SRC} {DIRECTORY_TEST}",
            f"flake8 --format junit-xml {DIRECTORY_SRC} {DIRECTORY_TEST} > {DIRECTORY_LINTER_JUNIT_XML}"
        )

        for command in commands:
            return_code: int = os.system(command)

            if return_code != 0:
                raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>TEST LINTER -> ERROR")
        exit(-1)
    else:
        print("=>TEST LINTER -> FINISH")


def reexecute() -> None:
    """Clean reports and execute linter."""
    clean()
    execute()
