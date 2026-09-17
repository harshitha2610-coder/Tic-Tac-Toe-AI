# 🎮 Tic-Tac-Toe with AI

A simple and interactive **Tic-Tac-Toe game built with Python and Streamlit**, where a human player competes against an AI opponent.

The computer uses the **Minimax algorithm** to analyze possible moves and choose the best available move.

## 🚀 Live Demo

**Streamlit App:**
*https://tic-tac-toe-ai-mo30harshi10.streamlit.app/*

## 📌 Project Overview

Tic-Tac-Toe is a classic two-player game played on a 3×3 grid.

In this project:

* The **player** plays as `X`
* The **computer** plays as `O`
* The board is displayed using an interactive Streamlit interface
* The AI uses the **Minimax algorithm**
* The game automatically detects wins, losses, and draws
* A new game can be started at any time

## ✨ Features

* 🎮 Interactive web-based game
* 🤖 AI opponent using Minimax
* 🧠 Intelligent move selection
* 📋 Clear 3×3 game board
* 🏆 Win detection
* 🤖 Computer-win detection
* 🤝 Draw detection
* 🔄 New Game button
* ⚡ Fast and lightweight
* 🌐 Easy deployment with Streamlit Community Cloud

## 🧠 How the AI Works

The computer opponent uses the **Minimax algorithm**.

Minimax explores the possible future moves and assigns scores to different game outcomes.

The scoring system is:

| Game Result | Score |
| ----------- | ----: |
| AI wins     |  `+1` |
| Player wins |  `-1` |
| Draw        |   `0` |

The AI tries to **maximize its score**, while assuming that the player will try to minimize the score.

This allows the computer to make strategic decisions instead of choosing moves randomly.

## 🎯 Game Flow

```text
Start Game
    │
    ▼
Display Empty Board
    │
    ▼
Player chooses a position
    │
    ▼
Check for Player Win
    │
    ├── Yes ──► Player Wins 🎉
    │
    ▼
Check for Draw
    │
    ├── Yes ──► Draw 🤝
    │
    ▼
AI analyzes possible moves
using Minimax
    │
    ▼
AI makes its move
    │
    ▼
Check for AI Win
    │
    ├── Yes ──► AI Wins 🤖
    │
    ▼
Check for Draw
    │
    ├── Yes ──► Draw 🤝
    │
    ▼
Continue Game
```

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Minimax Algorithm**
* **Git & GitHub**
* **Streamlit Community Cloud**

## 📂 Project Structure

```text
tic-tac-toe-ai/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains:

* Streamlit user interface
* Game board
* Player moves
* AI moves
* Win and draw detection
* Minimax implementation
* Game reset functionality

### `requirements.txt`

Contains the Python dependency required to run the application:

```text
streamlit
```

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone [https://github.com/harshitha2610-coder/Tic-Tac-Toe-AI.git]
```

### 2. Navigate to the project directory

```bash
cd tic-tac-toe-ai
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select the repository.
5. Select `app.py` as the main file.
6. Deploy the application.

After deployment, Streamlit will provide a public URL for the game.

## 🎮 How to Play

1. Start the application.
2. You play as **❌ X**.
3. The computer plays as **⭕ O**.
4. Click any empty square to make your move.
5. The AI automatically makes its move.
6. Continue until there is a winner or a draw.
7. Click **New Game** to play again.

## 🏆 Winning Conditions

A player wins when they have three symbols in a row:

### Horizontal

```text
 X | X | X
---+---+---
 O |   | O
---+---+---
   |   | O
```

### Vertical

```text
 X | O |   
---+---+---
 X | O |   
---+---+---
 X |   |   
```

### Diagonal

```text
 X | O |   
---+---+---
   | X | O
---+---+---
   |   | X
```

## 🔍 Algorithm

The project uses **Minimax**, a recursive decision-making algorithm commonly used in two-player games.

For each possible AI move:

1. The move is temporarily placed on the board.
2. The algorithm explores possible future moves.
3. Terminal game states are evaluated.
4. Scores are propagated back through the game tree.
5. The AI selects the move with the highest score.

Because Tic-Tac-Toe has a relatively small game state, Minimax can evaluate the possible moves efficiently.

## 📊 Complexity

For a standard Tic-Tac-Toe board, the Minimax algorithm can explore the game tree because there are only nine possible initial positions.

The branching factor decreases after every move:

```text
9 → 8 → 7 → 6 → ... → 1
```

This makes Tic-Tac-Toe a suitable game for demonstrating recursive game-search algorithms.

## 🎓 Learning Objectives

This project demonstrates:

* Python programming
* Functions and conditional logic
* Lists and arrays
* Game-state management
* Recursion
* Artificial intelligence fundamentals
* Minimax decision making
* Streamlit application development
* GitHub project organization
* Web application deployment

## 🔮 Future Improvements

Possible improvements include:

* Add difficulty levels such as Easy, Medium, and Hard
* Add player name customization
* Add score tracking across multiple games
* Add sound effects
* Add animations
* Add a more advanced UI
* Add player-vs-player mode
* Add AI-vs-AI mode
* Improve the Minimax algorithm using Alpha-Beta Pruning
* Add game statistics
* Add a mobile-friendly interface

## 📜 License

This project is open-source and available for educational and personal use.

## 👩‍💻 Author

**Harshitha L**

GitHub:
*[Click_here](https://github.com/harshitha2610-coder)*

---

⭐ If you found this project useful, consider giving the repository a **star**!
