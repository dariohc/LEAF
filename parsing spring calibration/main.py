__author__ = 'Dario Hermida'
import csv

line_counter = 0
reading_measurement = False
new_measurement = False
measurement_rows = 8
current_measurement = []
with open('sources/MES_2016_4_14_10_6.CSV', 'r') as csvfile:
    # reader = csv.DictReader(csvfile, dialect='excel')
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        current_search = row[0].split(';')
        # print(current_search)
        if current_search[0] == '2016':
            new_measurement = True
            reading_measurement = False
            measurement_rows = 8
            line_counter = 0
            print('found 2016')
        if new_measurement and (line_counter == 5):
            reading_measurement = True
            print('also found the new measurement')
        if reading_measurement and (measurement_rows > 0):
            current_measurement.append(row)
            measurement_rows -= 1
            if measurement_rows == 0:
                print(current_measurement)
        line_counter += 1
    print(line_counter)



