import struct # to unpack the binary file
import numpy as np # to store matrix as array
import math # for math.sqrt
from MASAnalysis.frame import Frame

class DCDReader:
    
    def __init__(self, trajectoryFileName):

        self.trajectoryFileName = trajectoryFileName
        self.file = open(trajectoryFileName, "rb")
        
        
        struct.unpack('i', self.file.read(4))
        struct.unpack('ssss', self.file.read(4))
        self.nFrames = struct.unpack('i', self.file.read(4))[0]
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

        self.nAtoms = int(struct.unpack('i', self.file.read(4))[0])
        struct.unpack('i', self.file.read(4))
        
        

    def read_DCD_Frame(self, file, frame, nAtoms):
        
        arr = np.zeros((nAtoms,3))
        struct.unpack('i', file.read(4))
        struct.unpack('d'*6, file.read(8*6))
        struct.unpack('i'*2, file.read(4*2))
        for i in range(nAtoms):
            arr[i,0]=struct.unpack('f', file.read(4))[0]
            
        struct.unpack('i', file.read(4))
        struct.unpack('i', file.read(4))

        for i in range(nAtoms):
            arr[i,1]=struct.unpack('f', file.read(4))[0]
        struct.unpack('i', file.read(4))
        struct.unpack('i', file.read(4))

        for i in range(nAtoms):
            arr[i,2]=struct.unpack('f', file.read(4))[0]

        struct.unpack('i', file.read(4))
        
        return Frame(arr)
