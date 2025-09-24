import streamlit as st

from app.crud.database import get_entries_by_year_range
from app.utils.transformers import to_dataframe
from ui.utils.visualization import build_visualization


def display_multi_year():
    start_year, end_year = st.slider(
        "Select Year Range",
        min_value=2013,
        max_value=2024,
        value=(2013, 2024)
    )

    entries = get_entries_by_year_range(start_year=start_year, end_year=end_year)
    df = to_dataframe(entries=entries)

    if st.checkbox(label="Show Data", value=False, width="content"):
        st.markdown(
            f"<h4 style='text-align: center;'>Data for {start_year}-{end_year}</h4>",
            unsafe_allow_html=True
        )
        st.dataframe(df)
        st.write("---")

    st.markdown(
        f"<h4 style='text-align: center;'>Visualization for {start_year}-{end_year}</h4>",
        unsafe_allow_html=True
    )

    categorical_cols = [
        col.title() for col in df.columns if col not in [
            "killed",
            "wounded",
            "names",
            "city",
            "id",
            "date",
            "sources",
        ]
    ]
    x_axis = st.selectbox(
        label="Select X-axis", options=categorical_cols,
        index=categorical_cols.index("month") if "month" in categorical_cols else 0,
        width=220,
    ).lower()

    plot_df = df.groupby(x_axis)[["killed", "wounded"]].sum().reset_index()

    # Filter out some charts that do not work
    if x_axis == "year":
        chart_options = ["Bar", "Pie", "Heat Map", "Scatter Plot", "All"]  # remove Area Map
    elif x_axis == "month" or x_axis == "day":
        chart_options = ["Bar", "Pie", "Area", "Scatter Plot", "All"]  # remove Heat Map
    else:
        chart_options = ["Bar", "Pie", "Area", "Heat Map", "Scatter Plot", "All"]

    chart_type = st.radio(label="Select Chart Type", options=chart_options, horizontal=True)

    charts_to_show = chart_options[:len(chart_options) - 1] if chart_type == "All" else [chart_type]

    for chart_name in charts_to_show:
        st.write("---")

        chart = build_visualization(df=plot_df, x_axis=x_axis, keyword=chart_name)
        st.altair_chart(chart, use_container_width=True)

        if chart_name == "Pie":
            total = plot_df["killed"].sum() + plot_df["wounded"].sum()
            st.markdown(
                f"<h4 style='text-align: center;'>Total Killed and Wounded: {total}</h4>",
                unsafe_allow_html=True
            )
