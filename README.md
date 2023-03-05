# Deutsch-Josza Algorithm

## Problem 
Consider a black box which takes an `n` bit binary string and 
outputs a single binary bit. The black box is said to be
balanced if it outputs a 1 exactly half of the times and a 0
otherwise. Otherwise if the black box always outputs only a 0 (or only a 1) 
for every input it is said to be constant. We can assume that the black box is 
either constant or balanced (but cannot be something in between).
Our requirement is to determine if the black box is constant or balanced.

## Classical Solution
We have the following solution on a classical computer.
Let us check if the black box is balanced.
Then we need to check upto half (+1) of the `n` bit inputs if they all 
output the same value. In other words the algorithm will 
run in $2^(n-1)+1$ executions. If any value is not the same as the previous, 
then we know that it is balanced; otherwise it must be constant (since we assumed 
the black box is either balanced or constant).

Note it is slightly faster to check if the black box is balanced since if we try to check
if it is constant, then we must check all possible `n` bit srings in the worst 
case scenario, however for the balanced case we just need to 
check half+1 of all possible `n` bit strings. 

### Approach
This problem naturally lends itself to a TDD approach. In particular,
it makes sense to create black boxes to test on, before writing
the algorithm to check if the black box is balanced or constant. 

### Run the Classical program
Requires python3 and git installation.

Run the following commands.
```
git pull
python3 -m venv venv
source venv/bin/activate  # to activate the virtual environment
pip install requirements.txt  # if this file exists
python3 classical.py
```

To deactivate the virtual environment on completion
```
deactivate
```

### Run the tests
run tests with command: 
```python -m unittest tests``` 

To understand the program better, try adding (variations of) the following 
code to `classical.py` and running it
```
box = BlackBox(16, 'balanced')
print(box.get_all_input_output_pairs())
print(determine_classical(box)) # should output 'balanced'
```

## Quantum Solution
A quantum solution to this problem is termed the Deustch-Josza algorithm.
It runs in a single step so it is in theory significantly more efficient. 
Practically, the run-time will depend on the size of the input of the black box and
how long it takes to perform a quantum operation on a qpu vs a classical operation on a cpu. 

The black box $f$ can be implemented as an oracle $U_f$ which maps the state 
$\lvert x \rangle \lvert y \rangle \mapsto \lvert x \rangle \lvert y\oplus f(x) \rangle$
(where $\oplus$ is addition modulo 2).

## Improvements
This section is to detail possible improvements and tasks to this mini-project.

### To Do
- add type checking. specific.
- turn into zip file
- add tests for each of the BlackBox methods.
    - write unit test for each black_box case in generate_black_box method.
- add in error handling. Raising exceptions
- PEP guidelines. Make line length less than 78 characters.

### Structural Improvements
- improve structure 
    - setup.py
    - turn into package/module structure
    - (consider using docker container)
- add in hook to run linters, tests, etc. before commiting.
- improve types to make more specific
    - e.g. 0 | 1 ...instead of int (or perhaps byte type)
    - positive int, instead of int
    - specify length of lists
- improve docstrings
    - add sphinx for docstrings?
- check PEP guidelnes
    - add in black and/or flake8 (i.e. linters etc.)
- think about object oriented structure
    - add in abstract classes?
    - compare structure to popular python libraries. e.g. consts file?
- Tests always runs on different black boxes each time it is run, since the black boxes are generated after the code runs. Advantage: more chance of finding an error in code. Disadvantage: Not consistent. Improvement: needs both. 
- allow some of the public BlackBox methods (e.g. get_output, get_all_input_output_pairs) to be run on an optional BlackBox paramater, to take any BlackBox rather than just itself. Would this really be useful? Perhaps it is not good structure.
- make it work on larger bit_length efficiently!! (e.g. 64 bit etc.)
- more tests, e.g.
    - the output is a 1 bit string 
    - the black box is indeed balanced or constant (not something in between)
    - the inputs are all `n` bits
    - if any inputs are missing in get_all_inputs. especially the edge cases 
    - the output and input are strings of blackbox are binary strings
    - output list is of the right length, and balanced!

### Additional feature ideas
- Run quantum algorithm on some different quantum computers/quantum simulators? See how long it takes on different quantum computers to run.
- Use a Quantum Random Number Generator to create your black boxes
    - generate_black_box_with_QRNG. 
    - Can create an abstract BlackBox class first. BlackBoxClassical, BlackBoxQuantum (subclasses).
- Use threads (to parallel process)
- Use streams (to pass some amount of data into it at a time)
- Can I add a stopper/timer... so can stop algorithm running 
and it outputs a probability for it being balanced or constant?
- Generate only a sample of `n` bit inputs, and use machine learning?....using pseudo random number generator? Or a QRNG? To test a sample.
- Make a CLI for users to make various black boxes and store them in a database on the cloud
- Build a checker to see if the black box has already been generated. 

