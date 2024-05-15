# MASContactCalculator
Calculate contact distances from a dcd file. Example of how to read in dcd binary. Also simple example of python project.

## For the Vessels 

This code is setup to read in from a binary "trajectory" file, which stores the atomic coordinates of all atoms involved in molecular simulation. An example can be found at `data/R1.dcd`. 

We read in these `dcd` trajectories using the `DCD` object class. We store each timestep as a `Frame` object, which stores the atomic coordinates at each timestep read in from the `dcd`. We can then break our mental block against physics and compute molecular properties, such as the distance between atoms `compute_distance_matrix`.

## For myself

Things to implement
- A `Selection` class: Allow the user to subselect atoms in a frame.
- One class per type of calculation i.e distance calculations should be stored in a `Distance` class w/ static methods to compute properties on a frame.
- Better documentation
- Unit tests? How do you unit test io functions??
