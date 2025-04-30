from pytrends.request import TrendReq
import pandas as pd
import time

# PyTrends Session aufbauen
pytrends = TrendReq(hl='de-CH', tz=360)

# --- Begriffe definieren ---
buyer_kw_list = [
    "Immobilie kaufen Zürich",
    "Haus kaufen Zürich",
    "Wohnung kaufen Zürich",
    "Immobilien Kaufpreise"
]

seller_kw_list = [
    "Hausbewertung Zürich",
    "Wohnung schätzen Zürich",
    "Wohnung verkaufen Zürich",
    "Haus verkaufen Tipps Zürich",
    "Immobilienbewertung Zürich"
]

# --- Käuferdaten holen ---
print("🔎 Lade Käuferdaten...")
pytrends.build_payload(buyer_kw_list, cat=0, timeframe='today 12-m', geo='CH')
time.sleep(2)
df_buyer = pytrends.interest_over_time()

if df_buyer.empty:
    print("⚠️ Achtung: Keine Käuferdaten gefunden!")
else:
    df_buyer = df_buyer.reset_index()
    if 'isPartial' in df_buyer.columns:
        df_buyer = df_buyer.drop(columns=['isPartial'])
    df_buyer.to_csv("trends/google_trends_buyer.csv", index=False)
    print("✅ Käuferdaten gespeichert als 'google_trends_buyer.csv'")

# --- Wichtige Pause vor neuem Request ---
time.sleep(5)

# --- Verkäuferdaten holen ---
print("🔎 Lade Verkäuferdaten...")
pytrends.build_payload(seller_kw_list, cat=0, timeframe='today 12-m', geo='CH-ZH')
time.sleep(2)
df_seller = pytrends.interest_over_time()

if df_seller.empty:
    print("⚠️ Achtung: Keine Verkäuferdaten gefunden!")
else:
    df_seller = df_seller.reset_index()
    if 'isPartial' in df_seller.columns:
        df_seller = df_seller.drop(columns=['isPartial'])
    df_seller.to_csv("trends/google_trends_seller.csv", index=False)
    print("✅ Verkäuferdaten gespeichert als 'google_trends_seller.csv'")
