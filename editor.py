# -*- coding: utf-8 -*-
# Functions leading by a underscore is the helper functions.
import os,csv,sys


# list all txt files in current directory
def _finder():
    files = [f for f in os.listdir('.') if f.lower().endswith('.txt')]
    return files

# modify the source file and save as middleware
# 1. delete the trailing \n
# 2. append a double quote at the end of each line
# 3. save modified lines in a new file(called middleware)
def _preprcessor(source):
    input_file = open(source, 'r')
    middleware = open('middleware.txt.tmp', 'w')

    # process
    m = 0
    for row in input_file.readlines():
        # skip the first row
        if m >= 1:
            new_row = row.rstrip() + '"\n' 
            middleware.write(new_row)
        else:
            middleware.write(row)
        m += 1

    input_file.close()
    middleware.close()

# from middleware to new file
# delete(remove) middleware when process is done.
def _editor(source, number):

    _preprcessor(source)

    # open the middleware and read it as csv
    input_file = open('middleware.txt.tmp', 'r')
    reader = csv.reader(input_file, delimiter=',' , quotechar='"', quoting=csv.QUOTE_ALL)

    # create output file
    new_file = 'after_' + source
    output_file = open(new_file, 'wb')
    writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    # process
    i = 0;
    for row in reader:
        if i >= 1:
            row[20] = number
            writer.writerow(row)
        else:
            writer.writerow(row)
        i += 1

    input_file.close()
    output_file.close()
    os.remove('middleware.txt.tmp')

def main():

    txt_files = _finder()

    if len(txt_files) > 0:
        voucher_no = raw_input('Input your voucher number: ')

        for txt_file in txt_files:
            try:
                _editor(txt_file, voucher_no)
                message = txt_file + ': Process complete!'
                print message
            except:
                raw_input('Oops, Error. Press Enter to exit...')

    else: 
        raw_input('TXT file not found! Press Enter to exit...')
        sys.exit()


if __name__ == '__main__': 
    main()
    raw_input('All done!\nPress Enter to exit...')

