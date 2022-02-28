import os

os.system('clear')



print("------------------------------------------")
print("1) airscript")
print("2) cracker   | SSH")
print("3) AMFinder")
print("4) nmapper")
print("------------------------------------------")

tool = input("Enter the tool u want to use(ctrl + C to exit): ")



def Function_airscript():
    os.system('airmon-ng check kill')
    os.system('clear')

    print("Automated Aircrack-ng tool By Jeffrey")
    print("-------------------------------------------")

    interface = input("Type interface: ")
    print("-------------------------------------------")
    print("Interface set to: " + interface)
    print("-------------------------------------------")
    input("Press Enter to continue")

    os.system('clear')

    input("Press Enter to start monitor mode")
    print("-------------------------------------------")

    os.system('airmon-ng start ' + interface)

    print("-------------------------------------------")
    input("Press enter to continue")


    os.system('airodump-ng ' + interface + 'mon')
    input("Press enter to continue")



    os.system('clear')


    os.system('airodump-ng --bssid ' + bssid + ' -c ' + channel + ' --write WPAcrack mon0')
    print("-------------------------------------------")
    input("Press enter to continue")

    deauth = input("Enter the number of de-authenticate frames you want to send (example: 100): ")

    os.system('aireplay-ng --deauth ' + deauth + ' -a ' + bssid + ' mon0')

    os.system('JeffTools')



def Function_cracker_ssh():
    import os


    def ssh(wrdList, Host):
          os.system('hydra -L ' + wrdList + ' -P ' + wrdList + ' ' + Host + ' ssh')




    path = input("Enter the path of the Wordlist: ")
    print("------------------------------------------")
    print("Path set to: " + path)
    print("------------------------------------------")
    input("Press enter to continue")

    os.system('clear')

    ip = input("Enter Target ip: ")
    print("------------------------------------------")
    print("Set ip to: " + ip)
    print("------------------------------------------")
    input("Press enter to start attack")

    os.system('clear')


    ssh(path, ip)

    os.system('JeffTools')



def Function_AMFinder():
    import os


    os.system('clear')


    print("----------------------------------------------------------------")
    print("|  Welcome to AdminFinder an automated nikto tool by Jeffrey   |")
    print("----------------------------------------------------------------")

    url = input("Enter Host/url: ")

    os.system('clear')


    print("----------------------------------------------------------------")
    print("|  Welcome to AdminFinder an automated nikto tool by Jeffrey   |")
    print("----------------------------------------------------------------")
    print("----------------------------------------------------------------")
    print("|  Set host to: " + url)
    print("----------------------------------------------------------------")

    input("Press enter to start scanning: " + url)


    os.system('clear')

    os.system('nikto -host ' + url)
    os.system('JeffTools')


def Function_nmapper():
    import os

    os.system('clear')


    ip = input("Enter Target ip(Ctrl + c to exit): ")
    os.system('clear')
    print("-----------------------------")
    print("Target Ip set to: " + ip)
    print("-----------------------------")

    os.system('clear')



    def Function_IP_protocol(host):
        os.system('nmap -sO ' + host)
        input("Press enter to go back")
        os.system('nmapper')


    def Function_Service_Version(host):
        os.system('nmap -sV ' + host)
        input("Press enter to go back")
        os.system('nmapper')

    def Function_All_Hosts(host):
        os.system('nmap -sV ' + host + ' -Pn')
        os.system("Press enter to go back")
        os.system('nmapper')


    def Function_Exit():
    	os.system('exit')




    print("Ip: " + ip)
    print("--------------------------------")
    print("Choose option")
    print("--------------------------------")
    print("1) Ip Protocol")
    print("2) Service/Version")
    print("3) All Hosts (slow)")
    print("4) Exit")
    print("--------------------------------")

    oP = input("Choose option: ")


    os.system('clear')



    if oP == "1":
        Function_IP_protocol(ip)

    elif oP == "2":
        Function_Service_Version(ip)

    elif oP == "3":
        Function_All_Hosts(ip)

    elif oP == "4":
        Function_Exit()

    else:
        print("This Number is invalid.")


    os.system('JeffTools')



if tool == "1":
    Function_airscript()

elif tool =="2":
    Function_cracker_ssh()

elif tool == "3":
    Function_AMFinder()

elif tool == "4":
    Function_nmapper()

else:
    print("Invalid number pls try again")
    os.system('JeffTools')
    
