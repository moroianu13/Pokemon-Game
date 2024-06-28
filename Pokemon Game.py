import random
import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.SysFont("Engravers MT", 36)
DELAY_BETWEEN_ATTACKS = 3  # Delay in seconds between attacks
SKILL_DURATION = 2  # Duration in seconds for each skill image to be shown

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Battle")

# Function to resize images proportionally
def resize_image(image, size):
    return pygame.transform.scale(image, size)

# Function to load sound
def load_sound(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        print(f"{file_path} sound loaded successfully.")
        return sound
    except pygame.error as e:
        print(f"Error loading {file_path} sound: {e}")
        return None

# Load images
sian_quake_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Ario\Char Ario.png"), (200, 200))
skaravenj_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Char.png"), (200, 200))
afklax_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Maik\Maik_char.png"), (200, 200))
background_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\logo.webp"), (WIDTH, HEIGHT))
wisomantix_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Wiso-removebg-preview.png"), (200, 200))
saturncoin_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Sophia\Comercia2-ezgif.com-webp-to-jpg-converter (1).png"), (200, 200))
professor_piet_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\Professor Piet.webp"), (200, 200))
logo_img = resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\logo.webp"), (WIDTH, HEIGHT))

# Load and resize skill images
def load_skill_images(paths):
    return [resize_image(pygame.image.load(path), (150, 150)) for path in paths]

wisomantix_skill_imgs = load_skill_images([
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Data Vision.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Mystic Smoke skill..webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Cyber Meditation skill..webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Quantum Leap skill.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Ancient Wisdom skill..webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Digital Shield skill.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\Enlightened Strike skill.webp"
])

skaravenj_skill_imgs = load_skill_images([
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Artic_Scream_Skill.jpeg",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Frost_Wings_Skill.jpeg",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Glacial_Regeneration_Skill.png",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Ice_Claws_Skill.jpeg",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Ice_Mastery_Skill.jpeg",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Shadow_Of_The_Night_Skill.jpeg"
])

professor_piet_skill_imgs = load_skill_images([
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Alchemy Burst.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Code Alchemy.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Elemental Infusion.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Potion Mastery.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Rune Casting.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Transmutation.webp"
])

saturncoin_skill_imgs = load_skill_images([
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Sophia\banckcrupsy attack.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Sophia\Inflation Attack.webp"
])

afklax_skill_imgs = load_skill_images([
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Maik\skills\Munch.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Maik\skills\Rest.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Maik\skills\Snore.webp"
])

sian_quake_skill_imgs = load_skill_images([
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Ario\skills\Earthquake spell.webp",
    r"C:\Users\moroi\OneDrive\Desktop\pokemon\Ario\skills\Rock Throw spell.webp"
])

# Load arena images
arenas = [
    resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\Zalman arena.webp"), (WIDTH, HEIGHT)),
    resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\AFKlax arena.webp"), (WIDTH, HEIGHT)),
    resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\Saturncoin arena.webp"), (WIDTH, HEIGHT)),
    resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\Skaravenj arena.webp"), (WIDTH, HEIGHT)),
    resize_image(pygame.image.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\Wisomantix arena.webp"), (WIDTH, HEIGHT))
]

# Load attack sounds for Wisomantix
data_vision_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\data_vision.mp3")
mystic_smoke_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\mystic_smoke.mp3")
cyber_meditation_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\cyber_meditation.mp3")
quantum_leap_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\quantum_leap.mp3")
ancient_wisdom_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\ancient wisdome.mp3")
digital_shield_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\digital_shield.mp3")
enlightened_strike_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Adrian\enlightened_strike.mp3")

# Load attack sounds for Skaravenj
artic_scream_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Artic_Scream.mp3")
frost_wings_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Frost_Wings.mp3")
glacial_regeneration_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Glacial_Regeneration.mp3")
ice_claws_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Ice_Claws.mp3")
ice_mastery_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Ice_Mastery.mp3")
shadow_of_the_night_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Damien\Shadow_Of_The_Night.mp3")

# Load attack sound for AFKlax
afklax_attack_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Maik\Atack Sound.mp3")

# Load attack sounds for Saturncoin
bankcrupsy_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Sophia\bankcrupsy_attack.wav")
inflation_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Sophia\inflation_attack.mp3")

# Load attack sounds for Sian Quake
earthquake_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Ario\skills\Eartquake.mp3")
rock_throw_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Ario\skills\Rock_Throw.mp3")

# Load attack sounds for Professor Piet
alchemy_burst_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Alchemy Burst.mp3")
code_alchemy_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Code Alchemy.mp3")
elemental_infusion_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Elemental Infusion.wav")
potion_mastery_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Potion Mastery.wav")
rune_casting_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Rune Casting.mp3")
transmutation_sound = load_sound(r"C:\Users\moroi\OneDrive\Desktop\pokemon\Piet\skills\Transmutation.mp3")

# Classes
class AttackSkill:
    def __init__(self, attack, damage, sound=None, image=None):
        self.attack = attack
        self.damage = damage
        self.sound = sound
        self.image = image

class Pokemon:
    def __init__(self, name, health, image):
        self.name = name
        self.health = health
        self.skills = []
        self.counter = 0
        self.image = image

    def learn_attack_skill(self, newskill):
        self.skills.append(newskill)

    def show_status(self, screen, x, y):
        health_text = max(0, self.health)  # Ensure health does not go below 0
        text = FONT.render(f"{self.name} - Health: {health_text}", True, BLACK)
        screen.blit(text, (x, y - 40))
        pygame.draw.rect(screen, RED, (x, y, 200, 20))
        pygame.draw.rect(screen, GREEN, (x, y, 200 * (self.health / 100), 20))
        # Show Pokémon name below health bar
        name_text = FONT.render(self.name, True, BLACK)
        screen.blit(name_text, (x, y + 30))

    def is_alive(self):
        return self.health > 0

    def animate_health_change(self, screen, original_health, opponent):
        steps = 30
        health_change = (self.health - original_health) / steps
        for step in range(steps):
            current_health = original_health + health_change * step
            screen.blit(current_arena, (0, 0))  # Draw the background
            self.show_status(screen, 20, 20)
            opponent.show_status(screen, WIDTH - 220, 20)
            screen.blit(self.image, (50, HEIGHT // 2 - 100))  # Display the attacking Pokémon image on the left
            screen.blit(opponent.image, (WIDTH - 250, HEIGHT // 2 - 100))  # Display the opponent Pokémon image on the right
            pygame.display.flip()
            pygame.time.wait(30)
        self.show_status(screen, 20, 20)
        opponent.show_status(screen, 920, 20)

    def attack(self, skill_name, opponent, screen):
        if not self.is_alive() or not opponent.is_alive():
            return

        for skill in self.skills:
            if skill.attack == skill_name:
                original_health = opponent.health
                opponent.health -= skill.damage
                self.counter += 1
                message = f"{self.name} attacks {opponent.name} with {skill_name}, causing {skill.damage} damage."

                # Play skill sound and show skill image
                if skill.sound:
                    print(f"Playing {skill_name} sound.")
                    skill.sound.play()
                if skill.image:
                    screen.blit(current_arena, (0, 0))  # Draw the background
                    self.show_status(screen, 20, 20)  # Show status for the first Pokémon
                    opponent.show_status(screen, WIDTH - 220, 20)  # Show status for the second Pokémon
                    screen.blit(self.image, (50, HEIGHT // 2 - 100))  # Display the attacking Pokémon image on the left
                    screen.blit(opponent.image, (WIDTH - 250, HEIGHT // 2 - 100))  # Display the opponent Pokémon image on the right
                    screen.blit(skill.image, (WIDTH // 2 - skill.image.get_width() // 2, HEIGHT // 2 - skill.image.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(SKILL_DURATION)
                    if skill.sound:
                        skill.sound.stop()  # Stop the skill sound

                self.display_attack(opponent, screen, message)
                opponent.animate_health_change(screen, original_health, self)
                return

        message = f"{self.name} does not know the skill {skill_name}."
        self.display_message(screen, message)

    def display_attack(self, opponent, screen, message):
        screen.blit(current_arena, (0, 0))  # Draw the background
        self.show_status(screen, 20, 20)  # Show status for the first Pokémon
        opponent.show_status(screen, WIDTH - 220, 20)  # Show status for the second Pokémon
        screen.blit(self.image, (50, HEIGHT // 2 - 100))  # Display the attacking Pokémon image on the left
        screen.blit(opponent.image, (WIDTH - 250, HEIGHT // 2 - 100))  # Display the opponent Pokémon image on the right
        text = FONT.render(message, True, RED)
        screen.blit(text, (20, HEIGHT - 40))
        pygame.display.flip()
        time.sleep(2)

    def display_message(self, screen, message):
        screen.blit(current_arena, (0, 0))  # Draw the background
        text = FONT.render(message, True, RED)
        screen.blit(text, (20, HEIGHT - 40))
        pygame.display.flip()
        time.sleep(2)

def display_winner(screen, winner_name, winner_image):
    screen.blit(logo_img, (0, 0))  # Use the logo image as background
    text = FONT.render(f"{winner_name} wins!", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 150))
    screen.blit(winner_image, (WIDTH // 2 - winner_image.get_width() // 2, HEIGHT // 2 - winner_image.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)

def announce_fight(screen, pokemon1, pokemon2):
    screen.blit(logo_img, (0, 0))  # Use the logo image as background
    text = FONT.render(f"{pokemon1.name} VS {pokemon2.name}", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    time.sleep(3)

# Initialize Pokemons
wisomantix = Pokemon("Wisomantix", 150, wisomantix_img)
sian_quake = Pokemon("Sian_Quake", 95, sian_quake_img)
skaravenj = Pokemon("Skaravenj", 130, skaravenj_img)
afklax = Pokemon("AFKlax", 120, afklax_img)
saturncoin = Pokemon("Saturncoin", 110, saturncoin_img)
professor_piet = Pokemon("Professor Piet", 140, professor_piet_img)

# Initialize Skills for Wisomantix
wisomantix.learn_attack_skill(AttackSkill("Data Vision", 50, data_vision_sound, wisomantix_skill_imgs[0]))
wisomantix.learn_attack_skill(AttackSkill("Mystic Smoke", 20, mystic_smoke_sound, wisomantix_skill_imgs[1]))
wisomantix.learn_attack_skill(AttackSkill("Cyber Meditation", 0, cyber_meditation_sound, wisomantix_skill_imgs[2]))
wisomantix.learn_attack_skill(AttackSkill("Quantum Leap", 0, quantum_leap_sound, wisomantix_skill_imgs[3]))
wisomantix.learn_attack_skill(AttackSkill("Ancient Wisdom", 0, ancient_wisdom_sound, wisomantix_skill_imgs[4]))
wisomantix.learn_attack_skill(AttackSkill("Digital Shield", 0, digital_shield_sound, wisomantix_skill_imgs[5]))
wisomantix.learn_attack_skill(AttackSkill("Enlightened Strike", 60, enlightened_strike_sound, wisomantix_skill_imgs[6]))

# Initialize Skills for Skaravenj
skaravenj.learn_attack_skill(AttackSkill('Artic Scream', 50, artic_scream_sound, skaravenj_skill_imgs[0]))
skaravenj.learn_attack_skill(AttackSkill('Frost Wings', 30, frost_wings_sound, skaravenj_skill_imgs[1]))
skaravenj.learn_attack_skill(AttackSkill('Ice Claws', 60, ice_claws_sound, skaravenj_skill_imgs[3]))
skaravenj.learn_attack_skill(AttackSkill('Ice Mastery', 40, ice_mastery_sound, skaravenj_skill_imgs[4]))
skaravenj.learn_attack_skill(AttackSkill('Glacial Regeneration', 0, glacial_regeneration_sound, skaravenj_skill_imgs[2]))
skaravenj.learn_attack_skill(AttackSkill('Shadow of the Night', 40, shadow_of_the_night_sound, skaravenj_skill_imgs[5]))

# Initialize Skills for AFKlax
afklax.learn_attack_skill(AttackSkill("Rest", 0, afklax_attack_sound, afklax_skill_imgs[1]))
afklax.learn_attack_skill(AttackSkill("Munch", 30, afklax_attack_sound, afklax_skill_imgs[0]))
afklax.learn_attack_skill(AttackSkill("Snore", 50, afklax_attack_sound, afklax_skill_imgs[2]))

# Initialize Skills for Saturncoin
saturncoin.learn_attack_skill(AttackSkill("Bankcrupsy", 40, bankcrupsy_sound, saturncoin_skill_imgs[0]))
saturncoin.learn_attack_skill(AttackSkill("Inflation", 50, inflation_sound, saturncoin_skill_imgs[1]))

# Initialize Skills for Sian_Quake
sian_quake.learn_attack_skill(AttackSkill("Earthquake", 40, earthquake_sound, sian_quake_skill_imgs[0]))
sian_quake.learn_attack_skill(AttackSkill("Rock Throw", 30, rock_throw_sound, sian_quake_skill_imgs[1]))

# Initialize Skills for Professor Piet
professor_piet.learn_attack_skill(AttackSkill("Alchemy Burst", 45, alchemy_burst_sound, professor_piet_skill_imgs[0]))
professor_piet.learn_attack_skill(AttackSkill("Code Alchemy", 35, code_alchemy_sound, professor_piet_skill_imgs[1]))
professor_piet.learn_attack_skill(AttackSkill("Elemental Infusion", 50, elemental_infusion_sound, professor_piet_skill_imgs[2]))
professor_piet.learn_attack_skill(AttackSkill("Potion Mastery", 40, potion_mastery_sound, professor_piet_skill_imgs[3]))
professor_piet.learn_attack_skill(AttackSkill("Rune Casting", 30, rune_casting_sound, professor_piet_skill_imgs[4]))
professor_piet.learn_attack_skill(AttackSkill("Transmutation", 55, transmutation_sound, professor_piet_skill_imgs[5]))

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    # Start background music
    pygame.mixer.music.load(r"C:\Users\moroi\OneDrive\Desktop\pokemon\media\RPG Battle Music _ Enter The Arena.mp3.mp3")
    pygame.mixer.music.play(-1)

    pokemons = [wisomantix, sian_quake, skaravenj, afklax, saturncoin, professor_piet]
    random.shuffle(pokemons)  # Shuffle the Pokémon for random matchups

    def battle(pokemon1, pokemon2):
        global current_arena
        current_arena = random.choice(arenas)
        announce_fight(screen, pokemon1, pokemon2)
        while pokemon1.is_alive() and pokemon2.is_alive():
            screen.blit(current_arena, (0, 0))  # Draw the background
            pokemon1.show_status(screen, 20, 20)  # Show status for the first Pokémon
            pokemon2.show_status(screen, WIDTH - 220, 20)  # Show status for the second Pokémon
            screen.blit(pokemon1.image, (50, 100))  # Display the attacking Pokémon image on the left
            screen.blit(pokemon2.image, (WIDTH - 250, 100))  # Display the opponent Pokémon image on the right
            pygame.display.flip()

            # Pokémon 1 attacks Pokémon 2
            skill = random.choice(pokemon1.skills)
            pokemon1.attack(skill.attack, pokemon2, screen)
            time.sleep(DELAY_BETWEEN_ATTACKS)  # Add delay between attacks

            if not pokemon2.is_alive():
                return pokemon1  # Pokémon 1 wins

            # Pokémon 2 attacks Pokémon 1
            skill = random.choice(pokemon2.skills)
            pokemon2.attack(skill.attack, pokemon1, screen)
            time.sleep(DELAY_BETWEEN_ATTACKS)  # Add delay between attacks

        return pokemon2  # Pokémon 2 wins

    # First round
    winner1 = battle(pokemons[0], pokemons[1])
    winner2 = battle(pokemons[2], pokemons[3])
    winner3 = battle(pokemons[4], pokemons[5])

    # Second round
    semifinal_winner1 = battle(winner1, winner2)
    semifinal_winner2 = winner3  # Winner of match 3 goes to the final directly

    # Final
    ultimate_winner = battle(semifinal_winner1, semifinal_winner2)

    # Display the ultimate winner
    display_winner(screen, ultimate_winner.name, ultimate_winner.image)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
