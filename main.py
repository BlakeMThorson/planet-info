# https://stackoverflow.com/questions/62656633/lambda-function-for-sortkey-in-python
# https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators

planet_info = [
  {
    "name": "Jupiter",
    "mass_kg": 1898200000000000000000000000,
    "distance_km" : 777908928,
    "moons" : ["Io", "Europa", "Ganymede", "Callisto"]
  },
  {
    "name": "Mercury",
    "mass_kg": 330110000000000000000000,
    "distance_km": 70000000,
    "moons": []
  },
  {
    "name": "Venus",
    "mass_kg": 4867500000000000000000000,
    "distance_km": 108940000,
    "moons": []
  },
  {
    "name": "Earth",
    "mass_kg": 5972168000000000000000000,
    "distance_km": 152097597,
    "moons": ["The Moon"]
  },
  {
    "name": "Mars",
    "mass_kg": 641710000000000000000000,
    "distance_km": 249261000,
    "moons": ["Phobos,"]
  },
  {
    "name": "Saturn",
    "mass_kg": 568340000000000000000000000,
    "distance_km": 1514498923,
    "moons": ["Titan", "Rhea", "Lapetus", "Dione", "Tethys"]
  },
  {
    "name": "Uranus",
    "mass_kg": 86810000000000000000000000,
    "distance_km": 3006393609,
    "moons": ["Titania", "Oberon", "Umbriel", "Ariel", "Miranda"]
  },
  {
    "name": "Neptune",
    "mass_kg": 102409000000000000000000000,
    "distance_km": 4537303418,
    "moons": ["Triton", "Proteus", "Nereid", "Larissa", "Galatea"]
  }
]

all_planets = []

# MAIN PLANET CLASS
class Planet:
  def __init__(self, name="", mass=0, distance_from_sun=0, moons=[]):
    self.name = name
    self.mass = mass
    self.distance_from_sun = distance_from_sun
    self.moons = moons

  def print(self):
    print(f"""
{self.name}:
  - Mass : {self.mass:,} kg
  - Distance from the sun at aphelion : {self.distance_from_sun:,} km
  - Moons : {", tel".join(self.moons) if len(self.moons) > 0 else "None"}.
""")

for planet in planet_info:
  all_planets.append(Planet(planet["name"], planet["mass_kg"], planet["distance_km"], planet["moons"]))

title = """________________________________________________
**************** PLANET INFO *******************
************** BY BLAKE THORSON ****************
________________________________________________"""

menu = """Available Options :
- List all planets alphabetically.
- List all planets by distance.
- Tell me about ___.
- How massive is ___?
- Is ___ in the list of planets?
- How many moons does ___ have?
- Name the moons of ___.
- How far is ___ from the sun?
- How far is ___ from ___?
- Compare mass for ___ and ___
- See Options
- Quit
Example : "How far is Earth from the sun?" 
"""

def get_planet_object_from_name(command, starting_index, ending_index = 0):
  name = ""
  if len(command) < starting_index or len(command) < ending_index:
    print("I don't think you input a planet, please try again")
  else:
    name = command[starting_index:ending_index] if ending_index != 0 else command[starting_index:]
    planet = get_planet_from_name(name)
    if planet:
      return planet
    else:
      return None

def get_planet_from_name(name):
  found_planet = None

  for planet in all_planets:
    if planet.name == name.title():
      found_planet = planet

  if found_planet:
    return found_planet
  else:
    print(f"You requested info on the planet '{name}', which doesn't exist. Please try again.")
    return None


def handle_command(command):
  # - List all planets alphabetically.
  if command == "list all planets alphabetically":
    names = [planet.name for planet in all_planets]
    names.sort()
    print(", ".join(names) + ".")
  # - List all planets by distance.
  elif command == "list all planets by distance":
    distance_sort = sorted(all_planets, key = lambda planet: planet.distance_from_sun )
    print(", ".join([planet.name for planet in distance_sort]) + ".")
  # - Tell me about ___.
  elif command.startswith("tell me about"):
    planet = get_planet_object_from_name(command, 14)
    if planet:
      planet.print()
  # - How massive is ___?
  elif command.startswith("how massive is"):
    planet = get_planet_object_from_name(command, 15)
    if planet:
      print(f"{planet.name} weighs {planet.mass:,} kg.")
  # - Is ___ in the list of planets?
  elif command.endswith("in the list of planets") and command.startswith("is"):
    planet_name = command[3: command.index(" in the list")]
    if planet_name.title() in [planet.name for planet in all_planets]:
      print(f"Yes, '{planet_name}' is in the list of planets.")
    else:
      print(f"No, '{planet_name}' is not in the list of planets.")
  # - How many moons does ___ have?
  elif command.startswith("how many moons does") and command.endswith("have"):
    planet = get_planet_object_from_name(command, 20, command.index(" have"))
    if planet:
      print(f"{planet.name} has {len(planet.moons)} moon{"s" if len(planet.moons) != 1 else ""}.")
  # - Name the moons of ___.
  elif command.startswith("name the moons of"):
    planet = get_planet_object_from_name(command, 18)
    if planet:
      if len(planet.moons) > 1:
        print(f"{planet.name} has the following moons: {", ".join(planet.moons)}.")
      elif len(planet.moons) == 1:
        print(f"{planet.name} has the following moon: {planet.moons[0]}.")
      else:
        print(f"{planet.name} has no moons.")
  # - How far is ___ from the sun?
  elif command.startswith("how far is") and command.endswith("from the sun"):
    planet = get_planet_object_from_name(command, 11, command.index(" from the sun"))
    if planet:
      print(f"{planet.name} is {planet.distance_from_sun:,}km from the sun at its aphelion.")
  # - How far is ___ from ___?
  elif command.startswith("how far is"):
    first_planet = get_planet_object_from_name(command, 11, command.index(" from"))
    second_planet = get_planet_object_from_name(command, command.index(" from") + 6)
    if first_planet and second_planet:
      print(f"{first_planet.name} is {abs(first_planet.distance_from_sun - second_planet.distance_from_sun):,}km away from {second_planet.name}")
  # - Compare mass for ___ and ___
  elif command.startswith("compare mass for"):
    first_planet = get_planet_object_from_name(command, 17, command.index(" and"))
    second_planet = get_planet_object_from_name(command, command.index(" and") + 5)
    if first_planet and second_planet:
      print(f"{first_planet.name} is {abs(first_planet.mass - second_planet.mass):,}kg {"lighter" if first_planet.mass < second_planet.mass else "heavier"} than {second_planet.name}")
  # - See Options
  elif command == "see options":
    print(menu)
  # - Quit
  elif command == "quit":
    print("Goodbye!")
  else:
    print("Invalid command was given, please type 'See options' for all valid inputs.")


if __name__ == "__main__":
  print(title)
  print(menu)

  command = ""

  while command != "quit":
    command = input("> ").lower().replace("?","").replace(".","")
    handle_command(command)