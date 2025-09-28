import random

def generate_event():
    events = [
        {"description": "You encounter a wild beast.", "choices": ["Fight", "Run"]},
        {"description": "You find a treasure chest.", "choices": ["Open", "Ignore"]},
        {"description": "A merchant offers you a deal.", "choices": ["Buy", "Decline"]},
        {"description": "You fall into a trap.", "choices": ["Escape", "Wait"]}
    ]
    return random.choice(events)

def resolve_event(user, choice, event):
    hp = user['hp']
    gold = user['gold']
    xp = user['xp']
    inventory = user.get('inventory', [])

    message = ""

    if event['description'] == "You encounter a wild beast.":
        if choice == "Fight":
            win = random.choice([True, False])
            if win:
                xp += 20
                gold += 10
                message = "You defeated the beast! +20 XP, +10 Gold"
            else:
                hp -= 20
                message = "You got hurt! -20 HP"
        else:
            message = "You ran away safely."

    elif event['description'] == "You find a treasure chest.":
        if choice == "Open":
            gold_found = random.randint(5, 30)
            gold += gold_found
            inventory.append("Treasure")
            message = f"You found treasure! +{gold_found} Gold"
        else:
            message = "You ignored the chest."

    elif event['description'] == "A merchant offers you a deal.":
        if choice == "Buy":
            if gold >= 10:
                gold -= 10
                inventory.append("Potion")
                message = "You bought a potion."
            else:
                message = "Not enough gold!"
        else:
            message = "You declined the deal."

    elif event['description'] == "You fall into a trap.":
        if choice == "Escape":
            success = random.choice([True, False])
            if success:
                message = "You escaped unharmed!"
            else:
                hp -= 15
                message = "You failed to escape! -15 HP"
        else:
            hp -= 10
            message = "You waited too long! -10 HP"

    return {"hp": hp, "gold": gold, "xp": xp, "inventory": inventory, "message": message}
