import os, platform


def check_reachability(ip_address):
    hostname = ip_address
    response = os.system("ping " + ("-n 1 " if platform.system().lower()=="windows" else "-c 1 ") + hostname)

    # and then check the response...
    if response == 0:
        pingstatus = "Up"
    else:
        pingstatus = "Down"
    return pingstatus



#check_reachability("172.16.0.1")