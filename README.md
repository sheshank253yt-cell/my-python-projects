# Shashank's Python Projects

Welcome! This repository is a collection of small Python projects by Shashank.
They are beginner-friendly programs for practicing Python through games and
useful little tools.

## Projects

- **Dice Game** (`dice_game.py`) - Roll two dice whenever you like.
- **Number Guessing Game** (`num_guess.py`) - Try to guess a randomly chosen
  number from 1 to 100. The game tells you if your guess is too high or too low.
- **Arithmetic Challenge** (`problems.py`) - Practice random addition,
  subtraction, and multiplication questions. It tracks your answers and shows a
  final time when you finish all 10 problems.
- **Rock, Paper, Scissors** (`rock _game.py`) - Play the classic game against
  the computer.
- **QR Code Generator** (`qr_gen.py`) - Turn text or a link into a QR code image.
- **Password Manager** (`password_m.py`) - A simple example of a password
  manager with a master-password prompt and JSON files for storing entries.

## Getting started

Install Python 3, open a terminal in this folder, and run a project like this:

```text
python dice_game.py
```

For the arithmetic challenge:

```text
python problems.py
```

You can run any of the other projects by replacing `dice_game.py` with its file
name. The QR code generator needs the `qrcode` package with Pillow:

```text
python -m pip install "qrcode[pil]"
```

Then run `python qr_gen.py` and follow the prompts to create an image.

## Password manager note

The password manager is a learning project, not a secure way to store real
passwords. Its JSON files store passwords as plain text, so only use sample
details. It expects `mas_pass.json` to contain a password, like this:

```json
{
    "password": "your-master-password"
}
```

Saved entries are kept in `passwords.json`. The add option in the current menu
is not connected yet, so it displays the saved entries instead of adding one.
