def is_duplicate(name, item_names):
    return name in item_names

def is_found(name, item_names):
    return name in item_names

if __name__ == "__main__":

    print("==== INVENTORY MENU ====")

    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Exit\n")

    item_names = []
    item_prices = {}

    while True:
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Invalid Input! Enter an integer.\n")
            continue

        match choice:
            case 1:
                item_name = input("Enter item name: ")
                if is_duplicate(item_name, item_names):
                    print("Item already exists.\n")
                    continue
                else:
                    try:
                        item_price = int(input("Enter price: "))
                        if item_price < 0:
                            print("Invalid Input! Negative numbers are not allowed.")
                            continue
                    except ValueError:
                        print("Invalid Input! Enter a valid price.\n")
                        continue

                    item_names.append(item_name)
                    item_prices[item_name] = item_price

                    print("Item added successfully!\n")
            case 2:
                search_name = input("Enter item name to update: ")

                if is_found(search_name, item_names):
                    try:
                        new_price = int(input("Enter price: "))
                        if new_price < 0:
                            print("Invalid Input! Negative numbers are not allowed.")
                            continue
                    except ValueError:
                        print("Invalid Input! Enter a valid price.\n")
                        continue

                    item_prices[search_name] = new_price
                else:
                    print("Item not found in the inventory.\n")
                    continue

                print("Price updated successfully!\n")

            case 3:
                print("Exiting system...")
                break
            case _:
                print("Invalid Choice!\n")

        
