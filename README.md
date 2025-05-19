# codex-demo

Dette repoet inneholder et enkelt eksempel paa hvordan man kan kalle Google
Directions API for aa optimalisere rekkefolgen paa leveranser. Scriptene her
kan brukes som et utgangspunkt for videre integrasjon i en egen app.

## Forutsetninger

- Python 3 installert
- En Google Maps API-noekkel med tilgang til Directions API

API-noekkelen kan settes i miljoevariabelen `GOOGLE_MAPS_API_KEY` foer
programmet koeres.

## Eksempelbruk

Kjoer `google_route_optimization.py` med en liste av adresser der den foerste er
startpunkt og den siste er sluttpunkt. Adressene imellom blir behandlet som
waypoints og rekkefolgen optimaliseres av Google.

```bash
export GOOGLE_MAPS_API_KEY="din_nokkel"
python google_route_optimization.py
```

Skriptet printer da responsen fra Google som blant annet inneholder den
optimaliserte rekkefolgen.

## Enkel GUI

Skriptet `delivery_route_gui.py` viser noen eksempelpakker med tilhoerende
adresse og tidspunkt i et lite vindu. Naar du trykker paa knappen **Vis optimal
rute** beregnes rekkefolgen med Google Directions API og ruten aapnes i din
nettleser med Google Maps.

```bash
export GOOGLE_MAPS_API_KEY="din_nokkel"
python delivery_route_gui.py
```
