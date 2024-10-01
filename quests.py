class Quest:
    def __init__(self, name, description, target_type, target_amount, reward):
        self.name = name
        self.description = description
        self.target_type = target_type
        self.target_amount = target_amount
        self.progress = 0
        self.reward = reward

    def update_progress(self):
        self.progress += 1
        if self.is_complete():
            return self.complete()

    def is_complete(self):
        return self.progress >= self.target_amount

    def complete(self):
        print(f"Quest Completed: {self.name}! Reward: {self.reward} XP")
        return self.reward
