import streamlit as st


def write_introduction(concept_img):
    st.markdown(
        "<h1 style='text-align: left;'> 🌍 Carbon Monitor City 2.0</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align: left;'> 🏠 Residential</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("## Objective")
    st.markdown("""
                Evaluate **near real-time** CO2 emission for the **community blocks** (gridded map) including two parts:
                
                1. Actual CO2 emission that is emitted inside the block, i.e. residential emissions.
                2. Virtual CO2 emission that is emitted in the power plants but consumed inside the block.
                """, unsafe_allow_html=True)

    st.markdown("""
## Model Concepts

<u>**BIGCarbonEDM**</u> (Building Integral Gridded Carbon Emission Disaggregating Model) is developed for disaggregating
total regional CO2 emission to community blocks level based on features from building-level to regional-level, 
as well as their temporal variations, which are estimated with big data and machine learning models.
""", unsafe_allow_html=True)

    st.image(concept_img, caption='BIGCarbonEDM Concept')


    st.markdown("""

    BIGCarbonEDM has the flexibility of extracting information from various types of datasets currently including:

    1. <u>Building-level datasets </u>: Microsoft Building Footprints, OpenStreetMap, and OpenStreetMap Building.
    2. <u>Urban footprint datasets </u>: Global Human Settlement, World Settlement Footprint, and VIIRS Nightlights.
    3. <u>Land cover and land usage datasets </u>: Local Climate Zone and Copernicus Digital Elevation.
    4. <u>Climate datasets </u>: land surface temperature.
    5. <u>Census data </u> from regional and national reports.
    6. [Carbon Monitor City](https://cities.carbonmonitor.org/) for the regional near real-time CO2 emission.

    BIGCarbonEDM firstly estimates the basic emission patterns for the community blocks based on building-level and regional-level features based on input datasets and machine learning models. Then BIGCarbonEDM estimates near real-time feature variations as well as temporal emission variation proxies to produce the real-time CO2 emission for the community blocks.
                    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    ## Current Version

    For the current version, BIGCarbonEDM outputs *basic emission patterns* for the community blocks.

    - First, we estimate the building-level emission features. We train machine learning models that predict building-level features, such as building height and type. We use OpenStreetMap and OpenStreetMap Building as training datasets, Microsoft Building Footprints as prediction datasets, and features extracted from other datasets as model predictors. Note that machine learning models are necessary as building-level data are not available for those developing countries.
    - Then we analyzed the regional-level emission features based on census data and other input datasets, such as GDP, population, and Nightlights that can capture the regional emission differences.
    - Finally, we combine the building-level and regional-level emission features for each community block using an emission estimation model based on domain knowledge to capture the community's basic emission patterns

                    """, unsafe_allow_html=True)

    st.markdown("""
                    """, unsafe_allow_html=True)
