class LoreEntry:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class LoreManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def display_lore(self):
        print("Lore Entries:")
        for entry in self.entries:
            print(f"{entry.title}: {entry.content}")
