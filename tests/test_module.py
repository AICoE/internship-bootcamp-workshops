#!/usr/bin/env python3
# Copyright(C) 2019 <your-name and e-mail>
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Verify implementation of myproject/module.py, implementation of Fibonacci sequence computation."""

import pytest
from hypothesis import given
from hypothesis import example
from hypothesis.strategies import integers


# It's important to have myproject on PYTHONPATH before running the test suite.
from myproject.module import fib


def test_fib_one():
    assert fib(1) == 0, "The very first Fibonacci number should be 0"


def test_fib_two():
    assert fib(2) == 1, "Should be 1 for the second Fibonacci number"


def test_fib_three():
    assert fib(3) == 1, "Wrong third Fibonacci number"


def test_fib_zero():
    """Check zero'th element of an Fibonacci sequence - does 0th number exist?"""
    with pytest.raises(ValueError):
        fib(0)


def test_fib_minus_one():
    """Check that calling fib function raises an exception if called with minus one."""
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_minus_two():
    """Check that calling fib function with minus two raises an exception."""
    with pytest.raises(ValueError):
        fib(-2)


def test_fib_minus_tree():
    """Check that calling fib function with minus three raises an exception."""
    with pytest.raises(ValueError):
        fib(-3)


# D'oh... Let's make a better approach - Hypothesis!


@given(integers(max_value=-1))
@example(-1)
def test_fib_all_negative(n: int):
    """Check that all negative values raise value error."""
    # Why not just use PyTest's parameters here?
    with pytest.raises(ValueError):
        fib(n)
