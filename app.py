import streamlit as st
import pandas as pd
import random
import time
import plotly.express as px

# Page Configurations
st.set_page_config(
    page_title="GreenVestify",
    page_icon="🌱",
    layout="wide"
)

# Global State to Store Project Data
if "projects" not in st.session_state:
    # Adding dummy initial projects
    st.session_state["projects"] = [
        {
            "Name": "Solar Power for Rural Areas",
            "Goals": "To provide renewable solar energy to off-grid rural communities.",
            "Budget": 1000000,
            "Timeline": 24,
            "Problems Solved": "Access to sustainable energy, reduction in dependency on fossil fuels.",
            "ESG Score": 85
        },
        {
            "Name": "Green Urban Farming",
            "Goals": "To promote urban farming using sustainable techniques in city spaces.",
            "Budget": 500000,
            "Timeline": 18,
            "Problems Solved": "Local food production, reduction in carbon footprint, and urban waste recycling.",
            "ESG Score": 90
        },
        {
            "Name": "Eco-Friendly Packaging Solutions",
            "Goals": "To reduce single-use plastic packaging by introducing biodegradable alternatives.",
            "Budget": 800000,
            "Timeline": 12,
            "Problems Solved": "Reducing plastic waste and promoting circular economy.",
            "ESG Score": 92
        }
    ]

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Add Project", "Dashboard"])

# Home Page
if page == "Home":
    st.title("🌱 GreenVestify")
    st.markdown("""
        Welcome to **GreenVestify**!  
        This platform empowers investors and organizations to prioritize and optimize their green finance investments.
        
        ### Features:
        - Add and manage project details.
        - AI-powered ESG score fetching.
        - Evaluate projects with detailed dashboards.
    """)

# Add Project Page
elif page == "Add Project":
    st.title("Add a New Project")
    with st.form("project_form"):
        st.subheader("Project Details")
        name = st.text_input("Project Name")
        goals = st.text_area("Sustainability Goals")
        budget = st.number_input("Requested Budget (in USD)", min_value=0, step=1000)
        timeline = st.slider("Timeline (in months)", 1, 60)
        problems_solved = st.text_area("Problems Solved")
        
        # ESG Score Input
        col1, col2 = st.columns([2, 1])
        with col1:
            esg_score = st.number_input("ESG Score (Optional)", min_value=0, max_value=100, step=1)
        with col2:
            st.warning("Click the button below to fetch the ESG score using AI.")

        submit = st.form_submit_button("Submit Project")

    # AI Fetch Button - Outside the form
    if st.button("AI Fetch ESG Score"):
        with st.spinner("Fetching ESG score..."):
            time.sleep(2)  # Simulate processing delay
        esg_score = random.randint(50, 100)  # Generate random ESG score
        st.success(f"AI-generated ESG Score: {esg_score}")

    # Submit the project when the submit button is pressed
    if submit:
        # Use the ESG score from the input or the AI-generated value
        if esg_score == 0:
            esg_score = random.randint(50, 100)  # If no ESG score is provided, use AI-generated one

        st.session_state["projects"].append({
            "Name": name,
            "Goals": goals,
            "Budget": budget,
            "Timeline": timeline,
            "Problems Solved": problems_solved,
            "ESG Score": esg_score
        })
        st.success(f"Project '{name}' added successfully!")

# Dashboard Page
elif page == "Dashboard":
    st.title("Project Evaluation Dashboard")

    # Convert Projects to DataFrame
    if st.session_state["projects"]:
        projects_df = pd.DataFrame(st.session_state["projects"])
        st.subheader("Layer 1 Results")
        st.write("### Shortlisted Projects")
        
        # Add Dummy Scores for Layer 1
        projects_df["Goal Match Score"] = [random.randint(70, 100) for _ in range(len(projects_df))]
        projects_df["Problem Solved Score"] = [random.randint(60, 100) for _ in range(len(projects_df))]
        projects_df["Budget Match Score"] = [random.randint(50, 90) for _ in range(len(projects_df))]
        
        st.dataframe(projects_df)

        # Bar Graph for Layer 1
        layer1_fig = px.bar(
            projects_df, 
            x="Name", 
            y=["Goal Match Score", "Problem Solved Score", "Budget Match Score"],
            barmode="group", 
            title="Layer 1 Evaluation Scores"
        )
        st.plotly_chart(layer1_fig, use_container_width=True)

        # Layer 2 Results
        st.subheader("Layer 2 Results")
        projects_df["Risk Score"] = [random.choice(["Low", "Medium", "High"]) for _ in range(len(projects_df))]
        projects_df["Final Score"] = projects_df[["Goal Match Score", "Problem Solved Score", "Budget Match Score"]].mean(axis=1).round(2)
        
        st.write("### Final Evaluations")
        st.dataframe(projects_df[["Name", "Risk Score", "ESG Score", "Final Score"]])

        # Bar Graph for Layer 2
        layer2_fig = px.bar(
            projects_df, 
            x="Name", 
            y="Final Score",
            color="Risk Score",
            title="Final Project Rankings"
        )
        st.plotly_chart(layer2_fig, use_container_width=True)

    else:
        st.warning("No projects added yet. Please add projects from the 'Add Project' page.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("GreenVestify © 2025")
