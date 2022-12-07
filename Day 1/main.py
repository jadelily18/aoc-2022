def main():
    file_content = open("input.txt", "r").read()

    elf_inventories = file_content.split("\n\n")

    calorie_totals = get_totals(elf_inventories)
    calorie_totals.sort(reverse=True)
    print(get_top_three_total(calorie_totals))


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


def get_top_three_total(totals):
    total = 0
    for index, num in enumerate(totals):
        if index == 3:
            return total
        total += num


if __name__ == "__main__":
    main()
