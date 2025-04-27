import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np
import os

# --- Trenddaten laden ---
buyer_df = pd.read_csv("/Users/dominiqueulrich/PycharmProjects/BachelorThesis_hypothesis2/trends/google_trends_buyer.csv")

# Alle relevanten Käuferbegriffe mitteln
google_trends = buyer_df[
    ["Immobilie kaufen Zürich", "Haus kaufen Zürich", "Wohnung kaufen Zürich", "Immobilien Kaufpreise"]
].mean(axis=1).fillna(0).tolist()

# --- Dynamische Schwelle berechnen ---
threshold = np.percentile(google_trends, 60)  # z.B. 60%-Perzentil als Aktivierungsschwelle
print(f"📈 Dynamische Schwelle gesetzt bei: {threshold:.2f}")

# Verkaufszahlen basierend auf dynamischer Schwelle ableiten
trend_sales = np.cumsum([1 if t > threshold else 0 for t in google_trends])

# Vergleich: Random-Modell
np.random.seed(42)
random_sales = np.cumsum(np.random.binomial(1, 0.4, size=len(google_trends)))

# --- Korrelation berechnen ---
corr_trend, p_trend = pearsonr(google_trends, trend_sales)
corr_random, p_random = pearsonr(google_trends, random_sales)

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(trend_sales, label="Verkäufe (mit Google-Trends)", linewidth=2)
plt.plot(random_sales, label="Verkäufe (zufällige Aktivierung)", linestyle="--")
plt.xlabel("Kalenderwochen")
plt.ylabel("Kumulative Verkäufe")
plt.title("Vergleich: Verkäufe mit und ohne Google-Trends")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("trend_vs_random_plot.png")
plt.show()

# --- Ausgabe ins Terminal ---
print("📊 Korrelation mit Google-Trends:")
print(f"→ Mit Google-Trends:     r = {corr_trend:.2f}, p = {p_trend:.3f}")
print(f"→ Zufallsaktivierung:    r = {corr_random:.2f}, p = {p_random:.3f}")
