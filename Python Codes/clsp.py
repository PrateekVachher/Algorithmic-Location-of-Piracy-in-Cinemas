while True:
    print " "
    option = input("Enter '1' for Integer to Binary; Enter '2' for Binary to Integer, Enter '0' to end the program: ")
    name = {'1': 'DT Cinemas', '2': 'DT Cinemas', '3': 'DT Cinemas', '4': 'DT Cinemas', '5': 'DT Cinemas',
            '6': 'Fun Cinemas', '7': 'Fun Cinemas', '8': 'Fun Cinemas', '9': 'Fun Cinemas', '10': 'INOX Cinemas',
            '11': 'INOX Cinemas', '12': 'INOX Cinemas', '13': 'PVR Cinemas', '14': 'PVR Cinemas', '15': 'PVR Cinemas',
            '16': 'PVR Cinemas', '17': 'PVR Cinemas', '18': 'PVR Cinemas', '19': 'PVR Cinemas', '20': 'PVR Cinemas'}
    location = {'1': 'Saket', '2': 'GK2', '3': 'Shalimar Bagh', '4': 'Gurgaon', '5': 'Vasant Kunj', '6': 'Shahdara',
                '7': 'Moti Nagar', '8': 'Pitampura', '8': 'Laxmi Nagar', '9': 'Ghaziabad', '10': 'Faridabad',
                '11': 'Gurgaon', '12': 'Greater Noida', '13': 'Gurgaon', '14': 'Faridabad', '15': 'Kaushambi',
                '16': 'Vaishali', '17': 'Naraina', '18': 'Ghaziabad', '19': 'Prashant Vihar', '20': 'Saket'}
    if option == 1:
        ID1 = input("Enter Cinema ID to be converted to Binary: ")
        ID2 = input("Enter Time ID to be converted to Binary: ")
        binary1 = bin(ID1)[2:]
        binary2 = bin(ID2)[2:]
        print "Primary Binary of entered Cinema ID:", binary1
        print "Secondary Binary of entered Time ID:", binary2
    elif option == 2:
        binary = input("Enter Primary Binary to be converted to Cinema ID: ")
        date = input("Enter Secondary Binary to be converted to Time ID: ")
        integer = int(str(binary), 2)
        secondary = str(int(str(date), 2))
        if len(str(secondary)) != 7:
            print "Incorrect Secondary Binary"
        tod1 = secondary[0]
        if tod1 == '1':
            tod2 = "Morning (8am to 12noon)"
        elif tod1 == '2':
            tod2 = "Afternoon (12noon to 4pm)"
        elif tod1 == '3':
            tod2 = "Evening (4pm to 8pm)"
        elif tod1 == '4':
            tod2 = "Night (8pm to 12am)"
        else:
            print "Incorrect Secondary Binary"
        date = secondary[1:3]
        month = secondary[3:5]
        year = 2000 + int(secondary[5:])
        if integer <= len(name):
            print "Cinema ID:", integer
            print "Cinema Name:", name[str(integer)]
            print "Cinema Location:", location[str(integer)]
            print "Time of the Day:", tod2
            print "Date:", [str(date) + "/" + str(month) + "/" + str(year)]
        else:
            print "No Cinema Found as per ID"
    if option == 0:
        break

while True:
    print " "
    option = input("Enter '1' for Integer to Binary; Enter '2' for Binary to Integer, Enter '0' to end the program: ")
    name = {'1': 'DT Cinemas', '2': 'DT Cinemas', '3': 'DT Cinemas', '4': 'DT Cinemas', '5': 'DT Cinemas',
            '6': 'Fun Cinemas', '7': 'Fun Cinemas', '8': 'Fun Cinemas', '9': 'Fun Cinemas', '10': 'INOX Cinemas',
            '11': 'INOX Cinemas', '12': 'INOX Cinemas', '13': 'PVR Cinemas', '14': 'PVR Cinemas', '15': 'PVR Cinemas',
            '16': 'PVR Cinemas', '17': 'PVR Cinemas', '18': 'PVR Cinemas', '19': 'PVR Cinemas', '20': 'PVR Cinemas'}
    location = {'1': 'Saket', '2': 'GK2', '3': 'Shalimar Bagh', '4': 'Gurgaon', '5': 'Vasant Kunj', '6': 'Shahdara',
                '7': 'Moti Nagar', '8': 'Pitampura', '8': 'Laxmi Nagar', '9': 'Ghaziabad', '10': 'Faridabad',
                '11': 'Gurgaon', '12': 'Greater Noida', '13': 'Gurgaon', '14': 'Faridabad', '15': 'Kaushambi',
                '16': 'Vaishali', '17': 'Naraina', '18': 'Ghaziabad', '19': 'Prashant Vihar', '20': 'Saket'}
    if option == 1:
        ID1 = input("Enter Cinema ID to be converted to Binary: ")
        ID2 = input("Enter Time ID to be converted to Binary: ")
        binary1 = bin(ID1)[2:]
        binary2 = bin(ID2)[2:]
        print "Primary Binary of entered Cinema ID:", binary1
        print "Secondary Binary of entered Time ID:", binary2
    elif option == 2:
        binary = input("Enter Primary Binary to be converted to Cinema ID: ")
        date = input("Enter Secondary Binary to be converted to Time ID: ")
        integer = int(str(binary), 2)
        secondary = str(int(str(date), 2))
        if len(str(secondary)) != 7:
            print "Incorrect Secondary Binary"
        tod1 = secondary[0]
        if tod1 == '1':
            tod2 = "Morning (8am to 12noon)"
        elif tod1 == '2':
            tod2 = "Afternoon (12noon to 4pm)"
        elif tod1 == '3':
            tod2 = "Evening (4pm to 8pm)"
        elif tod1 == '4':
            tod2 = "Night (8pm to 12am)"
        else:
            print "Incorrect Secondary Binary"
        date = secondary[1:3]
        month = secondary[3:5]
        year = 2000 + int(secondary[5:])
        if integer <= len(name):
            print "Cinema ID:", integer
            print "Cinema Name:", name[str(integer)]
            print "Cinema Location:", location[str(integer)]
            print "Time of the Day:", tod2
            print "Date:", [str(date) + "/" + str(month) + "/" + str(year)]
        else:
            print "No Cinema Found as per ID"
    if option == 0:
        break

