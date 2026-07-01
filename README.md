# Catalyte-War-Activity

A Python recreation of the classic card game **War**.

## Overview

This project simulates a two-player game of War with a standard 52-card deck. Players take turns drawing cards, and the higher card wins the round. If both players draw the same rank, a war is triggered and the round winner takes all contested cards.

## Project Structure

- `src/`
  - `card.py` - Card representation and value comparison logic.
  - `deck.py` - Deck creation, shuffle, and dealing.
  - `player.py` - Player card pile management and draw behavior.
  - `game.py` - Game flow, round resolution, and war handling.
  - `main.py` - Entry point for starting the interactive game.
- `tests/`
  - `test_card.py` - Tests for card behavior and comparison.
  - `test_deck.py` - Tests for deck creation, shuffle, and dealing.
  - `test_player.py` - Tests for player actions and card handling.
  - `test_game.py` - Game initialization tests.

## Requirements

- Python 3.8+

## Running the Game

From the repository root, run the game from the `src` directory:

```bash
cd src
python main.py
```

Alternatively, from the repository root you can set `PYTHONPATH` to `src` and run:

```bash
PYTHONPATH=src python src/main.py
```

On Windows PowerShell, use:

```powershell
$env:PYTHONPATH = "src"
python src/main.py
```

## Gameplay

- Enter names for Player 1 and Player 2 when prompted.
- Each round, both players draw their top card.
- The player with the higher card wins the round and collects both cards.
- If the cards are equal, a war begins:
  - Each player places three cards face down and one card face up.
  - The higher face-up card wins all cards in the war.
  - If the face-up cards tie again, the war continues recursively.
- The game ends when one player runs out of cards.

## Testing

From the repository root, run:

```bash
pytest
```

This will execute the unit tests in the `tests/` directory.

## Design Notes

- `Card` objects compare rank values and support human-readable string output.
- `Deck` creates a standard 52-card set, shuffles it, and deals evenly to both players.
- `Player` manages a queue of cards and can draw or receive won cards.
- `Game` controls the round cycle, determines winners, and resolves war scenarios.

## Notes

- The current implementation uses a simple interactive console interface.
- The player piles are managed as first-in, first-out (FIFO) queues to mirror card play order.
