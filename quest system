class Quest:
    def __init__(self, name, description, target_type, target_amount):
        self.name = name
        self.description = description
        self.target_type = target_type
        self.target_amount = target_amount
        self.progress = 0

    def update_progress(self):
        self.progress += 1

    def is_complete(self):
        return self.progress >= self.target_amount
