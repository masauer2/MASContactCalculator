import struct # to unpack the binary file
import numpy as np # to store matrix as array
import math # for math.sqrt
from MASAnalysis.frame import Frame

class DCDReader:
    """
    The DCDReader class is used to read in a .dcd trajectory, one timestep at a time.
    Each timestep is stored as a Frame object (see frame.io) which can be used to calculate molecular properties from MD simulation.

    Keyword arguments:
    trajectoryFileName -- file name of DCD trajectory
    file -- File object containing DCD trajectory
    nAtoms -- number of atoms in system
    nFrames -- number of timesteps in simulation
    """
    def __init__(self, trajectoryFileName):
        self.trajectoryFileName = trajectoryFileName
        self.file = open(trajectoryFileName, "rb")
        self.nAtoms, self.nFrames = self.read_DCD_Header()
    
    def __len__(self):
        return self.nFrames
        
    def read_DCD_Header(self):
        struct.unpack('i', self.file.read(4)) 
        struct.unpack('ssss', self.file.read(4))
        nFrames = struct.unpack('i', self.file.read(4))[0]
        t0 = struct.unpack('i', self.file.read(4))[0]
        dt = struct.unpack('i', self.file.read(4))[0]

        #Dummy variables
        for i in range(6):
            struct.unpack('i', self.file.read(4))
        struct.unpack('f', self.file.read(4))
        for i in range(10):
            struct.unpack('i', self.file.read(4))
        struct.unpack('i', self.file.read(4))

        titleLength = int(struct.unpack('i', self.file.read(4))[0])
        title = struct.unpack(f'{titleLength}s', self.file.read(titleLength))

        #Dummies
        struct.unpack('i', self.file.read(4))
        struct.unpack('i', self.file.read(4))

        nAtoms = int(struct.unpack('i', self.file.read(4))[0])
        struct.unpack('i',  self.file.read(4))
        return nAtoms, nFrames

    def read_DCD_Frame(self):
        arr = np.zeros((self.nAtoms,3))
        struct.unpack('i', self.file.read(4))
        struct.unpack('d'*6, self.file.read(8*6))
        struct.unpack('i'*2,self.file.read(4*2))
        for i in range(self.nAtoms):
            arr[i,0]=struct.unpack('f', self.file.read(4))[0]
            
        struct.unpack('i', self.file.read(4))
        struct.unpack('i', self.file.read(4))

        for i in range(self.nAtoms):
            arr[i,1]=struct.unpack('f', self.file.read(4))[0]
        struct.unpack('i', self.file.read(4))
        struct.unpack('i', self.file.read(4))

        for i in range(self.nAtoms):
            arr[i,2]=struct.unpack('f', self.file.read(4))[0]

        struct.unpack('i', self.file.read(4))
        
        # Coordinates in each timestep are stored as Frame (see frame.io)
        return Frame(arr) 
