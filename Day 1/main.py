def main():
    file_content = open("input.txt", "r").read()
    elf_inventories = file_content.split("\n\n")
    print(max(get_totals(elf_inventories)))


def get_totals(inventories):
    totals = []
    for inv in inventories:
        inv_list = inv.split("\n")
        calorie_total = 0
        for i in inv_list:
            if i != '':
                calorie_total += int(i)
        totals.append(calorie_total)
    return totals


if __name__ == "__main__":
    main()
