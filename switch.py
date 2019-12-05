#!/usr/bin/python

import sys, os, csv

account_dict = {}

if (len(sys.argv) < 2):
    print("Please enter first name before any flags")
    sys.exit()

with open('accounts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            pass
        else:
            account_dict[row[0]] = (row[1],row[2])

if sys.argv[1] in account_dict.keys():
    print("Global settings set using: " + str(account_dict[sys.argv[1]]))
    os.system('git config --global user.email ' + account_dict[sys.argv[1]][0])
    os.system('git config --global user.name ' + account_dict[sys.argv[1]][1])
    if sys.argv[2] == "-m":
        os.system('git commit -m ' + '"' + ' '.join(sys.argv[3:]) + '"')
    else:
        os.system('git commit')
else:
    print("Please enter first name before any flags or message")
    sys.exit()
