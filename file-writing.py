
import csv
import datetime
dt = datetime.datetime.now()
time = dt.strftime('%H:%M:%S.%f')[:-7]

## write text file
file = open("py-test-file.txt", "w")
file.write("Hello world!\n")
file.write("The time is: " + str(time) + "\n")
for x in range(10):
    file.write(str(x) + "\n")
file.close()

## write csv file
test_rows = [["n1", "n2", "n3"], [1, 2, 3], [10, 20, 30], [100, 200, 300]]
test_rows.append([time, time, time])
writer = csv.writer(open("py-test-sheet.csv", "w"))
for x in test_rows:
    writer.writerow(x)
