def get_distraction():
    name = input("Task name: ")
    importance = int(input("Importance (1–5): "))
    time = int(input("Time wasted (minutes): "))

    cost = importance * time

    return {
        "name": name,
        "importance": importance,
        "time": time,
        "cost": cost
    }


distractions = []

while True:
    distraction = get_distraction()
    distractions.append(distraction)

    choice = input("Add another distraction? (y/n): ").lower()
    if choice != "y":
        break


print("\n--- Distraction Summary ---")
for d in distractions:
    print(f"{d['name']} → Cost Score: {d['cost']}")

total_cost = 0
for d in distractions:
    total_cost += d["cost"]

print(f"\nTotal Distraction Cost: {total_cost}")
