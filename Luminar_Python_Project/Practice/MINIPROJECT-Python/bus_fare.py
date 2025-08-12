import sys
routes = {
    'Kochi to Trivandrum': {'time': '08:00 AM', 'price': 300},
    'Kozhikode to Kochi': {'time': '01:30 PM', 'price': 450},
    'Trivandrum to Palakkad': {'time': '10:00 AM', 'price': 550},
    'Kochi to Bangalore': {'time': '09:00 PM', 'price': 900},
}
def routecalc(route):
    for k in routes:
        if route==1:
            if k=='Kochi to Trivandrum':
                amt=routes[k]['price']
                return amt
        elif route==2:
            if k=='Kozhikode to Kochi':
                amt=routes[k]['price']
                return amt
        elif route==3:
            if k=='Trivandrum to Palakkad':
                amt=routes[k]['price']
                return amt
        elif route==4:
            if k=='Kochi to Bangalore':
                amt=routes[k]['price']
                return amt
        else:
            print("Invalid choice!")
            break
def dis(cat,amount,seat,age):
    if cat==1:
        disc =amount *(15 / 100)
        total_disc=disc*seat
        return total_disc
    elif cat==2 and age>60:
        disc = amount * (20 / 100)
        total_disc = disc * seat
        return total_disc
    elif cat==2 and age<60:
        print("No discount!")
        return 0
    elif cat==3:
        print("No discount!")
        return 0
name=input("Enter your name:")
age=int(input("Enter your age:"))
phn=int(input("Enter your phone number:"))
print("1.Kochi to Trivandrum: time:08:00 AM, price:300\n2.Kozhikode to Kochi: time: 01:30 PM, price: 450\n3.Trivandrum to Palakkad: time: 10:00 AM, price: 550\n4.Kochi to Bangalore: time:09:00 PM, price: 900")
route=int(input("Select your route:"))
amount=routecalc(route)
seat=int(input("Enter the number of seats needed:"))
cat=int(input("Enter your category(1.Student/2.Senior/3.General):"))
total=amount*seat #Total amount
disc=dis(cat,amount,seat,age) #Total discount
final=total-disc #Final ticket price
filename = f"{name}_{phn}.txt"
original_stdout = sys.stdout
with open(filename, "w") as f:
    sys.stdout=f
    print('-----------------------------------')
    print('BUS TICKET -TRAVEL AGENCY')
    print('-----------------------------------\n')
    print(f'Passenger name: {name}')
    print(f'Phone Number: {phn}')
    print(f'Age: {age}')
    print(f'Category: {cat}\n')
    if route==1:
        print(f'Route: Kochi to trivandrum')
        print(f"Departure Time: {routes['Kochi to Trivandrum']['time']}")
    elif route==2:
        print(f'Route: Kozhikode to Kochi')
        print(f"Departure Time: {routes['Kozhikode to Kochi']['time']}")
    elif route==3:
        print(f'Route: Trivandrum to Palakkad')
        print(f"Departure Time: {routes['Trivandrum to Palakkad']['time']}")
    elif route==4:
        print(f'Route: Kochi to Bangalore')
        print(f"Departure Time: {routes['Kochi to Bangalore']['time']}")
    print(f'Seats Booked: {seat}\n')
    print('-------------------------')
    if route==1:
        print(f"Ticket Price: {routes['Kochi to Trivandrum']['time']}")
    elif route==2:
        print(f"Ticket Price: {routes['Kozhikode to Kochi']['time']}")
    elif route==3:
        print(f"Ticket Price: {routes['Trivandrum to Palakkad']['time']}")
    elif route==4:
        print(f"Ticket Price: {routes['Kochi to Bangalore']['time']}")
    print(f'Total Amount: {total}')
    print(f'Discount: {disc}')
    print(f'Final Amount: {final}')
    print('-----------------------------------\n')
    print('Thank you for booking with us!')
    nam=name.split(' ')
    print(f'Have a safe journey, {nam[0]}!')
sys.stdout=original_stdout
print('-----------------------------------')
print('BUS TICKET -TRAVEL AGENCY')
print('-----------------------------------\n')
print(f'Passenger name: {name}')
print(f'Phone Number: {phn}')
print(f'Age: {age}')
print(f'Category: {cat}\n')
if route==1:
    print(f'Route: Kochi to trivandrum')
    print(f"Departure Time: {routes['Kochi to Trivandrum']['time']}")
elif route==2:
    print(f'Route: Kozhikode to Kochi')
    print(f"Departure Time: {routes['Kozhikode to Kochi']['time']}")
elif route==3:
    print(f'Route: Trivandrum to Palakkad')
    print(f"Departure Time: {routes['Trivandrum to Palakkad']['time']}")
elif route==4:
    print(f'Route: Kochi to Bangalore')
    print(f"Departure Time: {routes['Kochi to Bangalore']['time']}")
print(f'Seats Booked: {seat}\n')
print('-------------------------')
if route==1:
    print(f"Ticket Price: {routes['Kochi to Trivandrum']['time']}")
elif route==2:
    print(f"Ticket Price: {routes['Kozhikode to Kochi']['time']}")
elif route==3:
    print(f"Ticket Price: {routes['Trivandrum to Palakkad']['time']}")
elif route==4:
    print(f"Ticket Price: {routes['Kochi to Bangalore']['time']}")
print(f'Total Amount: {total}')
print(f'Discount: {disc}')
print(f'Final Amount: {final}')
print('-----------------------------------\n')
print('Thank you for booking with us!')
nam=name.split(' ')
print(f'Have a safe journey, {nam[0]}!')

