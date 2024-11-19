# Snake Game 

A classic Snake game implemented in Python using the Turtle module. Control the snake, eat the food, and compete for the highest score!

---

## Features
- **Snake Movement**: Control the snake using arrow keys (Up, Down, Left, Right).
- **Food Generation**: Randomly generates food; eating food increases the snake's length.
- **Scoring System**: Tracks your current score and saves the highest score across sessions in a `data.txt` file.
- **Collision Detection**: Resets the game if the snake collides with the screen boundaries or itself.

---

## How to Play
1. Run the `main.py` file.
2. Use the arrow keys to move:
   - **Up**: Move up
   - **Down**: Move down
   - **Right**: Move right
   - **Left**: Move left
3. Avoid hitting the walls or your own tail.
4. Eat the food to score points and grow the snake.

---

## File Structure
- **`main.py`**: Initializes the game window, listens for user inputs, and runs the main game loop.
- **`snake.py`**: Handles the snake's behavior, including movement, growing, and resetting.
- **`food.py`**: Defines the food object and handles its random placement on the screen.
- **`score.py`**: Manages the score display, tracks the high score, and updates the `data.txt` file.

---

## ⚙️ Prerequisites
- Python 3.x installed
- Turtle module (included with Python)

---

