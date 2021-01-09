import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from netmiko import ConnectHandler
import re
from connection import device_list_dic, login_file_dic


sw1_ipaddress = device_list_dic[0]["ip_address"]
sw1_username = login_file_dic[0]["sw1_username"]
sw1_password = login_file_dic[0]["sw1_password"]


switch_1 = {
    "device_type": "cisco_ios",
    "host": sw1_ipaddress,
    "username": sw1_username,
    "password": sw1_password
}

def send_commands(device, command):
    # Send commands for mikrotik
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(command)
    net_connect.disconnect()
    cpu_line = str(output.splitlines()[1])



    if cpu_line.startswith("CPU"):

        print(cpu_line)
        digits = re.findall(r"[0-9]+", cpu_line)
        print(digits[0])


        return digits[0]
while True:
    cpu_load = send_commands(switch_1, "show processes cpu sorted")
    print(cpu_load)
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    time_now = time.time()
    x = []
    y = []
    x.append(float(cpu_load))
    y.append(float(time_now))
    ax1.clear()
    ax1.plot(x, y)
    plt.show()

