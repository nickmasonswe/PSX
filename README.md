# PSX

PSX is a Python Learning Platform inspired by CSX.

PSX contains a set of problems and their corresponding tests.

## Directory Structure

- `units/`: Contains a number of folders representing a subset of problem types
  for learning and implementing Python.
- `tests/`: Mirrors units, but for test files for each individual problem subset
  and file.

# Project Structure

- Root/
  - units/
    - part1/
      - **init** .py
      - problem1
      - ...
    - part2/
      - **init** .py
      - problem1
      - ...
    - functions_and_execution_context/
      - **init** .py
      - problem1
      - ...
    - callbacks/
      - **init** .py
      - problem1
      - ...
    - closure/
      - **init** .py
      - problem1
      - ...
    - recursion/
      - **init** .py
      - problem1
      - ...
    - OOP/
      - **init** .py
      - problem1
      - ...
  - tests/
    - part1/
      - **init** .py
      - test_problem1
      - ...
    - part2/
      - **init** .py
      - test_problem1
      - ...
    - functions_and_execution_context/
      - **init** .py
      - test_problem1
      - ...
    - callbacks/
      - **init** .py
      - test_problem1
      - ...
    - closure/
      - **init** .py
      - test_problem1
      - ...
    - recursion/
      - **init** .py
      - test_problem1
      - ...
    - OOP/
      - **init** .py
      - test_problem1
      - ...

## How to Run Tests

1. Install dependencies: In the CLI:

   pip3 install -r requirements.txt

2. To make sure that the testing suite as working correctly, run:

pytest tests/part1/canary_test.py

This should yield exactly 3 passing tests and 3 failing tests if it is working
correctly.

3. To run the built in tests for a specific problem use the pytest keyword and
   specify the tests folder, unit, and problem that you want to test. For
   example, to test problem3 in the closure unit, you would type the following
   into the CLI:

   pytest tests/closure/problem3_test.py

I encourage you to make and run your own test cases making use of print statements and the console!


## UNDER CONSTRUCTION

**Key**
- [x] Done
- [ ] Not started
  [-] In progress

**MVP**
- [x] : Priority 1: Working project skeleton with pytest.ini config
- [x] : Priority 2: Requirements.txt for dependencies
- [x] : Priority 3: Documentation for other devs to use the platform 
- [ ] : Priority 4: Add all problems for each unit
- [ ] : Priority 5: Add tests for each problem in each unit

**Stretch**
- [ ] Stretch 1: Basic GUI
- [ ] Stretch 2: connect back end to front end
- [ ] Stretch 2: Hosting
- [ ] Stretch 3: Improve front end
