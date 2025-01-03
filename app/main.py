import os
import streamlit as st
import altair as alt

# @st.fragment(run_every="5s")
# def plot_line_chart(c):
#     data = c.query(
#         "SELECT * FROM vw_crypto_prices",
#         ttl=5
#     )
#     st.table(data)

@st.fragment(run_every="5s")
def plot_line_chart(c):
    data = c.query(
        "SELECT * FROM vw_crypto_prices",
        ttl=5
    )
    line = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x="created_at",
            y=alt.Y("price").scale(domain=(93000,94000)) # need to adjust the domain based on current price
        )
        .properties(width=800, height=400)
    )
    st.altair_chart(line)


if __name__ == '__main__':
    sql_conn = st.connection(
        "postgresql",
        type="sql",
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host = os.getenv("POSTGRES_HOST"),
        dialect = "postgresql",
    )

    st.title("Bitcoin price - Coingecko")
    plot_line_chart(sql_conn)