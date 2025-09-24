import altair as alt


def build_visualization(df, x_axis, keyword):
    plot_df = df

    if keyword == "Bar":
        chart = (
            alt.Chart(plot_df)
            .transform_fold(
                ["killed", "wounded"],
                as_=["variable", "value"]
            )
            .mark_bar()
            .encode(
                x=alt.X(x_axis, type="nominal", title=x_axis.capitalize()),
                y=alt.Y("value:Q", stack="zero", title="Total Killed and Wounded"),
                color=alt.Color("variable:N", title="Type"),
                tooltip=[x_axis, "variable:N", "value:Q"]
            )
        )
        return chart

    elif keyword == "Pie":
        pie_df = plot_df.copy()
        pie_df["total"] = pie_df["killed"] + pie_df["wounded"]

        chart = (
            alt.Chart(pie_df)
            .mark_arc(innerRadius=25)
            .encode(
                theta=alt.Theta("total:Q", title="Total killed and Wounded"),
                color=alt.Color(f"{x_axis}:N", title=x_axis.capitalize()),
                tooltip=[x_axis, "total:Q"]
            )
        )

        return chart

    elif keyword == "Area":
        chart = (
            alt.Chart(plot_df)
            .transform_fold(["killed", "wounded"], as_=["variable", "value"])
            .mark_area()
            .encode(
                x=alt.X(x_axis, title=x_axis.capitalize()),
                y=alt.Y("value:Q", title="Total Killed and Wounded"),
                color="variable:N",
                tooltip=[x_axis, "variable:N", "value:Q"]
            )
        )

        return chart

    elif keyword == "Heat Map":
        plot_df_melted = plot_df.melt(
            id_vars=[x_axis],
            value_vars=["killed", "wounded"],
            var_name="metric",
            value_name="value"
        )

        chart = (
            alt.Chart(plot_df_melted)
            .mark_rect()
            .encode(
                x=alt.X(x_axis, title=x_axis.capitalize()),
                y=alt.Y("metric:N", title="Metric"),
                color=alt.Color("value:Q", scale=alt.Scale(scheme="reds")),
                tooltip=[x_axis, "metric", "value"]
            )
        )

        return chart

    elif keyword == "Scatter Plot":
        chart = (
            alt.Chart(plot_df)
            .mark_circle(size=60)
            .encode(
                x="killed:Q",
                y="wounded:Q",
                color=alt.Color(f"{x_axis}:N", title=x_axis.capitalize()),
                tooltip=["killed:Q", "wounded:Q", x_axis]
            )
        )

        return chart
