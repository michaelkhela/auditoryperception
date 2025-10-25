import pygame
import sys
import math

# Initialize pygame
pygame.init()
SLIDE_WIDTH = 1200
screen = pygame.display.set_mode((SLIDE_WIDTH, 800))
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 22)
title_font = pygame.font.SysFont("Arial", 32, bold=True)
caption_font = pygame.font.SysFont("Arial", 20, italic=True)

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GOLD = (204, 153, 0)
BLACK = (0, 0, 0)

# Load and scale images
def load_image(path, size):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

# Update these paths to your system
pinna_img     = load_image('/Users/michaelkhela/Desktop/Perception/Unknown.jpeg',        (250, 250))
ear_canal_img = load_image('/Users/michaelkhela/Desktop/Perception/Screenshot 2025-04-08 at 8.33.18\u202fPM.png', (250, 250))
tympanic_img  = load_image('/Users/michaelkhela/Desktop/Perception/Unknown-2.jpeg',      (250, 250))
ossicles_img  = load_image('/Users/michaelkhela/Desktop/Perception/Screenshot 2025-04-08 at 8.32.59\u202fPM.png', (250, 250))
cochlea_img   = load_image('/Users/michaelkhela/Desktop/Perception/Screenshot 2025-04-17 at 4.25.52 PM.png', (250, 250))
nerve_img     = load_image('/Users/michaelkhela/Desktop/Perception/Screenshot 2025-04-17 at 4.25.29 PM.png', (250, 250))
brainstem_img = load_image('/Users/michaelkhela/Desktop/Perception/Unknown-5.jpeg',      (250, 250))
thalamus_img  = load_image('/Users/michaelkhela/Desktop/Perception/Unknown-6.jpeg',      (250, 250))
cortex_img    = load_image('/Users/michaelkhela/Desktop/Perception/Unknown-7.jpeg',      (250, 250))

# Image positions (offset each by slide width)
image_positions = [
    None,  # Slide 0: no image, just sound wave in air
    (SLIDE_WIDTH * 1 + 475, 200, pinna_img, "Pinna"),
    (SLIDE_WIDTH * 2 + 475, 200, ear_canal_img, "Ear Canal"),
    (SLIDE_WIDTH * 3 + 475, 200, tympanic_img, "Tympanic Membrane"),
    (SLIDE_WIDTH * 4 + 475, 200, ossicles_img, "Ossicles"),
    (SLIDE_WIDTH * 5 + 475, 200, cochlea_img, "Cochlea"),
    (SLIDE_WIDTH * 6 + 475, 200, cochlea_img, "Cochlea"),
    (SLIDE_WIDTH * 7 + 475, 200, nerve_img, "Auditory Nerve"),
    (SLIDE_WIDTH * 8 + 475, 200, brainstem_img, "Brainstem"),
    (SLIDE_WIDTH * 9 + 475, 200, thalamus_img, "Thalamus"),
    (SLIDE_WIDTH * 10 + 475, 200, cortex_img, "Auditory Cortex")
]

captions = [
    "The vibration of objects causes the air to be shifted thus producing sound waves, which are captured by the outer ear. Initially, these sound waves reach the Pinna–the part of the ear that is visible.",
    "The pinna funnels sound waves into the auditory/ear canal. Sound waves are transmitted from the pinna to the auditory canal (also known as the ear canal).",
    "Sound travels down the ear canal toward the eardrum. By traveling through a long, narrow tunnel-like figure, the frequency (which is perceived by us as pitch) of the sound is enhanced. Eventually, this sound reaches the Tympanic membrane (also known as the eardrum) that is located at the end of the ear canal.",
    "Sound hits the tympanic membrane, causing it to vibrate. The tympanic membrane is a thin sheet of skin located at the end of the ear canal and acts as a protective barrier, separating the outer ear from its internal structures. As sound waves reach the tympanic membrane/eardrum, it vibrates.",
    "The sound now enters the middle ear as it passes the eardrum. It reaches three tiny bone structures–the tiniest bones of the human body– located just behind the eardrum called the ossicles. These bones work like levers due to their hinged joints, meaning that the movement cascades from the first ossicle until the last. The ossicle that is directly connected to the eardrum and first receives the vibrations from the Tympanic membrane is called the Malleus. The vibrations then travel through the Incus–the middle ossicle–onto the Stapes, which is connected to the oval window of the cochlea. These structures are responsible for the amplification of sound (what we perceive as how loud a sound is). By amplifying the sound as it arrives in the inner ear, the ossicles help intensify faint sounds that might otherwise go unheard, which is essential as the sound travels from air to fluid since it takes more energy to generate a sound wave in fluid.",
    "When the stapes–the last ossicle to move– vibrates, it moves the oval window that it is attached to back and forth. This is the barrier that separates the middle ear from the inner ear–much like the tympanic membrane which separates the outer ear from the middle ear, yet about 20 times smaller. The movement of the oval window leads to pressure changes in the cochlea–a spiral structure in the inner ear with three parallel canals that are filled with fluid.",
    "As the sound waves travel into the cochlea, the fluid within one of its canals–the vestibular canal–vibrates and leads to displacements of about 14,000 hair cells in the Organ of Corti within the cochlea and these can either send auditory information to the brain (using afferent fibers) or interpret information from the brain (using efferent fibers). Following the vibrations throughout the cochlea, the tectorial membrane moves across the Organ of Corti, which bends the stereocilia (tiny hair-like structures) on the inner hair cells. The bending of these hair cells is powerful enough to cause a voltage change (due to the opening of ion channels), which releases neurotransmitters. This action–which is called transduction– is an integral part of the auditory pathway, since it ultimately leads to signals being sent to the brain stem which initiates the cognitive process of auditory perception.",
    "The auditory signals sent from transduction travel through a nerve pathway called the 8th cranial nerve, bringing these signals to the brainstem.",
    "Afferent auditory nerve fires first synapse (the connection between neurons that allows information to transfer) at a location on the brainstem called the cochlear nucleus.",
    "Auditory signals pass through the medial geniculate nucleus, which is a part of the thalamus that interprets signals from the temporal cortex and receives input from the auditory cortex.",
    "Signals arrive at the primary auditory cortex, the area of the brain responsible for processing and interpreting sounds. This area has three regions: the core, the belt Area, and the Parabelt Area. In the belt and parabelt area, neurons interpret more complex characteristics of sounds. The parabelt area also interprets information from other senses to factor into the audio perception. After being interpreted in the Auditory Cortex we are able to fully perceive the noises in our environment, interpreting the unique combination of amplitude, frequency, and timbre to come to conclusions about what we hear."
]

def label(text, x, y):
    txt = font.render(text, True, BLACK)
    screen.blit(txt, txt.get_rect(center=(x, y)))

def draw_title():
    txt = title_font.render("The Auditory Pathway by Michael Khela and Sophia Gaitanis", True, BLACK)
    screen.blit(txt, txt.get_rect(center=(SLIDE_WIDTH // 2, 40)))

def draw_caption(text):
    caption_rect = pygame.Rect(50, 500, 1100, 260)
    pygame.draw.rect(screen, WHITE, caption_rect)
    wrapped = wrap_text(text, caption_font, caption_rect.width)
    for i, line in enumerate(wrapped):
        caption = caption_font.render(line, True, BLACK)
        line_rect = caption.get_rect(center=(caption_rect.centerx, caption_rect.y + i * 22))
        screen.blit(caption, line_rect)

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current = ''
    for word in words:
        test = current + word + ' '
        if font.size(test)[0] < max_width:
            current = test
        else:
            lines.append(current)
            current = word + ' '
    lines.append(current)
    return lines

def draw_wave(x, y):
    center_x = SLIDE_WIDTH // 2
    points = [(center_x + i, y + math.sin(i / 20 * 2 * math.pi) * 10) for i in range(-50, 50, 4)]
    if len(points) > 1:
        pygame.draw.lines(screen, BLUE, False, points, 4)

def draw_vibration(x, y, frame):
    offset = math.sin(frame / 5.0) * 10
    pygame.draw.ellipse(screen, BLUE, (x - 30 + offset, y - 30, 60, 60), 4)
    pygame.draw.ellipse(screen, BLUE, (x - 40 - offset, y - 40, 80, 80), 2)

def draw_pulse(x, y, frame):
    if frame % 20 < 10:
        pygame.draw.circle(screen, GOLD, (int(x), int(y)), 15)

def draw_slide(index, frame):
    offset_x = -index * SLIDE_WIDTH
    screen.fill(WHITE)
    draw_title()

    # Draw main image and label if present
    if index > 0:
        for i, pos in enumerate(image_positions):
            if pos is None:
                continue
            x, y, img, label_text = pos
            screen.blit(img, (x + offset_x, y))
            label(label_text, x + offset_x + img.get_width() // 2, y + img.get_height() + 20)

    # Draw wave, vibration, or pulse
    if index == 0:
        draw_wave(0, 300)
    elif index <= 3:
        x, y, _, _ = image_positions[index]
        draw_wave(x + offset_x + 125, y + 50)
    elif index == 4:
        x, y, _, _ = image_positions[index]
        draw_vibration(x + offset_x + 125, y + 125, frame)
    elif index >= 5:
        x, y, _, _ = image_positions[index]
        draw_pulse(x + offset_x + 125, y + 125, frame)

    draw_caption(captions[index])

# Main loop
def slideshow():
    index = 0
    frame = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and index < len(captions) - 1:
                    index += 1
                elif event.key == pygame.K_LEFT and index > 0:
                    index -= 1

        draw_slide(index, frame)
        pygame.display.flip()
        clock.tick(60)
        frame += 1

# Run it
slideshow()
