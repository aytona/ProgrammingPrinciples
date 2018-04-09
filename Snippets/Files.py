# Files: Section 11
def main():
    org = str(input("Enter the organization name: ")).casefold()
    file_path = open("Snippets/LIST of AS.txt")
    for lines in file_path:
        try:
            # By default, Python 3 encodes using UTF-8
            line_list = lines.split()
        except UnicodeDecodeError:
            pass
            line_list = lines.encode(encoding='ascii').split()
        if org in str(line_list).casefold():
            print(line_list)

main()