---
title: Application - 🎲 Board games
date: 06/02/2021
mentors: 
  - TimSando
tags:
  - Emulation
links:
  - '[Capstone template code](https://github.com/CapgeminiInventIDE/PyCap/tree/main/src/intro-to-python/capstone/board_game){target=_blank}'
---

{{ course_summary(title, date, mentors=mentors, tags=tags, links=links) }}

## Problem

Create a basic commandline application using Python 3.6+ that allows a user to play a game of "pythons" and ladders (snakes and ladders).
Your code should be well documented with a docstrings, comments and a README describing how your program works, unit tests to ensure it works as expected and type annotations and finally well formatted using Black. This is so other developers can understand how to help build upon your program.

You should add a summary to your README that includes the next steps (dot points) and also the strengths and weaknesses of your program in its current state.
A list of operations that your should support, as well as how we expect them to be called can be found in the table below.

> Each board should be composed of a 10x10 grid where each square can either be blank, a python or a ladder.

| Operation                                            | Usage | Required |
|------------------------------------------------------|-------|----------|
| Start a new single player game                      | `"python board_game.py"`      | TRUE     |
| Keep the game running until cancelled by the player  | `"Game is active"`      | TRUE     |
| Roll a 6 sided die                                | `"Press a button to roll the die"`      | TRUE     |
| Print out the player's current location on the board | `"Press a button to show current location"`      | TRUE     |
| Move a player to a new square based on their die roll | `"Moving player forward x squares"`      | TRUE     |
| Move a player to a different square if it lands on a python  | `"Player landed on a python, sliding back to square X"`      | TRUE     |
| Move a player to a different square if it lands on a ladder  | `"Player landed on a ladder, climbing up to square X"`       | TRUE     |
| Game finishes when the player exceeds the final square | `"You've reached square 100 and won the game. Congratulations!"`      | TRUE     |

## Optional Extras

- Dynamically generate a new board using code
- Make a the game multiplayer
- Visualise the board layout
- Require the final roll to be the exact number required to get to 100 or else move back squares
- Save a game in progress and load it later