from netmiko import ConnectHandler
from getpass import getpass

location = 'C:/Users/Windows1/Documents/SDN'
host = input("Enter Hostname: ")
username = input("Enter Username: ")

cisco = {
    'device_type': 'cisco_ios', 
    'host': host,           ## 1.1.1.1
    'username': username, 
    'password': getpass(),
    'secret': 'admin',
}
net_connect = ConnectHandler(**cisco)
net_connect.enable()
output = net_connect.send_command("show ver | i Ver")
print(output)
