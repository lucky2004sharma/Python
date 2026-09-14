score = 0
score += 1 if input("Do you like mornings? (y/n): ").lower() == "y" else 0
score += 1 if input("Do you enjoy planning ahead? (y/n): ").lower() == "y" else 0
score += 1 if input("Do you prefer quiet over loud? (y/n): ").lower() == "y" else 0

if score >= 2:
    print("You're a Planner Owl 🦉 — organized and thoughtful.")
else:
    print("You're a Free Spirit Fox 🦊 — spontaneous and bold.")