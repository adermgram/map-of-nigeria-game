# Nigerian States Game

This is a simple interactive game that helps users learn and memorize the 37 states of Nigeria. The game uses the Turtle graphics library to display a map of Nigeria, and the user must guess the name of each state, one at a time. The guessed states are displayed on the map at their correct location.

## How it Works

- A map of Nigeria is displayed using the Turtle graphics library.
- The user is prompted to guess the name of a Nigerian state.
- If the guessed state is correct, it is displayed on the map at its corresponding location.
- The game continues until all 37 states are guessed or the user decides to exit.
- At the end of the game, a file named `states_to_practice.csv` is generated, which contains the list of states the user failed to guess.

## 
![map of nigeria game](https://github.com/user-attachments/assets/44582b21-0609-4eca-b0a7-472b1b559fd7)


## Requirements

Make sure you have the following libraries installed:

- `turtle` (Comes pre-installed with Python)
- `pandas` (For reading and writing CSV files)

You can install pandas using pip:

```bash
pip install pandas
```

# How to Run
Clone the repository and navigate to the project directory:
``` bash
git clone https://github.com/adermgram/map-of-nigeria-game.git
cd nigerian-states-game
```
run main.py

# Output
After exiting or completing the game, the program will generate a CSV file named states_to_practice.csv which contains a list of states you missed during the game. You can use this file to practice the states you did not guess.
