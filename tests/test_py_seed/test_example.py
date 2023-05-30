"""Sample module test."""
import unittest

import py_seed.example


class TestExample(unittest.TestCase):
    """Tests for the example module."""

    def test_function(self) -> None:
        """Function test."""
        self.assertEqual(
            first=py_seed.function(),
            second="EXAMPLE",
            msg="Error in the example test"
        )
