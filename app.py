import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Talking Rabbitt AI", layout="wide")

st.title("🐰 Talking Rabbitt AI")
st.subheader("Talk to your business data")
st.write("Upload a CSV dataset and ask a simple business question.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Data Preview")
    st.dataframe(df.head())

    question = st.text_input("Ask a question", placeholder="Which region had the highest revenue?")

    if question:
        q = question.lower()

        if "region" in q and "highest" in q and "revenue" in q:
            result = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
            top_region = result.index[0]
            top_value = result.iloc[0]

            st.success(f"{top_region} region had the highest revenue: {top_value}")

            st.write("### Revenue by Region")
            fig, ax = plt.subplots()
            result.plot(kind="bar", ax=ax)
            ax.set_ylabel("Revenue")
            ax.set_title("Revenue by Region")
            st.pyplot(fig)
        else:
            st.warning("Try asking: Which region had the highest revenue?")
else:
    st.info("Please upload a CSV file to continue.")
