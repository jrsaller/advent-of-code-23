# python day1.py 1 for PART 1,
# python day1.py 2 for PART 2
import os
import sys

def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()

def getIndeces(line):
    d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    start = {"nameindex": len(line), "name": "", "intindex": len(line), "int": -1}
    end = {"nameindex": -1, "name": "", "intindex": -1, "int": -1}
    for i in range(10):
        name = d[i]
        if name in line:
            lowindex = line.find(name)
            highindex = line.rfind(name)
            if lowindex < start["nameindex"]:
                start["nameindex"] = lowindex
                start["name"] = i
            if highindex > end["nameindex"]:
                end["nameindex"] = highindex
                end["name"] = i
        if str(i) in line:
            lowindex = line.find(str(i))
            highindex = line.rfind(str(i))
            if lowindex < start["intindex"]:
                start["intindex"] = lowindex
                start["int"] = i
            if highindex > end["intindex"]:
                end["intindex"] = highindex
                end["int"] = i
    return start, end

def calculate_fuel(line, checkNames):
    temp_fuel = 0
    if checkNames:
        start, end = getIndeces(line)

        if start["nameindex"] < start["intindex"]:
            temp_fuel += start["name"] * 10
        else:
            temp_fuel += start["int"] * 10

        if end["nameindex"] > end["intindex"]:
            temp_fuel += end["name"]
        else:
            temp_fuel += end["int"]
    else:
        temp_fuel = 0
        for char in line:
            if char.isdigit():
                temp_fuel += int(char) * 10
                break
        for char in line[::-1]:
            if char.isdigit():
                temp_fuel += int(char)
                break
    return temp_fuel

def init(checkNames):
    if checkNames:
        print("PART 2")
    else:
        print("PART 1")
    filename = os.path.join(sys.path[0], "source.txt")
    lines = read_file(filename)
    total_fuel = 0
    for line in lines:
        total_fuel += calculate_fuel(line, checkNames)
    print(total_fuel)


if __name__ == "__main__":
    init(sys.argv[1]=="2")
