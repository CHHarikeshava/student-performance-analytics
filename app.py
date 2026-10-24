import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analytics System")
st.write("Analyze student marks, grades, and academic performance.")

uploaded_file = st.file_uploader(
    "Upload your students.csv file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Student Data")
    st.dataframe(df, use_container_width=True)

    st.subheader("Dataset Summary")
    st.write("Total students:", len(df))

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:
        st.subheader("Numerical Statistics")
        st.dataframe(df[numeric_columns].describe())

        selected_column = st.selectbox(
            "Select a column to visualize",
            numeric_columns
        )

        fig, ax = plt.subplots()
        df[selected_column].plot(
            kind="bar",
            ax=ax,
            title=f"{selected_column} by Student"
        )
        ax.set_xlabel("Student Index")
        ax.set_ylabel(selected_column)
        plt.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

    st.subheader("Download Data")
    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False),
        file_name="student_analysis.csv",
        mime="text/csv"
    )

else:
    st.info("Upload your students.csv file to begin analysis.")
