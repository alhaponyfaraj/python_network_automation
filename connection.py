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


sw1_ipaddress = device_list_dic[0]["ip_address"]
sw1_username = login_file_dic[0]["sw1_username"]
sw1_password = login_file_dic[0]["sw1_password"]

sw2_ipaddress = device_list_dic[1]["ip_address"]
sw2_username = login_file_dic[1]["sw2_username"]
sw2_password = login_file_dic[1]["sw2_password"]

router_ipaddress = device_list_dic[2]["ip_address"]
router_username = login_file_dic[2]["router_username"]
router_password = login_file_dic[2]["router_password"]

switch_1 = {
    "device_type": "cisco_ios",
    "host": sw1_ipaddress,
    "username": sw1_username,
    "password": sw1_password
}

switch_2 = {
    "device_type": "cisco_ios",
    "host": sw2_ipaddress,
    "username": sw2_username,
    "password": sw2_password,
}

mikrotik = {
    "device_type": "mikrotik_routeros",
    "host": router_ipaddress,
    "username": router_username,
    "password": router_password,
}

# Test reachability

def send_commands(device, command):
    # Send commands for switch 1
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(command)
    net_connect.disconnect()
    print(f"\n{output}\n")

