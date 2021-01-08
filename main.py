import connection
import cpu_utilizer
import packet_sniffer

def main():
    run_loop = True
    while run_loop:
        choice = input('''Type 1 or 2 to run a function:-

        1. Function A . 
        _____________________________________________________

        2. Function B .
        _____________________________________________________

        3. Exit .
        _____________________________________________________

         Your Choice: ''')
