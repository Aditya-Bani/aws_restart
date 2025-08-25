# composite-data.py
# Creating a car inventory program

import csv
import copy

# Defining the dictionary
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Tampilkan isi awal dictionary
print("Initial dictionary:")
for key, value in myVehicle.items():
    print(f"{key} : {value}")

print("----------------------")

# List kosong untuk menyimpan data mobil
myInventoryList = []

# Copying the CSV file into memory
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            # Header
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Buat salinan dictionary baru untuk setiap mobil
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            # Tambahkan ke list inventory
            myInventoryList.append(currentVehicle)
            lineCount += 1

    print(f'Processed {lineCount} lines.')

print("----------------------")

# Printing the car inventory
print("Car Inventory:\n")
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print(f"{key} : {value}")
    print("-----")
