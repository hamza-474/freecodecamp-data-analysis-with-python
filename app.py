import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Data Analysis with Python — Hamza Madni", layout="wide")
st.title("📊 Data Analysis with Python — Live Projects")
st.write("Hamza Madni's five freeCodeCamp **Data Analysis with Python** certification projects, running live. "
         "Pick a project from the sidebar and press **Run**.")
st.markdown("🎓 Certificate: https://www.freecodecamp.org/certification/fcc-e2b594ad-6279-46f6-b5e7-f344e25e0c82/data-analysis-with-python-v7")
st.markdown("💻 Code: https://github.com/hamza-474/freecodecamp-data-analysis-with-python")

project = st.sidebar.selectbox("Choose a project", [
    "Mean-Variance-Standard Deviation Calculator",
    "Demographic Data Analyzer",
    "Medical Data Visualizer",
    "Page View Time Series Visualizer",
    "Sea Level Predictor",
])

if project == "Mean-Variance-Standard Deviation Calculator":
    st.header(project)
    st.write("Type 9 numbers and the calculator works out mean, variance, standard deviation, max, min and sum — by row, by column, and overall.")
    nums = st.text_input("9 numbers (comma separated)", "0,1,2,3,4,5,6,7,8")
    if st.button("Run"):
        try:
            values = [float(x) for x in nums.split(",")]
            from mean_var_std import calculate
            result = calculate(values)
            for key, val in result.items():
                st.write(f"**{key}:** {val}")
        except Exception as e:
            st.error(str(e))

elif project == "Demographic Data Analyzer":
    st.header(project)
    st.write("Answers ten questions about the US census dataset (32,561 people) using Pandas.")
    if st.button("Run"):
        from demographic_data_analyzer import calculate_demographic_data
        r = calculate_demographic_data(print_data=False)
        st.write("**Number of each race:**")
        st.write(r["race_count"])
        st.write(f"**Average age of men:** {r['average_age_men']}")
        st.write(f"**Percentage with Bachelors degrees:** {r['percentage_bachelors']}%")
        st.write(f"**Higher education, earn >50K:** {r['higher_education_rich']}%")
        st.write(f"**Without higher education, earn >50K:** {r['lower_education_rich']}%")
        st.write(f"**Minimum work hours/week:** {r['min_work_hours']}")
        st.write(f"**Rich among those who work the fewest hours:** {r['rich_percentage']}%")
        st.write(f"**Country with highest percentage of rich:** {r['highest_earning_country']} ({r['highest_earning_country_percentage']}%)")
        st.write(f"**Top occupation in India (>50K):** {r['top_IN_occupation']}")

elif project == "Medical Data Visualizer":
    st.header(project)
    st.write("Charts from 70,000 medical examination records — how body features relate to cardiovascular disease.")
    if st.button("Run"):
        from medical_data_visualizer import draw_cat_plot, draw_heat_map
        st.pyplot(draw_cat_plot())
        st.pyplot(draw_heat_map())

elif project == "Page View Time Series Visualizer":
    st.header(project)
    st.write("Daily freeCodeCamp forum page views from 2016 to 2019, drawn three ways.")
    if st.button("Run"):
        from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
        st.pyplot(draw_line_plot())
        st.pyplot(draw_bar_plot())
        st.pyplot(draw_box_plot())

elif project == "Sea Level Predictor":
    st.header(project)
    st.write("Sea level measurements since 1880, with a prediction line out to the year 2050.")
    if st.button("Run"):
        from sea_level_predictor import draw_plot
        ax = draw_plot()
        st.pyplot(ax.figure)
