import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from itinerary_solver import plan_itinerary

def test_example():
    H = 6
    customers = [
        ([0, 2, 3], None),
        ([0], 5),
        ([5], 0),
        ([], 2)
    ]
    expected = ['by-sea', 'by-sea', 'airborne', 'by-sea', 'by-sea', 'by-sea']
    assert plan_itinerary(H, customers) == expected

def test_no_itinerary():
    H = 1
    customers = [([0], None), ([], 0)]
    assert plan_itinerary(H, customers) is None
