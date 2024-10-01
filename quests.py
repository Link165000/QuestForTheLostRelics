class Quest:
    def __init__(self, title, description, difficulty):
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.completed = False

    def complete_quest(self):
        self.completed = True

class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def show_quests(self):
        for quest in self.quests:
            status = "Completed" if quest.completed else "Incomplete"
            print(f"{quest.title} - {status}")

# Example usage
if __name__ == "__main__":
    quest_manager = QuestManager()
    quest1 = Quest("Defeat the Goblin", "Find and defeat the goblin in the forest.", "Common")
    quest_manager.add_quest(quest1)
    quest_manager.show_quests()
