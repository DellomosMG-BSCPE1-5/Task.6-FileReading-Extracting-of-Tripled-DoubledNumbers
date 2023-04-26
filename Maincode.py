#Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
#The first output file will be named double.txt containing the square of all even integers found
#The second file will be named triple.txt containing the cube of all odd numbers found in the integer.txt

#define a function
def read_append_file():
    #open files named: numbers.txt file (read), even.txt file (append), odd.txt file (append)   
        #read the numbers.txt file line by line
        #check each lines of numbers.txt
            #IF the line has even number,
                #THEN extract this number and square it
                #THEN the squared even number will append/write to double.txt file
            #ELSE, if the line has odd number
                #THEN extract this number and get its cube
                #THEN the cubed odd number will append/write to triple.txt file

read_append_file()