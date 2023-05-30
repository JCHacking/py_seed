"""Build Management.

This module provides the necessary methods to generate and clean builds.
"""
import os.path
import shutil

DIRECTORY_BUILD: str = "dist"


def clean() -> None:
    """Removes all builds."""
    print("=>CLEAN BULDS -> IN PROGRESS")

    try:
        if os.path.exists(DIRECTORY_BUILD):
            shutil.rmtree(DIRECTORY_BUILD)

        os.mkdir(DIRECTORY_BUILD)
    except Exception as e:
        print(e)
        print("=>CLEAN BUILD -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN BUILDS -> FINISH")


def generate() -> None:
    """Generate build."""
    print("=>GENERATE BUILD -> IN PROGRESS")

    try:
        command: str = "poetry build"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>GENERATE BUILD -> ERROR")
        exit(-1)
    else:
        print("=>GENERATE BUILD -> FINISH")


def regenerate() -> None:
    """Remove all builds and Generate new build."""
    clean()
    generate()
