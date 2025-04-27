from model.housing_market_model import HousingMarketModel
import matplotlib.pyplot as plt
from analysis.compare_trend_vs_random import *


# Simulation starten
model = HousingMarketModel(initial_buyers=15, initial_sellers=5)

# Laufzeit in "Wochen"
for _ in range(52):
    model.step()

# Daten abrufen
results = model.datacollector.get_model_vars_dataframe()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(results["Verkäufe"], label="Kumulative Verkäufe")
plt.plot(results["Angebot"], label="Angebot (aktive Listings)")
plt.plot(results["Nachfrage"], label="Nachfrage (aktive Käufer:innen)")
plt.xlabel("Kalenderwochen")
plt.ylabel("Anzahl")
plt.title("Immobilienmarktaktivität über 52 Wochen (Hypothese 2)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
