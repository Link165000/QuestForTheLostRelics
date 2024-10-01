class Quest:
    def __init__(self, name, description, difficulty, quest_type, rewards, dependencies=None):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.quest_type = quest_type
        self.rewards = rewards
        self.dependencies = dependencies if dependencies else []
        self.is_completed = False
        self.current_stage = 0
        self.total_stages = 1  # Default to 1 stage; can be increased for multi-stage quests

    def complete_stage(self):
        if self.current_stage < self.total_stages:
            self.current_stage += 1
            print(f"Stage {self.current_stage}/{self.total_stages} of '{self.name}' completed.")
            if self.current_stage == self.total_stages:
                self.is_completed = True
                print(f"Quest '{self.name}' completed!")
                return True  # Quest is fully completed
        return False  # Quest is still ongoing


class QuestSystem:
    def __init__(self):
        self.active_quests = []

    def add_quest(self, quest):
        if all(dep.is_completed for dep in quest.dependencies):
            self.active_quests.append(quest)
            print(f"Quest '{quest.name}' added!")
        else:
            print(f"Quest '{quest.name}' cannot be accepted until dependencies are completed.")

    def complete_quest(self, quest_name):
        for quest in self.active_quests:
            if quest.name == quest_name and quest.is_completed:
                self.active_quests.remove(quest)
                print(f"Quest '{quest.name}' removed from active quests.")
                return
            elif quest.name == quest_name:
                print(f"Quest '{quest.name}' is not yet completed.")
                return
        print("Quest not found!")

    def show_active_quests(self):
        print("Active Quests:")
        for quest in self.active_quests:
            status = "Completed" if quest.is_completed else "Active"
            print(f"{quest.name} - {status} ({quest.difficulty}): {quest.description} [Type: {quest.quest_type}]")
            print(f"Current Stage: {quest.current_stage}/{quest.total_stages} | Rewards: {quest.rewards}")

    def complete_stage(self, quest_name):
        for quest in self.active_quests:
            if quest.name == quest_name:
                completed = quest.complete_stage()
                if completed:
                    # Give rewards to the player here
                    print(f"You received rewards: {quest.rewards}!")
                return
        print("Quest not found!")
