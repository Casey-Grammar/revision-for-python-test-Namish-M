# Task 8 Call signs
# A portmanteau is a word made by combining parts of two other
# words. This could be used to create call signs for an online
# group.

#For example, david and jones would make daones.

#Let's make some call signs!

#Write a program that asks a user for their first name and last
#name and then takes the first two letters of the first name and
#the last four letters of the last name and combines them to make
#a new call sign. (N.B. we won't test your program with any input
#that's too short!)

def main():
    #Write your code here
    first_and_last = input("First and Last Name? ")
    first_name = first_and_last.split()[0]
    last_name = first_and_last.split()[1]
    call_sign = first_name[:2] + last_name[-4:]
    print(f"The new call sign is: {call_sign}")

    # End of your code here





if __name__ == '__main__':
    main()