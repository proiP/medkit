from time import sleep

user_name = "bob"
user_password = "123"
login = False


# A function for the patient's corner
def patient_corner():
    pass


# A function for the doctor's corner    
def doctor_corner():
    pass


# A funciton for the medical messages    
def medical_messages():
    pass


# A function for the about    
def about():
    pass


# A function for the contact us    
def contact_us():
    pass


# A function for the main program
def main():
    exit = False
    
    print "\nWhat can I do for you?"
    print "\n1. Patient's Corner"
    print "2. Doctor's Corner"
    print "3. Medical Messages"
    print "4. About"
    print "5. Contact Us"
    print "Exit"
    
    while True:
        
        if "1":
            print "\nPatient's Corner"
            patient_corner()
        elif "2":
            print "Doctor's Corner"
            doctor_corner
        elif "3":
            print "Medical Messages"
            medical_messages()
        elif "4":
            print "About"
            about()
        elif "5":
            print "Contact Us"
            contact_us()
        elif "6":
            print "Good bye"
            sleep(5)
            exit(0)
        else:
             print "Incorrect Input. Please try again."


# Iterates when the username and password are incorrect
while True:
    uName = raw_input("Enter username: ")
    uPassword = raw_input("Enter password: ")
    
    if uName == user_name and uPassword == user_password:
        print "Welcome %s!" % uName
        sleep(3)
        main()
    else:
        print "Error: Incorrect username and password."
        
        
