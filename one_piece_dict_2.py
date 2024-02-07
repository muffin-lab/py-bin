pirate_list = [
  {"name": "Luffy", "group": "Strawhat Pirates", "power": "Hito Hito no Mi"},
  {"name": "Zorro", "group": "Strawhat Pirates", "power": "Three Sword Style"},
  {"name": "Ace", "group": "Whitebeard Pirates", "power": "Mera Mera no Mi"},
  {"name": "Sabo","group": "Revolutionary Army", "power": "Mera Mera no Mi"},
]

for pl in pirate_list:
  print(pl["name"], pl["group"], sep=", ")