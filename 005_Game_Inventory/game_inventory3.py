def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for key, value in inventory.items():
        print("{} {}" .format(value, key))
        total += value
    print("Total number of items: {}" .format(total))


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def print_inv(inv_list, length):
    for i, j in inv_list:
        print("{0:>{width}d}   {1:>{width}s}".format(
            j, i, width=length))


def print_table(inv, order=""):
    longest_length = len(max(inv, key=len))

    print("Inventory:")
    print("{0:>{width}s}   {1:>{width}s}".format(
        "count", "item name", width=longest_length))

    dashline_lenght = longest_length * 2 + 3
    print_dashline(dashline_lenght)

    inv_list = [(key, value) for key, value in inv.items()]

    if order == "count,asc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1])
    elif order == "count,desc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1], reverse=True)

    print_inv(inv_list, longest_length)
    print_dashline(dashline_lenght)
    print("Total number of items: {}" .format(total_number(inv)))


def print_dashline(lenght):
    for i in range(lenght):
        print("-", end="")
    print("\n")


def total_number(inventory):
    total = 0
    for value in inventory.values():
        total += value
    return total


def import_inventory(target_inventory, source_file="import_inventory.csv"):
    try:
        with open(source_file, "r+") as imp_file:
            for line in imp_file:
                line = line.strip()

                current_data = ""
                datas = []
                for char in line:
                    if not char == ",":
                        current_data += char
                    else:
                        datas.append(current_data)
                        current_data = ""
                datas.append(current_data)

                if datas[1].isalpha():
                    pass
                else:
                    try:
                        target_inventory[datas[0]] += int(datas[1])
                    except KeyError:
                        target_inventory[datas[0]] = int(datas[1])
    except FileNotFoundError:
        print("No such file or directory: {}".format(source_file))


def export_inventory(source_inventory, target_file="export_inventory.csv"):
    """ Export inventory into csv file format

    Arguments:
    target_file -- the name of the exported file (default: export_inventory.csv)
    """
    text_to_write = ""
    for element in source_inventory:
        text_to_write += str(element) + "," + \
            str(source_inventory[element]) + "\n"

    with open(target_file, "w+") as exp_file:
        exp_file.write(text_to_write)


def main():
    inv = {"rope": 1, "torch": 6, "gold_coin": 42, "dagger": 1, "arrow": 12}
    dragon_loot = ["gold_coin", "dagger", "gold_coin", "gold_coin", "ruby"]

    add_to_inventory(inv, dragon_loot)
    print_table(inv)
    print_table(inv, "count,asc")
    print_table(inv, "count,desc")
    import_inventory(inv)
    export_inventory(inv)
    display_inventory(inv)

if __name__ == '__main__':
    main()
