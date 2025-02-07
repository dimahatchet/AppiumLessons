import random

import pytest


def test_skip_it():
    name = "Rahul1"
    if name == "Rahul":
        pytest.skip('Skipping as name is Rahul')
