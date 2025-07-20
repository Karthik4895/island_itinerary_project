# Aegean Tour Itinerary Planner 


Given:
- `H` hops between consecutive islands.
- A list of `C` customers, each with preferences on certain hops and transport modes.

The program computes:
- A valid itinerary that satisfies all customer preferences.
- With the **minimum number of airborne hops** (air travel is expensive and polluting).
- Or returns **NO ITINERARY** if no valid solution exists.



##  How to Run

Create or edit input.txt like:
6
4
0 by-sea, 2 by-sea, 3 by-sea
0 by-sea, 5 airborne
0 airborne, 5 by-sea
2 airborne


Run the Program
From the project root:
python main.py < input.txt


Running Tests

Install pytest if not already:
pip install pytest


pytest tests/test_solver.py


Sample Output

For the input above, the output would be:
0 by-sea, 1 by-sea, 2 airborne, 3 by-sea, 4 by-sea, 5 by-sea