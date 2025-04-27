from mesa import Agent

class SellerAgent(Agent):
    def __init__(self, unique_id, model, price, location):
        super().__init__(unique_id, model)
        self.price = price
        self.location = location
        self.listed = True

    def step(self):
        pass  # Verkäufer:innen sind passiv, Listing bleibt bestehen
