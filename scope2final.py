import webbrowser
import streamlit as st
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.set_page_config(layout="wide")


# GHG emission factors and GWP (consider using a separate data file for maintainability)
ghg_data = {
    "CH4": {"Emission Factor": 0.0005, "Emission Factor Unit": "ton/kL", "GWP": 27},
    "CO2": {"Emission Factor": 0.0015, "Emission Factor Unit": "ton/kL", "GWP": 1},
    "N2O": {"Emission Factor": 0.0001, "Emission Factor Unit": "ton/kL", "GWP": 273},
    "HFC": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1},
    "CO2e": {"Emission Factor": 0.45, "Emission Factor Unit": "ton/kL", "GWP": 1},
    "PFCS": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1},
    "SF6": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1},
    "NF3": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1},
    "R-404a": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 3922},
    "R-410a": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 2088},
    "R-407c": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1774},
    "HFC-134a": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1430},
    "HCFC-22": {"Emission Factor": 1, "Emission Factor Unit": "ton/kL", "GWP": 1810}
}


# # Dummy department and sub-department options
# departments = [
#     "College of Arts and Science",
#     "College of Business and Economics",
#     "College of Education",
#     "College of Engineering",
#     "College of Law",
#     "QU Health",
#     "College of Health Sciences",
#     "College of Medicine",
#     "College of Pharmacy",
#     "College of Dental Medicine",
#     "College of Nursing",
#     "College of Sharia and Islamic Studies"
# ]
# sub_departments = {
#     "College of Arts and Science": [
#         "Arabic for Non-Native Speakers",
#         "Arabic Language",
#         "Biological and Environmental Sciences",
#         "Chemistry and Earth Sciences",
#         "English Literature and Linguistics",
#         "Gulf Studies Program",
#         "Humanities",
#         "International Affairs",
#         "Mass Communication",
#         "Materials Science and Technology",
#         "Mathematics, Statistics and Physics",
#         "Social Sciences"
#     ],
#     "College of Business and Economics": [
#         "Accounting & Information Systems",
#         "Finance & Economics",
#         "Management & Marketing"
#     ],
#     "College of Education": [
#         "Department of Educational Sciences",
#         "Department of Psychological Sciences",
#         "Department of Physical Education",
#         "Department of Art Education"
#     ],
#     "College of Engineering": [
#         "Architecture and Urban Planning",
#         "Chemical Engineering",
#         "Civil and Environmental Engineering",
#         "Computer Science and Engineering",
#         "Electrical Engineering",
#         "Mechanical and Industrial Engineering",
#         "Technology Innovation and Engineering Education Unit"
#     ],
#     "College of Law": [
#         "Private Law Department",
#         "Public Law Department",
#         "Legal Skills Department"
#     ],
#     "QU Health": [
#         "Clinical Affairs",
#         "Research and Graduate Studies",
#         "Academic Quality and Strategy",
#         "Clinical Operations and Engagement",
#         "Interprofessional Education",
#         "Continuous Professional Development"
#     ],
#     "College of Health Sciences": [
#         "Biomedical Sciences",
#         "Public Health",
#         "Human Nutrition",
#         "Rehabilitation Sciences"
#     ],
#     "College of Medicine": ["College of Medicine"],
#     "College of Pharmacy": [
#         "Scholarships",
#         "SPEP Program",
#         "Programs",
#         "Interprofessional Education"
#     ],
#     "College of Dental Medicine": ["College of Dental Medicine"],
#     "College of Nursing": ["College of Nursing"],
#     "College of Sharia and Islamic Studies": [
#         "Department of Quran and Sunnah",
#         "Department of Creed and Da'wah",
#         "Department of Jurisprudence and its Fundamentals"
#     ]
# }
def create_big_box(text):
    st.markdown(
        f"""
        <div style="padding: 10px; border: 3px solid green; border-radius: 10px; text-align: center; display: inline-block; margin: 30px;">
           <h3>Total SCOPE 2 GHG Emissions</h3>
            <h2>{text}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


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

# Improved main function with enhanced styling and UI
def main():
    

    # Enhanced CSS for a professional and stylish look (place in a separate CSS file for better organization)
    with open("style.css") as f:
        #st.set_page_config(page_title="GHG Emission Calculator", page_icon="", layout="wide")
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    st.sidebar.image('logo.png')

    st.sidebar.title("GHG Emission Calculator")
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
    st.markdown(
    """
<style>
text_input {
    height: auto;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    width: 40% !important;
}
</style>
""",
    unsafe_allow_html=True,
)


    # Create buttons using st.button with custom CSS class
    page = "Scope 1"
 
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
   

     
    st.title("SCOPE-2 Emission Calculation")
   
    st.table(ghg_data)
        
    #################################Electricity#######################################
        
    st.subheader(f"Electricity GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_electricity_1 = st.text_input(f"Data for Electricity", value="A", key="electricity_data1", disabled=True)
            
        data_electricity_2 = st.text_input(f"Data for Electricity", value="B", key="electricity_data2", disabled=True) 
        data_electricity_3 = st.text_input(f"Data for Electricity", value="C", key="electricity_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_electricity_1 = st.number_input(f"Quantity for A", key="electricity_qty1")  # Add unique key for each activity's quantity input
            
        qty_electricity_2 = st.number_input(f"Quantity for B", key="electricity_qty2")  # Add unique key for each activity's quantity input
        qty_electricity_3 = st.number_input(f"Quantity for C", key="electricity_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_electricity_1_1 = qty_electricity_1 * CO2_EF * CO2_GWP
    ghg_emission_data_electricity_1_2 = qty_electricity_1 * CH4_EF * CH4_GWP
    ghg_emission_data_electricity_1_3 = qty_electricity_1 * N2O_EF * N2O_GWP
    ghg_emission_data_electricity_2_1=qty_electricity_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_electricity_3_1=qty_electricity_3 * CO2_EF * CO2_GWP
    ghg_emission_data_electricity_3_2=qty_electricity_3 * HFC_EF * HFC_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_electricity_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_electricity_1_2:.5f}")
        st.write(f"N2O Emission for A: {ghg_emission_data_electricity_1_3:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_electricity_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_electricity_3_1:.5f}")
        st.write(f"HFC Emission for C: {ghg_emission_data_electricity_3_2:.5f}")
    with col8:
        total_ghg_data_electricity_1=ghg_emission_data_electricity_1_1+ghg_emission_data_electricity_1_2+ghg_emission_data_electricity_1_3
        total_ghg_data_electricity_2=ghg_emission_data_electricity_2_1
        total_ghg_data_electricity_3=ghg_emission_data_electricity_3_1+ghg_emission_data_electricity_3_2
        total_ghg_electricity=total_ghg_data_electricity_1+total_ghg_data_electricity_2+total_ghg_data_electricity_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_electricity_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_electricity_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_electricity_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Electricity: {total_ghg_electricity:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places


    ############################Steam####################################
        
    st.subheader(f"Steam GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_steam_1 = st.text_input(f"Data for Steam", value="A", key="Steam_data1", disabled=True)
            
        data_steam_2 = st.text_input(f"Data for Steam", value="B", key="Steam_data2", disabled=True) 
        data_steam_3 = st.text_input(f"Data for Steam", value="C", key="Steam_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_steam_1 = st.number_input(f"Quantity for A", key="Steam_qty1")  # Add unique key for each activity's quantity input
            
        qty_steam_2 = st.number_input(f"Quantity for B", key="Steam_qty2")  # Add unique key for each activity's quantity input
        qty_steam_3 = st.number_input(f"Quantity for C", key="Steam_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_steam_1_1 = qty_steam_1 * CO2_EF * CO2_GWP
    ghg_emission_data_steam_1_2 = qty_steam_1 * CH4_EF * CH4_GWP
    ghg_emission_data_steam_2_1=qty_steam_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_steam_3_1=qty_steam_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_steam_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_steam_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_steam_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_steam_3_1:.5f}")
    with col8:
        total_ghg_data_steam_1=ghg_emission_data_steam_1_1+ghg_emission_data_steam_1_2
        total_ghg_data_steam_2=ghg_emission_data_steam_2_1
        total_ghg_data_steam_3=ghg_emission_data_steam_3_1
        total_ghg_steam=total_ghg_data_steam_1+total_ghg_data_steam_2+total_ghg_data_steam_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_steam_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_steam_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_steam_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Steam: {total_ghg_steam:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places

    
    ############################HEATING####################################
        
    st.subheader(f"Heating GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_heating_1 = st.text_input(f"Data for Heating", value="A", key="heating_data1", disabled=True)
            
        data_heating_2 = st.text_input(f"Data for Heating", value="B", key="heating_data2", disabled=True) 
        data_heating_3 = st.text_input(f"Data for Heating", value="C", key="heating_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_heating_1 = st.number_input(f"Quantity for A", key="heating_qty1")  # Add unique key for each activity's quantity input
            
        qty_heating_2 = st.number_input(f"Quantity for B", key="heating_qty2")  # Add unique key for each activity's quantity input
        qty_heating_3 = st.number_input(f"Quantity for C", key="heating_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_heating_1_1 = qty_heating_1 * CO2_EF * CO2_GWP
    ghg_emission_data_heating_1_2 = qty_heating_1 * CH4_EF * CH4_GWP
    ghg_emission_data_heating_1_3 = qty_heating_1 * N2O_EF * N2O_GWP
    ghg_emission_data_heating_2_1=qty_heating_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_heating_3_1=qty_heating_3 * CO2_EF * CO2_GWP
    ghg_emission_data_heating_3_2=qty_heating_3 * HFC_EF * HFC_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_heating_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_heating_1_2:.5f}")
        st.write(f"N2O Emission for A: {ghg_emission_data_heating_1_3:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_heating_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_heating_3_1:.5f}")
        st.write(f"HFC Emission for C: {ghg_emission_data_heating_3_2:.5f}")
    with col8:
        total_ghg_data_heating_1=ghg_emission_data_heating_1_1+ghg_emission_data_heating_1_2+ghg_emission_data_heating_1_3
        total_ghg_data_heating_2=ghg_emission_data_heating_2_1
        total_ghg_data_heating_3=ghg_emission_data_heating_3_1+ghg_emission_data_heating_3_2
        total_ghg_heating=total_ghg_data_heating_1+total_ghg_data_heating_2+total_ghg_data_heating_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_heating_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_heating_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_heating_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Leakage of Refrigerator: {total_ghg_heating:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places

        
    #################################COOLING#######################################
        
    st.subheader(f"Cooling GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_cooling_1 = st.text_input(f"Data for Cooling", value="A", key="cooling_data1", disabled=True)
            
        data_cooling_2 = st.text_input(f"Data for Cooling", value="B", key="cooling_data2", disabled=True) 
        data_cooling_3 = st.text_input(f"Data for Cooling", value="C", key="cooling_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_cooling_1 = st.number_input(f"Quantity for A", key="cooling_qty1")  # Add unique key for each activity's quantity input
            
        qty_cooling_2 = st.number_input(f"Quantity for B", key="cooling_qty2")  # Add unique key for each activity's quantity input
        qty_cooling_3 = st.number_input(f"Quantity for C", key="cooling_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_cooling_1_1 = qty_cooling_1 * CO2_EF * CO2_GWP
    ghg_emission_data_cooling_1_2 = qty_cooling_1 * CH4_EF * CH4_GWP
    ghg_emission_data_cooling_2_1=qty_cooling_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_cooling_3_1=qty_cooling_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_cooling_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_cooling_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_cooling_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_cooling_3_1:.5f}")
    with col8:
        total_ghg_data_cooling_1=ghg_emission_data_cooling_1_1+ghg_emission_data_cooling_1_2
        total_ghg_data_cooling_2=ghg_emission_data_cooling_2_1
        total_ghg_data_cooling_3=ghg_emission_data_cooling_3_1
        total_ghg_cooling=total_ghg_data_cooling_1+total_ghg_data_cooling_2+total_ghg_data_cooling_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_cooling_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_cooling_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_cooling_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Cooling: {total_ghg_cooling:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places
    col9, col10, col11 =st.columns(3)
    with col10:
        total_scope2_emission=total_ghg_electricity+total_ghg_steam+total_ghg_heating+total_ghg_cooling
        create_big_box(total_scope2_emission)
    submit_button = st.button(label='Submit')
    if submit_button:
        st.success('Scope 2 Data submitted successfully!')


if __name__ == "__main__":
    main()

