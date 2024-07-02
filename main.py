import tkinter as tk
import customtkinter as ctk
from getData import *
import utils
import time

def updateOutput(text):
    result_label.configure(state="normal")
    result_label.delete("0.0", "end")
    result_label.insert("0.0", text)
    result_label.configure(state="disabled")

def fetch_amenities():
    try:
        zip_code = zip_entry.get()
        radius = float(radius_entry.get())
        fetch_addresses = address_checkbox_var.get()

        if radius < 10:  # Optimize later
            latitude, longitude = utils.zipToLatLong(int(zip_code))
            
            indoorActivities = ["restaurant", "arts_centre", "cinema", "exhibition_centre", "music_venue", "planetarium", "theatre"]
            outdoorActivities = ["fishing", "garden", "miniature_golf", "nature_reserve", "park", "pitch", "swimming_area", "water_park", "wildlife_hide"]
            
            amenities = fetchAmenitiesOfTypeMultiple(latitude, longitude, indoorActivities, utils.miToMeters(radius))
            if getRainChance(latitude, longitude) < 20:
                outdoorAmenities = fetchLeisure(latitude, longitude, outdoorActivities, utils.miToMeters(radius))
                amenities.extend(outdoorAmenities)
            
            result_text = ""

            for location in amenities:
                if fetch_addresses:
                    location["address"] = utils.latLongtoAddress(location["lat"], location["long"])["displayName"] #1 per second
                    #time.sleep(1)
                else:
                    location["address"] = "Address fetching disabled"
            
            for amenity in amenities:
                result_text += f"{amenity['amenityType'].title()}: {amenity['name']} ({amenity['address']})\n\n"
            
            updateOutput(result_text)

        else:
            raise Exception("Radius too large")

    except Exception as e:
        updateOutput(str(e))

# Setting up the GUI
app = ctk.CTk()
app.geometry("800x600")
app.title("Amenity Finder")

ctk.set_appearance_mode("dark")

zip_label = ctk.CTkLabel(app, text="ZIP Code:")
zip_label.grid(row=0, column=0, padx=10, pady=10)

zip_entry = ctk.CTkEntry(app)
zip_entry.grid(row=0, column=1, padx=10, pady=10)

radius_label = ctk.CTkLabel(app, text="Radius (miles):")
radius_label.grid(row=1, column=0, padx=10, pady=10)

radius_entry = ctk.CTkEntry(app)
radius_entry.grid(row=1, column=1, padx=10, pady=10)

address_checkbox_var = tk.BooleanVar()
address_checkbox = ctk.CTkCheckBox(app, text="Fetch Addresses", variable=address_checkbox_var)
address_checkbox.grid(row=2, column=0, columnspan=2, pady=10)

fetch_button = ctk.CTkButton(app, text="Fetch Amenities", command=fetch_amenities)
fetch_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = ctk.CTkTextbox(app)
result_label.insert("0.0", "")
result_label.grid(row=4, column=1, columnspan=2, sticky="nsew")
result_label.configure(state="disabled", width=500)

app.mainloop()
