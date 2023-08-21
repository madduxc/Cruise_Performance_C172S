# Author:       Charles D. Maddux
# Revision:     0.0.1
# Date Revised: 20 Aug 2023
# Description:  given file names, retrieve performance data from libraries and populate a given data structure
#               return results

import csv


def readCSV(file_name, data_name):
    with open(file_name) as data_file:
        data = csv.reader(data_file, delimiter=',')
        line_count = 0
        for row in data:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if str(row[0]) not in data_name:
                    data_name[str(row[0])] = {'alt': int(row[0])}
                    data_name[str(row[0])]['RPM'] = [{'rpm': int(row[1]), 'pctPwr': float(row[2]), 'TAS': float(row[3]), 'gph': float(row[4])}]
                else:
                    data_name[str(row[0])]['RPM'] += [{'rpm': int(row[1]), 'pctPwr': float(row[2]), 'TAS': float(row[3]), 'gph': float(row[4])}]

                line_count += 1
        print(f'Processed {line_count} lines.')
    return data_name


def main():
    belowSTP = dict()
    belowSTP = readCSV("C172S_STP_low.csv", belowSTP)
    print("chickens")
    for pressure_alt in belowSTP:
        # print(belowSTP[pressure_alt]['alt'])
        for rpm in belowSTP[pressure_alt]:
            print (belowSTP[pressure_alt][rpm])

    return


if __name__ == "__main__":
    main()
