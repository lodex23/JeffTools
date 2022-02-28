import os

os.system('clear')



print("------------------------------------------")
print("1) aircrack-ng")
print("2) hydra")
print("3) nikto")
print("4) nmap")
print("------------------------------------------")

tool = input("Enter the tool u want to use(ctrl + C to exit): ")



def Function_Aircrack():
    os.system('python3 ---Path to aircrack-ng file---')


def Function_hydra():
    os.system('python3 ---Path to hydra file---')


def Function_nikto():
    os.system('python3 ---Path to nikto file---')


def Function_nmap():
    os.system('python3 ---Path to nmap file---')





if tool = "1":
    Function_Aircrack()

elif tool = "2":
    Function_hydra()


elif tool = "3":
    Function_nikto()


elif tool = "4":
    Function_nmap()


else:
    print('This number is invalid.')
