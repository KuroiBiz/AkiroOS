print("Hello, welcome to AkiroOS!\n") #v0.1 wifi, basic boot, login and 2 apps
user = input("Enter your name: ")
password = input("Enter your password: ")

wifi_status = "OFF"  #initial wifi status

def info_app(): #system-info app function
    print("system-info.app")
    print("AkiroOS Version: 0.1")
    print("Developer: Akiro")
    print("Status: Early Development\n")
    desktop()  #return to desktop after showing info

def show_wifi(wifi_status):
    print("Current WiFi status:")
    if wifi_status == True:
        print("WiFi is ON\n")
    elif wifi_status == False:
        print("WiFi is OFF\n")

def wifi_stats(wifi_status): #print wifi function ON/OFF feature only for v0.1
    print("WiFi Manager")
    if wifi_status.lower() == "on":
        print("Turning WiFi ON...")
        print("WiFi is now ON!\n")
        wifi_status = True
        desktop() 
        return wifi_status 
    elif wifi_status.lower() == "off":
        print("Turning WiFi OFF...")
        print("WiFi is now OFF!\n")
        wifi_status = False
        desktop()
        return wifi_status
    else:
        print("Invalid option. Please try again.")
        wifi_manager()  #try again
        return wifi_status

def wifi_manager(): #wifi manager function
    print("WiFi Manager\n")
    option = input("Do you want to turn WiFi ON or OFF? (on/off): \nOr check status(1): \n")
    if option == "on":
        wifi_status(wifi_status)
    elif option == "1":
        show_wifi()
    else:
        wifi_manager()
    quit_option = input("Do you want to return to the desktop? (yes/no): \n")
    if quit_option.lower() == "yes":
        desktop()
    else:
        print("Staying in WiFi Manager.\n")
        wifi_manager()

def desktop(): #main desktop function
    print("Loading AkiroOS desktop...")
    print("AkiroOS desktop is now ready!\n")
    # wifi manager and system-info app
    print("Available apps:\n1. WiFi Manager\n2. system-info.app")
    app = input("Which do you want to open? (1/2): ")
    if app == "1":
        print("Opening WiFi Manager...")
        print("WiFi Manager is now running!\n")
        wifi_manager()
    elif app == "2":
        print("Opening system-info.app...")
        print("system-info.app is now running!\n")
        info_app()
    else:
        print("Invalid app selection.\n")
        #try again
        desktop()

def main(): #setup and boot function
    print("Setting up AkiroOS...\n \n")
    print("AkiroOS")
    print("setup complete\n")
    boot = input("Do you want to boot AkiroOS? (yes/no): ")
    if boot.lower() == "yes":
        print("Booting AkiroOS...")
        print("AkiroOS is now running!\n")
        desktop()
    else:
        print("AkiroOS boot canceled.\n")
        return

if user == "Akiro" and password == "Akiro123":
    print("Access granted. Welcome, Akiro!")
    main()
else:
    print("Access denied. Incorrect username or password.\n")