import connection as conn
import cpu_utilizer
#import packet_sniffer
import reachability_check

def start():
    run_loop = True
    while run_loop:
        choice = input('''Type 1 or 2 to run a function:-

        1. Test Reachability . 
        _____________________________________________________

        2. Function B .
        _____________________________________________________

        3. Exit .
        _____________________________________________________

         Your Choice: ''')




        if choice == "1":
            max_device_index = len(conn.device_list_dic)-1
            for ip in range(max_device_index):
                ipaddress = conn.device_list_dic[ip]["ip_address"]
                if reachability_check.check_reachability(ipaddress) == "Up":
                    print("The host: " + ipaddress +" is up.")
                else:
                    print("Can not reach the host: " + ipaddress)
        else:
            print("Please type a valid option")


start()