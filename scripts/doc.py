"""Documentation Management.

This module provides the necessary methods to generate and clean documentation.
"""
import os.path
import shutil

DIRECTORY_DOC_ROOT: str = "docs"
DIRECTORY_HTML: str = "docs/dist"
DIRECTORY_CONFIG: str = "docs/src"
DIRECTORY_SRC: str = "src"


def clean() -> None:
    """Removes documentation."""
    clean_doc()
    clean_rst()


def clean_doc() -> None:
    """Remove documentation files."""
    print("=>CLEAN DOC -> IN PROGRESS")
    try:
        if os.path.exists(DIRECTORY_HTML):
            shutil.rmtree(DIRECTORY_HTML)
        elif not os.path.exists(DIRECTORY_DOC_ROOT):
            os.mkdir(DIRECTORY_DOC_ROOT)

        os.mkdir(DIRECTORY_HTML)
    except Exception as e:
        print(e)
        print("=>CLEAN DOC -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN DOC -> FINISH")


def clean_rst() -> None:
    """Remove RST files."""
    print("=>CLEAN RST -> IN PROGRESS")
    try:
        files = os.listdir(DIRECTORY_CONFIG)

        for file in files:
            if file.endswith("rst") and file != "index.rst":
                os.remove(f"{DIRECTORY_CONFIG}/{file}")
    except Exception as e:
        print(e)
        print("=>CLEAN RST -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN RST -> FINISH")


def generate() -> None:
    """Generate documentation."""
    generate_rst()
    generate_doc()


def generate_rst() -> None:
    """Generate RST files."""
    print("=>GENERATE RST -> IN PROGRESS")
    try:
        command: str = f"sphinx-apidoc -f -o {DIRECTORY_CONFIG} {DIRECTORY_SRC}"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>GENERATE RST -> ERROR")
        exit(-1)
    else:
        print("=>GENERATE RST -> FINISH")


def generate_doc() -> None:
    """Generate documentation files."""
    print("=>GENERATE DOC -> IN PROGRESS")
    try:
        command: str = f"sphinx-build -b html {DIRECTORY_CONFIG} {DIRECTORY_HTML}"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>GENERATE DOC -> ERROR")
        exit(-1)
    else:
        print("=>GENERATE DOC -> FINISH")


def regenerate() -> None:
    """Remove documentation and Generate new documentation."""
    clean()
    generate()
