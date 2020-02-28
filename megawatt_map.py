#!/usr/bin/env python
"""show simple constant radius circles around megawatt class MW transmitters"""
from pathlib import Path
import pandas as pd
import folium
import webbrowser

geo = "data/world-countries.json"
fn = Path("data/megawatt_mw.csv")


def main():

    dat = pd.read_csv(fn, index_col=0)

    m = folium.Map(location=[30, 15], zoom_start=3)

    for _, d in dat.iterrows():
        folium.Circle([d["Lat"], d["Lon"]], radius=500e3).add_to(m)

    # %%
    ofn = fn.with_suffix(".html")
    print("writing", ofn)
    m.save(str(ofn))

    webbrowser.open(str(ofn))


if __name__ == "__main__":
    main()
