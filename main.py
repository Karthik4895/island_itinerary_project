from parser import parse_input
from itinerary_solver import plan_itinerary
from formatter import format_output
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print("NO ITINERARY")
        return
    H, customers_prefs = parse_input(data)
    itinerary = plan_itinerary(H, customers_prefs)
    print(format_output(itinerary))

if __name__ == "__main__":
    main()