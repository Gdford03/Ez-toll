'''
Garrett Langford

The following code will calculate a toll fee based on the state time of day and vehicle.
The state must be MI, IL, OH, IN, or WI. As well as the vehicle must be a car, truck, or EV.

I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.

September 27th 2023
'''

# true or false boolean for the weekend/ week day
def weekend():
    if week == 'y' or week == 'Y':
        return True
    else:
        return False
vehicle_charge = 0
state_charge = 0
Toll = 0
hour = int(input('Hour: '))
week= input('Is it a weekend (Y,N): ')
state = input('State: ')
vehicle = input('Vehicle type (Car, Truck, EV): ')

# error code for if user inputs higher then 23
if hour >= 24:
    print("Oops! Hour must be 0 - 23.")
    exit()

# Truck surcharge
if vehicle == 'Truck' or vehicle == 'Car' or vehicle == 'EV' or vehicle == 'TRUCK' or vehicle == 'CAR' or vehicle == 'Ev' or vehicle == 'ev':
    if vehicle == 'Truck':
        vehicle_charge = 2.50
    else:
        vehicle_charge = 0

# error code for user inputs a not valid vehicle type
elif vehicle != 'Truck' or vehicle != 'Car' or vehicle != 'EV' or vehicle != 'TRUCK' or vehicle != 'CAR' or vehicle != 'Ev' or vehicle != 'ev':
    print("Oops! Vehicle type must be Car, Truck or EV.")
    exit()

# State check for surcharge
if state == 'IL' or state == 'MI' or state == 'OH' or state == 'IN' or state == 'WI':
    if state == 'IL':
        state_charge = 0
    else:
        state_charge = 1.50

# Check for invalid state
elif state != 'IL' or state != 'MI' or state != 'OH' or state != 'IN' or state != 'WI':
    print("Oops! State must be IL, OH, IN, WI or MI.")
    exit()

# price table for if it is a weekend
if weekend() == True:
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

    # MI state charge
    if state == 'MI':
        print('Toll: $0.05')
        exit()

    # EV discount
    if vehicle == 'EV':
        ev_discount = (state_charge + Toll) * .25
        total = (state_charge + Toll) - ev_discount
        if state_charge > 0:
            print(f'{state} surcharge: ${state_charge:.2f}')
            print(f'{vehicle} discount: ${ev_discount:.2f}')
            print(f'Total: ${total:.2f}')
            exit()

        # In case there is no state charge but vehicle is still a EV
        else:
            print(f'{vehicle} discount: ${ev_discount:.2f}')
            print(f'Total: ${total:.2f}')
            exit()

    # Checks for vehicle charge and state charge
    if vehicle_charge > 0 and state_charge > 0:
        total = vehicle_charge + state_charge + Toll
        print(f'{vehicle} surcharge: ${vehicle_charge:.2f}')
        print(f'{state} surcharge: ${state_charge:.2f}')
        print(f'Total: ${total:.2f}')
        exit()

    # checks for just vehicle charge
    elif vehicle_charge > 0:
        total = vehicle_charge + Toll
        print(f'{vehicle} surcharge: ${vehicle_charge:.2f}')
        print(f'Total: ${total:.2f}')
        exit()

    # Checks for just state charge
    elif state_charge > 0:
        total = Toll + state_charge
        print(f'{state} surcharge: ${state_charge:.2f}')
        print(f'Total: ${total:.2f}')
        exit()

    # if there are no charges prints just the toll
    else:
        print(f'Toll: ${Toll:.2f}')

# recalls weekend for if it's a week day
elif weekend() == False:
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

    # MI state charge
    if state == 'MI':
        print('Toll: $0.05')
        exit()

    # checks for EV and displays EV charges
    if vehicle == 'EV':
        ev_discount = (state_charge + Toll) * .25
        total = (state_charge + Toll) - ev_discount

        # checks for state charge so it can be displayed
        if state_charge > 0:
            print(f'{state} surcharge: ${state_charge:.2f}')
            print(f'{vehicle} discount: ${ev_discount:.2f}')
            print(f'Total: ${total:.2f}')
            exit()

        # Displays EV's discount for when there is no state charge
        else:
            print(f'{vehicle} discount: ${ev_discount:.2f}')
            print(f'Total: ${total:.2f}')
            exit()

    # Checks for if there is a vehicle charge and displays needed info
    if vehicle_charge > 0 and state_charge > 0:
        total = vehicle_charge + state_charge + Toll
        print(f'{vehicle} surcharge: ${vehicle_charge:.2f}')
        print(f'{state} surcharge: ${state_charge:.2f}')
        print(f'Total: ${total:.2f}')
        exit()

    # Checks for just vehicle charge
    elif vehicle_charge > 0:
        total = vehicle_charge + Toll
        print(f'{vehicle} surcharge: ${vehicle_charge:.2f}')
        print(f'Total: ${total:.2f}')
        exit()

    # checks for just state charge so it displays correct info
    elif state_charge > 0:
        total = Toll + state_charge
        print(f'{state} surcharge: ${state_charge:.2f}')
        print(f'Total: ${total:.2f}')
        exit()

    # Displays only toll if there are no other charges
    else:
        print(f'Toll: ${Toll:.2f}')
