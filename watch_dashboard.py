
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Authenticate using Streamlit Cloud secrets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("Watch_Inventory_Data").worksheet("Inventory")
data = sheet.get_all_records()
df = pd.DataFrame(data)

st.title("📊 Watch Trading Dashboard")
st.dataframe(df)
