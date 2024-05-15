from MASAnalysis import *
import time
import sys

def main(arg1, arg2): 
    
    sel1 = np.arange(0,253,1) #Generate selections from user input
    sel2 = np.arange(0,253,1)

    options = {
        "trajectory": str(arg1),
        "skipFrames": 1,
        "framesToRead": 5,
        "grp1": sel1,
        "grp2": sel2,
        "outFile": str(arg2)
    }

    start = time.time()
    
    # New dcd stream
    dcd = DCDReader(options["trajectory"])
    print(f"Read in DCD header for trajectory with {dcd.nFrames} frames and {dcd.nAtoms} atoms.")
    
    # Store coordinates to compute contact distances
    frames = np.empty(dcd.nFrames, dtype=object)

    # For each frame
    for frameNum in range(options["framesToRead"]):
    # Read in the coordinates
        frames[frameNum] = dcd.read_DCD_Frame(dcd.file, frameNum, dcd.nAtoms)
        if(frameNum % options["skipFrames"] == 0):
            print("Compute distance matrix for frame %d" % int(frameNum/options["skipFrames"]))
            distance_matrix = Frame.compute_distance_matrix(frames[frameNum].get_selection(sel1), frames[frameNum].get_selection(sel2))
            Frame.output_distance_matrix(distance_matrix, options["outFile"])
    
    end = time.time()
    print(f"{end - start} seconds to read")

if __name__ == "__main__":
	main("R1.dcd", "tmp")
