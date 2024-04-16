import streamlit as st
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import io
from PIL import Image

st.set_page_config(layout="wide")



# Dummy user credentials
valid_users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}
ghg_data = {
            "CH4": {"Emission Factor": 0.0005, "Emission Factor Unit": "ton/kL", "GWP": 25},
            "CO2": {"Emission Factor": 0.0015, "Emission Factor Unit": "ton/kL", "GWP": 1},
            "N2O": {"Emission Factor": 0.0001, "Emission Factor Unit": "ton/kL", "GWP": 300},
            "HFC": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1},
            "CO2e": {"Emission Factor": 0.00045, "Emission Factor Unit": "ton/lit", "GWP": 1}
        }
# Dummy department and sub-department options
departments = ["Dept A", "Dept B", "Dept C", "Dept D"]
sub_departments = {
            "Dept A": ["A-1", "A-2", "A-3"],
            "Dept B": ["B-1", "B-2", "B-3"],
            "Dept C": ["C-1", "C-2", "C-3"],
            "Dept D": ["D-1", "D-2", "D-3"]
        }


EFU="ton/kL"
CH4_EF=0.0005
CH4_GWP=25
CO2_EF=0.0015
CO2_GWP=1
N2O_EF=0.0001
N2O_GWP=300
HFC_EF=1
HFC_GWP=1
CO2e_EF=0.00045
CO2e_GWP=1
PFCS_EF=1
PFCS_GWP=1
SF6_EF=1
SF6_GWP=1
NF3_EF=1
NF3_GWP=1

# Function to check user credentials
def authenticate(username, password):
    return valid_users.get(username) == password

# Improved main function with enhanced styling and UI
def main():
    
    if "login" not in st.session_state:
        st.session_state.login = False

    if not st.session_state.login:
        col1, col2, col3 =st.columns(3)
        with col2:
            st.image('logo.png')
            st.title("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if authenticate(username, password):
                    st.session_state.login = True
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
        return

  
    
    st.sidebar.image('logo.png')
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    
    st.markdown(
    """
<style>
button {
    height: auto;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    width: 100% !important;
}
</style>
""",
    unsafe_allow_html=True,
)
#     st.markdown(
#     """
# <style>
# text_input {
#     height: auto;
#     padding-top: 10px !important;
#     padding-bottom: 10px !important;
#     width: 40% !important;
# }
# </style>
# """,
#     unsafe_allow_html=True,
# )
    st.sidebar.title("GHG Emission Calculator")
    

    # Create buttons using st.button with custom CSS class
    page = "Dashboard"
 
    if st.sidebar.button("Dashboard"):
        page = "Dashboard"
    if st.sidebar.button("Scope 1"):
        # switch_page("https://hsserisk-ghgemissioncalculator-scope1.streamlit.app/")
        # webbrowser.open("https://hsserisk-ghgemissioncalculator-scope1.streamlit.app/") #this is final
        webbrowser.open("http://localhost:8502")
        page = "Scope 1"
    if st.sidebar.button("Scope 2"):
        webbrowser.open("http://localhost:8503")
        page = "Scope 2"
    if st.sidebar.button("Scope 3"):
        webbrowser.open("http://localhost:8504")
        page = "Scope 3"
    if st.sidebar.button("Logout"):
        page = "Logout"
    if st.sidebar.button("Contact Support"):
        webbrowser.open("http://localhost:8505")
        page = "Contact Support"
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    
    imagehsse = Image.open("hsse.png")
    newhsse_image = imagehsse.resize((400, 100))
    st.sidebar.image(newhsse_image)

   
    if page == "Dashboard":
        
        st.title("Dashboard")
        st.write("Welcome to the GHG Emission Calculator Dashboard!")
        # Add dashboard content here
        # # Create dummy data for plotting
        # np.random.seed(0)
        # data = {
        #     'Category': ['A', 'B', 'C', 'D', 'E'],
        #     'Value': np.random.randint(1, 100, size=5)
        # }
        # Display graphs in one row
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Bar Plot')
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.bar_chart(chart_data)

        # # Line plot
        with col2:
            st.subheader('Line Plot')
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
            st.line_chart(chart_data)
            


        df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
        
        buffer = io.BytesIO()

        # Create some Pandas dataframes from some data.
        # Creating the DataFrame
        data = {
            "Month": ["April"],
            "Year": [2024],
            "Department": ["College of Engineering"],
            "Sub-department": ["Computer Science and Engineering"],
            "Total SCOPE 1 GHG Emissions": [800],
            "Total GHG Emission for Stationary Combustion": [400],
            "Total GHG Emission for Captive Power Generation from combustion of fossil fuel HSD (diesel generator)": [300],
            "Total GHG Emission for LPG consumption in canteen": [300],
            "Total GHG Emission for LPG consumption in laboratories": [127],
            "Total GHG Emission for Mobile Combustion": [873],
            "Total GHG Emission for Transportation": [300],
            "Total GHG Emission for Leakage of Refrigerator/ Air Conditioner": [300],
            "Total GHG Emission for R-404a": [300],
            "Total GHG Emission for R-410a": [300],
            "Total GHG Emission for R-407c": [300],
            "Total GHG Emission for HFC-134a": [300],
            "Total GHG Emission for HCFC-22": [300],
            "Total GHG Emission for Process Emission": [300],
            "Total GHG Emission for Pasteurized Compost and Peat Moss (organic type)": [300],
            "Total GHG Emission for Urea (synthetic type)": [0],
            "Total SCOPE 2 GHG Emissions": [300],
            "Total GHG Emission for Electricity": [300],
            "Total GHG Emission for Steam": [0],
            "Total GHG Emission for Heating": [300],
            "Total GHG Emission for Cooling": [300],
            "Total SCOPE 3 GHG Emissions": [300],
            "Total GHG Emission for Purchased Goods and Services": [300],
            "Total GHG Emission for Work From Home": [300],
            "Total GHG Emission for Fuel- and Energy-Related Activities Not Included in Scope 1 or Scope 2": [300],
            "Total GHG Emission for Transmission and distribution loss for electricity": [300],
            "Total GHG Emission for Waste": [300],
            "Total GHG Emission for Business Travel": [300],
            "Total GHG Emission for Employee Commuting": [300],
            "Total GHG Emission for In-campus special needs vehicles": [300],
            "Total GHG Emission for Home-campus bus fleet": [300],
            "Total GHG Emission for Transportation cars to travel admin/academic staff from and to the campus in special occasions": [300],
            "Total GHG Emission for Capital Goods": [300],
            "Total GHG Emission for water supply and waste water treatment": [300],
            "Total GHG Emission for Franchises": [300]
        }

        df = pd.DataFrame(data)

        # df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
        # df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            # Write each dataframe to a different worksheet.
            df.to_excel(writer, sheet_name='Sheet1')
            # df2.to_excel(writer, sheet_name='Sheet2')
            # df3.to_excel(writer, sheet_name='Sheet3')

            # Close the Pandas Excel writer and output the Excel file to the buffer
            writer.close()

            st.download_button(
                label="Download Report as Excel worksheets",
                data=buffer,
                file_name="Report_17_April_2024.xlsx",
                mime="application/vnd.ms-excel"
            )
        with open("Report_17_April_2024.pdf", "rb") as f:
            st.download_button("Download Report as pdf", f, "Report_17_April_2024.pdf")

        st.table(df)
            

    
    if page == "Scope 2":
        st.title("SCOPE-2 Emission Calculation")
        st.write("Add Scope 2 calculation form here")

    if page == "Scope 3":
        st.title("SCOPE-3 Emission Calculation")
        st.write("Add Scope 3 calculation form here")

    if page == "Logout":
        st.session_state.login = False
        st.rerun()
    if page == "Contact Support":
        st.title("Contact Support")
        st.write("Contact Us")

if __name__ == "__main__":
    main()

