import json
import os

def create_ticket():
    title = input("enter ticket title: ")
    description = input("enter ticket description: ")

    ticket = {
        "id": 1,
        "title": title,
        "description": description,
        "status": "open"
    }

    return ticket

def save_create(ticket):
    filename = "tickets.json"

    if os.path.exists(filename):
        with open(filename,"r") as file:
            tickets = json.load(file)
    else:
        tickets = []
    
    ticket["id"] = len(tickets) + 1
    tickets.append(ticket)

    with open(filename, "w") as file:
        json.dump(tickets, file,indent=4)


    print("ticket created and saved succesfully!")

ticket = create_ticket()
save_create(ticket)
    

