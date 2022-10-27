import streamlit as st
import os
import pickle
import json

from PIL import Image

from utils import write_introduction

# emoji: https://emojifinder.com/map

def init_state(state):
    state.fig_path_1 = os.path.join("fig")
    state.fig_path_2 = os.path.join(".", "fig")
    state.data_path = os.path.join("data")
    
    if "df" not in state:
        state.df = pickle.load(open(os.path.join(state.data_path, "emission_grid_map.pkl"), "rb"))
        
    if "cities" not in state:
        state.cities = json.load(open(os.path.join(state.data_path, "cities.json")))
        state.city_names = list(state.cities.keys())
        state.city_names.remove("note")
        state.city_names.remove("Ordu")
        state.city_names.insert(0, "Ordu")
        
    if "dataset_infor" not in state:
        state.dataset_infor = json.load(open(os.path.join(state.data_path, "dataset_infor.json")))
    
    if "selected" not in state:
        state.selected = None    
    
    return state

def run():
    init_state(st.session_state)
    st.set_page_config(
        page_title="Carbon Monitor City 2.0 - Residential",
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state='expanded'
    )
    
    concept_img = Image.open(os.path.join(st.session_state.fig_path_1, "concept.png"))
    write_introduction(concept_img)
    
    
if __name__ == '__main__':
    run()
