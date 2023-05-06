import pygame
import random

# Define some constants for the game
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Initialize pygame
pygame.init()

# Create the game window and set its size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define a function to draw the snake
def draw_snake(snake):
    for cell in snake:
        rect = pygame.Rect(cell[0] * CELL_SIZE, cell[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)

# Define a function to draw the food
def draw_food(food):
    rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)

# Define a function to generate a new food location
def generate_food(snake):
    while True:
        x = random.randint(0, WIDTH // CELL_SIZE - 1)
        y = random.randint(0, HEIGHT // CELL_SIZE - 1)
        if (x, y) not in snake:
            return (x, y)

# Define the main game function
def game():
    # Initialize the snake and the food
    snake = [(4, 4), (4, 3), (4, 2)]
    food = generate_food(snake)
    direction = "right"

    # Set the game over flag to False
    game_over = False

    # Set the clock for the game
    clock = pygame.time.Clock()

    # Start the game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game if the user closes the window
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                elif event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"

        # Move the snake
        if direction == "up":
            head = (snake[0][0], snake[0][1] - 1)
        elif direction == "down":
            head = (snake[0][0], snake[0][1] + 1)
        elif direction == "left":
            head = (snake[0][0] - 1, snake[0][1])
        elif direction == "right":
            head = (snake[0][0] + 1, snake[0][1])

        # Check for collision with the walls
        if head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE:
            game_over = True

        # Check for collision with the snake's body
        if head in snake[1:]:
            game_over = True

        
        # Check for collision with the food
        if head == food:
            # Add a new cell to the snake
            snake.insert(0, head)
            # Generate a new food location
            food = generate_food(snake)
        else:
            # Move the snake by removing the last cell and adding a new cell to the front
            snake.pop()
            snake.insert(0, head)

        # Fill the background with black
        screen.fill((0, 0, 0))

        # Draw the snake and the food
        draw_snake(snake)
        draw_food(food)

        # Update the screen
        pygame.display.update()

        # Tick the clock
        clock.tick(10)

    # Game over screen
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()


# Wait for the user to press a key
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Restart the game if the user presses enter
                game()
            elif event.key == pygame.K_ESCAPE:
                # Quit the game if the user presses escape
                pygame.quit()
                quit()

