import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from player import Player
from asteroid import Asteroid
from asteroids import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        shots.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                return
        screen.fill("black")
        for img in drawable:
            img.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000 #convert from milliseconds to seconds

if __name__ == "__main__":
    main()
