# bmi203-project3

![Unit test status](https://github.com/khanu263/bmi203-project3/workflows/Unit%20tests/badge.svg)

# Assignment Overview
The purpose of this assignment is to implement Prim's algorithm, a non-trivial greedy algorithm used to construct minimum spanning trees. 

# Assignment Tasks

## Coding Assessment
* ~~Complete the `Graph.construct_mst` method found in the mst/graph.py~~

## Software Development Assessment

* ~~Add more assertions to the `check_mst` function in test/test_mst.py~~
* ~~Write at least one more unit test (in the test_mst.py file) for your construct_mst implementation~~
* ~~Automate testing with [Github Actions](https://docs.github.com/en/actions)~~

# Getting Started
To get started you will need to fork this repository onto your own Github account. Work on the codebase from your own repo and commit changes. 

The following packages will be needed:
    - numpy
    - scikit-learn
    - pytest
    - heapq [optional, but highly encouraged]

# Completing the assignment
Make sure to push all your code to Github, ensure that your unit tests are correct, and submit a link to your Github through the Google classroom assignment.

# Grading

## Code (6 points)
* Minimum spanning tree construction works correctly (6)
    * Correct implementation of Prim's algorithm (4)
    * Produces expected output on small graph (1) 
    * Produces expected output on single cell data (1) 

## Unit tests (3 points)
* Added additional checks in `check_mst` to ensure correctness of your implementation (2)
* Added effective unit tests (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
