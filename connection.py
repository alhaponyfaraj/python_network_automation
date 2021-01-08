import ast
import re
from netmiko import ConnectHandler, file_transfer
from pprint import pprint


ip_validate_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

device_list = open("device_list.txt", "r")
login_file = open("login.txt", "r")
commands_file = open("commands.txt", "r")

device_list_reader = device_list.read()
login_file_reader = login_file.read()
commands_file_reader = commands_file.read()
# convert string to list
device_list_dic = ast.literal_eval(device_list_reader)
login_file_dic = ast.literal_eval(login_file_reader)
#commands_file_dic = ast.literal_eval(commands_file_reader)


print(type(device_list_dic))
print(device_list_dic)
print(device_list_dic[0]["ip_address"])

sw1_ipaddress = device_list_dic[0]["ip_address"]
sw1_username = login_file_dic[0]["sw1_username"]
sw1_password = login_file_dic[0]["sw1_password"]
switch_1 = {
    "device_type": "cisco_ios",
    "host": sw1_ipaddress,
    "username": sw1_username,
    "password": sw1_password
}

switch_2 = {
    "device_type": "cisco_ios",
    "host": "172.16.1.2",
    "username": "webmaster",
    "password": "webmaster",
}

mikrotik = {
    "device_type": "mikrotik",
    "host": "172.16.0.1",
    "username": "admin",
    "password": "admin",
}

command = "show arp"
net_connect = ConnectHandler(**switch_1)
output = net_connect.send_command(command)
net_connect.disconnect()
print(f"\n{output}\n")

