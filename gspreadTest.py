from numpy import average
import gspread
from oauth2client.service_account import ServiceAccountCredentials
gp = gspread.service_account(filename='akatsuki-attendance-system-87bab91de172.json')
gsheet = gp.open(r'Sheets API test')
wsheet = gsheet.worksheet("Sheet1")
sheetData = wsheet.get_all_values()

prn = '1951721245056'
studentDetails = {}
headers = sheetData[0]
for i in sheetData:
    if i[1] == prn:
        for x in range(len(i)):
            studentDetails[headers[x]] = i[x]

print(studentDetails)

subject1 = 'sub1'
subject2 = 'sub2'
subject3 = 'sub3'
subject4 = 'sub4'

totalLecturesSubject1 = 10
totalLecturesSubject2 = 10
totalLecturesSubject3 = 10
totalLecturesSubject4 = 10

attendedSubject1 = int(studentDetails[subject1])
attendedSubject2 = int(studentDetails[subject2])
attendedSubject3 = int(studentDetails[subject3])
attendedSubject4 = int(studentDetails[subject4])

attendanceSubject1 = (attendedSubject1/totalLecturesSubject1)*100
attendanceSubject2 = (attendedSubject2/totalLecturesSubject2)*100
attendanceSubject3 = (attendedSubject3/totalLecturesSubject3)*100
attendanceSubject4 = (attendedSubject4/totalLecturesSubject4)*100

totalStudentAttendance = average([attendanceSubject1, attendanceSubject2, attendanceSubject3, attendanceSubject4])

print("Subject 1 attendance", attendanceSubject1)
print("Subject 2 attendance", attendanceSubject2)
print("Subject 3 attendance", attendanceSubject3)
print("Subject 4 attendance", attendanceSubject4)
print("total student attendance", totalStudentAttendance)