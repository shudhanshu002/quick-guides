class Cloud:
    def __init__(self):
        self.budgets = {}
        self.spend = {}
        self.alerts = {}
        
    def set_budget(self,service,limit):
        self.budgets[service] = limit
        
    def add_spend(self,service, amount):
        self.spend[service] = self.spend.get(service, 0) + amount
        
        if service in self.budgets:
            if self.spend[service] > self.budgets[service]:
                self.alerts.add(service)
                
    def get_alerts(self):
        result = []
        for service in self.alerts:
            result.append(
                f"{service} exceeded budget: spent {self.spent[service]}, limit {self.budgets[service]}"
            )
        return result

    def get_summary(self):
        return self.spent