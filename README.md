# MASContactCalculator
Calculate molecular properties from a dcd file.

## Setup

```
cd MASContactCalculator
pip install -e .
```
Currently only requiring numpy for array usage.



## To-Do List
- A `Selection` class: Allow the user to subselect atoms in a frame.
- One class per type of calculation i.e distance calculations should be stored in a `Distance` class w/ static methods to compute properties on a frame.
- Better documentation
- Unit tests? How do you unit test io functions??
