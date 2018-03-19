# This program takes a filename/path (starting at this file's location)
# Reads out each line and outputs the total line count
def main():
    while True:
        filename = input("Name/Path of file: ")
        try:
            file_object = open(filename)
            lines = iter(file_object.readlines())
            counter = 0
            while True:
                try:
                    line = next(lines)
                    print(line)
                except StopIteration:
                    break
                counter += 1
            print("This file has " + str(counter) + " lines")
            break
        except IOError:
            pass
            print("Invalid filename/path")

main()