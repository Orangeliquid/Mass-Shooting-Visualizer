import streamlit as st

from ui.information import display_information
from ui.single_year import display_single_year
from ui.multi_year import display_multi_year

st.set_page_config(page_title="Mass Shooting Data Visualizer", page_icon="assets/orange_alien.ico")


def main():

    # Header Creation
    st.markdown(
        "<h1 style='color:#FFA500; text-align: center; '>ORANGELIQUID</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='color:#4227F5; text-align: center; text-style: italic; padding-bottom: 40px;'>"
        "<i>MASS SHOOTING VISUALIZER</i></h2>",
        unsafe_allow_html=True
    )

    if "page" not in st.session_state:
        st.session_state.page = "information"

    # Page Button Creation
    single_year_col, multi_year_col, info_col = st.columns([1, 1, 1])
    with single_year_col:
        if st.button(label="Single Year Data", type="primary", width="stretch"):
            st.session_state.page = "single_year_data"

    with multi_year_col:
        if st.button(label="Multi-Year Data", type="primary", width="stretch"):
            st.session_state.page = "multi_year_data"

    with info_col:
        if st.button(label="Information", type="primary", width="stretch"):
            st.session_state.page = "information"

    if st.session_state.page == "information":
        display_information()
    elif st.session_state.page == "single_year_data":
        display_single_year()
    elif st.session_state.page == "multi_year_data":
        display_multi_year()


if __name__ == '__main__':
    main()
