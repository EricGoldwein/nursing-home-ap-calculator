import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Dosing Down, DOGE-ing Up",
    page_icon="📈",
    layout="wide"
)

# Constants
TOTAL_RESIDENTS = 1210000  # 1.21M total residents
CURRENT_AP_RATE = 0.2262   # 22.62% (derived from 77.38% not receiving APs)
DAYS_PER_YEAR = 365

# Page layout with custom CSS for width control
st.markdown("""
    <style>
        /* Disable dark mode */
        [data-testid="stAppViewContainer"] {
            background-color: white;
        }
        
        [data-testid="stHeader"] {
            background-color: transparent;
        }
        
        /* Control width of sliders */
        [data-testid="stHorizontalBlock"] > div:first-child {
            max-width: 600px;
            margin: 0;
        }
        
        /* Control image size and position */
        [data-testid="stImage"] {
            max-width: 600px !important;
            width: 100% !important;
            margin: 0 !important;
            display: block !important;
            margin-top: 1rem !important;
        }
        
        /* Adjust column widths and spacing */
        [data-testid="column"]:nth-child(2) {
            padding-left: 0 !important;
        }
        
        /* Add space between sliders */
        .stSlider {
            margin-bottom: 1rem !important;
            margin-top: 0.5rem !important;
        }

        /* Title styling */
        h1 {
            font-size: 2.5rem !important;
            font-weight: bold !important;
            margin-bottom: 0.5rem !important;
        }
        
        /* Custom title styling */
        .custom-title {
            font-size: 2.5rem !important;
            font-weight: bold !important;
            line-height: 1.1 !important;
            margin: 0 0 0.5rem 0 !important;
            padding: 0 !important;
            color: rgb(49, 51, 63) !important;
        }
        
        .title-line {
            display: inline !important;
        }
        
        .mobile-break {
            display: none !important;
            line-height: 0.9 !important;
        }
        
        @media (min-width: 768px) {
            .custom-title {
                white-space: nowrap !important;
            }
        }
        
        @media (max-width: 767px) {
            .custom-title {
                font-size: 2rem !important;
            }
            .title-line {
                display: block !important;
                line-height: 1 !important;
            }
            .mobile-break {
                display: block !important;
            }
        }

        /* Enhanced savings box */
        .savings-box {
            background-color: #f0f7ff;
            padding: 20px;
            border-radius: 15px;
            margin: 10px 0;
            border: 2px solid #cce3ff;
            max-width: 600px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease;
        }
        .savings-box:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        }
        
        /* Force light mode text */
        .stMarkdown, .stSlider, p, h1, h2, h3 {
            color: rgb(49, 51, 63) !important;
        }
        
        /* Container class for better control */
        .content-container {
            max-width: 600px;
            margin: 0;
            padding: 0;
        }
        
        /* Ensure consistent widths on mobile */
        @media (max-width: 767px) {
            /* Force all main elements to same width */
            [data-testid="stHorizontalBlock"] > div:first-child,
            .stSlider,
            .savings-box,
            [data-testid="stImage"],
            .element-container,
            .content-container {
                width: 100% !important;
                max-width: 400px !important;
                min-width: 0 !important;
                margin-left: auto !important;
                margin-right: auto !important;
                box-sizing: border-box !important;
            }
            
            /* Override any column settings */
            [data-testid="column"] {
                width: 100% !important;
                max-width: 400px !important;
                margin: 0 auto !important;
                padding: 0 !important;
            }
            
            /* Ensure image fits container */
            [data-testid="stImage"] img {
                width: 100% !important;
                max-width: 400px !important;
                height: auto !important;
                margin: 0 !important;
            }
            
            /* Tighter spacing on mobile */
            .stSlider {
                margin-bottom: 0.75rem !important;
                margin-top: 0.5rem !important;
            }
            
            /* Adjust savings box padding on mobile */
            .savings-box {
                padding: 15px !important;
                margin: 8px 0 !important;
            }
            
            /* Reduce description text size on mobile */
            .stMarkdown p {
                font-size: 0.9rem !important;
                margin-bottom: 0.5rem !important;
            }
        }

        /* Adjust main content spacing */
        [data-testid="stVerticalBlock"] > div {
            padding-top: 0.5rem !important;
            padding-bottom: 0.5rem !important;
        }

        /* Hide About section on mobile for initial view */
        @media (max-width: 767px) {
            [data-testid="stMarkdown"] h3,
            [data-testid="stMarkdown"] ul {
                display: none !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Adjust column ratio to push image more to the right
col1, col2 = st.columns([1.5, 1])

with col1:
    # Custom title with consistent styling
    st.markdown("""
        <div class="custom-title">
            <span class="title-line">Dosing Down,</span>
            <span class="title-line">DOGE-ing Up</span>
        </div>
    """, unsafe_allow_html=True)
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