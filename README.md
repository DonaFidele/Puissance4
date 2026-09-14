# 🔴🟡 Puissance4

A terminal-based **Connect Four** game written in Python, featuring emoji game pieces and a built-in AI opponent that can spot winning moves and block yours.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey)
![Status](https://img.shields.io/badge/Status-Playable-brightgreen)

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Demo](#-demo)
- [How to Play](#-how-to-play)
- [Installation](#-installation)
- [Usage](#-usage)
- [Game Logic Overview](#-game-logic-overview)
- [Project Structure](#-project-structure)
- [Known Limitations](#-known-limitations)
- [Roadmap](#-roadmap)
- [Author](#-author)
- [License](#-license)

## 🎮 About

**Puissance4** (French for *Connect Four*) is a classic two-player strategy game reimplemented in pure Python, playable directly in your terminal. The player competes against a computer opponent on a traditional 7-column x 6-row grid, using emoji pieces (🏐️ / 😁️) instead of plain characters for a more playful experience.

The goal is simple: align **four pieces in a row** — horizontally, vertically, or diagonally — before the computer does.

## ✨ Features

- 🕹️ Fully playable in the terminal, no external dependencies
- 🤖 Computer opponent with basic decision-making:
  - Checks if it can win immediately
  - Blocks the player's winning move if it can't win itself
  - Otherwise picks a strategic column based on row priority
- 🧩 Full win detection: horizontal, vertical, and both diagonal directions
- 😁️ Emoji-based game pieces for a fun visual touch
- 🔁 Replay option at the end of each game

## 🖼️ Demo

```
        ___________a_______________b_________________c_______________d________________e________________f________________g_____________

          |                }                }                }                }                }                }                }
          |       😁️        }       😁️       }        🏐️      }         🏐️     }        😁️      }                }       😁️       }
          |                }                }                }                }                }                }                }
```

*(Example of a mid-game board state — columns are selected by letter, pieces drop to the lowest available row.)*

## 🕹️ How to Play

1. Launch the game — you'll be asked to enter a **pseudo** (your name).
2. Choose your piece color: `blanc` (white 🏐️) or `jaune` (yellow 😁️).
3. On your turn, type the **letter of the column** (`a` to `g`) where you want to drop your piece.
4. The piece automatically falls to the lowest empty slot in that column.
5. The computer plays its turn right after you.
6. First to align **4 pieces in a row** (any direction) wins!
7. At the end of a round, choose to play again or quit.

## ⚙️ Installation

No external libraries required — only the Python standard library.

```bash
git clone https://github.com/DonaFidele/Puissance4.git
cd Puissance4
```

**Requirements:**
- Python 3.x

## ▶️ Usage

Run the game from your terminal:

```bash
python3 puissance4.py
```

> 💡 For best results, use a terminal that supports emoji rendering (most modern terminals on macOS/Linux do; on Windows, use Windows Terminal rather than the classic `cmd.exe`).

## 🧠 Game Logic Overview

- The board is represented internally as a **42-cell grid** (7 columns × 6 rows), mapped with numbers `01`–`42`.
- Columns are addressed by letters `a`–`g`; the game calculates the lowest available cell in the chosen column using regex-based cell tracking.
- Win detection (`end_game`) checks all four alignment directions by splitting the grid into 6 rows and comparing adjacent cells.
- The AI (`ordi_game`) follows a simple priority strategy:
  1. **Win** if a winning move is available.
  2. **Block** the opponent's winning move.
  3. **Fallback**: pick a random available column, prioritizing lower rows first.

## 📁 Project Structure

```
Puissance4/
│
└── puissance4.py    # Main game file — contains the Puissance_4 class and game loop
```

## ⚠️ Known Limitations

- No input validation for full columns — selecting a completely filled column may cause unexpected behavior.
- `clean()` uses `os.system("clear")`, which is Unix/macOS-specific (won't work as-is on Windows `cmd.exe`).
- Display formatting depends on emoji rendering width, which can vary slightly across terminals.

## 🗺️ Roadmap

- [ ] Handle full-column selection gracefully
- [ ] Cross-platform terminal clearing (Windows support)
- [ ] Optional two-player (human vs human) mode
- [ ] Smarter AI (minimax algorithm)

## 👤 Author

**DonaFidele**
[GitHub Profile](https://github.com/DonaFidele)

## 📄 License

Free to fork and contribute.

---

<p align="center">Made with 🏐️😁️ by <b>Dona😎</b></p>
