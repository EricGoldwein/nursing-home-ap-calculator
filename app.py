import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Dosing Down, DOGE-ing Up",
    page_icon="💊",
    layout="wide"
)

# Constants
TOTAL_RESIDENTS = 1210000  # 1.21M total residents
CURRENT_AP_RATE = 0.2262   # 22.62% (derived from 77.38% not receiving APs)
DAYS_PER_YEAR = 365

# Page layout with custom CSS for width control
st.markdown("""
    <style>
        /* Control width of sliders */
        [data-testid="stHorizontalBlock"] > div:first-child {
            max-width: 600px;
            margin: 0 auto;
        }
        
        /* Control image size and position */
        [data-testid="stImage"] {
            max-width: 600px !important;
            margin-left: auto !important;
            display: block !important;
            margin-top: 3rem !important;
        }
        
        /* Adjust column widths and spacing */
        [data-testid="column"]:nth-child(2) {
            padding-left: 4rem !important;
        }
        
        /* Add space between sliders */
        .stSlider {
            margin-bottom: 2rem !important;
        }

        /* Make title stay on one line */
        h1 {
            white-space: nowrap !important;
            font-size: 2.5rem !important;
        }

        /* Enhanced savings box */
        .savings-box {
            background-color: #f0f7ff;
            padding: 25px;
            border-radius: 15px;
            margin: 20px 0;
            border: 2px solid #cce3ff;
            max-width: 400px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease;
        }
        .savings-box:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Adjust column ratio to push image more to the right
col1, col2 = st.columns([1.5, 1])

with col1:
    st.title("💊 Dosing Down, DOGE-ing Up")
    st.markdown("Calculate potential savings from reducing antipsychotic drug use in nursing homes.")
    
    # Create a container with controlled width
    with st.container():
        # Sliders
        target_ap_rate = st.slider(
            "Target AP Rate (Current: 22.6%)",
            min_value=1.0,
            max_value=25.0,
            value=3.0,  # Default to 3%
            step=0.1,
            format="%0.1f%%",
            help="Target antipsychotic drug rate. Current national rate is 22.6%. Clinical guidelines suggest 3 percent as appropriate."
        ) / 100  # Convert to decimal

        cost_per_day = st.slider(
            "Daily Drug Cost",
            min_value=1,
            max_value=50,
            value=15,  # Default to mid-range
            step=1,
            format="$%d",
            help="Daily drug costs - Generic: USD 3, Mid-range: USD 15, Brand Name: USD 50"
        )

        # Calculate savings
        current_ap_residents = TOTAL_RESIDENTS * CURRENT_AP_RATE
        target_ap_residents = TOTAL_RESIDENTS * target_ap_rate
        reduced_residents = current_ap_residents - target_ap_residents
        annual_savings = reduced_residents * cost_per_day * DAYS_PER_YEAR
        savings_billions = annual_savings / 1e9

        # Enhanced savings box with hover effect
        st.markdown(f"""
            <div class="savings-box">
                <p style="color: #1a5fb4; font-size: 16px; font-weight: 600; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">Potential Annual Savings</p>
                <p style="color: #0d4a9b; font-size: 56px; font-weight: 700; margin: 0 0 12px 0; line-height: 1;">${savings_billions:.2f}B</p>
                <p style="color: #1a5fb4; font-size: 18px; margin: 0; line-height: 1.4;">By reducing AP drug rate from 22.6% to {target_ap_rate*100:.1f}% at ${cost_per_day}/day drug cost</p>
            </div>
        """, unsafe_allow_html=True)

with col2:
    st.image("assets/ap-drug-cuckoo.jpg", width=600)

# Additional context
st.markdown("---")
st.markdown("""
### About the Data
- Based on Q3 2024 MDS data showing 22.6% of nursing home residents receive antipsychotic medications
- Calculations use total nursing home population of 1.21M residents
- Daily drug costs range from 3 USD (Generic) to 50 USD (Brand Name)
- Target rate of 3% based on clinical guidelines for appropriate use
""") 