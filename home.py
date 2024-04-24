import streamlit as st
import requests

def get_tour_packages(destination):
    api_key = 'YOUR_API_KEY'
    endpoint = f"https://api.expediapartnercentral.com/.../search?destination={destination}"
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(endpoint, headers=headers)
    return response.json()

def display_homepage():
    

   
    st.title("Welcome to Explore Ethiopia!")
    st.subheader("Your gateway to the cradle of civilization")

   
    st.write("""
        Ethiopia, often referred to as the 'Cradle of Civilization,' is a country rich in history and culture, unmatched in its natural beauty and archaeological significance. From the breathtaking landscapes of the Simien Mountains to the ancient rock-hewn churches of Lalibela, Ethiopia offers a journey through time. As you explore the diverse regions from the lush, bird-filled jungles to the stark beauty of the desert, you'll find a warm welcome in every town and village.
    """)

    
    st.header("Featured Destinations")
    st.write("""
    - **Lalibela:** Visit the UNESCO World Heritage site, famous for its rock-hewn churches carved in the 12th century.
    - **Axum:** The ancient city where the original Ark of the Covenant is reputedly housed.
    - **Addis Ababa:** The vibrant capital city, blending past and present, with bustling markets, museums, and a burgeoning coffee culture.
    - **Omo Valley:** Known for its diverse ethnic groups and unique cultural practices, it's a place where traditional lifestyles are preserved.
    - **Danakil Depression:** One of the hottest and most alien landscapes on Earth, with volcanic activity and salt lakes.
    """)

    
    st.header("Travel Tips & Advisories")
    st.write("""
        Before embarking on your journey, here are some essential travel tips:
        - **Visa Requirements:** Make sure to check the latest visa requirements and obtain your visa well in advance.
        - **Health Precautions:** Vaccinations may be required; consult with a travel health specialist at least a month before your trip.
        - **Cultural Etiquette:** Respect local customs and traditions. Dress modestly in religious sites and rural areas.
        - **Weather Preparedness:** Pack appropriately for both hot and cold climates, as temperatures can vary dramatically, especially in mountainous regions.
    """)

    
    st.header("Cultural Insights")
    st.write("""
        Ethiopia's cultural fabric is woven from the threads of its over 80 ethnic groups. The country's calendar, filled with colorful festivals and events, offers a glimpse into its rich traditions:
        - **Timkat (Epiphany):** A spectacular festival celebrated with processions, music, and dancing, commemorating the baptism of Jesus Christ.
        - **Meskel:** Discover the unique celebration of the finding of the True Cross on which Jesus was crucified.
        - **Coffee Ceremony:** Experience the traditional Ethiopian coffee ceremony—a daily ritual practiced by locals.
    """)

    
    st.subheader("Explore More")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Book Your Tour"):
            destination = st.text_input("Enter your destination")
            if destination:
                packages = get_tour_packages(destination)
                st.write("Explore tour packages and customize your itinerary.")
                st.write(packages)
    with col2:
        if st.button("Ethiopian Cuisine"):
            st.write("Learn about Ethiopia’s rich culinary traditions and where to experience the best local dishes.")
    with col3:
        if st.button("Travel Stories"):
            st.write("Read experiences from fellow travelers to get inspired for your own adventure.")

    # Footer
    st.markdown("---")
    st.caption("© 2024 Guzo. All rights reserved.")

if __name__ == "__main__":
    display_homepage()
