import streamlit as st
import threading

from datetime import datetime
from time import sleep
from libs.auth import is_authenticated
from token_manager.angel_one_token_manager import AngelOneTokenManager
from views.dashboard import Dashboard
from views.login import Login
from views.risk_reward import RiskReward
from views.settings import Settings

def async_task():
    try:
        token_manager = AngelOneTokenManager()

        print(token_manager)

        while True:
            # Your square-off logic goes here
            print("datetime", datetime.now())
            sleep(1)  # Replace with your desired sleep time
    except Exception as e:
        print(e)

def start_background_task():
    # Use a global flag to track if the process is already running
    if not getattr(threading, "background_process_running", False):
        print("starting...")
        thread = threading.Thread(target=async_task)
        thread.daemon = True
        thread.start()
        setattr(threading, "background_process_running", True)

if __name__ == "__main__":
    # Start the background task only once
    start_background_task()

    # Authentication and Page Selection
    authenticated = is_authenticated()

    if not authenticated:
        page = Login()
    else:
        # User authenticated - Choose between Dashboard and Settings
        page_selection = st.sidebar.selectbox("Select Page", ["Dashboard", "Risk Reward", "Settings"])

        if page_selection == "Dashboard":
            page = Dashboard()
        elif page_selection == "Settings":
            page = Settings()
        elif page_selection == "Risk Reward":
            page = RiskReward()