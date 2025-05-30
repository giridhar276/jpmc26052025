with open("empinfo.csv","r") as fobj:   # read
    with open("29_May_2025.csv","w") as fw:   # write
        for line in fobj:
            line = line.strip()
            line  = line.replace(" United-States","USA")
            fw.write(line + "\n")






import csv
with open("empinfo.csv","r") as fobj:   # read
    with open("29_May_2025.csv","w") as fw:   # write
        reader = csv.reader(fobj)
        for line in reader:
            if " United States" in line:
                line[-2] = "USA"
                print(line)