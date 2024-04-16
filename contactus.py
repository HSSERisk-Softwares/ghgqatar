import streamlit as st
import smtplib
from email.mime.text import MIMEText
import webbrowser
import io
from PIL import Image


st.set_page_config(layout="wide")
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
    page = "Contact Support"
 
    if st.sidebar.button("Dashboard"):
        webbrowser.open("http://localhost:8501")
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
    
    col1, col2, col3=st.columns(3)
    with col2:
        st.image('logo.png')
        st.title("Contact HSSERisk")

        # Taking inputs
        #email_sender = st.text_input('hsserisksoftware@gmail.com')
        email_sender = 'hsserisksoftwares@gmail.com'
        # email_receiver = st.text_input('hsserisksoftware@gmail.com')
        email_receiver = 'hsserisksoftwares@gmail.com'
        subject = st.text_input('Subject')
        body = st.text_area('Body')
        # password = st.text_input('jqcq vpes jbhb ctqu', type="password") 
        password = 'jqcq vpes jbhb ctqu'

        if st.button("Send Email"):
            try:
                msg = MIMEText(body)
                msg['From'] = email_sender
                msg['To'] = email_receiver
                msg['Subject'] = subject

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_sender, password)
                server.sendmail(email_sender, email_receiver, msg.as_string())
                server.quit()

                st.success('Email sent successfully!')
            except Exception as e:
                st.error(f"Error in sending the mail!: {e}")

if __name__ == "__main__":
    main()

