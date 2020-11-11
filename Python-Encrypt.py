import py_compile
import os
import time
import sys
os.system('clear')
def banner():
    print("\033[34m")
    print('''    
██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗      
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║      
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║      
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║      
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║      
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝      

███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗            
██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝            
█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░            
██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░            
███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░            
╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░            ''')
def banner2():
    print("\033[34m")
    print("_______________________________ ")
    print("|  Coded by H3LL0-H4CK3R       |")
    print("|  Thanks for using my tool    |")
    print("|______________________________|")
message ="\033[31m WELCOME TO PYTHON ENCRYPT "
for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
time.sleep(1)
banner()
time.sleep(1)
banner2()
time.sleep(1)

print("\033[91m")

print("PYTHON ENCRYPT")
time.sleep(1)
a =  input("Enter your file name : ")
py_compile.compile(a)
message = "\033[31m ............DONE ENCRYPTED SUCCESSFULL"
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

message = "\033[31m THANKS FOR USING MY TOOL\n"
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

