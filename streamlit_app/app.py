import streamlit as st
import datetime
from data import (
    LANGUAGES, PASSENGER_TYPES, UI_TRANSLATIONS, TERMINAL_ZONES, 
    PEAK_HOURS_DATA, FAQs_DATA, get_guides
)
from gemini_service import gemini_service
from ui_components import load_custom_css, render_terminal_map, render_stats_chart, render_guide_card

# --- Config ---
st.set_page_config(
    page_title="Aeronix Assistant",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_custom_css()

# --- State Management ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'selected_zone' not in st.session_state:
    st.session_state.selected_zone = None

# --- Sidebar ---
with st.sidebar:
    st.title("Aeronix Settings")
    
    # Language Selector
    selected_lang_code = st.selectbox(
        "Language",
        options=[l.code for l in LANGUAGES],
        format_func=lambda x: next((f"{l.flag} {l.name}" for l in LANGUAGES if l.code == x), x),
        index=0
    )
    
    # Passenger Type
    selected_pax_id = st.selectbox(
        "Passenger Type",
        options=[p.id for p in PASSENGER_TYPES],
        format_func=lambda x: next((f"{p.icon} {p.name}" for p in PASSENGER_TYPES if p.id == x), x),
        index=0
    )
    
    st.divider()
    st.info(f"**Mode:** {selected_pax_id.capitalize()}")
    st.caption("Aeronix provides tailored advice based on your traveler profile.")

# --- Translations Helper ---
t = UI_TRANSLATIONS.get(selected_lang_code, UI_TRANSLATIONS['en'])

# --- Main Layout ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"<h1 class='main-header'>Aeronix</h1>", unsafe_allow_html=True)
    st.subheader(t['hero']['title'])
    st.write(t['hero']['desc'])
    
    # Status Badge
    st.markdown(f"**{t['hero']['cta2']}** 🟢")
    
    st.divider()
    
    # Terminal Map Section
    st.markdown(f"### {t['sections']['mapTitle']}")
    st.write(t['sections']['mapDesc'])
    
    # Fetch localized zones
    from data import get_terminal_zones
    current_zones = get_terminal_zones(selected_lang_code)
    
    # Zone selector to mimic map interaction
    zone_options = ["None"] + [z.name for z in current_zones]
    selected_zone_name = st.selectbox("Highlight Zone", zone_options)
    
    active_zone_id = next((z.id for z in current_zones if z.name == selected_zone_name), None)
    render_terminal_map(active_zone_id, current_zones)
    
    if active_zone_id:
        zone = next(z for z in current_zones if z.id == active_zone_id)
        st.info(f"**{zone.name}**: {zone.description} | Wait: {zone.waitTime} min | Status: {zone.status}")

    # Process Guide Section
    st.markdown(f"### {t['sections']['checklistTitle']}")
    st.write(t['sections']['checklistDesc'])
    
    guides = get_guides(selected_lang_code)
    cols = st.columns(len(guides))
    # Streamlit columns are tight, maybe expanders are better stacked or 2 per row
    # Let's use a cleaner flow:
    
    for guide in guides:
        render_guide_card(guide)


with col2:
    # Live Assistant / Chat
    st.markdown(f"### {t['sections']['assistantTitle']}")
    with st.container(border=True):
        # Chat History
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        
        # Initial Greeting if empty
        if not st.session_state.messages:
            with st.chat_message("assistant"):
                st.markdown(t['chat']['assistantGreeting'])
        
        # Input
        if prompt := st.chat_input(t['chat']['placeholder']):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = gemini_service.send_message(
                        prompt, 
                        st.session_state.messages, 
                        language=selected_lang_code, 
                        passenger_type=selected_pax_id
                    )
                    st.markdown(response)
            
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Stats
    st.markdown(f"### {t['sections']['analyticsTitle']}")
    render_stats_chart(PEAK_HOURS_DATA, t['stats']['loadDesc'])
    
    st.metric(t['stats']['waitTime'], "18 mins", delta_color="normal")
    st.metric(t['stats']['securityStatus'], "Operational", "Normal")

# --- Footer ---
st.divider()
st.caption("Aeronix Ground Operations Assistant • Powered by Google Gemini")
