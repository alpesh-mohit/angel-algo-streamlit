import streamlit as st

from libs.token_manager import validate_token_manager
    
def Settings():
    try:
        st.title("Settings")

        client_id = st.text_input(label="Client ID", type="default", key="client_id_input")
        totp_key = st.text_input(label="TOTP Key", type="password", key="totp_key_input")
        mpin = st.text_input(label="MPIN", type="password", key="mpin_input")
        api_key = st.text_input(label="API Key", type="default", key="api_key_input")
        api_secret = st.text_input(label="API Secret", type="password", key="api_secret_input")
        redirect_url = st.text_input(label="Redirect URL", type="default", key="redirect_url_input")
        submit = st.button(label="Authenticate", type="primary", key="login_submit_button")

        if submit:
            is_valid_api_details = validate_token_manager(
                client_id, totp_key, mpin, api_key, api_secret, redirect_url
            )

            if not is_valid_api_details:
                st.error("Invalid API Details.")
            else:
                st.success("Updated Successfully.")
    except Exception as e:
        st.error("Update failed. Invalid Credentials")