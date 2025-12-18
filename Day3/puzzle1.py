def calc_volt(data_elements):
    volt = 0

    for bank in data_elements:
        l_volt = 0
        r_volt = 0
        for i in range(int(len(bank)) - 1):
            if int(bank[i]) > l_volt:
                l_volt = int(bank[i])
                r_volt = 0
            elif int(bank[i]) > r_volt:
                r_volt = int(bank[i])
        if int(bank[int(len(bank)) - 1]) > r_volt:
            r_volt = int(bank[int(len(bank)) - 1])

        volt += (l_volt * 10) + r_volt
    print(volt)

# rawdata to string list
with open("puzzleInput", "r") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")
    calc_volt(dataElements)

