# Programming Principles Assignment 3
# By: Christopher Aytona
def port_number(source_list):
    """Returns the L4 Encapsulated Protocol, byte 34 & byte 35"""
    port_num = int(source_list[34]+source_list[35], 16)
    if port_num == 20 or port_num == 21:
        return "File Transfer Protocol FTP"
    elif port_num == 22:
        return "Secure Shell SSH"
    elif port_num == 23:
        return "TELNET"
    elif port_num == 25:
        return "Email SMTP"
    elif port_num == 53:
        return "Domain Name System DNS"
    elif port_num == 80:
        return "Hypertext Transfer Protocol HTTP"
    elif port_num == 143:
        return "Internet Message Access Protocol IMAP"
    elif port_num == 161:
        return "Simple Network Management Protocol SNMP"
    elif port_num == 179:
        return "Routing Border Gateway Protocol BGP"
    elif port_num == 520:
        return "Routing Information Protocol RIP"
    elif port_num == 443:
        return "Secure HTTP (HTTPS)"
    elif port_num == 903:
        return "VMWare Remote Console"
    else:
        return "Invalid port number"

def protocol_number(source_list):
    """Returns the Encapsulated Protocol, byte 23"""
    protocol_num = int(source_list[23], 16)
    if protocol_num == 1:
        return "Internet Control Message ICMP"
    elif protocol_num == 2:
        return "Internet Group Management IGMP"
    elif protocol_num == 6:
        return "Transmission Control Protocol TCP"
    elif protocol_num == 17:
        return "Transport User Datagram UDP"
    elif protocol_num == 88:
        return "Routing Protocol EIGRP"
    elif protocol_num == 89:
        return "Routing Protocol OSPF"
    else:
        return "Invalid protocol number"

def type_number(source_list):
    """Returns the Ethernet type, byte 12 & byte 13"""
    output = "IP Protocol "
    if source_list[12] == "08" and source_list[13] == "00":
        return output + "(IPv4)"
    elif source_list[12] == "86" and source_list[13] == "DD":
        return output + "(IPv6)"
    elif source_list[12] == "08" and source_list[13] == "06":
        return output + "(ARP)"
    else:
        return output

def source_ip(source_list):
    """Returns the source IP address, byte 26 - byte 29"""
    output = ""
    for i in range(26,30):
        output += str(int(source_list[i], 16)) + "."
    return output[:-1]

def destination_ip(source_list):
    """Returns the destination IP address, byte 30 - byte 33"""
    output = ""
    for i in range(30, 34):
        output += str(int(source_list[i], 16)) + "."
    return output[:-1]

def destination_mac(source_list):
    """Returns the destination MAC address, byte 0 - byte 5"""
    output = ""
    for i in range(6):
        output += source_list[i] + " "
    return output[:-1]

def source_mac(source_list):
    """Returns the source MAC address, byte 6 - byte 11"""
    output = ""
    for i in range(6, 12):
        output += source_list[i] + " "
    return output[:-1]

def main():
    tries = True
    while tries:
        while True:
            try:
                file_path = open(input("Enter file path: "))
                break
            except FileNotFoundError:
                pass
                print("File does not exist")
        src = []
        for lines in file_path:
            try:
                src.append(lines.split())
            except UnicodeDecodeError:
                pass
                src.append(lines.encode(encoding='ascii').split())
        new_src = []
        for i in range(len(src)):
            new_src += src[i]
        divider = "------------------------------------------\n"
        output = divider
        output += port_number(new_src) + "\n"
        output += divider
        output += protocol_number(new_src) + "\n"
        output += "Source Port: " + str(int(new_src[34]+new_src[35], 16)) + "\n"
        output += "Destination Port: " + str(int(new_src[36]+new_src[37], 16)) + "\n"
        output += divider
        output += type_number(new_src) + "\n"
        output += "Source IP Address: " + source_ip(new_src) + "\n"
        output += "Destination IP Address: " + destination_ip(new_src) + "\n"
        output += divider
        output += "Ethernet Protocol\n"
        output += "Destination MAC address: " + destination_mac(new_src) + "\n"
        output += "Source MAC address: " + source_mac(new_src) + "\n"
        output += divider
        print(output)
        tries = True if input("Try again?(Y/N)").casefold() == "y" else False

main()