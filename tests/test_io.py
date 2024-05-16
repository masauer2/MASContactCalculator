import pytest
from MASAnalysis.io import DCDReader
import numpy as np

# Ensure that we are reading in the file correctly
def test_DCDReader_init():
    dcd = DCDReader("../data/R1.dcd") 
    assert dcd.trajectoryFileName == "../data/R1.dcd" 
    assert dcd.nAtoms == 253
    assert dcd.nFrames == 501

# Ensure that the frame is read in correctly
def test_DCDReader_reader():
    dcd = DCDReader("../data/R1.dcd") 
    values = dcd.read_DCD_Frame()
    assert len(values) == 253

# Add Unit Test for coordinate matching - requires pdb reader to compare against..

