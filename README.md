# 🎵 Top Spotify Songs 2023 – Power BI & Python Analyse

Dit project biedt een interactieve analyse van de populairste Spotify-nummers uit 2023. Het combineert een Power BI-dashboard met een Python-script dat via de Spotify API albumhoezen toevoegt aan de dataset.

## 📊 Overzicht

- Visualisatie van Spotify-data via Power BI (inclusief Deneb visuals).
- Verrijking van de dataset met albumcovers via de Spotify API (Python).
- Filters op genre, artiest en populariteit.
- Gebouwd als leerproject met echte (Kaggle) data.

## 📁 Bestanden in deze repository

| Bestand                    | Beschrijving                                                       |
|---------------------------|---------------------------------------------------------------------|
| `SpotifyRapport.pbix`     | Power BI dashboard met interactieve visualisaties.                 |
| `spotify-2023.csv`        | Originele dataset (Kaggle, 2023).                                  |
| `sorted_spotify_2023.xlsx`| Gesorteerde versie van de dataset (optioneel gebruikt).            |
| `Spotify_Python.py`       | Python-script dat albumcovers ophaalt via de Spotify API.          |
| `README.md`               | Dit bestand.                                                       |

---

## 🎯 Doel van het project

- Trends ontdekken in muziekvoorkeuren uit 2023.
- Visualiseren van populariteit, artiesten en genres.
- Oefenen met data-analyse in Power BI en API-integratie via Python.

---

## 🔧 Python: Verrijk de dataset met albumcovers

Het script `Spotify_Python.py` gebruikt de Spotify API om albumafbeeldingen toe te voegen aan elke track in de dataset.

### Vereisten
- Python 3.x
- Packages: `pandas`, `requests`

### Uitvoeren

1. Installeer dependencies:
   ```bash
   pip install pandas requests
   ```
2. Voeg je eigen Spotify API `CLIENT_ID` en `CLIENT_SECRET` in het script in.
3. Zorg dat `spotify-2023.csv` in dezelfde map staat.
4. Run het script:
   ```bash
   python Spotify_Python.py
   ```
5. Output: `spotify-2023-with-urls.csv`

> ⚠️ Let op: de Spotify API heeft een limiet op het aantal verzoeken per tijdseenheid.

---

## 📊 Power BI Dashboard

### Vereisten

- Power BI Desktop
- Internetverbinding voor Deneb visuals

### Features

- **Deneb Gauge**: visualiseert relatieve populariteit.
- **Heatmap**: toont prestaties per nummer over weken.
- **Filters**: genre, artiest en tijd.
- **Slicers**: interactief segmenteren van data.

---

## 📚 Gegevensbron

- Dataset: [Top Spotify Songs 2023 (Kaggle)](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?resource=download)

Extra visuals zijn geïnspireerd op:
- [Deneb Gauge Visual (StackOverflow)](https://stackoverflow.com/questions/75881301/convert-vega-deneb-gauge-to-work-in-powerbi)
- [Deneb Heatmap Template](https://github.com/PowerBI-tips/Deneb-Templates/blob/main/templates/heatmap%20with%20bars%20-%20red%20themed.json)
