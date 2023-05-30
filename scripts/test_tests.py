"""Tests  Management.

This module provides the necessary methods to execute tests.
"""
import os.path
import shutil

DIRECTORY_SOURCE: str = "src"
DIRECTORY_REPORTS_ROOT: str = "reports"
DIRECTORY_TEST_REPORT: str = "reports/tests"
DIRECTORY_COVERAGE_REPORT = "reports/coverage"


def clean() -> None:
    """Clean tests and coverage report."""
    clean_coverage()
    clean_test()


def clean_coverage() -> None:
    """Clean coverage reports."""
    print("=>CLEAN COVERAGE REPORTS -> IN PROGRESS")

    try:
        if os.path.exists(DIRECTORY_COVERAGE_REPORT):
            shutil.rmtree(DIRECTORY_COVERAGE_REPORT)
        elif not os.path.exists(DIRECTORY_REPORTS_ROOT):
            os.mkdir(DIRECTORY_REPORTS_ROOT)

        os.mkdir(DIRECTORY_COVERAGE_REPORT)
    except Exception as e:
        print(e)
        print("=>CLEAN COVERAGE REPORTS -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN COVERAGE REPORTS -> FINISH")


def clean_test() -> None:
    """Clean tests reports."""
    print("=>CLEAN TESTS -> IN PROGRESS")

    try:
        if os.path.exists(DIRECTORY_TEST_REPORT):
            shutil.rmtree(DIRECTORY_TEST_REPORT)
        elif not os.path.exists(DIRECTORY_REPORTS_ROOT):
            os.mkdir(DIRECTORY_REPORTS_ROOT)

        os.mkdir(DIRECTORY_TEST_REPORT)
    except Exception as e:
        print(e)
        print("=>CLEAN TESTS -> ERROR")
        exit(-1)
    else:
        print("=>CLEAN TESTS -> FINISH")


def test() -> None:
    """Execute tests."""
    print("=>TESTS -> IN PROGRESS")

    try:
        commands: tuple[str, ...] = (
            f"nose2 --coverage {DIRECTORY_SOURCE}",
            "coverage html",
            "coverage xml"
        )

        for command in commands:
            return_code: int = os.system(command)

            if return_code != 0:
                raise Exception(f"COMMAND '{command}' RETURN -> {return_code}")
    except Exception as e:
        print(e)
        print("=>TESTS -> ERROR")
        exit(-1)
    else:
        print("=>TESTS -> FINISH")


def retest() -> None:
    """Clean and execute tests."""
    clean()
    test()
