import pytest
from MASAnalysis import Frame
import numpy as np

# Make sure distance compute is correct

# Test 1 - simple calc - should work
def test_distance_pass():
    assert Frame.compute_distance(np.array([0.0,0.0,0.0]), np.array([1.0,0.0,0.0])) == 1.0

# Test 2 - simple calc - wrong format
def test_distance_wrong():
    with pytest.raises(Exception) as excinfo:   
        Frame.compute_distance(np.array([0.0,0.0,0.0]), np.array([1.0,0.0]))
    assert "Distance calculator requires 2 arrays of length 3." in str(excinfo.value)

# Make sure inverse distance compute is correct

# Test 1 - simple calc - should work
def test_inverse_distance():
    assert Frame.compute_inverse_distance(np.array([0.0,0.0,0.0]), np.array([1.0,0.0,0.0])) == 1.0

# Test 2 - simple calc - wrong format
def test_inverse_distance_wrong1():
    with pytest.raises(Exception) as excinfo:   
        Frame.compute_inverse_distance(np.array([0.0,0.0,0.0]), np.array([0.0,1.0]))
    assert "Distance calculator requires 2 arrays of length 3." in str(excinfo.value)

# Test 3 - simple calc - same atom - should return -1
def test_inverse_distance_sameAtom():
    assert Frame.compute_inverse_distance(np.array([0.0,0.0,0.0]), np.array([0.0,0.0,0.0])) == -1

