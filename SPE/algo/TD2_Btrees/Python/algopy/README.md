# README

This repository contains classes and objects used throughout the 
algorithmic course @Epita, as well as coding and writing conventions
details in [algopep](https://github.com/Prepa-Epita-Algo/algopy/blob/master/reading_material/algopep.md).

## `algopep`

Writing conventions and coding for algorithmics coursese @Epita. Repo
has a single markdown file containing

  * Naming conventions for files, functions, and classes.

  * Python functions, keywords and modules whose use is allowed in the
    Algorithmic course @Epita. By convention **anything not explicitly
    allowed in algopep is not to be used**.

  * Progress stages ; depending on sudents' progress along their first
    2 years they are allowed a number of extra built-in python
    functions. Each stage corresponds to a specific coding maturity
    presumably achieved by students.

Any modification of coding conventions in the course are first
expected to be pointed out at algopep. 

## `algopy`

`algopy` contains classes and objects used throughout the algorithmic
course @Epita. Coding and writing conventions follow algopep rules.

algopy is an existing Python module!!! (https://pythonhosted.org/algopy/).
Do we have to rename ours?

## Suggestions for Structuring `algopy`

Only bare minimum of OOP might be used, structure of `algo``py` is among :

- One file per type/class containing display, save and load primitives
- Since used classes follow a linear hierarchy conversions of earlier types
  into later ones is included in the latter.
- Data files are stored in a seperate data directory at root level. Each 
  file has prefix the type of data it stores: `bintree_` for objects 
  wrapping BinTrees etc.
- All tests files are in one directory at top level, their naming follows 
  python unittest default naming.

### On-course Modification Question

Switch to object oriented versions at end of S2 (instead of iterative
traversals).
Keep iterative traversals for start of S3 with toolbox (as an extra
assignment?).
