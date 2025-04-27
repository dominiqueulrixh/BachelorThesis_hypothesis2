import pandas as pd

def load_trend_data():
    # Lade Kauf-Trends
    df_buy = pd.read_csv("trends/google_trends_buyer.csv")
    df_buy["avg_buy"] = df_buy[["Immobilie kaufen Zürich", "Haus kaufen Zürich", "Wohnung kaufen Zürich", "Immobilien Kaufpreise"]].mean(axis=1)
    buy_trend = (df_buy["avg_buy"] / 100).tolist()  # Normierung

    # Lade Verkaufsdaten (synthetisch oder teilweise leer)
    df_sell = pd.read_csv("trends/google_trends_seller.csv")
    df_sell["avg_sell"] = df_sell[[    "Hausbewertung Zürich", "Wohnung schätzen Zürich", "Wohnung verkaufen Zürich", "Haus verkaufen Tipps Zürich", "Immobilienbewertung Zürich"]].mean(axis=1)

    # Wenn alles 0 ist → Fallback: z.B. gleichbleibender Wert oder ableiten aus Verkäufen
    sell_trend_raw = df_sell["avg_sell"].tolist()
    if all(v == 0 for v in sell_trend_raw):
        sell_trend = [0.2] * len(sell_trend_raw)  # Konstante Verkaufsneigung als Fallback
    else:
        sell_trend = [v / 100 for v in sell_trend_raw]

    return buy_trend, sell_trend
