# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    
    ### Creating Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ### Setting FPS
    clock = pygame.time.Clock()
    # delta time
    dt = 0

    # Creating PyGame groups for easy updating
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Adding Player to Groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    ### Creating Player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    astroField = AsteroidField()

    ### Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update Units:
        for unit in updatable:
            unit.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                return
            
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
    
        # Draw screen
        screen.fill("black")
        
        # Draw Units
        for unit in drawable:
            unit.draw(screen)

        pygame.display.flip()        

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()