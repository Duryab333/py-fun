# tests/__init__.py
import unittest

def load_tests(loader, tests, pattern):
    """Automatically load all test cases even if file names don’t start with test_."""
    # Explicitly discover inside subdirectories
    suite = unittest.TestSuite()
    suite.addTests(loader.discover("tests/calculator", pattern="calculator_test.py"))
    return suite
