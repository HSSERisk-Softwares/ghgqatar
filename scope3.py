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
           <h3>Total SCOPE 3 GHG Emissions</h3>
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
     
    st.title("SCOPE-3 Emission Calculation")
   
    st.table(ghg_data)
        
    #################################Purchased Goods and Services#######################################
        
    st.subheader(f"Purchased Goods and Services GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_purchased_goods_and_services_1 = st.text_input(f"Data for Purchased Goods and Services", value="Work From Home", key="purchased_goods_and_services_data1", disabled=True)
            
        data_purchased_goods_and_services_2 = st.text_input(f"Data for Purchased Goods and Services", value="B", key="purchased_goods_and_services_data2", disabled=True) 
        data_purchased_goods_and_services_3 = st.text_input(f"Data for Purchased Goods and Services", value="C", key="purchased_goods_and_services_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_purchased_goods_and_services_1 = st.number_input(f"Quantity for Work From Home", key="purchased_goods_and_services_qty1")  # Add unique key for each activity's quantity input
            
        qty_purchased_goods_and_services_2 = st.number_input(f"Quantity for B", key="purchased_goods_and_services_qty2")  # Add unique key for each activity's quantity input
        qty_purchased_goods_and_services_3 = st.number_input(f"Quantity for C", key="purchased_goods_and_services_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_purchased_goods_and_services_1_1 = qty_purchased_goods_and_services_1 * CO2_EF * CO2_GWP
    ghg_emission_data_purchased_goods_and_services_1_2 = qty_purchased_goods_and_services_1 * CH4_EF * CH4_GWP
    ghg_emission_data_purchased_goods_and_services_1_3 = qty_purchased_goods_and_services_1 * N2O_EF * N2O_GWP
    ghg_emission_data_purchased_goods_and_services_2_1=qty_purchased_goods_and_services_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_purchased_goods_and_services_3_1=qty_purchased_goods_and_services_3 * CO2_EF * CO2_GWP
    ghg_emission_data_purchased_goods_and_services_3_2=qty_purchased_goods_and_services_3 * HFC_EF * HFC_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for Work From Home: {ghg_emission_data_purchased_goods_and_services_1_1:.5f}")
        st.write(f"CH4 Emission for Work From Home: {ghg_emission_data_purchased_goods_and_services_1_2:.5f}")
        st.write(f"N2O Emission for Work From Home: {ghg_emission_data_purchased_goods_and_services_1_3:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_purchased_goods_and_services_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_purchased_goods_and_services_3_1:.5f}")
        st.write(f"HFC Emission for C: {ghg_emission_data_purchased_goods_and_services_3_2:.5f}")
    with col8:
        total_ghg_data_purchased_goods_and_services_1=ghg_emission_data_purchased_goods_and_services_1_1+ghg_emission_data_purchased_goods_and_services_1_2+ghg_emission_data_purchased_goods_and_services_1_3
        total_ghg_data_purchased_goods_and_services_2=ghg_emission_data_purchased_goods_and_services_2_1
        total_ghg_data_purchased_goods_and_services_3=ghg_emission_data_purchased_goods_and_services_3_1+ghg_emission_data_purchased_goods_and_services_3_2
        total_ghg_purchased_goods_and_services=total_ghg_data_purchased_goods_and_services_1+total_ghg_data_purchased_goods_and_services_2+total_ghg_data_purchased_goods_and_services_3
        
        st.write(f"Total GHG Emission for Work From Home: {total_ghg_data_purchased_goods_and_services_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_purchased_goods_and_services_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_purchased_goods_and_services_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Purchased Goods and Services: {total_ghg_purchased_goods_and_services:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places


    ############################Fuel- and Energy-Related Activities Not Included in Scope 1 or Scope 2 (TNDLE)Transmission and distribution loss for electricity####################################
        
    st.subheader(f"Fuel- and Energy-Related Activities Not Included in Scope 1 or Scope 2")
    col5, col6 = st.columns(2)
    with col5:

        data_fuel_1 = st.text_input(f"Data for Fuel- and Energy-Related Activities Not Included in Scope 1 or Scope 2", value="Transmission and distribution loss for electricity", key="fuel_data1", disabled=True)
            
        # data_tdle_2 = st.text_input(f"Data for Transmission and distribution loss for electricity", value="B", key="tdle_data2", disabled=True) 
        # data_tdle_3 = st.text_input(f"Data for Transmission and distribution loss for electricity", value="C", key="tdle_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_fuel_1 = st.number_input(f"Quantity for Transmission and distribution loss for electricity", key="fuel_qty1")  # Add unique key for each activity's quantity input
            
        # qty_tdle_2 = st.number_input(f"Quantity for B", key="tdle_qty2")  # Add unique key for each activity's quantity input
        # qty_tdle_3 = st.number_input(f"Quantity for C", key="tdle_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_fuel_1_1 = qty_fuel_1 * CO2_EF * CO2_GWP
    ghg_emission_data_fuel_1_2 = qty_fuel_1 * CH4_EF * CH4_GWP
    ghg_emission_data_fuel_1_3=qty_fuel_1 * N2O_EF * N2O_GWP
    # ghg_emission_data_tdle_3_1=qty_tdle_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for Transmission and distribution loss for electricity: {ghg_emission_data_fuel_1_1:.5f}")
        st.write(f"CH4 Emission for Transmission and distribution loss for electricity: {ghg_emission_data_fuel_1_2:.5f}")
        st.write(f"CO2e Emission for Transmission and distribution loss for electricity: {ghg_emission_data_fuel_1_3:.5f}")
        # st.write(f"CO2 Emission for C: {ghg_emission_data_tdle_3_1:.5f}")
    with col8:
        total_ghg_data_fuel_1=ghg_emission_data_fuel_1_1+ghg_emission_data_fuel_1_2+ghg_emission_data_fuel_1_3
        # total_ghg_data_tdle_2=ghg_emission_data_tdle_2_1
        # total_ghg_data_tdle_3=ghg_emission_data_tdle_3_1
        total_ghg_fuel=total_ghg_data_fuel_1
        # +total_ghg_data_tdle_2+total_ghg_data_tdle_3
        
        st.write(f"Total GHG Emission for Transmission and distribution loss for electricity: {total_ghg_data_fuel_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        # st.write(f"Total GHG Emission for B: {total_ghg_data_tdle_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        # st.write(f"Total GHG Emission for C: {total_ghg_data_tdle_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Transmission and distribution loss for electricity: {total_ghg_fuel:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places

  

        
    #################################Waste#######################################
        
    st.subheader(f"Waste GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_waste_1 = st.text_input(f"Data for Waste", value="A", key="waste_data1", disabled=True)
            
        data_waste_2 = st.text_input(f"Data for Waste", value="B", key="waste_data2", disabled=True) 
        data_waste_3 = st.text_input(f"Data for Waste", value="C", key="waste_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_waste_1 = st.number_input(f"Quantity for A", key="waste_qty1")  # Add unique key for each activity's quantity input
            
        qty_waste_2 = st.number_input(f"Quantity for B", key="waste_qty2")  # Add unique key for each activity's quantity input
        qty_waste_3 = st.number_input(f"Quantity for C", key="waste_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_waste_1_1 = qty_waste_1 * CO2_EF * CO2_GWP
    ghg_emission_data_waste_1_2 = qty_waste_1 * CH4_EF * CH4_GWP
    ghg_emission_data_waste_2_1=qty_waste_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_waste_3_1=qty_waste_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_waste_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_waste_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_waste_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_waste_3_1:.5f}")
    with col8:
        total_ghg_data_waste_1=ghg_emission_data_waste_1_1+ghg_emission_data_waste_1_2
        total_ghg_data_waste_2=ghg_emission_data_waste_2_1
        total_ghg_data_waste_3=ghg_emission_data_waste_3_1
        total_ghg_waste=total_ghg_data_waste_1+total_ghg_data_waste_2+total_ghg_data_waste_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_waste_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_waste_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_waste_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Waste: {total_ghg_waste:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places
    


        
    #################################Business Travel#######################################
        
    st.subheader(f"Business Travel GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_business_travel_1 = st.text_input(f"Data for Business Travel", value="A", key="business_travel_data1", disabled=True)
            
        data_business_travel_2 = st.text_input(f"Data for Business Travel", value="B", key="business_travel_data2", disabled=True) 
        data_business_travel_3 = st.text_input(f"Data for Business Travel", value="C", key="business_travel_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_business_travel_1 = st.number_input(f"Quantity for A", key="business_travel_qty1")  # Add unique key for each activity's quantity input
            
        qty_business_travel_2 = st.number_input(f"Quantity for B", key="business_travel_qty2")  # Add unique key for each activity's quantity input
        qty_business_travel_3 = st.number_input(f"Quantity for C", key="business_travel_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_business_travel_1_1 = qty_business_travel_1 * CO2_EF * CO2_GWP
    ghg_emission_data_business_travel_1_2 = qty_business_travel_1 * CH4_EF * CH4_GWP
    ghg_emission_data_business_travel_2_1=qty_business_travel_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_business_travel_3_1=qty_business_travel_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_business_travel_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_business_travel_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_business_travel_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_business_travel_3_1:.5f}")
    with col8:
        total_ghg_data_business_travel_1=ghg_emission_data_business_travel_1_1+ghg_emission_data_business_travel_1_2
        total_ghg_data_business_travel_2=ghg_emission_data_business_travel_2_1
        total_ghg_data_business_travel_3=ghg_emission_data_business_travel_3_1
        total_ghg_business_travel=total_ghg_data_business_travel_1+total_ghg_data_business_travel_2+total_ghg_data_business_travel_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_business_travel_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_business_travel_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_business_travel_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Business Travel: {total_ghg_business_travel:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places
    



        
    #################################Employee Commuting#######################################
        
    st.subheader(f"Employee Commuting GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_employee_community_1 = st.text_input(f"Data for Employee Commuting", value="In-campus special needs vehicles", key="employee_community_data1", disabled=True)
            
        data_employee_community_2 = st.text_input(f"Data for Employee Commuting", value="Home-campus bus fleet", key="employee_community_data2", disabled=True) 
        data_employee_community_3 = st.text_input(f"Data for Employee Commuting", value="Transportation cars to travel admin/academic staff from and to the campus in special occasions", key="employee_community_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_employee_community_1 = st.number_input(f"Quantity for In-campus special needs vehicles", key="employee_community_qty1")  # Add unique key for each activity's quantity input
            
        qty_employee_community_2 = st.number_input(f"Quantity for Home-campus bus fleet", key="employee_community_qty2")  # Add unique key for each activity's quantity input
        qty_employee_community_3 = st.number_input(f"Quantity for Transportation cars to travel admin/academic staff from and to the campus in special occasions", key="employee_community_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_employee_community_1_1 = qty_employee_community_1 * CO2_EF * CO2_GWP
    ghg_emission_data_employee_community_1_2 = qty_employee_community_1 * CH4_EF * CH4_GWP
    ghg_emission_data_employee_community_1_3 = qty_employee_community_1 * N2O_EF * N2O_GWP
    ghg_emission_data_employee_community_2_1 = qty_employee_community_2 * CO2_EF * CO2_GWP
    ghg_emission_data_employee_community_2_2 = qty_employee_community_2 * CH4_EF * CH4_GWP
    ghg_emission_data_employee_community_2_3 = qty_employee_community_2 * N2O_EF * N2O_GWP
    ghg_emission_data_employee_community_3_1 = qty_employee_community_3 * CO2_EF * CO2_GWP
    ghg_emission_data_employee_community_3_2 = qty_employee_community_3 * CH4_EF * CH4_GWP
    ghg_emission_data_employee_community_3_3 = qty_employee_community_3 * N2O_EF * N2O_GWP

    # ghg_emission_data_employee_community_2_1=qty_employee_community_2 * CO2e_EF * CO2e_GWP
    # ghg_emission_data_employee_community_3_1=qty_employee_community_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for In-campus special needs vehicles: {ghg_emission_data_employee_community_1_1:.5f}")
        st.write(f"CH4 Emission for In-campus special needs vehicles: {ghg_emission_data_employee_community_1_2:.5f}")
        st.write(f"N2O Emission for In-campus special needs vehicles: {ghg_emission_data_employee_community_1_3:.5f}")

        st.write(f"CO2 Emission for Home-campus bus fleet: {ghg_emission_data_employee_community_2_1:.5f}")
        st.write(f"CO2 Emission for Home-campus bus fleet: {ghg_emission_data_employee_community_2_2:.5f}")
        st.write(f"CO2 Emission for Home-campus bus fleet: {ghg_emission_data_employee_community_2_3:.5f}")

        st.write(f"CO2 Emission for Transportation cars to travel admin/academic staff from and to the campus in special occasions: {ghg_emission_data_employee_community_3_1:.5f}")
        st.write(f"CO2 Emission for Transportation cars to travel admin/academic staff from and to the campus in special occasions: {ghg_emission_data_employee_community_3_2:.5f}")
        st.write(f"CO2 Emission for Transportation cars to travel admin/academic staff from and to the campus in special occasions: {ghg_emission_data_employee_community_3_3:.5f}")

    with col8:
        total_ghg_data_employee_community_1=ghg_emission_data_employee_community_1_1+ghg_emission_data_employee_community_1_2+ghg_emission_data_employee_community_1_3
        total_ghg_data_employee_community_2=ghg_emission_data_employee_community_2_1+ghg_emission_data_employee_community_2_2+ghg_emission_data_employee_community_2_3
        total_ghg_data_employee_community_3=ghg_emission_data_employee_community_3_1+ghg_emission_data_employee_community_3_2+ghg_emission_data_employee_community_3_3
        total_ghg_employee_community=total_ghg_data_employee_community_1+total_ghg_data_employee_community_2+total_ghg_data_employee_community_3
        
        st.write(f"Total GHG Emission for In-campus special needs vehicles: {total_ghg_data_employee_community_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for Home-campus bus fleet: {total_ghg_data_employee_community_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for Transportation cars to travel admin/academic staff from and to the campus in special occasions: {total_ghg_data_employee_community_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Employee Commuting: {total_ghg_employee_community:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places

    #################################Capital Goods#######################################
        
    st.subheader(f"Capital Goods GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_capital_goods_1 = st.text_input(f"Data for Capital Goods", value="A", key="capital_goods_data1", disabled=True)
            
        data_capital_goods_2 = st.text_input(f"Data for Capital Goods", value="B", key="capital_goods_data2", disabled=True) 
        data_capital_goods_3 = st.text_input(f"Data for Capital Goods", value="C", key="capital_goods_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_capital_goods_1 = st.number_input(f"Quantity for A", key="capital_goods_qty1")  # Add unique key for each activity's quantity input
            
        qty_capital_goods_2 = st.number_input(f"Quantity for B", key="capital_goods_qty2")  # Add unique key for each activity's quantity input
        qty_capital_goods_3 = st.number_input(f"Quantity for C", key="capital_goods_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_capital_goods_1_1 = qty_capital_goods_1 * CO2_EF * CO2_GWP
    ghg_emission_data_capital_goods_1_2 = qty_capital_goods_1 * CH4_EF * CH4_GWP
    ghg_emission_data_capital_goods_2_1=qty_capital_goods_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_capital_goods_3_1=qty_capital_goods_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_capital_goods_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_capital_goods_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_capital_goods_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_capital_goods_3_1:.5f}")
    with col8:
        total_ghg_data_capital_goods_1=ghg_emission_data_capital_goods_1_1+ghg_emission_data_capital_goods_1_2
        total_ghg_data_capital_goods_2=ghg_emission_data_capital_goods_2_1
        total_ghg_data_capital_goods_3=ghg_emission_data_capital_goods_3_1
        total_ghg_capital_goods=total_ghg_data_capital_goods_1+total_ghg_data_capital_goods_2+total_ghg_data_capital_goods_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_capital_goods_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_capital_goods_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_capital_goods_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Capital Goods: {total_ghg_capital_goods:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

    #################################water supply and waste water treatment#######################################
        
    st.subheader(f"Water supply and waste water treatment GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_water_1 = st.text_input(f"Data for water supply and waste water treatment", value="A", key="water_data1", disabled=True)
            
        data_water_2 = st.text_input(f"Data for water supply and waste water treatment", value="B", key="water_data2", disabled=True) 
        data_water_3 = st.text_input(f"Data for water supply and waste water treatment", value="C", key="water_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_water_1 = st.number_input(f"Quantity for A", key="water_qty1")  # Add unique key for each activity's quantity input
            
        qty_water_2 = st.number_input(f"Quantity for B", key="water_qty2")  # Add unique key for each activity's quantity input
        qty_water_3 = st.number_input(f"Quantity for C", key="water_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_water_1_1 = qty_water_1 * CO2_EF * CO2_GWP
    ghg_emission_data_water_1_2 = qty_water_1 * CH4_EF * CH4_GWP
    ghg_emission_data_water_2_1=qty_water_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_water_3_1=qty_water_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_water_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_water_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_water_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_water_3_1:.5f}")
    with col8:
        total_ghg_data_water_1=ghg_emission_data_water_1_1+ghg_emission_data_water_1_2
        total_ghg_data_water_2=ghg_emission_data_water_2_1
        total_ghg_data_water_3=ghg_emission_data_water_3_1
        total_ghg_water=total_ghg_data_water_1+total_ghg_data_water_2+total_ghg_data_water_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_water_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_water_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_water_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for water supply and waste water treatment: {total_ghg_water:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

    #################################Franchises#######################################
        
    st.subheader(f"Franchises GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_franchises_1 = st.text_input(f"Data for Franchises", value="A", key="franchises_data1", disabled=True)
            
        data_franchises_2 = st.text_input(f"Data for Franchises", value="B", key="franchises_data2", disabled=True) 
        data_franchises_3 = st.text_input(f"Data for Franchises", value="C", key="franchises_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_franchises_1 = st.number_input(f"Quantity for A", key="franchises_qty1")  # Add unique key for each activity's quantity input
            
        qty_franchises_2 = st.number_input(f"Quantity for B", key="franchises_qty2")  # Add unique key for each activity's quantity input
        qty_franchises_3 = st.number_input(f"Quantity for C", key="franchises_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_franchises_1_1 = qty_franchises_1 * CO2_EF * CO2_GWP
    ghg_emission_data_franchises_1_2 = qty_franchises_1 * CH4_EF * CH4_GWP
    ghg_emission_data_franchises_2_1=qty_franchises_2 * CO2e_EF * CO2e_GWP
    ghg_emission_data_franchises_3_1=qty_franchises_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for A: {ghg_emission_data_franchises_1_1:.5f}")
        st.write(f"CH4 Emission for A: {ghg_emission_data_franchises_1_2:.5f}")
        st.write(f"CO2e Emission for B: {ghg_emission_data_franchises_2_1:.5f}")
        st.write(f"CO2 Emission for C: {ghg_emission_data_franchises_3_1:.5f}")
    with col8:
        total_ghg_data_franchises_1=ghg_emission_data_franchises_1_1+ghg_emission_data_franchises_1_2
        total_ghg_data_franchises_2=ghg_emission_data_franchises_2_1
        total_ghg_data_franchises_3=ghg_emission_data_franchises_3_1
        total_ghg_franchises=total_ghg_data_franchises_1+total_ghg_data_franchises_2+total_ghg_data_franchises_3
        
        st.write(f"Total GHG Emission for A: {total_ghg_data_franchises_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for B: {total_ghg_data_franchises_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for C: {total_ghg_data_franchises_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Franchises: {total_ghg_franchises:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

   
    
    col9, col10, col11 =st.columns(3)
    with col10:
        total_scope3_emission=total_ghg_purchased_goods_and_services+total_ghg_fuel+total_ghg_employee_community+total_ghg_business_travel+total_ghg_waste+total_ghg_capital_goods+total_ghg_water+total_ghg_franchises
        create_big_box(total_scope3_emission)
    
    submit_button = st.button(label='Submit')
    if submit_button:
        st.success('Scope 3 Data submitted successfully!')


if __name__ == "__main__":
    main()

