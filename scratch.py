# import pandas as pd
# dataframe = pd.read_csv("firstCSVtry.csv")

# # print(dataframe['prn'])
# print(dataframe)
# tofind = int(1951721245051)
# reqd_index = 0
# for i in range(dataframe.shape[1]):
#     print(i)
#     if tofind == dataframe['prn'][i]:
#         print('yes', i)
#         reqd_index = i
#         break
# subjects = list(dataframe.columns[4:])
# print('subjects : ',subjects)
# studentName = dataframe['name'][reqd_index]
# print(str(studentName))

# def sheetFinder(PRN):
#     sheetDict = {'Sheet1':[1951721245049, 1951721245052],
#                 'Sheet2':[1951721245053, 1951721245055],
#                 'Sheet3':[1951721245056, 1951721245063],
#                 'Sheet4':[1951721245064, 1951721245069]}
#     output = ''
#     for key in sheetDict:
#         if PRN >= sheetDict[key][0] and PRN <= sheetDict[key][1]:
#             output = key
#             break
#     return output

# print(sheetFinder(1951721245069))


# 0 roll no
# 1 prn
# 2 student name
# 3 lg
# 4 subject 1
# 30 total attended
# 31 total conducted
# 32 total percentage

import json
data = json.load(open("TYA Test Sheet 1.json", "r"))


# ---------------------------------------prn based index finder
prn = "1951721245100"
index = 0
for i in range(len(data["0"])):
    if data["1"][str(i)] == prn:
        print("found at", i)
        index = i
        break

# ---------------------------------------------getting data for the index
# for i in range(len(data["0"])):
#     try:
#         print(data[str(i)][str(index)])
#     except:
#         pass

# ----------------------------------------------getting subjects from data
subWiseData = {}
for i in range(4, len(data["0"])):
    try:
        if data[str(i)]['1'] != "":
            subWiseData[data[str(i)]['1']] = {}
    except:
        pass
var = ""
for i in range(4, len(data["0"])):
    try:
        if data[str(i)]['1'] == "":
            subWiseData[var][data[str(i)]['3']] = data[str(i)][str(index)]
        else:
            var = data[str(i)]['1']    
            subWiseData[var][data[str(i)]['3']] = data[str(i)][str(index)]
    except:
        pass
print(subWiseData)