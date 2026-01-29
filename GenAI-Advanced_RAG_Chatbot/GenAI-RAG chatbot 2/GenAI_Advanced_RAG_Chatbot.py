import streamlit as st
import pandas as pd
import altair as alt

# Establish Snowflake session (trial/community)
session = st.connection("snowflake").session()

# Create tabs
tab1, tab2 = st.tabs(["Data & Plots", "RAG App"])

# -------------------------------
# Tab 1: Data and Plots
# -------------------------------
with tab1:
    st.title("Customer Sentiment and Delivery Analysis")

    # Data loading function
    @st.cache_data
    def load_data():
        query_reviews = """
        SELECT
            *
        FROM
            REVIEWS_WITH_SENTIMENT
        """
        return session.sql(query_reviews).to_pandas()

    # Load data
    df = load_data()

    # Average sentiment by product
    st.header("Average Sentiment by Product")
    avg_sentiment_product = df.groupby("PRODUCT")["SENTIMENT_SCORE"].mean().reset_index()

    chart1 = (
        alt.Chart(avg_sentiment_product)
        .mark_bar(color="skyblue")
        .encode(
            x=alt.X("SENTIMENT_SCORE:Q", title="Sentiment Score"),
            y=alt.Y("PRODUCT:N", sort="-x", title="Product"),
            tooltip=["PRODUCT", "SENTIMENT_SCORE"]
        )
    )
    st.altair_chart(chart1, use_container_width=True)

    # Filter by product selection
    product = st.selectbox("Choose a product", ["All Products"] + list(df["PRODUCT"].unique()))

    if product != "All Products":
        filtered_data = df[df["PRODUCT"] == product]
    else:
        filtered_data = df

    # Display combined dataset
    st.subheader(f"📁 Reviews for {product}")
    st.dataframe(filtered_data)

    # Average sentiment by delivery status
    st.header(f"Average Sentiment by Delivery Status for {product}")
    avg_sentiment_status = filtered_data.groupby("STATUS")["SENTIMENT_SCORE"].mean().reset_index()

    chart2 = (
        alt.Chart(avg_sentiment_status)
        .mark_bar(color="slateblue")
        .encode(
            x=alt.X("SENTIMENT_SCORE:Q", title="Sentiment Score"),
            y=alt.Y("STATUS:N", sort="-x", title="Delivery Status"),
            tooltip=["STATUS", "SENTIMENT_SCORE"]
        )
    )
    st.altair_chart(chart2, use_container_width=True)

# -------------------------------
# Tab 2: RAG App
# -------------------------------
with tab2:
    st.title("RAG App")

    # Input box for user prompt
    prompt = st.text_input("Enter your query:", value="goggles")

    if prompt:
        if st.button("Run Query"):
            # Search directly in REVIEWS_WITH_SENTIMENT table
            query = f"""
            SELECT REVIEW_TEXT, PRODUCT
            FROM REVIEWS_WITH_SENTIMENT
            WHERE REVIEW_TEXT ILIKE '%{prompt}%'
            LIMIT 3
            """
            try:
                search_df = session.sql(query).to_pandas()
                if search_df.empty:
                    st.warning(f"No reviews found for keyword: {prompt}. Try another keyword like 'delivery' or 'excellent'.")
                else:
                    for _, row in search_df.iterrows():
                        st.write(f"**{row['REVIEW_TEXT']}**")
                        st.caption(row['PRODUCT'])
                        st.write('---')
            except Exception as e:
                st.error(f"Query failed: {e}")
