python
import requests
import json
import folium

# Fetch real-time public transport data
transport_api_url = "https://api.abudhabi.transport/realtime"
transport_data = requests.get(transport_api_url).json()

# Fetch air quality data
air_quality_api_url = "https://api.abudhabi.airquality/realtime"
air_quality_data = requests.get(air_quality_api_url).json()

# Initialize a map
abudhabi_map = folium.Map(location=[24.453884, 54.3773438], zoom_start=12)

# Add public transport data to the map
for vehicle in transport_data['vehicles']:
    folium.Marker(
        location=[vehicle['latitude'], vehicle['longitude']],
        popup=f"Vehicle: {vehicle['id']}\nRoute: {vehicle['route']}\nNext Stop: {vehicle['next_stop']}\nETA: {vehicle['eta']} minutes",
        icon=folium.Icon(color="blue", icon="bus", prefix="fa")
    ).add_to(abudhabi_map)

# Add air quality data to the map
for station in air_quality_data['stations']:
    folium.CircleMarker(
        location=[station['latitude'], station['longitude']],
        radius=10,
        color="green" if station['aqi'] <= 50 else "red",
        fill=True,
        fill_opacity=0.7,
        popup=f"Station: {station['name']}\nAQI: {station['aqi']}\nPM2.5: {station['pm25']} µg/m³\nNO2: {station['no2']} µg/m³"
    ).add_to(abudhabi_map)

# Save the map to an HTML file
abudhabi_map.save("abudhabi_transport_air_quality_map.html")
