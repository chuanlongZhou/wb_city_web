import folium
import geopandas
import shapely

def empty_map():
    m = folium.Map()
    return m

def create_map(state,  city):
    cities = state.cities
    df = state.df
    
    fua = cities[city]['fua']
    fua = shapely.geometry.Polygon(fua)
    fua = geopandas.GeoDataFrame(index=[0], crs='epsg:4326', geometry=[fua])

    m = df[city].explore(
        name="Emission",
        column="emission_residential",
        cmap="hot",
        tooltip=["residential"],
        popup=True,
        # opacity=0.3,
        style_kwds={
            "stroke": True,
            "weight": 1,
            "opacity": 0.1,
            "fillOpacity": 0.4
        }
    )

    df[city].explore(
        m=m,
        name="Population",
        column="emission_population",
        cmap="hot",
        tooltip=["emission_population"],
        popup=True,
        style_kwds={
            "stroke": True,
            "weight": 1,
            "opacity": 0.1,
            "fillOpacity": 0.4
        }
    )

    fua.explore(m=m,
                name="Functional Urban Area",
                style_kwds={
                    "opacity": 0.75,
                    "fill": False,
                    "color": "#e81a32"
                }
                )

    folium.LayerControl().add_to(m)  # use folium to add layer control
    
    return m