from time import sleep
from datetime import datetime
from sheetsToJSON import sheetsToJSON
# sheets = ['TY Test Sheet 2']
sheets = ['TY Test Sheet 1', 'TY Test Sheet 2', 'SY DS Test Sheet 1', 'TY Mech Test Sheet 1']
while True:
    print("Refilling sheets")
    for i in range(len(sheets)):
        sheetsToJSONInstance1 = sheetsToJSON(sheets[i], 'Current Attendance')
        # sheetsToCSVInstance1 = sheetsToCSV(sheets[i], 'TY')
        sheetsToJSONInstance1.convertToJSON()
        print("last commit time :", datetime.now())
    print("Entering sleep state")
    sleep(60)
