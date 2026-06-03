import streamlit as st
from travel_helper import (
    search_destinations,
    get_destination_info,
    get_travel_tips,
    get_budget_comparison
)

# PAGE CONFIG
st.set_page_config(
    page_title="Travel Guide ChatBot",
    page_icon="✈️",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.main {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
    border-radius: 10px;
    padding: 12px;
}

.stButton button {
    background-color: #FF6B35;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #FF8C42;
    color: white;
}

.css-1d391kg {
    background-color: #111111;
}

.destination-card {
    background-color: #1a1a2e;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
    border-left: 5px solid #FF6B35;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🌍 Travel Guide ChatBot")

st.sidebar.markdown("""
## About

Travel Guide ChatBot helps users discover amazing destinations instantly using a comprehensive travel database.

### Features
- 🏙️ Destination Search
- 💰 Budget Comparison
- 🎒 Travel Tips
- 🍽️ Food Recommendations
- 🏛️ Top Attractions
- ⏰ Best Time to Visit
""")

# HERO SECTION
st.markdown("""
# ✈️ Travel Guide ChatBot

### Your Smart Travel Discovery Assistant 🌍
""")

st.write("")

# TABS FOR DIFFERENT FEATURES
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Search Destination", "💰 Budget Compare", "🎒 Travel Tips", "ℹ️ Help"])

with tab1:
    st.subheader("Search Your Favorite Destination")
    
    col1, col2 = st.columns([4, 1])
    
    with col1:
        destination_name = st.text_input(
            "Enter destination name",
            key="destination_search"
        )
    
    with col2:
        search_button = st.button("🔍 Search", key="search_btn")
    
    if search_button:
        if destination_name.strip() == "":
            st.warning("⚠️ Please enter a destination name")
        else:
            with st.spinner("Finding amazing destinations for you..."):
                destinations = search_destinations(destination_name)
            
            if not destinations:
                st.error("❌ No destinations found. Try searching for: Paris, Tokyo, New York, Bangkok, London, Dubai")
            else:
                st.success(f"✅ Found {len(destinations)} destination(s)!")
                st.write("")
                
                for destination in destinations:
                    info = get_destination_info(destination)
                    if info:
                        st.markdown(info)
                        st.divider()

with tab2:
    st.subheader("Compare Budgets Between Destinations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        dest1 = st.text_input("First destination", key="dest1")
    
    with col2:
        dest2 = st.text_input("Second destination", key="dest2")
    
    if st.button("💰 Compare Budgets", key="compare_btn"):
        if dest1.strip() == "" or dest2.strip() == "":
            st.warning("⚠️ Please enter both destinations")
        else:
            comparison = get_budget_comparison([dest1, dest2])
            st.markdown(comparison)

with tab3:
    st.subheader("Get Travel Tips & Advice")
    
    if st.button("🎒 Show Travel Tips", key="tips_btn"):
        tips = get_travel_tips()
        st.markdown(tips)

with tab4:
    st.subheader("Available Destinations")
    
    st.markdown("""
    ### Search Options:
    - **Search by Name**: Enter any destination name (e.g., "Paris", "Tokyo")
    - **Available Destinations**: Paris, Tokyo, New York, Bangkok, London, Dubai
    
    ### What You Can Do:
    1. 🏙️ **Search Destinations** - Get detailed info about any city
    2. 💰 **Compare Budgets** - Compare costs between destinations
    3. 🎒 **Travel Tips** - Get helpful travel advice
    4. 🍽️ **Food Info** - Learn about local cuisine
    5. 🏛️ **Attractions** - Discover top tourist spots
    6. ⏰ **Best Time** - Find ideal travel seasons
    
    ### Example Searches:
    - Search for "Paris" to get comprehensive travel guide
    - Compare "Tokyo" and "Bangkok" to see which fits your budget
    - Click "Show Travel Tips" for general travel advice
    """)

# FOOTER
st.write("")
st.markdown("---")
st.markdown(
    "Made with ❤️ by Your Travel AI Assistant"
)
