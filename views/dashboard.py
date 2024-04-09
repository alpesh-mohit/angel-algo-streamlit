import streamlit as st

from libs.auth import get_authenticated_user
from tasks.background_task import BackgroundTask
from time import sleep
from libs.risk_reward import load_data

def Dashboard():
    st.title("Auto Square Off Algo")
    st.write("This tool will auto square off based on MTM")

    authenticated_user = get_authenticated_user("dashboard")

    background_task = BackgroundTask(authenticated_user, st.session_state)

    thread_button = st.button("Start")

    if thread_button:
        background_task.run_thread()

    # Load existing values from JSON (or set defaults)
    data = load_data()
    stoploss = data.get("stoploss")
    target = data.get("target")

    # Display current stoploss and target values (optional)
    if stoploss is not None and target is not None:
        st.write(f":red[SL: {stoploss}]")
        st.write(f":green[TGT: {target}]")

    if 'pnl' not in st.session_state:
        st.session_state['pnl'] = 0

    pnl_text = st.empty()

    while True:
        pnl = st.session_state['pnl']

        if pnl < 0:
            pnl_text.write(f":red[P&L: {pnl}]")
        elif pnl > 0:
            pnl_text.write(f":green[P&L: {pnl}]")
        else:
            pnl_text.write(f":black[P&L: {pnl}]")
        
        sleep(1)