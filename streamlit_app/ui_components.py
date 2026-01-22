import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from data import TERMINAL_ZONES, TerminalZone, get_terminal_zones

def load_custom_css():
    st.markdown("""
    <style>
        .stButton button {
            border-radius: 12px;
            font-weight: bold;
        }
        .main-header {
            font-size: 2.5rem;
            font-weight: 800;
            background: -webkit-linear-gradient(left, #2563eb, #4f46e5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 1rem;
            box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            border: 1px solid #f1f5f9;
            margin-bottom: 1rem;
        }
        .stat-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #1e293b;
        }
        .stat-label {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            color: #94a3b8;
        }
    </style>
    """, unsafe_allow_html=True)

def render_terminal_map(selected_zone_id: str = None, zones: list = TERMINAL_ZONES):
    # Create a scatter plot to simulate the map zones
    # We use a shape or background image effectively
    
    # Terminal Outline
    fig = go.Figure()
    
    # Draw simple terminal shape
    fig.add_shape(type="rect",
        x0=10, y0=20, x1=90, y1=80,
        line=dict(color="#cbd5e1", width=2, dash="dash"),
        fillcolor="rgba(0,0,0,0)"
    )
    
    # Zones Data
    x = [z.x for z in zones]
    y = [z.y for z in zones]
    names = [z.name for z in zones]
    colors = []
    sizes = []
    
    for z in zones:
        color = '#10b981' if z.status == 'Clear' else '#f59e0b' if z.status == 'Busy' else '#ef4444'
        is_selected = z.id == selected_zone_id
        colors.append(color)
        sizes.append(25 if is_selected else 15)
        
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='markers+text',
        marker=dict(size=sizes, color=colors, line=dict(width=2, color='white')),
        text=names,
        textposition="bottom center",
        hoverinfo='text',
        hovertext=[f"{z.name}<br>Status: {z.status}<br>Wait: {z.waitTime} min" for z in zones],
        customdata=[z.id for z in zones]
    ))
    
    fig.update_layout(
        xaxis=dict(range=[0, 100], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(range=[100, 0], showgrid=False, zeroline=False, visible=False), # Inverted Y for consistency with SVG coords commonly top-left
        margin=dict(l=0, r=0, t=0, b=0),
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    
    # Handle click events in Streamlit is tricky without custom components.
    # We will use selectbox or radio buttons for zone selection alongside the map for now.
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_stats_chart(data: list, label: str):
    df = pd.DataFrame(data)
    fig = px.area(df, x='hour', y='load', title=label)
    fig.update_traces(line_color='#3b82f6', fill='tozeroy')
    fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(visible=False),
        margin=dict(l=0, r=0, t=30, b=0),
        height=200,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

def render_guide_card(guide, expanded=False):
    with st.expander(f"{guide['icon']} {guide['title']}", expanded=expanded):
        st.write(guide['desc'])
        st.markdown("---")
        for i, step in enumerate(guide['steps']):
            st.markdown(f"**{i+1}.** {step}")
            
