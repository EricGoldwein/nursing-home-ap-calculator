# Nursing Home Antipsychotic Cost Calculator

A Streamlit web application that calculates potential savings from reducing antipsychotic drug use in nursing homes.

## Features
- Interactive sliders for target AP rate and daily drug cost
- Real-time savings calculations
- Visual representation of cost impact
- Based on Q3 2024 MDS data

## Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Live Demo
Visit the live app at: [Your Streamlit Cloud URL will be here]

## Data Sources

- Resident data: MDS 3.0 Frequency Report (Q3 2024)
- Drug costs: Estimated based on typical antipsychotic medication prices
- Target usage rate: 3% based on clinical guidelines

## Usage

1. Select a drug cost scenario from the sidebar
2. Explore the interactive map to see usage patterns
3. View detailed metrics and costs in the data table
4. Compare states using the bar chart of excess costs

## Notes

- All calculations assume daily medication administration
- Costs are estimates and may vary by region and pharmacy
- The 3% target rate is a general guideline
- Some states may have redacted data (shown as asterisks in the source data) 