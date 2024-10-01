# Game Design Document (GDD)

## 1. Game Overview
- **Title**: Quest for the Lost Relics
- **Genre**: Multiplayer Turn-Based RPG
- **Platform**: PC (Python with Pygame)
- **Elden Ring style game**: elden ring style gameplay

## 2. Game Mechanics
- **Combat System**: 
  - Turn-based combat allowing for imaginative strategies.
  - Combos and elemental weaknesses will be crucial in battle.
  - Players can join raid parties to tackle larger enemies together.
- **Leveling System**: 
  - Experience points (XP) per level.
  - Players receive skill points to invest in skills, stats, or spells.
  - Skills require a minimum stat level for learning (e.g., mana for mages).
- **Quests**:
  - Basic quests to start with, evolving into more complex, lore-rich quests.
  - Quests will be categorized by difficulty: Common, Uncommon, Rare, Epic, Legendary.
  - Include faction-based quests tied to the overarching storyline.

## 3. World Structure
- **Map Design**: 
  - A massive open world (1000x1000) with detailed fog of war.
  - Procedural generation to create diverse terrain types (ice, fire, forest, etc.).
  - Main map shows details of the current chunk; mini-map shows an overview of the world (could be chunks, could be more open)
- **Elemental Regions**: 
  - Each region is themed around an elemental type with unique mobs and bosses.
  - Corruption spreads from specific points, affecting the environment and creatures.
  - Regions denoted by different letters on minimap

## 4. Lore
- **Backstory**: 
  - The Elemental Cataclysm fractured the world; now a dark force seeks to corrupt the elemental energies.
- **Elemental Titans and the Corrupted One**: 
  - Players will face both elemental and corrupted versions of bosses.
- **Quest Integration**: 
  - Uncovering the history of the Cataclysm while combating the corruption.

## 5. Technical Design
- **Architecture**: 
  - Server-client structure for multiplayer functionality.
  - Consider using Python sockets for networking.
  - Multiplayer style game - collaboration, raid parties and chat
  - Raid parties for harder bosses, and 
- **Map Generation**: 
  - Use noise functions or grid-based approaches for terrain generation.
  - Chunk system to load and unload areas dynamically.
- **AI Design**: 
  - Different behaviors for elemental and corrupted creatures.
  - NPCs will provide quests and trading opportunities.

## 6. Art Style
- **ASCII Art**: 
  - Use ASCII art for characters, creatures, and environments for a text-based experience.
  - Top down view of surroundings
- **User Interface**: 
  - Simple and intuitive UI for navigation and interaction.
