import glob, xlsxwriter

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

fileslist = []
for file in glob.glob("C:/Users/sahithpixels/Documents/SDN/*"):
    fileslist.append(file)
    a = file.strip('\n')
#    print(a)
row = 0
column = 0

filedata = []
for line in fileslist:
    row = 0
    with open(line, 'r') as inputfile:
        f = inputfile.read().rstrip('\n\n')
        filedata.append(f)
        x = f.split('\n\n')
        for line2 in x:
            worksheet.write_string(row, column,line2)
            row += 1
    column += 1
print(filedata)
workbook.close()
