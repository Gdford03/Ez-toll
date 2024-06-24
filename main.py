Toll = 0
stateCharge = 0
vehicleCharge = 0


def weekEnd():
    if day == 'Y' or day == 'y':
        return True
    else:
        return False


print()
hour = int(input())
day = input()
state = input()
vehicle = input()
if hour >= 24:
    print("Oops! Hour must be 0 - 23.")
    exit()
if state == 'IL' or state == 'MI' or state == 'OH' or state == 'IN' or state == 'WI':
    if state == 'IL':
        stateCharge = 0
    else:
        stateCharge = 1.50
else:
    print("Oops! State must be IL, OH, IN, WI or MI.")
    exit()
if vehicle == 'Truck' or vehicle == 'Car' or vehicle == 'EV':
    if vehicle == 'Truck':
        vehicleCharge = 2.50
    elif vehicle != 'EV':
        vehicleCharge = 0
else:
    print("Oops! Vehicle type must be Car, Truck or EV.")
    exit()

if weekEnd() == True:
    if hour < 7:
        Toll = 0.95
    elif hour >= 7 and hour < 10:
        Toll = 1.75
    elif hour >= 10 and hour < 15:
        Toll = 1.75
    elif hour >= 15 and hour < 20:
        Toll = 1.75
    elif hour >= 20 and hour < 24:
        Toll = 1.10
    if state == 'MI':
        total = 0.05
        print(f"Toll: ${total:.2f}")
        exit()
    elif vehicle == 'EV':
        total = (Toll + stateCharge) * .25
        print(f"Toll: ${Toll:.2f}")
        print(f"{state} surcharge: ${stateCharge:.2f}")
        print(f"{vehicle} surcharge: 25% Discount")
        print(f"Toll total: ${total:.2f}")
        exit()
    if vehicleCharge == 0 and stateCharge == 0:
        print(f"Toll: ${Toll:.2f}")
    elif stateCharge == 0:
        total = Toll + vehicleCharge
        print(f"Toll: ${Toll:.2f}")
        print(f"{vehicle} surcharge: ${vehicleCharge:.2f}")
        print(f"Toll total: ${total:.2f}")
        exit()
    elif vehicleCharge == 0:
        total = Toll + stateCharge
        print(f"{state} surcharge: ${stateCharge:.2f}")
        print(f"Toll total: ${total:.2f}")
    else:
        total = Toll + stateCharge + vehicleCharge
        print(f"Toll: ${Toll:.2f}")
        print(f"{state} surcharge: ${stateCharge:.2f}")
        print(f"{vehicle} surcharge: ${vehicleCharge:.2f}")
        print(f"Toll total: ${total:.2f}")
        exit()
elif weekEnd() == False:
    if hour < 7:
        Toll = 1.05
    elif hour >= 7 and hour < 10:
        Toll = 3.25
    elif hour >= 10 and hour < 15:
        Toll = 2.50
    elif hour >= 15 and hour < 20:
        Toll = 3.45
    elif hour >= 20 and hour < 24:
        Toll = 1.15
    if state == 'MI':
        total = 0.05
        print(f"Toll: ${total:.2f}")
        exit()
    elif vehicle == 'EV':
        total = (Toll + stateCharge) * .25
        print(f"Toll: ${Toll:.2f}")
        print(f"{state} surcharge: ${stateCharge:.2f}")
        print(f"{vehicle} surcharge: 25% Discount")
        print(f"Toll total: ${total:.2f}")
        exit()
    if  vehicleCharge == 0 and stateCharge == 0:
        print(f"Toll: ${Toll:.2f}")
    elif stateCharge == 0:
        total = Toll + vehicleCharge
        print(f"Toll: ${Toll:.2f}")
        print(f"{vehicle} surcharge: ${vehicleCharge:.2f}")
        print(f"Toll total: ${total:.2f}")
        exit()
    elif vehicleCharge == 0:
        total = Toll + stateCharge
        print(f"Toll: ${Toll:.2f}")
        print(f"{state} surcharge: ${stateCharge:.2f}")
        print(f"Toll total: ${total:.2f}")
        exit()
    else:
        total = Toll + stateCharge + vehicleCharge
        print(f"Toll: ${Toll:.2f}")
        print(f"{state} surcharge: ${stateCharge:.2f}")
        print(f"{vehicle} surcharge: ${vehicleCharge:.2f}")
        print(f"Toll total: ${total:.2f}")
        exit()

