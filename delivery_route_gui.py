import os
import urllib.parse
import webbrowser
import tkinter as tk
from tkinter import messagebox

from google_route_optimization import optimize_route

# Simple package list with address and delivery time
PACKAGES = [
    {"address": "1 Infinite Loop, Cupertino, CA", "time": "09:00"},
    {"address": "500 Terry Francois Blvd, San Francisco, CA", "time": "11:00"},
]

ORIGIN = "1600 Amphitheatre Parkway, Mountain View, CA"
DESTINATION = "1600 Amphitheatre Parkway, Mountain View, CA"


def build_maps_url(addresses):
    """Create a Google Maps directions link for given addresses."""
    origin = addresses[0]
    destination = addresses[-1]
    waypoints = "|".join(addresses[1:-1])
    params = urllib.parse.urlencode(
        {
            "origin": origin,
            "destination": destination,
            "waypoints": waypoints,
            "travelmode": "driving",
        }
    )
    return f"https://www.google.com/maps/dir/?api=1&{params}"


def show_route():
    addresses = [ORIGIN] + [pkg["address"] for pkg in PACKAGES] + [DESTINATION]
    try:
        data = optimize_route(addresses)
        order = data["routes"][0]["waypoint_order"]
        ordered = [addresses[0]] + [addresses[i + 1] for i in order] + [addresses[-1]]
    except Exception as exc:
        messagebox.showerror("Error", str(exc))
        return
    url = build_maps_url(ordered)
    webbrowser.open(url)


def main():
    root = tk.Tk()
    root.title("Leveringsrute")

    listbox = tk.Listbox(root, width=60)
    for pkg in PACKAGES:
        listbox.insert(tk.END, f"{pkg['time']} - {pkg['address']}")
    listbox.pack(padx=10, pady=10)

    btn = tk.Button(root, text="Vis optimal rute", command=show_route)
    btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
