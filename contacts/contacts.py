import struct # to unpack the binary file
import numpy as np # to store matrix as array
import math # for math.sqrt


class DCDReader:
    
    def __init__(self, trajectoryFileName, analysisFrame, sel1, sel2):
        self.trajectoryFileName = trajectoryFileName
        self.analysisFrame = analysisFrame
        self.sel1 = sel1
        self.sel2 = sel2
        self.file = open(trajectoryFileName, "rb")
    
    def read_DCD_Header(self, file):
        struct.unpack('i', file.read(4))
        struct.unpack('ssss', file.read(4))
        nFrames = struct.unpack('i', file.read(4))[0]
        t0 = struct.unpack('i', file.read(4))[0]
        dt = struct.unpack('i', file.read(4))[0]

        #Dummy variables
        for i in range(6):
            struct.unpack('i', file.read(4))
        struct.unpack('f', file.read(4))
        for i in range(10):
            struct.unpack('i', file.read(4))
        struct.unpack('i', file.read(4))

        titleLength = int(struct.unpack('i', file.read(4))[0])
        title = struct.unpack(f'{titleLength}s', file.read(titleLength))

        #Dummies
        struct.unpack('i', file.read(4))
        struct.unpack('i', file.read(4))

        nAtoms = int(struct.unpack('i', file.read(4))[0])
        struct.unpack('i', file.read(4))

        return nFrames, nAtoms

    def read_DCD_Frame(self, file, frame, nAtoms):
        arr = np.zeros((nAtoms, 3))
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
        return arr

    def compute_distance(coord1, coord2):
        return np.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2 + (coord1[2]-coord2[2])**2)

    def compute_inverse_distance(self, coord1, coord2):
        tmp = DCDReader.compute_distance(coord1, coord2)
        if tmp != 0:
            return 1/tmp
        else:
            return -1
        
    def output_distance_matrix(matrix, outstr):
        for slice_2d in matrix:
            np.savetxt(outstr, slice_2d)
        