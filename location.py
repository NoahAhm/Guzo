import streamlit as st
import pydeck as pdk

def display_map():
    st.title("Famous Locations in Ethiopia")

    
    view_state = pdk.ViewState(
        latitude=9.145,  
        longitude=40.489673,
        zoom=5,
        pitch=20
    )

   
    locations = [
        {"name": "Addis Ababa", "coordinates": [38.7578, 9.0054], "color": [255, 0, 0], "description": "Capital city of Ethiopia, known for its rich history and diverse culture."},
        {"name": "Lalibela", "coordinates": [39.0419, 12.0310], "color": [255, 0, 0], "description": "Famous for its rock-hewn churches and a UNESCO World Heritage Site."},
        {"name": "Gondar", "coordinates": [37.4600, 12.6000], "color": [255, 0, 0], "description": "Known as the 'Camelot of Africa', home to castles and palaces."},
        {"name": "Axum", "coordinates": [38.7200, 14.1300], "color": [255, 0, 0], "description": "Ancient city with obelisks, tombs, castles, and historical churches."},
        {"name": "Simien Mountains", "coordinates": [38.2517, 13.1767], "color": [255, 0, 0], "description": "Home to some of the highest peaks in Africa, offering stunning views and unique wildlife."},
        {
    "name": "Harar Jugol",
    "coordinates": [42.1387, 9.3179],
    "color": [255, 0, 0],
    "description": "An ancient city in eastern Ethiopia known for its unique, walled historic center and vibrant markets."
},
{
    "name": "Bale Mountains",
    "coordinates": [39.5333, 6.8167],
    "color": [255, 0, 0],
    "description": "A mountain range in southeastern Ethiopia, known for its diverse ecosystems and as a habitat for many threatened species, including the Ethiopian wolf."
}
    ]

   
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=locations,
        get_position="coordinates",
        get_color="color",
        get_radius=25000,  
        pickable=True,
        tooltip={"text": "{name}\n{description}"}
    )

    
    map = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"html": "<b>{name}</b><br/>{description}"}  
    )

    
    st.pydeck_chart(map)

    st.markdown("---")
    st.caption("© 2024 Guzo. All rights reserved.")
if __name__ == "__main__":
    display_map()



# import streamlit as st
# import pydeck as pdk

# def display_map():
#     st.title("Famous Locations in Ethiopia")

#     # Define initial view state of the map
#     view_state = pdk.ViewState(
#         latitude=9.145,  # Center on Ethiopia
#         longitude=40.489673,
#         zoom=6,
#         pitch=20
#     )

#     # List of famous locations with unique attributes for different pins
#     locations = [
#         {"name": "Addis Ababa", "coordinates": [38.7578, 9.0054], "color": [255, 0, 0]},
#         {"name": "Lalibela", "coordinates": [39.0419, 12.0310], "color": [0, 255, 0]},
#         {"name": "Gondar", "coordinates": [37.4600, 12.6000], "color": [0, 0, 255]},
#         {"name": "Axum", "coordinates": [38.7200, 14.1300], "color": [255, 255, 0]},
#         {"name": "Simien Mountains", "coordinates": [38.2517, 13.1767], "color": [255, 165, 0]}
#     ]

#     # Prepare the layers for different locations
#     layer = pdk.Layer(
#         "ScatterplotLayer",
#         data=locations,
#         get_position="coordinates",
#         get_color="color",
#         get_radius=25000,  # Radius of each pin in meters
#         pickable=True
#     )

#     # Create the pydeck map with custom layers
#     map = pdk.Deck(
#         layers=[layer],
#         initial_view_state=view_state,
#         tooltip={"text": "{name}"}
#     )

#     # Display the map
#     st.pydeck_chart(map)

# if __name__ == "__main__":
#     display_map()
