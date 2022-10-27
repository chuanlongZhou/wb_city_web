import streamlit as st
import os
from PIL import Image

cases = {
    "Turkey": ["Ordu",
               "Adana",
               "Manisa",
               "Trabzon"],
    "Egypt": ["Cairo"],
    "South Africa": ["Johannesburg"],
    "All": ["Ordu",
            "Adana",
            "Manisa",
            "Trabzon",
            "Cairo",
            "Johannesburg"
            ],
}

country = st.sidebar.selectbox("Select Country", 
                               cases.keys())
     
city = st.sidebar.selectbox("Select City", cases[country])

plots = st.sidebar.selectbox("Select Plots", ["Model evaluation",
                                             "Prediction"])

st.markdown("## Building Feature Prediction")
st.markdown("Random Forest models are trained for predicting building height and type. Models were trained in each country, and all combined.")
st.markdown("Current model achieved accuracy around <span style='color:green'>0.8</span> for cross-validation, and over <span style='color:green'>0.95</span> for the final outputs in each city." , unsafe_allow_html=True)
st.markdown("More detail wil be added later...")

st.markdown("---")

if plots =="Model evaluation":
    st.markdown(f"### Building Height - {country}")

    matrix_plot = os.path.join(st.session_state.fig_path_2, "ML", f"{country}_height_1_res_30.png")
    st.image(Image.open(matrix_plot), caption=f'Confusion matrix for grouped building height prediction (left) and feature importance (right)')

    matrix_plot = os.path.join(st.session_state.fig_path_2, "ML", f"{country}_height_res_30.png")
    st.image(Image.open(matrix_plot), caption=f'Confusion matrix building height prediction (left) and feature importance (right)')
        

    st.markdown("---")
    st.markdown(f"### Building Type - {country}")

    matrix_plot = os.path.join(st.session_state.fig_path_2, "ML", f"{country}_type_level_2_res_30.png")
    st.image(Image.open(matrix_plot), caption=f'Confusion matrix for building type prediction (left) and feature importance (right)')

elif plots =="Prediction":
    st.markdown(f"### Prediction Difference - {country} - {city}")
    matrix_plot = os.path.join(st.session_state.fig_path_2, "ML", f"{country}_{city}_pred_diff.png")
    st.image(Image.open(matrix_plot), caption=f'Prediction difference')
    
    st.markdown("---")
    
    st.markdown(f"### Final Prediction - {country} - {city}")
    matrix_plot = os.path.join(st.session_state.fig_path_2, "ML", f"{country}_{city}_pred.png")
    st.image(Image.open(matrix_plot), caption=f'Predictions for testing set')
    