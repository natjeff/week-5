import streamlit as st
import plotly.express as px
from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')



st.write("Did children in third class have lower survival rates compared to children in higher classes?")
'''
# Titanic Visualization 1

'''
)
# Generate and display the figure
def visualize_demographic(results: pd.DataFrame):
    """
    Creates a Plotly visualization to compare survival rates of children
    across different passenger classes
    """
    
    children = results[results["AgeGroup"] == "Child"]

    # Plot survival rates by class and sex
    fig1 = px.bar(
        children,
        x="Pclass",
        y="survival_rate",
        color="Sex",
        barmode="group",
        labels={"survival_rate": "Survival Rate", "Pclass": "Passenger Class"},
        title="Survival Rates of Children Across Classes by Sex"
    )
    return fig1

df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')
results = survival_demographics(df)

# Display Fig 1
fig1 = visualize_demographic(results)
st.plotly_chart(fig1, use_container_width=True)





st.write("Did larger families in lower classes tend to pay less per person compared to smaller families or higher classes?")

'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
def visualize_families(results: pd.DataFrame):
    """
    Create a Plotly visualization to explore whether larger families
    in lower passenger classes paid less on average per person
    compared to smaller families or higher classes.
    """
    fig2 = px.line(
        results,
        x="family_size",
        y="avg_fare",
        color="Pclass",
        markers=True,
        labels={
            "family_size": "Family Size",
            "avg_fare": "Average Fare",
            "Pclass": "Passenger Class"
        },
        title="Average Fare by Family Size Across Passenger Classes"
    )
    return fig2

df = pd.read_csv("https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv")
family_results = family_groups(df)

fig2 = visualize_families(family_results)
st.plotly_chart(fig2, use_container_width=True)





"""
st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)
"""