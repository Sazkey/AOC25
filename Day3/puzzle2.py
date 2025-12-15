import math

def calc_volt(data_elements):
    n = 12
    voltage = 0

    for bank in data_elements:
        batteries = calc_batteries(bank, n)

        for i in range(n):
            voltage += batteries[i] * int(math.pow(10, i))

    return voltage


def calc_batteries(bank, n: int) -> list[int]:
    batteries = [0] * n
    badge_size = int(len(bank))
    for i in range(badge_size):
        leftovers = badge_size - i
        shift = 0
        if n > leftovers > 0:
            shift = n - leftovers
        j = shift
        voltage_size = n - 1
        while j < voltage_size + 1:
            change_loc = voltage_size - j
            if batteries[change_loc] < int(bank[i]):
                batteries[change_loc] = int(bank[i])
                while change_loc > 0:
                    change_loc -= 1
                    batteries[change_loc] = 0
                break
            j += 1
    return batteries


with open("puzzleInput", "r") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")
    print(calc_volt(dataElements))