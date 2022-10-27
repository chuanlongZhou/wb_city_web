import streamlit as st
import os
from PIL import Image

dataset = st.session_state.dataset_infor
selected = st.sidebar.selectbox("Remote Sensing Products", 
                                dataset["remote_sensing"].keys())

building_dataset = list(dataset["building"].keys())
building_dataset.insert(0, "")
selected2 = st.sidebar.selectbox("Building Datasets", building_dataset)

if st.sidebar.button("clear"):
    selected2=""
    
if selected2 !="":
    selected = selected2
    dataset = dataset["building"]
else:
    dataset = dataset["remote_sensing"]
    


st.markdown("## Dataset Information")
st.markdown("---")

st.markdown(f"### [{dataset[selected]['full_name']}]({dataset[selected]['link']})")
st.markdown(f"{dataset[selected]['description']}")

image = Image.open(os.path.join(st.session_state.fig_path_2, dataset[selected]["image_example"]))
st.image(image, caption=f'{selected} dataset example')