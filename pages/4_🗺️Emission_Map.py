import streamlit as st

from streamlit_folium import st_folium

from utils import create_map, empty_map

st.markdown("## Grided Emission Map")
st.markdown("---")
st.markdown("Emission = f(population, building height/area, night light, day night surface temperature difference)")

selected = st.sidebar.selectbox("Please select city", st.session_state.city_names)
m = create_map(st.session_state, selected)
    
st.sidebar.markdown("""
                    Notes:
                    1. Click to view detail of each grid.
                    2. Layer control is on the map.
                    3. Displaying Cairo and Johannesburg are slow.
                    """)
    

st_folium(m, width=1000)
