"""Outdated dependencies Management.

This module provides the necessary methods to create file with outdated dependencies.
"""
import os.path

OUTDATED_DEPENDENCIES_FILE = "dependencies_outdated.txt"


def clean() -> None:
    """Clean outated dependencies file."""
    print("=>CLEAN OUTDATED DEPENDENCIES FILE -> IN PROGRESS")

    try:
        if os.path.exists(OUTDATED_DEPENDENCIES_FILE):
            os.remove(OUTDATED_DEPENDENCIES_FILE)
    except Exception as e:
        print(e)
        print("=>CLEAN OUTDATED DEPENDENCIES FILE -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN OUTDATED DEPENDENCIES FILE -> FINISH")


def generate() -> None:
    """Generate outdated dependencies file."""
    print("=>CREATE OUTDATED DEPENDENCIES FILE -> IN PROGRESS")

    try:
        print("YOU WILL GET THE DEPENDENCIES DIRECTLY FROM PIP\n"
              "INSTALL ALL THE DEPENDENCY GROUPS AND NO OTHER DEPENDENCIES MANUALLY.")

        command: str = f"pip list --outdated > {OUTDATED_DEPENDENCIES_FILE}"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>CREATE OUTDATED DEPENDENCIES FILE -> ERROR")
        exit(-1)
    else:
        print("=>CREATE OUTDATED DEPENDENCIES FILE -> FINISH")


def regenerate() -> None:
    """Clean outdated dependencies file and generate new outdated dependencies file."""
    clean()
    generate()
