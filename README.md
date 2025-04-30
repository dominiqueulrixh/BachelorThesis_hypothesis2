# Hypothese 2 – Verhaltensbasierte Daten als Frühindikator auf dem Immobilienmarkt

Diese Simulation untersucht die Hypothese, dass verhaltensbasierte Daten, konkret Google-Suchtrends, einen frühzeitigen, datengetriebenen Einblick in Marktentwicklungen ermöglichen und zu präziseren Vorhersagen von Angebot und Nachfrage beitragen können als rein strukturbezogene Aktivierungsmuster.

---

## Ziel der Hypothese

> Verhaltensbasierte Daten wie Google-Suchtrends ermöglichen eine frühzeitigere und präzisere Vorhersage von Angebots- und Nachfrageschwankungen auf dem Immobilienmarkt als rein strukturbezogene Agenteninteraktionen.

Der Fokus liegt auf der Nachfrageseite: Die Aktivierung von Käuferagenten wird nicht mehr zufällig, sondern auf Grundlage realer Trendsignale gesteuert.

---

## Modellübersicht

| Komponente         | Beschreibung                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `BuyerAgent`        | Kaufinteressierte, deren Aktivierung an Google-Trends gekoppelt ist         |
| `SellerAgent`       | Anbieter wie in Hypothese 1, Angebotsmenge und Preis dynamisch               |
| `BrokerAgent`       | Vermittelt weiterhin zwischen Angebot und Nachfrage                          |
| `GoogleTrendsLoader`| Lädt und verarbeitet aggregierte Google Trends Zeitreihen (CSV)              |
| `compare_trend_vs_random.py` | Vergleich zwischen Trend-gesteuerter und zufällig aktivierter Simulation |

---

## Methodik

- Google Trends-Daten wurden über `pytrends` gesammelt (Begriffe: *Immobilie kaufen Zürich*, *Wohnung kaufen Zürich*, etc.)
- Diese Daten wurden als Zeitreihen in die Simulation eingespeist (`google_trends_buyer.csv`)
- Ein definierter Schwellenwert (`interest_threshold`) entscheidet, ob ein Käuferagent pro Woche aktiviert wird
- Es wurden zwei Szenarien simuliert:
  1. Aktivierung durch Trendsignale
  2. Aktivierung mit fixer Wahrscheinlichkeit (Baseline-Modell wie in Hypothese 1)

---

## Ergebnisse

- Leicht erhöhte Transaktionsrate** bei Trend-Aktivierung im Vergleich zur Zufallslogik
- Vor allem im Jahresverlauf sichtbarer Vorsprung zugunsten der verhaltensbasierten Steuerung
- Trendsignale führten zu besserem „Timing“ der Käuferaktivierung in Hochphasen des Suchinteresses

> Fazit: Google-Trends-Daten besitzen ein Potenzial als verhaltensbasierter Frühindikator. Die Wirkung bleibt jedoch begrenzt, da die Angebotsseite im Modell nicht reaktiv auf diese Signale ausgelegt war.

---

## Dateien im Projektordner

| Datei                          | Funktion                                               |
|--------------------------------|--------------------------------------------------------|
| `main.py`                      | Startpunkt der Simulation mit Google Trends            |
| `housing_market_model.py`      | Modell mit Trends-basierter Aktivierungslogik          |
| `buyer_agent.py`               | Aktivierung über externe Trendsignale                  |
| `GoogleTrendsLoader.py`        | Lese- und Zugriffsfunktion für CSV-Daten               |
| `google_trends_buyer.csv`      | Aggregierte Trenddaten der Suchanfragen (zeitlich)     |
| `compare_trend_vs_random.py`   | Direkter Vergleich zweier Aktivierungsmodelle          |
| `trend_vs_random_plot.png`     | Visualisierung kumulativer Verkäufe beider Szenarien   |

---

## Beispielhafte Visualisierungen

- Kumulative Verkäufe: Trendgesteuert vs. zufällig
- Aktivierungsverlauf im Zeitvergleich
- Käuferaktivitätsrate in Abhängigkeit von Trendsignalen

---

## Weiterführend

Die Simulation zeigt die Wirkung verhaltensbasierter Steuerung auf die Nachfrage, jedoch keine systemische Marktreaktion, da die Angebotsseite unverändert blieb. Diese Erkenntnis motiviert Hypothese 3, in der beide Marktseiten datengetrieben erweitert und zusätzliche Agententypen integriert werden.

---
