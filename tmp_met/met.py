import requests
import pandas as pd
import time

# Base URL for The Met API
MET_API_BASE = "https://collectionapi.metmuseum.org/public/collection/v1"

# Step 1: Fetch all object IDs
response = requests.get(f"{MET_API_BASE}/objects")
if response.status_code == 200:
    all_object_ids = response.json().get("objectIDs", [])[:200]  # Limit to 100 
else:
    print("Error fetching object IDs")
    all_object_ids = []


# Step 2: Define fields to extract for visualizations
fields_to_keep = [
    "objectID", 
    "isHighlight", # When "true" indicates a popular and important artwork in the collection
    "title", 
    "accessionYear",
    "objectName",
    "artistDisplayName", 
    "artistNationality", 
    "objectEndDate", 
    "classification", # want to filter only the paintings to minimize the scope
    "department", 
    "medium", 
    "culture", 
    "period", 
    "artistBeginDate", 
    "artistEndDate"
]

# Step 3: Fetch detailed metadata for each object
artworks_data = []
for object_id in all_object_ids:
    response = requests.get(f"{MET_API_BASE}/objects/{object_id}")
    if response.status_code == 200:
        data = response.json()
        filtered_data = {key: data.get(key, None) for key in fields_to_keep}
        artworks_data.append(filtered_data)
    
    # avoid overwhelming the API
    time.sleep(0.2)

# Step 4: Create a DataFrame and save the data
artworks_df = pd.DataFrame(artworks_data)
artworks_df.to_csv("met_artworks_data.csv", index=False)

# Display the first few rows
print(artworks_df.head())
