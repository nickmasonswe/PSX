# PSX

PSX is a Python Learning Platform inspired by CSX

PSX contains a set of problems and their corresponding tests.

## Directory Structure

- `units/`: Contains a number of folders representing a subset of problem types
  for learning and implementing Python.
  
- `tests/`: Mirrors units, but for test files for each individual problem subset
  and file.
  
Root/
│
├── units/
│   ├── part1/
│   │   ├── __init__.py
│   │   ├── problem1
│   │   └── ...
│   │
│   ├── part2/
│   │   ├── __init__.py
│   │   ├── problem1
│   │   └── ...
│   │
│   ├── functions_and_execution_context/
│   │   ├── __init__.py
│   │   ├── problem1
│   │   └── ...
│   │
│   ├── callbacks/
│   │   ├── __init__.py
│   │   ├── problem1
│   │   └── ...
│   │
│   ├── closure/
│   │   ├── __init__.py
│   │   ├── problem1
│   │   └── ...
│   │
│   ├── recursion/
│   │   ├── __init__.py
│   │   ├── problem1
│   │   └── ...
│   │
│   └── OOP/
│       ├── __init__.py
│       ├── problem1
│       └── ...
│
└── tests/
    ├── part1/
    │   ├── __init__.py
    │   ├── test_problem1
    │   └── ...
    │
    ├── part2/
    │   ├── __init__.py
    │   ├── test_problem1
    │   └── ...
    │
    ├── functions_and_execution_context/
    │   ├── __init__.py
    │   ├── test_problem1
    │   └── ...
    │
    ├── callbacks/
    │   ├── __init__.py
    │   ├── test_problem1
    │   └── ...
    │
    ├── closure/
    │   ├── __init__.py
    │   ├── test_problem1
    │   └── ...
    │
    ├── recursion/
    │   ├── __init__.py
    │   ├── test_problem1
    │   └── ...
    │
    └── OOP/
        ├── __init__.py
        ├── test_problem1
        └── ...


## How to Run Tests

1. Install dependencies: In the CLI:

   pip3 install -r requirements.txt

2. To run the built in tests for a specific problem use the pytest keyword and
   specify the tests folder, unit, and problem that you want to test. For
   example, to test problem_3 in the closure unit, you would type the following
   into the CLI:

   pytest tests/closure/test_problem3.py

I encourage you make and run your own test cases making use of print statements and the console!
