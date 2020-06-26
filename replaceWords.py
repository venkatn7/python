## below sccript will work help you to replace words in a text file by saving the result into a brand new file in a location.

# Enter input and output files location
inputfile_location = ''
outputfile_location = ''

# Open input file and read line by line
with open('test.txt', 'r') as inputfile:
    x = inputfile.read().strip()

    # For each line find word and replace
    for line in x:
        r1 = x.replace('NAME', 'name').replace('city', 'CITY')
        
        # Save the executed data into output file
        with open('test3.txt', 'w') as outpufile1:
            line1 = outpufile1.write(str(r1))
