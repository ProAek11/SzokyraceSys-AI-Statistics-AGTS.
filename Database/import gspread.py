import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up the credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials-file.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by title
sheet = client.open("Raw-Database of All Total").sheet1
sheet2 = client.open("Strategy Using High-Importance").sheet2
sheet3 = client.open("Fundamentals Macro-BigPicture").sheet3
sheet4 = client.open("Psychology of BigPlayers-Macro").sheet4
# Read data from the Google Sheet
data = sheet.get_all_records()
