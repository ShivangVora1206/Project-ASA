class sheetsToJSON:
    def __init__(self, sheetName, workSheetName):
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        self.sheetName = sheetName
        self.gp = gspread.service_account(filename='akatsuki-attendance-system-87bab91de172.json')
        self.gsheet = self.gp.open(sheetName)
        self.wsheet = self.gsheet.worksheet(workSheetName)

    def convertToJSON(self):
        import pandas as pd
        # dataFrame = pd.DataFrame(self.wsheet.get_all_records())
        dataFrame = pd.DataFrame(self.wsheet.get_values())
        try:
            dataToJSON = dataFrame.to_json(str(self.sheetName+".json"))

            print(self.sheetName, "Converted Successfully")
        except:
            print("Error while converting")

