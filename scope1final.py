import streamlit as st
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
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


# Dummy department and sub-department options
departments = [
    "College of Arts and Science",
    "College of Business and Economics",
    "College of Education",
    "College of Engineering",
    "College of Law",
    "QU Health",
    "College of Health Sciences",
    "College of Medicine",
    "College of Pharmacy",
    "College of Dental Medicine",
    "College of Nursing",
    "College of Sharia and Islamic Studies"
]
sub_departments = {
    "College of Arts and Science": [
        "Arabic for Non-Native Speakers",
        "Arabic Language",
        "Biological and Environmental Sciences",
        "Chemistry and Earth Sciences",
        "English Literature and Linguistics",
        "Gulf Studies Program",
        "Humanities",
        "International Affairs",
        "Mass Communication",
        "Materials Science and Technology",
        "Mathematics, Statistics and Physics",
        "Social Sciences"
    ],
    "College of Business and Economics": [
        "Accounting & Information Systems",
        "Finance & Economics",
        "Management & Marketing"
    ],
    "College of Education": [
        "Department of Educational Sciences",
        "Department of Psychological Sciences",
        "Department of Physical Education",
        "Department of Art Education"
    ],
    "College of Engineering": [
        "Architecture and Urban Planning",
        "Chemical Engineering",
        "Civil and Environmental Engineering",
        "Computer Science and Engineering",
        "Electrical Engineering",
        "Mechanical and Industrial Engineering",
        "Technology Innovation and Engineering Education Unit"
    ],
    "College of Law": [
        "Private Law Department",
        "Public Law Department",
        "Legal Skills Department"
    ],
    "QU Health": [
        "Clinical Affairs",
        "Research and Graduate Studies",
        "Academic Quality and Strategy",
        "Clinical Operations and Engagement",
        "Interprofessional Education",
        "Continuous Professional Development"
    ],
    "College of Health Sciences": [
        "Biomedical Sciences",
        "Public Health",
        "Human Nutrition",
        "Rehabilitation Sciences"
    ],
    "College of Medicine": ["College of Medicine"],
    "College of Pharmacy": [
        "Scholarships",
        "SPEP Program",
        "Programs",
        "Interprofessional Education"
    ],
    "College of Dental Medicine": ["College of Dental Medicine"],
    "College of Nursing": ["College of Nursing"],
    "College of Sharia and Islamic Studies": [
        "Department of Quran and Sunnah",
        "Department of Creed and Da'wah",
        "Department of Jurisprudence and its Fundamentals"
    ]
}


def create_big_box(text):
    st.markdown(
        f"""
        <div style="padding: 10px; border: 3px solid green; border-radius: 10px; text-align: center; display: inline-block; margin: 30px;">
           <h3>Total SCOPE 1 GHG Emissions</h3>
            <h2>{text}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


EFU="ton/kL"
CH4_EF=0.0005
CH4_GWP=27
CO2_EF=0.0015
CO2_GWP=1
N2O_EF=0.0001
N2O_GWP=273
HFC_EF=1
HFC_GWP=1
CO2e_EF=0.45
CO2e_GWP=1
PFCS_EF=1
PFCS_GWP=1
SF6_EF=1
SF6_GWP=1
NF3_EF=1
NF3_GWP=1
R_404a_EF=1
R_404a_GWP=3922
R_410a_EF=1
R_410a_GWP=2088
R_407c_EF=1
R_407c_GWP=1774
HFC_134a_EF=1
HFC_134a_GWP=1430
HCFC_22_EF=1
HCFC_22_GWP=1810



# Improved main function with enhanced styling and UI
def scope1():
    

    # Enhanced CSS for a professional and stylish look (place in a separate CSS file for better organization)
    st.sidebar.image('logo.png')
    with open("style.css") as f:
        #st.set_page_config(page_title="GHG Emission Calculator", page_icon="", layout="wide")
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
   
            
    st.title("SCOPE-1 Emission Calculation")
            # Create a session state variable to store the selected value

            # Improved layout for better organization
    col3, col4 = st.columns(2)
    with col3:
        month = st.selectbox("Select Month", range(1, 13), format_func=lambda x: datetime.strptime(str(x), "%m").strftime("%B"))
        department = st.selectbox("Select Department", departments)
                
                    
            # sub_department = st.selectbox("Select Sub-Department", sub_departments.get(department, []))
            #     # Display the selected option
                
                

    with col4:
            # month = st.selectbox("Select Month", range(1, 13), format_func=lambda x: datetime.strptime(str(x), "%m").strftime("%B"))
        year = st.selectbox("Select Year", range(2022, datetime.now().year + 1))
        sub_department = st.selectbox("Select Sub-Department", sub_departments.get(department, []))
                # Display the selected option

    period = datetime(year, month, 1)
            


            # GHG emission form for each activity
        # activities = [
        #         "Stationary Combustion", "Mobile Combustion", "Leakage of Refrigerant", "Process Emission"
        #     ]
    total_scope1 = 0
    st.table(ghg_data)
        
    #################################Stationary Combustion#######################################
        
    st.subheader(f"Stationary Combustion GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_stationary_comb_1 = st.text_input(f"Data for Stationary Combustion", value="Captive Power Generation from combustion of fossil fuel HSD (diesel generator)", key="Stationary_Combustion_data1", disabled=True)
            
        data_stationary_comb_2 = st.text_input(f"Data for Stationary Combustion", value="LPG consumption in canteen", key="Stationary_Combustion_data2", disabled=True) 
        data_stationary_comb_3 = st.text_input(f"Data for Stationary Combustion", value="LPG consumption in laboratories", key="Stationary_Combustion_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input 
    with col6:
        qty_stationary_comb_1 = st.number_input(f"Quantity for Captive Power Generation from combustion of fossil fuel HSD (diesel generator)", key="Stationary_Combustion_qty1")  # Add unique key for each activity's quantity input
            
        qty_stationary_comb_2 = st.number_input(f"Quantity for LPG consumption in canteen", key="Stationary_Combustion_qty2")  # Add unique key for each activity's quantity input
        qty_stationary_comb_3 = st.number_input(f"Quantity for LPG consumption in laboratories", key="Stationary_Combustion_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_stationary_comb_1_1 = qty_stationary_comb_1 * CO2_EF * CO2_GWP
    ghg_emission_data_stationary_comb_1_2 = qty_stationary_comb_1 * CH4_EF * CH4_GWP
    ghg_emission_data_stationary_comb_1_3 = qty_stationary_comb_1 * N2O_EF * N2O_GWP
    ghg_emission_data_stationary_comb_2_1=qty_stationary_comb_2 * CO2_EF * CO2_GWP
    ghg_emission_data_stationary_comb_2_2=qty_stationary_comb_2 * CH4_EF * CH4_GWP
    ghg_emission_data_stationary_comb_2_3=qty_stationary_comb_2 * N2O_EF * N2O_GWP
    ghg_emission_data_stationary_comb_3_1=qty_stationary_comb_3 * CO2_EF * CO2_GWP
    ghg_emission_data_stationary_comb_3_2=qty_stationary_comb_3 * CH4_EF * CH4_GWP
    ghg_emission_data_stationary_comb_3_3=qty_stationary_comb_3 * N2O_EF * N2O_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for Captive Power Generation from combustion of fossil fuel HSD (diesel generator): {ghg_emission_data_stationary_comb_1_1:.5f}")
        st.write(f"CH4 Emission for Captive Power Generation from combustion of fossil fuel HSD (diesel generator): {ghg_emission_data_stationary_comb_1_2:.5f}")
        st.write(f"N2O Emission for Captive Power Generation from combustion of fossil fuel HSD (diesel generator): {ghg_emission_data_stationary_comb_1_3:.5f}")
        st.write(f"CO2 Emission for LPG consumption in canteen: {ghg_emission_data_stationary_comb_2_1:.5f}")
        st.write(f"CH4 Emission for LPG consumption in canteen: {ghg_emission_data_stationary_comb_2_2:.5f}")
        st.write(f"N2O Emission for LPG consumption in canteen: {ghg_emission_data_stationary_comb_2_3:.5f}")
        st.write(f"CO2 Emission for LPG consumption in laboratories: {ghg_emission_data_stationary_comb_3_1:.5f}")
        st.write(f"CH4 Emission for LPG consumption in laboratories: {ghg_emission_data_stationary_comb_3_2:.5f}")
        st.write(f"N2O Emission for LPG consumption in laboratories: {ghg_emission_data_stationary_comb_3_3:.5f}")

    with col8:
        total_ghg_data_stationary_comb_1=ghg_emission_data_stationary_comb_1_1+ghg_emission_data_stationary_comb_1_2+ghg_emission_data_stationary_comb_1_3
        total_ghg_data_stationary_comb_2=ghg_emission_data_stationary_comb_2_1+ghg_emission_data_stationary_comb_2_2+ghg_emission_data_stationary_comb_2_3
        total_ghg_data_stationary_comb_3=ghg_emission_data_stationary_comb_3_1+ghg_emission_data_stationary_comb_3_2+ghg_emission_data_stationary_comb_3_3
        total_ghg_staionary_compbustion=total_ghg_data_stationary_comb_1+total_ghg_data_stationary_comb_2+total_ghg_data_stationary_comb_3
        
        st.write(f"Total GHG Emission for Captive Power Generation from combustion of fossil fuel HSD (diesel generator): {total_ghg_data_stationary_comb_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for LPG consumption in canteen: {total_ghg_data_stationary_comb_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for LPG consumption in laboratories: {total_ghg_data_stationary_comb_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Stationary Combustion: {total_ghg_staionary_compbustion:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places


    ############################Mobile Combustion####################################
        
    st.subheader(f"Mobile Combustion GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_mobile_comb_1 = st.text_input(f"Data for Mobile Combustion", value="Transportation: In-campus bus fleet used to travel the students between the buildings", key="Mobile_Combustion_data1", disabled=True)
            
        # data_mobile_comb_2 = st.text_input(f"Data for Mobile Combustion", value="Diesel2", key="Mobile_Combustion_data2", disabled=True) 
        # data_mobile_comb_3 = st.text_input(f"Data for Mobile Combustion", value="Diesel3", key="Mobile_Combustion_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_mobile_comb_1 = st.number_input(f"Quantity for Transportation", key="Mobile_Combustion_qty1")  # Add unique key for each activity's quantity input
        
        # qty_mobile_comb_2 = st.number_input(f"Quantity for Diesel2", key="Mobile_Combustion_qty2")  # Add unique key for each activity's quantity input
        # qty_mobile_comb_3 = st.number_input(f"Quantity for Diesel3", key="Mobile_Combustion_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_mobile_comb_1_1 = qty_mobile_comb_1 * CO2_EF * CO2_GWP
    ghg_emission_data_mobile_comb_1_2 = qty_mobile_comb_1 * CH4_EF * CH4_GWP
    ghg_emission_data_mobile_comb_1_3 = qty_mobile_comb_1 * N2O_EF * N2O_GWP
    # ghg_emission_data_mobile_comb_2_1=qty_mobile_comb_2 * CO2e_EF * CO2e_GWP
    # ghg_emission_data_mobile_comb_3_1=qty_mobile_comb_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for Transportation: {ghg_emission_data_mobile_comb_1_1:.5f}")
        st.write(f"CH4 Emission for Transportation: {ghg_emission_data_mobile_comb_1_2:.5f}")
        st.write(f"N2O Emission for Transportation: {ghg_emission_data_mobile_comb_1_3:.5f}")
        # st.write(f"CO2e Emission for Diesel2: {ghg_emission_data_mobile_comb_2_1:.5f}")
        # st.write(f"CO2 Emission for Diesel3: {ghg_emission_data_mobile_comb_3_1:.5f}")
    with col8:
        total_ghg_data_mobile_comb_1=ghg_emission_data_mobile_comb_1_1+ghg_emission_data_mobile_comb_1_2+ghg_emission_data_mobile_comb_1_3
        # total_ghg_data_mobile_comb_2=ghg_emission_data_mobile_comb_2_1
        # total_ghg_data_mobile_comb_3=ghg_emission_data_mobile_comb_3_1
        # total_ghg_mobile_compbustion=total_ghg_data_mobile_comb_1+total_ghg_data_mobile_comb_2+total_ghg_data_mobile_comb_3
        total_ghg_mobile_compbustion=total_ghg_data_mobile_comb_1
        
        st.write(f"Total GHG Emission for Transportation: {total_ghg_data_mobile_comb_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        # st.write(f"Total GHG Emission for Diesel2: {total_ghg_data_mobile_comb_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        # st.write(f"Total GHG Emission for Diesel3: {total_ghg_data_mobile_comb_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Mobile Combustion: {total_ghg_mobile_compbustion:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places

    
    ############################Leakage of Refrigerant####################################
        
    st.subheader(f"Leakage of Refrigerant/ Air Condition GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_leakage_of_refrigerator_1 = st.text_input(f"Data for Leakage of Refrigerant/ Air Conditioner", value="R-404a", key="leakage_of_refrigerator_data1", disabled=True)
            
        data_leakage_of_refrigerator_2 = st.text_input(f"Data for Leakage of Refrigerant/ Air Conditioner", value="R-410a", key="leakage_of_refrigerator_data2", disabled=True) 
        data_leakage_of_refrigerator_3 = st.text_input(f"Data for Leakage of Refrigerant/ Air Conditioner", value="R-407c", key="leakage_of_refrigerator_data3", disabled=True)
        data_leakage_of_refrigerator_4 = st.text_input(f"Data for Leakage of Refrigerant/ Air Conditioner", value="HFC-134a", key="leakage_of_refrigerator_data4", disabled=True) 
        data_leakage_of_refrigerator_5 = st.text_input(f"Data for Leakage of Refrigerant/ Air Conditioner", value="HCFC-22", key="leakage_of_refrigerator_data5", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_leakage_of_refrigerator_1 = st.number_input(f"Quantity for R-404a", key="leakage_of_refrigerator_qty1")  # Add unique key for each activity's quantity input
            
        qty_leakage_of_refrigerator_2 = st.number_input(f"Quantity for R-410a", key="leakage_of_refrigerator_qty2")  # Add unique key for each activity's quantity input
        qty_leakage_of_refrigerator_3 = st.number_input(f"Quantity for R-407c", key="leakage_of_refrigerator_qty3")  # Add unique key for each activity's quantity input
        qty_leakage_of_refrigerator_4 = st.number_input(f"Quantity for HFC-134a", key="leakage_of_refrigerator_qty4")  # Add unique key for each activity's quantity input
        qty_leakage_of_refrigerator_5 = st.number_input(f"Quantity for HCFC-22", key="leakage_of_refrigerator_qty5")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_leakage_of_refrigerator_1_1 = qty_leakage_of_refrigerator_1 * R_404a_EF * R_404a_GWP
    ghg_emission_data_leakage_of_refrigerator_2_1=qty_leakage_of_refrigerator_2 * R_410a_EF * R_410a_GWP
    ghg_emission_data_leakage_of_refrigerator_3_1=qty_leakage_of_refrigerator_3 * R_407c_EF * R_407c_GWP
    ghg_emission_data_leakage_of_refrigerator_4_1=qty_leakage_of_refrigerator_4 * HFC_134a_EF * HFC_134a_GWP
    ghg_emission_data_leakage_of_refrigerator_5_1=qty_leakage_of_refrigerator_5 * HCFC_22_EF * HCFC_22_GWP

                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for R-404a: {ghg_emission_data_leakage_of_refrigerator_1_1:.5f}")
        st.write(f"CO2e Emission for R-410a: {ghg_emission_data_leakage_of_refrigerator_2_1:.5f}")
        st.write(f"CO2 Emission for R-407c: {ghg_emission_data_leakage_of_refrigerator_3_1:.5f}")
        st.write(f"HFC Emission for HFC-134a: {ghg_emission_data_leakage_of_refrigerator_4_1:.5f}")
        st.write(f"HFC Emission for HCFC-22: {ghg_emission_data_leakage_of_refrigerator_5_1:.5f}")

    with col8:
        total_ghg_data_leakage_of_refrigerator_1=ghg_emission_data_leakage_of_refrigerator_1_1
        total_ghg_data_leakage_of_refrigerator_2=ghg_emission_data_leakage_of_refrigerator_2_1
        total_ghg_data_leakage_of_refrigerator_3=ghg_emission_data_leakage_of_refrigerator_3_1
        total_ghg_data_leakage_of_refrigerator_4=ghg_emission_data_leakage_of_refrigerator_4_1
        total_ghg_data_leakage_of_refrigerator_5=ghg_emission_data_leakage_of_refrigerator_5_1
        total_ghg_leakage_of_refrigerator=total_ghg_data_leakage_of_refrigerator_1+total_ghg_data_leakage_of_refrigerator_2+total_ghg_data_leakage_of_refrigerator_3+total_ghg_data_leakage_of_refrigerator_4+total_ghg_data_leakage_of_refrigerator_5
        
        st.write(f"Total GHG Emission for R-404a: {total_ghg_data_leakage_of_refrigerator_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for R-410a: {total_ghg_data_leakage_of_refrigerator_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        st.write(f"Total GHG Emission for R-407c: {total_ghg_data_leakage_of_refrigerator_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(f"Total GHG Emission for HFC-134a: {total_ghg_data_leakage_of_refrigerator_4:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(f"Total GHG Emission for HCFC-22: {total_ghg_data_leakage_of_refrigerator_5:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired

        st.write(" ")
        
        st.write(f"Total GHG Emission for Leakage of Refrigerator/ Air Conditioner: {total_ghg_leakage_of_refrigerator:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places

        
    #################################Process Emission#######################################
        
    st.subheader(f"Process Emission GHG Emission Calculation Form")
    col5, col6 = st.columns(2)
    with col5:

        data_process_emission_1 = st.text_input(f"Data for Process Emission", value="Pasteurized Compost and Peat Moss (organic type) ", key="Process_Emission_data1", disabled=True)
            
        data_process_emission_2 = st.text_input(f"Data for Process Emission", value="Urea (synthetic type)", key="Process_Emission_data2", disabled=True) 
        # data_process_emission_3 = st.text_input(f"Data for Process Emission", value="Diesel3", key="Process_Emission_data3", disabled=True)
                # data = st.text_input(r"$\textsf{\Large Data for {activity}$", key=f"{activity}_data") 
            # r"$\textsf{\Large Select Department}$"# Add unique key for each activity's data input
    with col6:
        qty_process_emission_1 = st.number_input(f"Quantity for Pasteurized Compost and Peat Moss (organic type) ", key="Process_Emission_qty1")  # Add unique key for each activity's quantity input
            
        qty_process_emission_2 = st.number_input(f"Quantity for Urea (synthetic type)", key="Process_Emission_qty2")  # Add unique key for each activity's quantity input
        # qty_process_emission_3 = st.number_input(f"Quantity for Diesel3", key="Process_Emission_qty3")  # Add unique key for each activity's quantity input
    
    ghg_emission_data_process_emission_1_1 = qty_process_emission_1 * N2O_EF * N2O_GWP
    ghg_emission_data_process_emission_2_1 = qty_process_emission_2 * N2O_EF * N2O_GWP
    # ghg_emission_data_process_emission_2_1=qty_process_emission_2 * CO2e_EF * CO2e_GWP
    # ghg_emission_data_process_emission_3_1=qty_process_emission_3 * CO2_EF * CO2_GWP
                    
    col7, col8 = st.columns(2)
    with col7:
        st.write(f"CO2 Emission for Pasteurized Compost and Peat Moss (organic type) : {ghg_emission_data_process_emission_1_1:.5f}")
        # st.write(f"CH4 Emission for Diesel1: {ghg_emission_data_process_emission_1_2:.5f}")
        st.write(f"CO2e Emission for Urea (synthetic type): {ghg_emission_data_process_emission_2_1:.5f}")
        # st.write(f"CO2 Emission for Diesel3: {ghg_emission_data_process_emission_3_1:.5f}")
    with col8:
        total_ghg_data_process_emission_1=ghg_emission_data_process_emission_1_1
        total_ghg_data_process_emission_2=ghg_emission_data_process_emission_2_1
        # total_ghg_data_process_emission_3=ghg_emission_data_process_emission_3_1
        total_ghg_process_emission=total_ghg_data_process_emission_1+total_ghg_data_process_emission_2
        
        st.write(f"Total GHG Emission for Pasteurized Compost and Peat Moss (organic type) : {total_ghg_data_process_emission_1:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        
        st.write(f"Total GHG Emission for Urea (synthetic type): {total_ghg_data_process_emission_2:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
            
        # st.write(f"Total GHG Emission for Diesel3: {total_ghg_data_process_emission_3:.5f}", style="font-size: 18px; font-weight: bold")  # Adjust font size and weight as desired
        st.write(" ")
        
        st.write(f"Total GHG Emission for Process Emission: {total_ghg_process_emission:.5f}", style="font-size: 25px; font-weight: bold")  # Adjust font size and weight as desired

            # st.write(f"{total_ghg:.2f}", style="font-size: 18px")  # Format emission value with 2 decimal places
            
            
            
    col9, col10, col11 =st.columns(3)
    with col10:
        total_scope1_emission=total_ghg_staionary_compbustion+total_ghg_mobile_compbustion+total_ghg_leakage_of_refrigerator+total_ghg_process_emission
        create_big_box(total_scope1_emission)
    submit_button = st.button(label='Submit')
    if submit_button:
        st.success('Scope 1 Data submitted successfully!')


   

if __name__ == "__main__":
    scope1()

