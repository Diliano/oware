# Oware


## Introduction

Oware is a game of strategy. This Python implementation allows two players to compete in a turn-based match directly from their console, with the goal of capturing more seeds than the opponent.

The objective is to capture more seeds than one's opponent, making it both a simple and strategic game.

## Features

- Two-player gameplay on a single console.
- Simple and intuitive terminal-based UI.
- Automatic capture and end-game detection.
- Detailed instructions and game rules within the game.

## Getting Started

To play Oware, you need to have Python installed on your machine.

### Prerequisites

- Python 3.x. You need Python installed on your machine to run this game. Most systems come with Python pre-installed. You can check your Python version by running `python --version` or `python3 --version` in your terminal. If you need to install Python, visit the [official Python website](https://www.python.org/downloads/) for download instructions tailored to your operating system.

### Installation

1. Clone the repository or download the source code.
    ```
    git clone https://github.com/Diliano/oware.git
    ```
2. Navigate to the project directory.
    ```
    cd oware
    ```

3. Run the game.
    ```
    python oware.py
    ```

## How to Play

1. The game board consists of two rows of six pits, with a large store at each end for the captured seeds.
2. Players take turns selecting a pit from their side to sow its seeds anti-clockwise.
3. If the final seed sown lands in an opponent's pit that, after sowing, contains exactly 2 or 3 seeds, those seeds are captured and placed into the player's store.
4. **Chain captures:** If the last seed sown results in a pit with 2 or 3 seeds, enabling a capture, and the preceding pits on the opponent's side also contain exactly 2 or 3 seeds, those seeds are also captured. This rule allows for capturing multiple pits in a single turn, provided each pit in the sequence meets the 2 or 3 seed condition.
5. The game ends when one player cannot make a move. The other player captures the remaining seeds on the board.
6. The player with the most seeds in their store at the end of the game wins.