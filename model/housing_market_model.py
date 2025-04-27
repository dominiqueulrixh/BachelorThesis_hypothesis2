from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random

from agents.buyer_agent import BuyerAgent
from agents.seller_agent import SellerAgent
from agents.broker_agent import BrokerAgent
from GoogleTrendsLoader import load_trend_data

class HousingMarketModel(Model):
    def __init__(self, initial_buyers=15, initial_sellers=5):
        self.schedule = RandomActivation(self)
        self.current_week = 0
        self.num_agents = 0
        self.completed_sales = 0

        # Google Trends nur für Käufer
        self.buy_trend, self.sell_trend_dummy = load_trend_data()

        # Broker
        self.broker = BrokerAgent(self.num_agents, self)
        self.schedule.add(self.broker)
        self.num_agents += 1

        # Käufer:innen
        for _ in range(initial_buyers):
            budget = random.randint(600_000, 1_000_000)
            location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
            b = BuyerAgent(self.num_agents, self, budget, location)
            self.schedule.add(b)
            self.num_agents += 1

        # Verkäufer:innen (Startangebot)
        for _ in range(initial_sellers):
            price = random.randint(500_000, 1_100_000)
            location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
            s = SellerAgent(self.num_agents, self, price, location)
            self.schedule.add(s)
            self.num_agents += 1

        # DataCollector
        self.datacollector = DataCollector(
            model_reporters={
                "Verkäufe": lambda m: m.completed_sales,
                "Angebot": lambda m: sum(1 for a in m.schedule.agents if isinstance(a, SellerAgent) and a.listed),
                "Nachfrage": lambda m: sum(1 for a in m.schedule.agents if isinstance(a, BuyerAgent) and a.active),
            }
        )

    def register_sale(self, buyer, seller):
        seller.listed = False
        self.completed_sales += 1

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_week += 1

        # Verkäufer-Logik (NEU Hypothese 2): Nachfrage-Überhang
        active_buyers = sum(1 for a in self.schedule.agents if isinstance(a, BuyerAgent) and a.active)
        active_sellers = sum(1 for a in self.schedule.agents if isinstance(a, SellerAgent) and a.listed)

        sell_pressure = active_buyers / (active_sellers + 1)

        if sell_pressure > 1.5 and active_buyers >= 5:
            if random.random() < 0.4:  # 40% Wahrscheinlichkeit für neuen Seller
                price = random.randint(500_000, 1_100_000)
                location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
                s = SellerAgent(self.num_agents, self, price, location)
                self.schedule.add(s)
                self.num_agents += 1
