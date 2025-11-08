# tests/calculator/__init__.py
import unittest
from . import calculator_test  # import your test module

def load_tests(loader, tests, pattern):
    """Expose tests from calculator_test.py."""
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(calculator_test))
    return suite
