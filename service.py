import json
import fastapi
import uvicorn
import pandas as pd
app = fastapi.FastAPI()

def sheetFinder(PRN):
    sheetDict = {'Sheet1.csv':[1951721245049, 1951721245052],
                'Sheet2.csv':[1951721245053, 1951721245055],
                'Sheet3.csv':[1951721245056, 1951721245063],
                'Sheet4.csv':[1951721245064, 1951721245069]}
    output = ''
    for key in sheetDict:
        if PRN >= sheetDict[key][0] and PRN <= sheetDict[key][1]:
            output = key
            break
    return output



@app.get('/getStudentAttendance/{PRN}')
def endpoint2(PRN:int):
    dataframe = pd.read_csv(sheetFinder(PRN))
    tofind = PRN
    reqd_index = 0
    subjects = list(dataframe.columns[4:])
    output = {}
    for i in range(dataframe.shape[1]):
        print(i)
        if tofind == dataframe['prn'][i]:
            found = True
            reqd_index = i
            break
    if found != False:
        for subs in subjects:
            output[subs] = int(dataframe[subs][reqd_index])
    # json_object = json.dumps(output, indent = len(output)) 
    return output

@app.get('/getStudentData/{PRN}')
def endpoint3(PRN:int):
    dataframe = pd.read_csv(sheetFinder(PRN))
    tofind = PRN
    reqd_index = 0
    subjects = list(dataframe.columns[4:])
    found = False
    for i in range(dataframe.shape[1]):
        if tofind == dataframe['prn'][i]:
            found = True
            reqd_index = i
            break
    if found != False:
        output = {
                    "packetSize":str(len(subjects)),
                    "studentName":dataframe['name'][reqd_index],
                    "studentPRN":str(dataframe['prn'][reqd_index]),
                    "studentRollNo":str(dataframe['rollno'][reqd_index]),
                }
        print(output)
        for subs in subjects:
            print("in subs loop")
            output[subs] = int(dataframe[subs][reqd_index])
            print(output)
            
        return output
    else:
        return {"packetSize":"1","message":"Error invalid PRN"}
        #if the json only has error message the packetSize should be 1
        #otherwise the packetSize will show the number of subjects the student is enrolled in.
#unfinished module
#why did i think pandas was a good idea
#csv this csv that


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)