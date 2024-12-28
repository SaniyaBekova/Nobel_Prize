import pandas as pd
import plotly.express as px

# Load the dataset
nobel_df = pd.read_csv("nobel_prize.csv")

# Prepare data: Aggregate laureates by country of birth
nobel_country_counts = nobel_df['birth_place_country'].value_counts().reset_index()
nobel_country_counts.columns = ['Country', 'Laureates']

# Create the choropleth map
fig = px.choropleth(
    nobel_country_counts,
    locations="Country",
    locationmode="country names",
    color="Laureates",
    color_continuous_scale="Blues",
    title="Nobel Laureates by Country of Birth",
    labels={"Laureates": "Number of Laureates"}
)

# Show the interactive map
fig.show()

# Save the map as an HTML file
fig.write_html("nobel_laureates_map.html")
