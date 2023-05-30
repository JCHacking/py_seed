"""Test typing Management.

This module provides the necessary methods to execute typing checker.
"""
import os.path
import shutil

DIRECTORY_REPORTS_ROOT: str = "reports"
DIRECTORY_TYPING: str = "reports/typing"


def clean() -> None:
    """Removes linter reports."""
    print("=>CLEAN TYPING REPORT -> IN PROGRESS")

    try:
        if os.path.exists(DIRECTORY_TYPING):
            shutil.rmtree(DIRECTORY_TYPING)
        elif not os.path.exists(DIRECTORY_REPORTS_ROOT):
            os.mkdir(DIRECTORY_REPORTS_ROOT)

        os.mkdir(DIRECTORY_TYPING)
    except Exception as e:
        print(e)
        print("=>CLEAN TYPING REPORT -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN TYPING REPORT -> FINISH")


def execute() -> None:
    """Execute typing check."""
    print("=>TEST TYPING CHECK -> IN PROGRESS")

    try:
        command: str = "mypy"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>TEST TYPING CHECK -> ERROR")
        exit(-1)
    else:
        print("=>TEST TYPING CHECK -> FINISH")


def reexecute() -> None:
    """Clean reports and execute typing check."""
    clean()
    execute()
