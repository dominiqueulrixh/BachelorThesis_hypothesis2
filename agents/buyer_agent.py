from mesa import Agent
import random

class BuyerAgent(Agent):
    def __init__(self, unique_id, model, budget, location):
        super().__init__(unique_id, model)
        self.budget = budget
        self.location = location
        self.active = False

    def step(self):
        # Aktivierung über Google-Trend-Daten
        if self.model.current_week < len(self.model.buy_trend):
            impulse = self.model.buy_trend[self.model.current_week]
        else:
            impulse = 0.3  # Fallback
        self.active = random.random() < impulse

        if self.active:
            listings = [a for a in self.model.schedule.agents
                        if hasattr(a, "listed") and a.listed and a.location == self.location and a.price <= self.budget]
            if listings:
                chosen = self.random.choice(listings)
                self.model.broker.mediate_transaction(self, chosen)
