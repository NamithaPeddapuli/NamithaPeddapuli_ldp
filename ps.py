def greedy_match(candidates, location_capacity):
    final = {}
    print(location_capacity)
    for candidate, preferences in candidates:
        assigned = False
        for i in preferences:
            if location_capacity[i] > 0:
                final[candidate] = i
                location_capacity[i] -= 1
                assigned = True
                break
        if not assigned:
            final[candidate] = None
    return final

candidates = [("John", ["Chennai", "Hyderabad", "Banglore"]), ("Alice", ["Banglore", "Chennai"]), ("Bob", ["Hyderabad", "Chennai", "Banglore"]), ("Eve", ["Chennai","Hyderabad"])]
locations = {"Chennai": 1, "Banglore": 1, "Hyderabad": 1}
assignments = greedy_match(candidates, locations)
print(assignments)
