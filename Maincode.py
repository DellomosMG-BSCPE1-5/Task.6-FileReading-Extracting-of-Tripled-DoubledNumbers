#Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
#The first output file will be named double.txt containing the square of all even integers found
#The second file will be named triple.txt containing the cube of all odd numbers found in the integer.txt

#define a function
def read_append_file():
    #open files named: numbers.txt file (read), even.txt file (append), odd.txt file (append)   
    with open("integers.txt") as source_file, open("double.txt", "a") as squared_nums, open("triple.txt", "a") as cubed_nums:    
        #read the numbers.txt file line by line
        for line in source_file:
            source_file_nums = int(line)
        #check each lines of numbers.txt
            #IF the line has even number,
            if source_file_nums % 2 == 0:
                #THEN extract this number and square it
                doubled_even = source_file_nums**2
                #THEN the squared even number will append/write to double.txt file
                squared_nums.write(str(doubled_even) + "\n")
            #ELSE, if the line has odd number
            else:
                #THEN extract this number and get its cube
                odd_tripled = source_file_nums**3
                #THEN the cubed odd number will append/write to triple.txt file
                cubed_nums.write(str(odd_tripled) + "\n")

read_append_file()