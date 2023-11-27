while True:
    print("\n\tWELCOME TO CAB SERVICE!\n")
    print("""     
                       _______
                      //  ||\ \\
                _____//___||_\ \___
               (  _          _     \\
                |_/ \________/ \___|
               ___(_)________(_)______
           """)
    print('--Which Vehicle Do you Want?-- ')
    print('')
    print('#1 Car')
    print('#2 Van')
    print('#3 Wheelers')
    print('#4 Trucks')
    print('#5 Lorry')
    print('#6 Exit')
    userInput=input('Please choose from one of the above options: ')
    if userInput == "1":
       #car
       class Car:
           def __init__(self):
                   self._Id = '0'
                   self._MaximumNumberOfPassengers = '0'
                   self._AcOrNonAc = ''

           def addVehicle(self):
                   try:
                       self._Id = input("Enter ID: ")
                       self._MaximumNumberOfPassengers = input('Enter maximum number of passenger: ')
                       self._AcOrNonAc = input('Enter Ac or Non-Ac: ')
                       return True
                   except ValueError:
                       print('Please try entering vehicle information')
                       return False

           def __str__(self):
                   return '\t'.join(str(x) for x in [self._Id, self._MaximumNumberOfPassengers, self._AcOrNonAc])


       class Inventory:
              def __init__(self):
                   self.vehicles = []

              def addVehicle(self):
                   vehicle = Car()
                   if vehicle.addVehicle() == True:
                       self.vehicles.append(vehicle)
                       print()
                       print('This vehicle has been added, Thank you')

              def viewInventory(self):
                   print('\t'.join(["  ",'Id', 'Maximum number of passengers', 'Ac or Non-Ac']))
                   for idx, vehicle in enumerate(self.vehicles):
                       print(idx + 1, end='\t')
                       print(vehicle)

       inventory = Inventory()
       while True:
               print('')
               print('---How We Can Help You?--- ')
               print('')
               print('#1 Add Vehicle to system')
               print('#2 Delete Vehicle from system')
               print('#3 View Current system')
               print('#4 Assign Hire')
               print('#5 complete hire')
               print('#6 Quit')
               userInput = input('Please choose from one of the above options: ')
               if userInput == "1":
                   # add a vehicle
                   inventory.addVehicle()
               elif userInput == '2':
                   # delete a vehicle
                   if len(inventory.vehicles) < 1:
                       print('Sorry there are no vehicles currently in inventory')
                       continue
                   inventory.viewInventory()
                   item = int(input('Please enter the number associated with the vehicle to be removed: '))
                   if item - 1 > len(inventory.vehicles):
                       print('This is an invalid number')
                   else:
                       inventory.vehicles.remove(inventory.vehicles[item - 1])
                       print()
                       print('This vehicle has been removed')
               elif userInput == '3':
                   # list all the vehicles
                   if len(inventory.vehicles) < 1:
                       print('Sorry there are no vehicles currently in inventory')
                       continue
                   inventory.viewInventory()
               elif userInput == '4':
                   if len(inventory.vehicles) < 1:
                       print('Sorry there are no vehicles currently in inventory')
                       continue
                   inventory.viewInventory()
                   name = input("Enter the customer name: ")
                   number = input("Enter the customer phone number: ")
                   item = int(input('Please enter the vehicle id do you want? : '))
                   if item - 1 > len(inventory.vehicles):
                       print('This is an invalid number')
                   else:
                       inventory.vehicles.remove(inventory.vehicles[item - 1])
                       print()
                       print('This vehicle has been assign hiered ')
               elif userInput == '5':
                   if len(inventory.vehicles) < 1:
                       print('Sorry there are no vehicles hired')
                       continue
                   inventory.viewInventory()
                   item = int(input('Please enter the vehicle id completed hire? : '))
                   if item - 1 > len(inventory.vehicles):
                       print('This is an invalid number')
                   else:
                       inventory.vehicles.append(inventory.vehicles[item - 1])
                       print()
                       print('This vehicle has been remove assign hire ')
               elif userInput == '6':
                    # exit the loop
                       print('Goodbye')
                       break
               else:
                    # invalid user input
                       print('This is an invalid input. Please try again.')

    elif userInput == '2':
        #Van
        class Van:
            def __init__(self):
                self._Id = '0'
                self._MaximumNumberOfPassengers = '0'
                self._AcOrNonAc = ''

            def addVan(self):
                try:
                    self._Id = input("Enter ID: ")
                    self._MaximumNumberOfPassengers = input('Enter maximum number of passenger: ')
                    self._AcOrNonAc = input('Enter Ac or Non-Ac: ')
                    return True
                except ValueError:
                    print('Please try entering vehicle information')
                    return False

            def __str__(self):
                return '\t'.join(str(x) for x in [self._Id, self._MaximumNumberOfPassengers, self._AcOrNonAc])


        class Inventory1:
            def __init__(self):
                self.vehicles = []

            def addVan(self):
                vehicle = Van()
                if vehicle.addVan() == True:
                    self.vehicles.append(vehicle)
                    print()
                    print('This vehicle has been added, Thank you')

            def viewInventory(self):
                print('\t'.join(['','Id', 'Maximum number of passengers', 'Ac or Non-Ac']))
                for idx, vehicle in enumerate(self.vehicles):
                    print(idx + 1, end='\t')
                    print(vehicle)
        inventory1 = Inventory1()

        while True:
            print('')
            print('---How We Can Help You?--- ')
            print('')
            print('#1 Add Vehicle to system')
            print('#2 Delete Vehicle from system')
            print('#3 View Current system')
            print('#4 Assign Hire')
            print('#5 complete hire')
            print('#6 Quit')
            userInput = input('Please choose from one of the above options: ')
            if userInput == "1":
                # add a vehicle
                inventory1.addVan()
            elif userInput == '2':
                # delete a vehicle
                if len(inventory1.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory1.viewInventory()
                item = int(input('Please enter the number associated with the vehicle to be removed: '))
                if item - 1 > len(inventory1.vehicles):
                    print('This is an invalid number')
                else:
                    inventory1.vehicles.remove(inventory1.vehicles[item - 1])
                    print()
                    print('This vehicle has been removed')
            elif userInput == '3':
                # list all the vehicles
                if len(inventory1.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory1.viewInventory()
            elif userInput == '4':
                if len(inventory1.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory1.viewInventory()
                name = input("Enter the customer name: ")
                number = input("Enter the customer phone number: ")
                item = int(input('Please enter the vehicle id do you want? : '))
                if item - 1 > len(inventory1.vehicles):
                    print('This is an invalid number')
                else:
                    inventory1.vehicles.remove(inventory1.vehicles[item - 1])
                    print()
                    print('This vehicle has been assign hiered ')
            elif userInput == '5':
                if len(inventory1.vehicles) < 1:
                    print('Sorry there are no vehicles hired')
                    continue
                inventory1.viewInventory()
                item = int(input('Please enter the vehicle id completed hire? : '))
                if item - 1 > len(inventory1.vehicles):
                    print('This is an invalid number')
                else:
                    inventory1.vehicles.append(inventory1.vehicles[item - 1])
                    print()
                    print('This vehicle has been remove assign hire ')
            elif userInput == '6':
                # exit the loop
                print('Goodbye')
                break
            else:
                # invalid user input
                print('This is an invalid input. Please try again.')
    elif userInput == '3':
        #Wheelers
        class Wheelers:
            def __init__(self):
                self._Id = '0'
                self._MaximumNumberOfPassengers = '0'

            def addWheelers(self):
                try:
                    self._Id = input("Enter ID: ")
                    self._MaximumNumberOfPassengers = input('Enter maximum number of passenger: ')
                    return True
                except ValueError:
                    print('Please try entering vehicle information')
                    return False

            def __str__(self):
                return '\t'.join(str(x) for x in [self._Id, self._MaximumNumberOfPassengers])

        class Inventory2:
            def __init__(self):
                self.vehicles = []

            def addWeelers(self):
                vehicle = Wheelers()
                if vehicle.addWheelers() == True:
                    self.vehicles.append(vehicle)
                    print()
                    print('This vehicle has been added, Thank you')

            def viewInventory(self):
                print('\t'.join(['','Id', 'Maximum number of passengers']))
                for idx, vehicle in enumerate(self.vehicles):
                    print(idx + 1, end='\t')
                    print(vehicle)
        inventory2 = Inventory2()

        while True:
            print('')
            print('---How We Can Help You?--- ')
            print('')
            print('#1 Add Vehicle to system')
            print('#2 Delete Vehicle from system')
            print('#3 View Current system')
            print('#4 Assign Hire')
            print('#5 complete hire')
            print('#6 Quit')
            userInput = input('Please choose from one of the above options: ')
            if userInput == "1":
                # add a vehicle
                inventory2.addWeelers()
            elif userInput == '2':
                # delete a vehicle
                if len(inventory2.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory2.viewInventory()
                item = int(input('Please enter the number associated with the vehicle to be removed: '))
                if item - 1 > len(inventory2.vehicles):
                    print('This is an invalid number')
                else:
                    inventory2.vehicles.remove(inventory2.vehicles[item - 1])
                    print()
                    print('This vehicle has been removed')
            elif userInput == '3':
                # list all the vehicles
                if len(inventory2.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory2.viewInventory()
            elif userInput == '4':
                if len(inventory2.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory2.viewInventory()
                name = input("Enter the customer name: ")
                number = input("Enter the customer phone number: ")
                item = int(input('Please enter the vehicle id do you want? : '))
                if item - 1 > len(inventory2.vehicles):
                    print('This is an invalid number')
                else:
                    inventory2.vehicles.remove(inventory2.vehicles[item - 1])
                    print()
                    print('This vehicle has been assign hiered ')
            elif userInput == '5':
                if len(inventory2.vehicles) < 1:
                    print('Sorry there are no vehicles hired')
                    continue
                inventory2.viewInventory()
                item = int(input('Please enter the vehicle id completed hire? : '))
                if item - 1 > len(inventory2.vehicles):
                    print('This is an invalid number')
                else:
                    inventory2.vehicles.append(inventory.vehicles[item - 1])
                    print()
                    print('This vehicle has been remove assign hire ')
            elif userInput == '6':
                # exit the loop
                print('Goodbye')
                break
            else:
                # invalid user input
                print('This is an invalid input. Please try again.')

    elif userInput == '4':
        #Truck
        class Trucks:
            def __init__(self):
                self._Id = '0'
                self._Size = '0'

            def addTrucks(self):
                try:
                    self._Id = input("Enter ID: ")
                    self._Size = input('Enter size: ')
                    return True
                except ValueError:
                    print('Please try entering vehicle information')
                    return False

            def __str__(self):
                return '\t'.join(str(x) for x in [self._Id, self._Size])

        class Inventory3:
            def __init__(self):
                self.vehicles = []

            def addTrucks(self):
                vehicle = Trucks()
                if vehicle.addTrucks() == True:
                    self.vehicles.append(vehicle)
                    print()
                    print('This vehicle has been added, Thank you')

            def viewInventory(self):
                print('\t'.join(['','Id', 'Size: ']))
                for idx, vehicle in enumerate(self.vehicles):
                    print(idx + 1, end='\t')
                    print(vehicle)
        inventory3 = Inventory3()

        while True:
            print('')
            print('---How We Can Help You?--- ')
            print('')
            print('#1 Add Vehicle to system')
            print('#2 Delete Vehicle from system')
            print('#3 View Current system')
            print('#4 Assign Hire')
            print('#5 complete hire')
            print('#6 Quit')
            userInput = input('Please choose from one of the above options: ')
            if userInput == "1":
                # add a vehicle
                inventory3.addTrucks()
            elif userInput == '2':
                # delete a vehicle
                if len(inventory3.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory3.viewInventory()
                item = int(input('Please enter the number associated with the vehicle to be removed: '))
                if item - 1 > len(inventory3.vehicles):
                    print('This is an invalid number')
                else:
                    inventory3.vehicles.remove(inventory3.vehicles[item - 1])
                    print()
                    print('This vehicle has been removed')
            elif userInput == '3':
                # list all the vehicles
                if len(inventory3.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory3.viewInventory()
            elif userInput == '4':
                if len(inventory3.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory3.viewInventory()
                name = input("Enter the customer name: ")
                number = input("Enter the customer phone number: ")
                item = int(input('Please enter the vehicle id do you want? : '))
                if item - 1 > len(inventory3.vehicles):
                    print('This is an invalid number')
                else:
                    inventory3.vehicles.remove(inventory3.vehicles[item - 1])
                    print()
                    print('This vehicle has been assign hiered ')
            elif userInput == '5':
                if len(inventory3.vehicles) < 1:
                    print('Sorry there are no vehicles hired')
                    continue
                inventory3.viewInventory()
                item = int(input('Please enter the vehicle id completed hire? : '))
                if item - 1 > len(inventory3.vehicles):
                    print('This is an invalid number')
                else:
                    inventory.vehicles.append(inventory.vehicles[item - 1])
                    print()
                    print('This vehicle has been remove assign hire ')
            elif userInput == '6':
                # exit the loop
                   print('Goodbye')
                   break
            else:
                # invalid user input
                   print('This is an invalid input. Please try again.')

    elif userInput == '5':
        #Lorry
        class Lorry:
            def __init__(self):
                self._Id = '0'
                self._load = '0'

            def addLorry(self):
                try:
                    self._Id = input("Enter ID: ")
                    self._load = input('Enter Max Load and size: ')
                    return True
                except ValueError:
                    print('Please try entering vehicle information')
                    return False

            def __str__(self):
                return '\t'.join(str(x) for x in [self._Id, self._load])

        class Inventory4:
            def __init__(self):
                self.vehicles = []

            def addLorry(self):
                vehicle = Lorry()
                if vehicle.addLorry() == True:
                    self.vehicles.append(vehicle)
                    print()
                    print('This vehicle has been added, Thank you')

            def viewInventory(self):
                print('\t'.join(['','Id', 'Size: ']))
                for idx, vehicle in enumerate(self.vehicles):
                    print(idx + 1, end='\t')
                    print(vehicle)
        inventory4 = Inventory4()

        while True:
            print('')
            print('---How We Can Help You?--- ')
            print('')
            print('#1 Add Vehicle to system')
            print('#2 Delete Vehicle from system')
            print('#3 View Current system')
            print('#4 Assign Hire')
            print('#5 complete hire')
            print('#6 Quit')
            userInput = input('Please choose from one of the above options: ')
            if userInput == "1":
                # add a vehicle
                inventory4.addLorry()
            elif userInput == '2':
                # delete a vehicle
                if len(inventory4.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory4.viewInventory()
                item = int(input('Please enter the number associated with the vehicle to be removed: '))
                if item - 1 > len(inventory4.vehicles):
                    print('This is an invalid number')
                else:
                    inventory4.vehicles.remove(inventory4.vehicles[item - 1])
                    print()
                    print('This vehicle has been removed')
            elif userInput == '3':
                # list all the vehicles
                if len(inventory4.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory4.viewInventory()
            elif userInput == '4':
                if len(inventory4.vehicles) < 1:
                    print('Sorry there are no vehicles currently in inventory')
                    continue
                inventory4.viewInventory()
                name = input("Enter the customer name: ")
                number = input("Enter the customer phone number: ")
                item = int(input('Please enter the vehicle id do you want? : '))
                if item - 1 > len(inventory4.vehicles):
                    print('This is an invalid number')
                else:
                    inventory4.vehicles.remove(inventory4.vehicles[item - 1])
                    print()
                    print('This vehicle has been assign hiered ')
            elif userInput == '5':
                if len(inventory4.vehicles) < 1:
                    print('Sorry there are no vehicles hired')
                    continue
                inventory.viewInventory()
                item = int(input('Please enter the vehicle id completed hire? : '))
                if item - 1 > len(inventory.vehicles):
                    print('This is an invalid number')
                else:
                    inventory.vehicles.append(inventory.vehicles[item - 1])
                    print()
                    print('This vehicle has been remove assign hire ')
            elif userInput == '6':
                # exit the loop
                print('Goodbye')
                break
            else:
                # invalid user input
                print('This is an invalid input. Please try again.')


    elif userInput == '6':
        #exit the loop
        print('Goodbye')
        break
    else:
        #invalid user input
        print('This is an invalid input. Please try again.')