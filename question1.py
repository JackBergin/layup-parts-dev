import pygame
import math

# Initialize Pygame
pygame.init()

# Configures the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Airplane Simulator")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 100, 200)
RED = (200, 50, 50)

# Airplane properties
x, y = WIDTH // 2, HEIGHT // 2  # Initial position
yaw = 90  # Start with the planefacing upwards
speed = 0  # Start at 0 speed
max_speed = 10 
min_speed = 0
turn_rate = 3  # Degrees per frame
acceleration = 0.1
trajectory = []  # List to store past positions

# Create a simple airplane shape
plane_img = pygame.Surface((40, 40), pygame.SRCALPHA)
pygame.draw.polygon(plane_img, BLUE, [(40, 20), (0, 35), (10, 20), (0, 5)])  # Flipped 180 degrees

clock = pygame.time.Clock()
running = True

# Main loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # User controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # Turn left (yaw decrease)
        yaw += turn_rate
    if keys[pygame.K_RIGHT]:  # Turn right (yaw increase)
        yaw -= turn_rate
    if keys[pygame.K_UP]:  # Increase speed
        speed = min(speed + acceleration, max_speed)
    if keys[pygame.K_DOWN]:  # Decrease speed
        speed = max(speed - acceleration, min_speed)
    if keys[pygame.K_SPACE]:  # Reset position
        x, y = WIDTH // 2, HEIGHT // 2
        yaw = 90
        speed = 0
        
    # Convert yaw to radians for movement calculation
    radians = math.radians(yaw)

    # Update position based on speed and yaw angle
    current_x = x + speed * math.cos(radians)
    current_y = y - speed * math.sin(radians) 

    # Keep plane within borders, accounting for plane size
    plane_size = 20  # Half the size of the plane surface (40/2)
    x = max(plane_size, min(current_x, WIDTH - plane_size))
    y = max(plane_size, min(current_y, HEIGHT - plane_size))

    # Store trajectory
    if len(trajectory) > 1000:
        trajectory.pop(0)  # Remove oldest points to save memory
    trajectory.append((int(x), int(y)))

    # Draw trajectory
    for point in trajectory:
        pygame.draw.circle(screen, RED, point, 2)

    # Rotate and draw the airplane
    rotated_plane = pygame.transform.rotate(plane_img, yaw)  # Adjust rotation
    rect = rotated_plane.get_rect(center=(x, y))
    screen.blit(rotated_plane, rect.topleft)

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()