def calc_volt(data_elements):
    volt = 0

    for bank in data_elements:
        lvolt = 0
        rvolt = 0
        for i in range(int(len(bank)) - 1):
            if int(bank[i]) > lvolt:
                lvolt = int(bank[i])
                rvolt = 0
            elif int(bank[i]) > rvolt:
                rvolt = int(bank[i])
        if int(bank[int(len(bank)) - 1]) > rvolt:
            rvolt = int(bank[int(len(bank)) - 1])

        volt += (lvolt * 10) + rvolt
    print(volt)

# rawdata to string list
with open("puzzleInput", "r") as file:
    data = file.read().replace("\n", " ")
    dataElements = data.split(" ")
    calc_volt(dataElements)

