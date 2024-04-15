# import the necessary libraries
import pygame
import math
import os
import png

# initialize pygame 
pygame.init()

# set the window size using the set_mode () function 
size = (800,800)
screen = pygame.display.set_mode(size)

# set the title of the window using the set_caption() function
pygame.display.set_caption("Project Solar System Visualizer")

# load images for each planet
sun_image = pygame.image.load(os.path.join("planets", "sun.png"))
mercury_image = pygame.image.load(os.path.join("planets", "mercury.png"))
venus_image = pygame.image.load(os.path.join("planets", "venus.png"))
earth_image = pygame.image.load(os.path.join("planets", "earth.png"))
mars_image = pygame.image.load(os.path.join("planets", "mars.png"))
jupiter_image = pygame.image.load(os.path.join("planets", "jupiter.png"))
saturn_image = pygame.image.load(os.path.join("planets", "saturn.png"))
uranus_image = pygame.image.load(os.path.join("planets", "uranus.png"))
neptune_image = pygame.image.load(os.path.join("planets", "neptune.png"))

# load background images
background_image = pygame.image.load(os.path.join("planets", "space.png"))

# resize image size of the planet using transform.scale()
sun_image = pygame.transform.scale(sun_image, (80,80))
mercury_image = pygame.transform.scale(mercury_image, (15,15))
venus_image = pygame.transform.scale(venus_image, (25,25))
earth_image = pygame.transform.scale(earth_image, (30,30))
mars_image = pygame.transform.scale(mars_image, (20,20))
saturn_image = pygame.transform.scale(saturn_image, (100,40))
uranus_image = pygame.transform.scale(uranus_image, (35,35))
jupiter_image = pygame.transform.scale(jupiter_image, (50,50))
neptune_image = pygame.transform.scale(neptune_image, (40,40))

# create a list of planets with their properties like distance, period and radius
planets = [{"name": "Sun", "image": sun_image, "radius": 200, "x": 400,"y": 390,"vx":0,"vy":0},
{"name": "Mercury", "image": mercury_image, "angle": 200, "distance": 65,"period": 0.24,"radius":10},
{"name": "Venus", "image": venus_image, "angle": 0, "distance": 90,"period": 0.62,"radius":20},
{"name": "Earth", "image": earth_image, "angle": 0, "distance": 125,"period": 1,"radius":25},
{"name": "Mars", "image": mars_image, "angle": 0, "distance": 155,"period": 1.88,"radius":15},
{"name": "Jupiter", "image": jupiter_image, "angle": 0, "distance": 195,"period": 11.86,"radius":45},
{"name": "Saturn", "image": saturn_image, "angle": 0, "distance": 260,"period": 29.5,"radius":40},
{"name": "Uranus", "image": uranus_image, "angle": 0, "distance": 320,"period": 84,"radius":30},
{"name": "Neptune", "image": neptune_image, "angle": 0, "distance": 370,"period": 164.8,"radius":35}]

# initiate the positions of the planets
for planet in planets [1:]:
    planet["x"] = planets[0]["x"] + math.cos(planet["angle"])*planet["distance"]
    planet["y"] = planets[0]["y"] + math.sin(planet["angle"])*planet["distance"]

# create a list of past positions for each planet
for planet in planets[1:]:
    planet["past _positions"] = []

# set the clock to control framerate
clock = pygame.time.Clock()
fps = 30

# creating the animation loop that will be responsible for updating the positions of 
# the planets, drawing them on the screen and handling user input.

# Run the game loop
running = True
while running:

    # handle events in the game loop
    for event in pygame.event.get():

        # check for QUIT event
        if event.type == pygame.QUIT:
            running = False
    
    # clear the screen with background image
    screen.blit(background_image, (0,0))

    # display the sun at the center
    image_rect = planets[0]["image"].get_rect()
    image_rect.center = (int(planets [0]["x"]), int(planets [0]["y"]))
    screen.blit(planets [0]["image"], image_rect)
    

    # draw and update the position of the planets
    for planet in planets [1:]:

        # increment the angle based on the period of the planet so 
        # that it completes on orbit in a given period
        planet["angle"] += 0.05 * (1 / planet['period'])
    

        # calculating the position of the planet based on the angle
        planet["x"] = planets[0]["x"] + math.cos(planet["angle"])* planet["distance"]
        planet["y"] = planets[0]["y"] + math.sin(planet["angle"])* planet["distance"]

        # add the current position to the list of past positions and draw a
        # trail behind the planet
        planet["past _positions"].append ((planet["x"], planet["y"]))

        # draw the trail
        for i in range(1, len(planet["past _positions"])):
            pygame.draw.line(screen, (153,153,0), planet["past _positions"][1-1], planet["past _positions"][i], 1)

        # get the rect of the planet's image and set its center to the planet's position
        image_rect = planet["image"].get_rect()
        image_rect.center = (int(planet["x"]), int(planet["y"]))

        # draw the planet's image
        screen.blit(planet["image"], image_rect)
    
    # update the display
    pygame.display.update()

    # wait for the specified number of frames per second
    clock.tick(fps)

# Quit game
pygame.quit



