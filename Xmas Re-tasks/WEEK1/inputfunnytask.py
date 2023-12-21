print("Enter number of lives.")
lives = int(input())

print("enter energy level.")
energy = int(input())

shield = int(input("enter shield level."))

lives_str = '♥ ' * lives
energy_str = '♦ ' * energy
shield_str = '♦ ' * shield

print("health has been set.")
print("lives: " + lives_str)
print("energy: " + energy_str)
print("shield: " + shield_str)
