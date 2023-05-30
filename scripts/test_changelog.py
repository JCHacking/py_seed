"""Test changelog format Management.

This module provides the necessary methods to test changelog format
"""
from typing import Pattern

import os
import re


def execute() -> None:
    """Execute test changelog format."""
    execute_check_format()
    execute_check_internal_format()


def execute_check_format() -> None:
    """Execute check format with ChangeLog standard."""
    print("=>CHECK CHANGELOG FORMAT -> IN PROGRESS")
    try:
        command: str = "kacl-cli verify"
        return_code: int = os.system(command)

        if return_code != 0:
            raise Exception(f"=>COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>CHECK CHANGELOG FORMAT -> ERROR")
        exit(-1)
    else:
        print("=>CHECK CHANGELOG FORMAT -> FINISH")


def execute_check_internal_format() -> None:
    """Check that lines contain JIRA task and IONOS user."""
    print("=>CHECK CHANGELOG INTERNAL FORMAT -> IN PROGRESS")
    try:
        pattern: Pattern[str] = re.compile(r"^- [A-Z]+-[0-9]+ - @[a-z]+ - ")
        with open(file="CHANGELOG.md", mode="r", encoding='utf-8') as changelog_file:
            for changelog_line in changelog_file.readlines():
                if changelog_line.startswith("-"):
                    if pattern.match(changelog_line) is None:
                        raise Exception(f"=>ERROR LINE -> {changelog_line}")
    except Exception as e:
        print(e)
        print("=>CHECK CHANGELOG INTERNAL FORMAT -> ERROR")
        exit(-1)
    else:
        print("=>CHECK CHANGELOG INTERNAL FORMAT -> FINISH")

