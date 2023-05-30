"""Test dependencies Management.

This module provides the necessary methods to create file for Dependency-Tracker.
"""
import os.path

BOM_FILE = "dependencies_bom.xml"


def clean() -> None:
    """Clean BOM file."""
    print("=>CLEAN BOM FILE -> IN PROGRESS")

    try:
        if os.path.exists(BOM_FILE):
            os.remove(BOM_FILE)
    except Exception as e:
        print(e)
        print("=>CLEAN BOM FILE -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN BOM FILE -> FINISH")


def generate() -> None:
    """Generate BOM file."""
    print("=>CREATE BOM FILE -> IN PROGRESS")

    try:
        print("YOU WILL GET THE DEPENDENCIES DIRECTLY FROM PIP\n"
              "INSTALL ALL THE DEPENDENCY GROUPS AND NO OTHER DEPENDENCIES MANUALLY.")

        command: str = f"cyclonedx-py --environment --output {BOM_FILE}"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>CREATE BOM FILE -> ERROR")
        exit(-1)
    else:
        print("=>CREATE BOM FILE -> FINISH")


def regenerate() -> None:
    """Clean BOM file and generate new BOM file."""
    clean()
    generate()
