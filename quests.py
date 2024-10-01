class Quest:
    def __init__(self, id, description, reward, difficulty):
        self.id = id
        self.description = description
        self.reward = reward
        self.difficulty = difficulty

class QuestManager:
    def __init__(self):
        self.quests = self.generate_quests()

    def generate_quests(self):
        return [
            Quest(1, "Collect 5 herbs", "50 gold", "Common"),
            Quest(2, "Defeat 3 goblins", "100 gold", "Uncommon"),
            Quest(3, "Find the hidden treasure", "150 gold", "Rare"),
            Quest(4, "Slay the Ice Dragon", "500 gold", "Legendary"),
        ]

# Example Usage
if __name__ == "__main__":
    quest_manager = QuestManager()
    for quest in quest_manager.quests:
        print(quest.description)
