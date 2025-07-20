def format_output(itinerary_list):
    if itinerary_list is None:
        return "NO ITINERARY"
    return ", ".join(f"{i} {mode}" for i, mode in enumerate(itinerary_list))