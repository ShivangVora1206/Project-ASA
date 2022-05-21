import json
import fastapi
import uvicorn
app = fastapi.FastAPI()


# 0 roll no
# 1 prn
# 2 student name
# 3 lg
# 4 subject 1
# 30 total attended
# 31 total conducted
# 32 total percentage

def totalCounter(subjectDataDict):
    output = {}
    attended = 0
    conducted = 0
    for key in subjectDataDict.keys():
        if key != '%':
            try:
                attended += int(subjectDataDict[key]['LA'])
                conducted += int(subjectDataDict[key]['LC'])
            except:
                attended += int(subjectDataDict[key]['PA'])
                conducted += int(subjectDataDict[key]['PC'])
    output['TA'] = str(attended)
    output['TC'] = str(conducted)
    output['%'] = subjectDataDict["%"]['Total']
    return output

attendanceSheetsList = ['TY Test Sheet 1', 'TY Test Sheet 2', 'SY DS Test Sheet 1', 'TY Mech Test Sheet 1']


@app.get('/getTotalStudentAttendance/{PRN}')
def endpoint(PRN:str):
    flag = True
    prn = PRN
    index = -1
    sheetIndex = 0
    while flag:
        data = json.load(open(attendanceSheetsList[sheetIndex]+".json", "r"))
        # ---------------------------------------prn based index finder
        for i in range(len(data["0"])):
            if data["1"][str(i)] == prn:
                print("found at", i)
                index = i
                flag = False
                break
        if(sheetIndex < len(attendanceSheetsList)-1):
            sheetIndex += 1
        else:
            flag = False
    if index == -1:
        return 404
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
    addons = ['TA', 'TC', '%']
    if addons[0] not in subWiseData.keys():
        calcTATC = totalCounter(subWiseData)
        for i in addons:
            subWiseData[i] = {"" : calcTATC[i]}
    output = {
            "studentName":data[str(2)][str(index)],
            "studentPRN":data[str(1)][str(index)],
            "studentRollNo":data[str(0)][str(index)],
            "studentLG":data[str(3)][str(index)],
            "subjectData":subWiseData
        }

    return output

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)