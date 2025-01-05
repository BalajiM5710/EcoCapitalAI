import streamlit as st
import pandas as pd

# Page Configurations
st.set_page_config(
    page_title="Green Finance Optimization Platform",
    page_icon="🌱",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Submit Project", "Investor Dashboard", "Evaluation Results"])

# Dummy Data
dummy_projects = [
    {"Name": "Project A", "Goal Match": "90%", "Problem Solved": "85%", "Budget": "80%", "Timeline": "100%"},
    {"Name": "Project B", "Goal Match": "70%", "Problem Solved": "95%", "Budget": "90%", "Timeline": "90%"},
    {"Name": "Project C", "Goal Match": "60%", "Problem Solved": "80%", "Budget": "70%", "Timeline": "85%"}
]
dummy_layer2 = [
    {"Name": "Project A", "Risk Score": "Low", "ESG Score": "95%", "Final Rank": 1},
    {"Name": "Project B", "Risk Score": "Medium", "ESG Score": "88%", "Final Rank": 2},
    {"Name": "Project C", "Risk Score": "High", "ESG Score": "75%", "Final Rank": 3}
]

# Home Page
if page == "Home":
    st.title("🌱 Green Finance Optimization Platform")
    st.markdown("""
        Welcome to the Green Finance Optimization Platform!  
        This platform helps investors and funding organizations prioritize and optimize their green finance investments using AI-driven insights.  
        ### Key Features:
        - Submit project proposals for evaluation.
        - View and filter projects aligned with sustainability goals.
        - Analyze and compare shortlisted projects based on key metrics.
    """)

# Submit Project Page
elif page == "Submit Project":
    st.title("Submit Your Project")
    with st.form("project_form"):
        st.subheader("Project Details")
        name = st.text_input("Project Name")
        goals = st.text_area("Sustainability Goals")
        budget = st.number_input("Requested Budget (in USD)", min_value=0)
        timeline = st.slider("Timeline (in months)", 1, 60)
        problems_solved = st.text_area("Problems Solved")
        esg_score = st.slider("ESG Score", 0, 100)
        submit = st.form_submit_button("Submit")
        if submit:
            st.success(f"Project '{name}' submitted successfully!")

# Investor Dashboard
elif page == "Investor Dashboard":
    st.title("Investor Dashboard")
    st.sidebar.subheader("Filters")
    goal_filter = st.sidebar.text_input("Sustainability Goal Filter (Keyword)")
    budget_filter = st.sidebar.slider("Budget Range (in USD)", 0, 100000, (0, 100000))
    timeline_filter = st.sidebar.slider("Timeline Range (in months)", 1, 60, (1, 60))

    st.subheader("Filtered Projects")
    filtered_projects = pd.DataFrame(dummy_projects)
    st.dataframe(filtered_projects)

# Evaluation Results
elif page == "Evaluation Results":
    st.title("Evaluation Results")
    st.subheader("Layer 1: Shortlisted Projects")
    layer1_results = pd.DataFrame(dummy_projects)
    st.dataframe(layer1_results)

    st.subheader("Layer 2: Final Evaluation")
    layer2_results = pd.DataFrame(dummy_layer2)
    st.dataframe(layer2_results)

    st.markdown("### Final Recommendation")
    best_project = dummy_layer2[0]  # Assuming Project A is the best
    st.write(f"**Recommended Project:** {best_project['Name']}")
    st.write(f"**Risk Score:** {best_project['Risk Score']}")
    st.write(f"**ESG Score:** {best_project['ESG Score']}")
    st.write(f"**Final Rank:** {best_project['Final Rank']}")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Green Finance Optimization Platform © 2025")
