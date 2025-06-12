import pygame
import random
import sys
import time

# Game 1: Flappy Bird Clone
def flappy_bird():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Flappy Bird")

    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    black = (0, 0, 0)

    bird_x, bird_y = 100, height // 2
    bird_radius = 15
    gravity = 0.5
    bird_speed = 0
    pipe_width = 70
    pipe_gap = 150
    pipe_x = width
    pipe_height = random.randint(100, height - pipe_gap - 100)

    score = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(white)

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_speed = -8

        # Bird Physics
        bird_speed += gravity
        bird_y += bird_speed

        # Collision Check
        if bird_y - bird_radius <= 0 or bird_y + bird_radius >= height:
            break
        if pipe_x <= bird_x + bird_radius <= pipe_x + pipe_width and \
                (bird_y - bird_radius <= pipe_height or bird_y + bird_radius >= pipe_height + pipe_gap):
            break

        # Pipe Movement
        pipe_x -= 5
        if pipe_x < -pipe_width:
            pipe_x = width
            pipe_height = random.randint(100, height - pipe_gap - 100)
            score += 1

        # Drawing Bird and Pipes
        pygame.draw.circle(screen, blue, (bird_x, int(bird_y)), bird_radius)
        pygame.draw.rect(screen, green, [pipe_x, 0, pipe_width, pipe_height])
        pygame.draw.rect(screen, green, [pipe_x, pipe_height + pipe_gap, pipe_width, height - pipe_height - pipe_gap])

        # Score Display
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, black)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    return "exit"



# Game 2: Rock, Paper, Scissors
def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("\nWelcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
        if user_choice == "exit":
            break
        if user_choice not in options:
            print("Invalid choice. Try again!")
            continue
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")


# Game 3: Hangman
def hangman():
    words = ["python", "hangman", "games", "developer"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    print("\nWelcome to Hangman!")
    while attempts > 0 and "_" in guessed_word:
        print("Word:", " ".join(guessed_word))
        guess = input("Guess a letter (or type 'exit' to quit): ").lower()
        if guess == "exit":
            return
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Try again!")
            continue
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts remaining: {attempts}")
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Out of attempts! The word was:", word)


# Game 4: Snake Game
def snake_game():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    black = (0, 0, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)

    clock = pygame.time.Clock()
    snake_block = 10
    snake_speed = 15

    x1, y1 = width // 2, height // 2
    x1_change, y1_change = 0, 0
    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            break

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                break

        for segment in snake_list:
            pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    return "exit"


# Game 5: Tic-Tac-Toe
def tic_tac_toe():
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return True
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " " or \
           board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False

    def is_full(board):
        for row in board:
            if " " in row:
                return False
        return True

    print("\nWelcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("Cell already taken. Choose another!")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Try again!")
            continue

        board[row][col] = current_player
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


# Main Menu
def main():
    while True:
        print("\nMain Menu:")
        print("1. Flappy Bird")
        print("2. Rock, Paper, Scissors")
        print("3. Hangman")
        print("4. Snake Game")
        print("5. Tic-Tac-Toe")
        print("6. Exit")
        choice = input("Choose a game to play (1-6): ")

        if choice == "1":
            if flappy_bird() == "exit":
                break
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            hangman()
        elif choice == "4":
            if snake_game() == "exit":
                break
        elif choice == "5":
            tic_tac_toe()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
