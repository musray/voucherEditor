# -*- coding: utf-8 -*-
import os,csv


# modify the source file
# 1. delete the \n
# 2. append a double quote at the end of each line
# 3. save modified lines in a new file(middleware)
def preprcessor(source):
    input_file = open(source, 'r')
    middleware = open('middleware.txt.tmp', 'w')

    # process
    m = 0
    for row in input_file.readlines():
        if m >= 1:
            new_row = row.rstrip() + '"\n' 
            middleware.write(new_row)
        else:
            middleware.write(row)
        m += 1

    input_file.close()
    middleware.close()


# open the 
def editor():
    user_input = raw_input('Input your new voucher number: ')

    # open the middleware and read it as csv
    input_file = open('middleware.txt.tmp', 'r')
    reader = csv.reader(input_file, delimiter=',' , quotechar='"', quoting=csv.QUOTE_ALL)

    # create output file
    output_file = open('pz-after.txt', 'wb')
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    # process
    i = 0;
    for row in reader:
        if i >= 1:
            row[20] = user_input
            writer.writerow(row)
        else:
            writer.writerow(row)
        i += 1

    input_file.close()
    output_file.close()

try:
    source = "pz.txt"
    preprcessor(source)
    editor()
    raw_input('Done!')
    os.remove('middleware.txt.tmp')
except:
    raw_input('Error')

