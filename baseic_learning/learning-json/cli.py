import json
import os

def budget_remaniing(budget, food, transport):
    return budget-food-transport

budget = int(input("budget: "))
food = int(input("food: "))
transport = int(input("transport: "))

remaniing = budget_remaniing(budget, food, transport)

def budget_massage(name, remaniing):
    return f"{name} has {remaniing} naira remaing."

name = str(input("enter user name: "))

massage = budget_massage(name, remaniing )

print(massage)

def save_create(massage):
    filename = "tickets.json"

    if os.path.exists(filename):
        with open(filename,"r") as file:
            tickets = json.load(file)
    else:
        tickets = []
    
    ticket = {
        "id": len(tickets) + 1,
        "massage": massage
    }
    tickets.append(ticket)

    with open(filename, "w") as file:
        json.dump(tickets, file,indent=4)


    print("ticket created and saved succesfully!")

#ticket = create_ticket()
save_create(massage)
    

