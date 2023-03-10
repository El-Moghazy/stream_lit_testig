# streamlit_app.py

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
text = st.text_input('WRITE YOUR THOUGHTS')
if text in "WRITE YOUR THOUGHTS":
    st.write("" + text)
else:
    st.write("STOP WRITING B2A")
for row in rows:
    st.write(f"{row.wholesaler_name} has a :{row.wholesaler_id_number}:")