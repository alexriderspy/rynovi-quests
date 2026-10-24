"""Gives your tests a `Cart` to test. Don't edit this file.

The quest runner swaps in versions with planted bugs to check that your tests catch them.
"""
import importlib
import os

import pytest


@pytest.fixture
def Cart():
    module = os.environ.get("RYNOVI_CART", "quests.day05.cart")
    return importlib.import_module(module).Cart
