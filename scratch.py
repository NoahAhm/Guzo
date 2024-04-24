import streamlit as st
from main import main
from home import display_homepage
from news import display_news
from location import display_map

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def show_login_signup():
    """Display login and signup options."""
    st.markdown("""
                <div style="text-align: center";>
                <h1 style="font-size: 66px;"> Guz0  ༘✈︎ - - -📍 </hi>
                </div>
                """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Sign Up", "Login"])

    with tab1:
        st.header("Sign Up")
        username_signup = st.text_input("Choose a Username", key="signup_username")
        password_signup = st.text_input("Choose a Password", type="password", key="signup_password")
        
        if st.button("Sign Up"):
            if username_signup in st.session_state.users:
                st.error("Username already exists. Please choose a different username.")
            elif username_signup and password_signup:
                st.session_state.users[username_signup] = password_signup
                st.success("You have successfully signed up. Please log in with your new credentials.")
            else:
                st.error("Username and password cannot be empty.")
        

    with tab2:
        
        st.header("Login")
        username_login = st.text_input("Username", key="login_username")
        password_login = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if username_login in st.session_state.users and st.session_state.users[username_login] == password_login:
                st.session_state['authenticated'] = True
                st.session_state['username'] = username_login
                st.rerun()
            else:
                st.error("Incorrect Username or Password")
def my_app():
    st.markdown("""
                <div style="text-align: center";>
                <h1 style="font-size: 66px;"> Guzo ༘✈︎ - - -📍 </hi>
                </div>
                """, unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Home", "News", "Translation", "Destinations"])
    with tab1:
         
         display_homepage()
    with tab2:

        display_news()
        
    with tab3:
        main()

    with tab4:
        
        display_map()
        
    
if 'users' not in st.session_state:
    st.session_state['users'] = {
        "user1": "password1",
        "user2": "password2",
    }               
def main_app():
    """Main function to manage app flow based on login status."""
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if st.session_state['authenticated']:
        my_app()
    else:
        show_login_signup()
                
if __name__ == "__main__":
    main_app()