class Quest:
    def __init__(self, title, description, difficulty, experience_reward):
        self.title = title
        self.description = description
        self.difficulty = difficulty
        self.completed = False
        self.experience_reward = experience_reward

    def complete(self):
        self.completed = True
        return self.experience_reward

    def __str__(self):
        return f"{self.title} (Difficulty: {self.difficulty}) - {self.description}"


class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def complete_quest(self, quest):
        if quest.completed:
            print("Quest already completed.")
            return 0

        experience_gained = quest.complete()
        return experience_gained

    def show_quests(self):
        for quest in self.quests:
            print(quest)
