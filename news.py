import streamlit as st

def display_news():
    st.title("Latest News")

   
    articles = [
        {
            "title": "Exploring Ethiopia's Hidden Gems: The Danakil Depression",
            "summary": "The Danakil Depression, often touted as one of the most hostile and visually fascinating places on Earth, ...",
            "full_text": """
                The Danakil Depression, often touted as one of the most hostile and visually fascinating places on Earth, continues to draw adventurous travelers from around the world. This stark landscape, known for its volcanic activity, including the bright yellow sulphur fields and the bubbling lava of Erta Ale, offers a glimpse into the dynamic forces shaping our planet.

                Recent upgrades to local infrastructure and the introduction of guided tours with enhanced safety measures make the Danakil Depression more accessible than ever. Tour operators based in Mekele offer packages that include visits to Dallol, one of the lowest points on Earth not covered by water, and the opportunity to observe the traditional salt mining process that has been a part of the local Afar tribe's culture for centuries.

                Travel Advisory: The Danakil Depression experiences some of the highest temperatures on earth year-round. Visitors are advised to prepare adequately, staying hydrated and protecting themselves from the sun.
            """
        },
        
        {
            "title": "Timkat Festival Celebrations Lead to Record Tourist Arrivals",
            "summary": "This year's Timkat Festival, which celebrates the Epiphany and marks the baptism of Jesus Christ in the River Jordan, ...",
            "full_text": """
                This year's Timkat Festival, which celebrates the Epiphany and marks the baptism of Jesus Christ in the River Jordan, has concluded with record attendance. Officials in Gondar, where the main celebrations took place, reported that over 50,000 tourists participated in the three-day festival, marking a 20% increase from last year.

                The festival, famous for its vibrant processions, colorful robes, and the ritualistic immersion of replicas of the Ark of the Covenant, provides a deep insight into the spiritual life and community bonds of the Ethiopian Orthodox community.

                Local businesses, especially those in the hospitality sector, have seen a significant boost. Hotels were booked months in advance, and local artisans found an eager market for their crafts, including traditional clothing, handwoven baskets, and religious icons.

                Cultural Insight: Timkat is best experienced in the historic cities of Gondar, Lalibela, or Addis Ababa, where the blend of ancient traditions and the presence of numerous historic churches adds a profound depth to the celebration.
            """
        },
        {
            "title": "Ethiopia Unveils New Cultural Exhibit at the National Museum of Addis Ababa",
            "summary": "A new exhibit titled 'Roots of Ethiopia' has opened this month, showcasing rare artifacts and manuscripts...",
            "full_text": """
                A new exhibit titled 'Roots of Ethiopia' has opened this month at the National Museum of Addis Ababa, showcasing rare artifacts and manuscripts that explore the deep and complex history of the region. The exhibit features pieces that date back over two millennia and includes items that have never before been displayed publicly.

                The exhibit aims to attract both international tourists and local visitors, providing a profound insight into Ethiopia's historical contributions to civilization. Highlights include ancient scrolls from the Kingdom of Aksum and traditional attire worn by Ethiopian monarchs.

                This exhibit is expected to run for the next six months, with guided tours available in multiple languages.
            """
        },
        {
            "title": "Ethiopia Advances Eco-Tourism with New Sustainable Travel Initiatives",
            "summary": "Ethiopia is setting a benchmark in eco-tourism with the launch of new sustainable travel initiatives aimed at preserving its unique landscapes...",
            "full_text": """
                Ethiopia is setting a benchmark in eco-tourism with the launch of new sustainable travel initiatives aimed at preserving its unique landscapes while fostering responsible travel. The new programs focus on minimizing environmental impact and promoting local culture and products.

                Among the initiatives is the 'Green Footprint' campaign, which encourages tourists to participate in tree planting activities. Additionally, several eco-lodges have been developed using local materials and sustainable practices, providing low-impact accommodations in stunning locations such as the Bale Mountains and the Simien National Park.

                These efforts are part of a broader strategy to attract environmentally conscious travelers and promote environmental stewardship.
            """
        },
        {
            "title": "Annual Ethiopian Cuisine Festival Draws Global Food Enthusiasts",
            "summary": "The much-anticipated Ethiopian Cuisine Festival has returned this year, attracting food enthusiasts from around the globe to the capital...",
            "full_text": """
                The much-anticipated Ethiopian Cuisine Festival has returned this year, attracting food enthusiasts from around the globe to the capital, Addis Ababa. The festival celebrates the diverse culinary traditions of Ethiopia's various regions and offers a tantalizing array of dishes, from spicy stews and sizzling barbecues to aromatic coffees and honey wines.

                This year's festival includes cooking workshops, live cooking demonstrations by renowned chefs, and opportunities to learn about the traditional farming and preparation methods of ingredients like teff and berbere. 

                The festival not only promotes Ethiopian food culture but also supports local farmers and producers, making it a key event in Ethiopia’s cultural calendar.
            """
        }

    ]

    for i, article in enumerate(articles, start=1):
        with st.container():
            st.subheader(article['title'])
            st.write(article['summary'])
            if st.button('Read Full Article', key=f'btn_{i}'):
                st.write(article['full_text'])
            st.markdown("---")  
    
    st.subheader("More Recent News")
    st.write("For the latest updates and more detailed news coverage, visit these local news sources:")
    st.markdown("""
    - [Ethiopian Broadcasting Corporation (EBC)](https://ebc.et/english/t)
    - [Addis Ababa News Agency (AANA)](http://www.aana.com)
    - [Fana Broadcasting Corporate](https://www.fanabc.com/english/)
    - [The Reporter](http://www.thereporterethiopia.com)
    """)

    st.markdown("---")
    st.caption("© 2024 Guzo. All rights reserved.")
if __name__ == "__main__":
    display_news()
