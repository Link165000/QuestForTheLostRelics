class Quest:
    def __init__(self, name, description, difficulty):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.is_completed = False

class QuestSystem:
    def __init__(self):
        self.active_quests = []

    def add_quest(self, quest):
        self.active_quests.append(quest)

    def complete_quest(self, quest_name):
        for quest in self.active_quests:
            if quest.name == quest_name:
                quest.is_completed = True
                print(f"Quest '{quest.name}' completed!")
                return
        print("Quest not found!")

    def show_active_quests(self):
        print("Active Quests:")
        for quest in self.active_quests:
            status = "Completed" if quest.is_completed else "Active"
            print(f"{quest.name} - {status}: {quest.description}")
