# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import necessary libraries
from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code

# Function to demonstrate working with DataFrames in Streamlit
def data_frame_demo():
    # Caching the data retrieval to improve performance
    @st.cache_data
    def get_UN_data():
        # URL for the dataset
        AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        # Reading the CSV file into a Pandas DataFrame
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        # Attempting to retrieve and process the data
        df = get_UN_data()
        print("HKHKHK")
        print(df)
        # Selecting countries using a multiselect widget
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        # Displaying an error message if no countries are selected
        if not countries:
            st.error("Please select at least one country.")
        else:
            # Processing and displaying the selected data
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            # Reshaping the data for Altair chart
            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            # Creating an Altair area chart
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            # Displaying the Altair chart in Streamlit
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        # Handling connection errors and displaying an error message
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

# Setting Streamlit page configuration
st.set_page_config(page_title="DataFrame Demo", page_icon="📊")
# Displaying the main title and introduction
st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)

# Calling the DataFrame demonstration function
data_frame_demo()

# Displaying the source code for the demonstration
show_code(data_frame_demo)
