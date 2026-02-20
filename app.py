import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("AI_Impact_on_Jobs_2030.csv")

st.title("Will Your Career Survive AI by 2030?")

st.write("Explore automation risk across 3,000 job profiles.")

# Slider for risk threshold
risk_threshold = st.slider(
    "Select Automation Risk Threshold",
    0.0, 1.0, 0.6
)

# Filter data
high_risk = df[df["Automation_Probability_2030"] > risk_threshold]

st.metric(
    "Jobs Above Selected Risk Level",
    len(high_risk)
)

if risk_threshold > 0.7:
    st.error("⚠ High Risk Threshold Selected — Significant Automation Exposure")
elif risk_threshold > 0.4:
    st.warning("Moderate Automation Risk Zone")
else:
    st.success("Low Automation Risk Zone")

# Show distribution
fig, ax = plt.subplots()
ax.hist(df["Automation_Probability_2030"], bins=30)
ax.set_title("Automation Probability Distribution")
ax.set_xlabel("Automation Probability")
ax.set_ylabel("Number of Profiles")

st.pyplot(fig)

# Show top future stable jobs
df["Future_Stability_Score"] = (
    (1 - df["Automation_Probability_2030"]) * 0.6 +
    df["Tech_Growth_Factor"] * 0.4
)

st.subheader("Top 5 Most Future-Stable Profiles")
st.dataframe(
    df.sort_values("Future_Stability_Score", ascending=False)
      .head(5)
)

