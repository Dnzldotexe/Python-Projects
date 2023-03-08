# python source code

import sys

menu = ['Append', 'Clear', 'Copy', 'Count', 'Extend', 
        'Index', 'Insert', 'Pop', 'Remove', 'Reverse', 'Sort']

while True:
    print("\n")
    for x in range(1, 12):
        print(f"[{x}] {menu[x-1]}")

    choice = str(input("Enter your Choice: "))

    if choice == '1' or choice == 'Append':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            add_brand = str(input("Enter Laptop Brand to Add: "))
            brands.append(add_brand)
            print("New List of Laptop Brands:")
            for x in range(1, size+2):
                print(f"[{x}] {brands[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '2' or choice == 'Clear':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            clear_yn = str(input("Clear Now [Y/N] ")).upper()
            if (clear_yn == 'Y'):
                brands.clear()
                print(f"Value: {brands}")
                #sys.exit()
            if (clear_yn == 'N'):
                print("Arrays Application Ended")
                #sys.exit()
            else:
                print("Invalid Input")
                #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '3' or choice == 'Copy':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            duplicate = brands.copy()
            print("Duplicate Copy:")
            for x in range(1, size+1):
                print(f"[{x}] {duplicate[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '4' or choice == 'Count':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            dummylist = []
            dummylist2 = []
            for x in brands:
                if x not in dummylist:
                    dummylist.append(x)
            for x in dummylist:
                if brands.count(x) > 1:
                    dummylist2.append(x)
            print(f"Number of Duplicated Value/s: {len(dummylist2)}")
            for x in range(1, len(dummylist2)+1):
                print(f"[{x}] {dummylist2[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '5' or choice == 'Extend':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            extended = []
            extended_size = int(input("Enter List Size for the Additional Values: "))
            if extended_size > 0:
                for x in range(1, extended_size+1):
                    extend_brand = input(f"Enter Additional Values for the [{x}/{extended_size}] Laptop Brands: ")
                    extended.append(extend_brand)
                brands.extend(extended)
                print("Extended Value/s:")
                for x in range(1, extended_size+size+1):
                    print(f"[{x}] {brands[x-1]}")
                #sys.exit()
            else:
                print("List size must be greater than Zero [0]")
                #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '6' or choice == 'Index':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            choose_brand = str(input("Choose from your inputted Laptop Brand: "))
            index_brand = brands.index(choose_brand)
            print(f"Index: {index_brand}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '7' or choice == 'Insert':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            index = int(input("Enter Element Number: "))
            add_brand = str(input("Enter Laptop Brand to be Inserted: "))
            brands.insert(index, add_brand)
            print("New List of Laptop Brands:")
            for x in range(1, size+2):
                print(f"[{x}] {brands[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '8' or choice == 'Pop':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            remove_element = int(input("Enter Number you want to remove: "))
            brands.pop(remove_element)
            print("New List of Laptop Brands:")
            for x in range(1, size):
                print(f"[{x}] {brands[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '9' or choice == 'Remove':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            remove_element = str(input("Enter the Laptop Brand you want to remove: "))
            brands.remove(remove_element)
            print("New List of Laptop Brands:")
            for x in range(1, size):
                print(f"[{x}] {brands[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '10' or choice == 'Reverse':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            brands.reverse()
            print("Reverse Order:")
            for x in range(1, size+1):
                print(f"[{x}] {brands[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    elif choice == '11' or choice == 'Sort':
        brands = []
        size = int(input("Enter List Size (int): "))
        if size > 0:
            for x in range(1, size+1):
                user_brand = str(input(f"Enter any [{x}/{size}] Laptop Brands: "))
                brands.append(user_brand)
            brands.sort()
            print("Sorted Value:")
            for x in range(1, size+1):
                print(f"[{x}] {brands[x-1]}")
            #sys.exit()
        else:
            print("List size must be greater than Zero [0]")
            #sys.exit()

    else:
        print("Invalid Input")
        #sys.exit()

    continue_yn = str(input("Continue [Y/N]?: ")).upper()
    if (continue_yn == 'Y'):
        continue
    if (continue_yn == 'N'):
        print("Arrays Application Ended")
        sys.exit()
    else:
        print("Invalid Input")
        sys.exit()