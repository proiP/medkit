from time import sleep
import sys

user_name = "bob"
user_password = "123"
login = False


# A function for the patient's corner
def patient_corner():
    
    patient_name = raw_input("Enter Patient's name: ")
    print patient_name.split()
    
    main()


# A function for the doctor's corner    
def doctor_corner():
    pass


# A funciton for the medical messages    
def medical_messages():
    pass


# A function for the about.
# This displays the basic information about the software.    
def about():
    print "\nThis Software is all about the Medical Kit"
    print "Copyright 2016. All Rights Reserved."
    main()


# A function for the contact us. 
# This displays the contact information of the owner.
def contact_us():
    contact = """\n
              Contact Us:
              Name: Some Guy at the desk
              Address: Somewhere out there
              Contact No.: (123)-456-7890
              Email: the.guy.at.desk@medkit.com
              """
    print contact
    main()

# A function for the main program
# Starts the main system 
# User chooses what to do
def main():
    exit = False
    
    print "\nWhat can I do for you?"
    print "\n1. Patient's Corner"
    print "2. Doctor's Corner"
    print "3. Medical Messages"
    print "4. About"
    print "5. Contact Us"
    print "6. Exit"
    
    while True:
        
        main_choose = raw_input("\nChoice: ")
        if main_choose == "1":
            print "\nPatient's Corner"
            patient_corner()
        elif main_choose == "2":
            print "Doctor's Corner"
            doctor_corner
        elif main_choose == "3":
            print "Medical Messages"
            medical_messages()
        elif main_choose == "4":
            print "About"
            about()
        elif main_choose == "5":
            print "Contact Us"
            contact_us()
        elif main_choose == "6":
            print "Goodbye"
            sleep(5)
            sys.exit()
        else:
             print "Incorrect Input. Please try again."


# Iterates when the username and password are incorrect
print "\nWelcome to Medkit."
sleep(3)
while True:
    uName = raw_input("\nEnter username: ")
    uPassword = raw_input("Enter password: ")
    
    if uName == user_name and uPassword == user_password:
        print "\nWelcome %s!" % uName
        sleep(3)
        main()
    else:
        print "Error: Incorrect username and password."
        
        
