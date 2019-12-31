import pandas as pd
import os
from os.path import basename

start_dir = os.getcwd()

print("Put files in " + start_dir)

sheetNumber = input('Enter the column you would like to merge each file.  Ex. enter "1" if you want to copy sheet 1.  ')

sheetNumber = int(sheetNumber)-1

columnNumber = input('Enter the column number you would like to compare from each sheet.  Ex. enter "1" if you want to compare the first column of each file.  ')

columnNumber = int(columnNumber)-1

#finds all excel files in directory
def excelfiles():
    file_list = []
    for root, dirs, files in os.walk(start_dir):
        for filename in files:
                if filename.endswith(".xls") or filename.endswith(".xlsx") or filename.endswith(".xlsm"):
                    #file_list.append(os.path.join(root, filename))
                    file_list.append(filename)
    return file_list

excel_names = excelfiles()

excels = [pd.ExcelFile(name) for name in excel_names]

# turn them into dataframes
frames = [x.parse(x.sheet_names[sheetNumber], header=None,index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first

all_data_st = []

for frame in frames:
    status = frame.iloc[:,columnNumber]
    all_data_st.append(status)

print(all_data_st)

result = pd.concat(all_data_st, axis=1)
result.to_excel("Merged.xlsx", header=False, index=False)

# write it out
#all_data_st.to_excel("Merged.xlsx", header=False, index=False)

# df = []
# for f in excels:
#     data = pd.read_excel(f, 'Sheet1').iloc[:-2]
#     data.index = [os.path.basename(f)] * len(data)
#     df.append(data)
#
# df = pd.concat(df)
#
# df.to_excel("Merged.xlsx", header=False, index=False)