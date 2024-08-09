import streamlit as st
from datetime import date

LOGO_PATH = "images/ctec.png"
REPORT_TITLE = "[TITLE]"
DELIVERY_DATE = date(2024, 1, 1)


if __name__ == "__main__":
    with st.sidebar:

        # Sidebar Header
        st.image(LOGO_PATH)
        st.title(f"Addendum: {REPORT_TITLE}")
        st.write("*SENSITIVE - NOT FOR PUBLIC DISTRIBUTION*")

        # Date
        delivered_date = DELIVERY_DATE
        current_date = date.today()
        st.write(f"Today's Date: {current_date.strftime('%m/%d/%Y')}")
        st.write(f"Delivered On: {delivered_date.strftime('%m/%d/%Y')}")
