# GreenVestify

GreenVestify is an AI-powered platform designed to evaluate, prioritize, and optimize green finance investments. It empowers investors and funding organizations to allocate resources effectively, ensuring impactful and sustainable project funding. This demonstration app showcases a user-friendly interface for managing projects, analyzing their sustainability goals, and displaying evaluation metrics.

---

## Features

### 1. **Add New Projects**
- Investors or funding organizations can add project details such as:
  - **Name**: Project title.
  - **Goals**: Sustainability goals aligned with ESG principles.
  - **Budget**: Project funding requirements.
  - **Timeline**: Estimated project duration (in months).
  - **Problems Solved**: Description of the problems the project addresses.
  - **ESG Score**: Input manually or generate using the **AI Fetch** feature.

### 2. **AI ESG Score Fetching**
- Click the **AI Fetch ESG Score** button to simulate the generation of a random ESG score (takes ~2 seconds to process).

### 3. **Layered Evaluation Dashboard**
- **Layer 1 Evaluation**: Filter projects based on sustainability goals, problems solved, and budget alignment.
  - Metrics: Goal Match Score, Problem Solved Score, and Budget Match Score.
  - Visualization: Bar chart displaying Layer 1 scores for all projects.
- **Layer 2 Evaluation**: Perform a detailed evaluation with additional metrics like risk scores and final scores.
  - Metrics: Risk Score, ESG Score, Final Score.
  - Visualization: Bar chart showing final scores with risk categories.

### 4. **Preloaded Dummy Projects**
- Three initial projects are preloaded for demonstration:
  1. **Solar Power for Rural Areas**
  2. **Green Urban Farming**
  3. **Eco-Friendly Packaging Solutions**

---

## Getting Started

### Prerequisites
- Python 3.8 or above installed on your system.
- The following libraries are required:
  - `streamlit`
  - `pandas`
  - `plotly`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/greenvestify.git
   cd greenvestify
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser at `https://ecocapitalai-iitmhackathon.streamlit.app/`.

---

## Usage Guide

### Add a New Project
1. Navigate to the **Add Project** page.
2. Fill in the project details, including Name, Goals, Budget, Timeline, and Problems Solved.
3. Either enter the ESG Score manually or click **AI Fetch ESG Score** to generate one.
4. Submit the project to add it to the database.

### View the Dashboard
1. Navigate to the **Dashboard** page.
2. Analyze Layer 1 and Layer 2 evaluation results:
   - **Layer 1**: Goal Match Score, Problem Solved Score, Budget Match Score.
   - **Layer 2**: Risk Score, ESG Score, Final Score.
3. Explore interactive bar charts for insights on project performance.

---

## Folder Structure
```
.
|-- app.py            # Main Streamlit app code
|-- requirements.txt  # Python dependencies
|-- README.md         # Documentation
```

---

## Key Technologies Used
- **Streamlit**: Frontend development for an interactive web application.
- **Pandas**: Data management and manipulation.
- **Plotly**: Visualization of project evaluation metrics.

---

## Future Enhancements
- Integration with backend systems for dynamic data storage.
- Incorporation of AI models for real ESG scoring.
- Advanced analytics for project impact predictions.


