### import libraries getpass, telnetlib for telnet session ###
import getpass
import telnetlib
import os

location = 'C:/Users/Windows1/Documents/SDN'

user = input("Enter your username: ") # Enter User name
password = getpass.getpass()

f = open("Nodes") # 'f' is used to call file 'Nodes' which as list IP's
for line in f: # reads each line in 'Nodes' which is an IP address
    print("Configuring Node: " + line) # this appears on console when each IP is accessed
    HOST = line.strip()  # HOST is each line in Nodes
    tn = telnetlib.Telnet(HOST) # performs telnet to HOST=IP address

    tn.read_until(b"Username: ") # Wait's until it gets username and password from input console
    tn.write(user.encode('ascii') + b"\n")  # used to encode binary to ascii format which is understood by remote device
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"sh run\n") # Executes the command on remote device
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    outputfile = os.path.join(location, str(HOST) + ".txt")
    with open(outputfile, 'w') as output: # creates a new text with name as IP address of device and writes
        output.write(tn.read_all().decode('ascii')) # the given output by device and saves in pycharmprojects folder
        print(tn.read_all().decode('ascii'))  # Prints the given data by device on terminal
f.close()