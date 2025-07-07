rain=input("Is it raining today?")
rain=rain.lower()
if rain=='yes':
    wind=input("Is it windy today?")
    wind=wind.lower()
    if wind=='yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day!")