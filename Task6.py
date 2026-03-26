# Task 6 Find bear
# Write a program to work out whether a line of input text contains a
# bear or not. Your program needs to find cases where the word
# appears in full, with no breaks.

def main():
    #Write your code here
    line = input("Enter line: ")
    word = "bear"
    if word in line:
        print("There's a bear in there")
    elif word not in line:
        print("No bears here.")    
        
    
    # End of your code here





if __name__ == '__main__':
    main()