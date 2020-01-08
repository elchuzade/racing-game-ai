# NEURAL NETWORK TO PLAY CAR RACING GAME

### Goals

- Implement a 2D Car Racing game environment using Pygame with possible play mode, autopilot mode and ai mode.
- Implement a Neural Network to play the game using Keras with categorical cross entropy loss function.

### Libraries

- Pygame
- Pandas
- Numpy
- Keras

### Tools and programming languages

- Python3
- Jupyter Notebook

### Installation

- Make sure python3 and all libraries mentioned above are installed
- Clone this repo
- Navigate into the folder
- Open terminal and run

```
python3 main.py
```

### Implementing your own Neural Network

Some of the parameters in main.py file are changeable. If you want to train your own Neural Network, open main.py and change some of the variables as shown below:

```
collect_data = True
ai = False
player_control = False
rows = 20000
```

In the code above
`collect_data = True` means you can write all the state-action pairs into a csv file for future data analytics purposes.
`ai = False` means you want to use an autopilot to play the game that will never fail, thus generate a proper state-action pairs to train you neural network
`player_control = False` means no input from a player will be affecting a state except Esc button that exists the game
`rows = 20000` means after 20000 state-action pairs the csv file will be saved

### Other changeable settings

You can go to `constants.py` file in `constants` folder, there You can set your own `FRAME_RATE` to influence how often the game frame will change in pygame, `DATA_ROWS` to limit amount of rows to be collected into a csv file, `ACTION_PERFORM_RATE` to decide how frequently your car will move ( Note: The new car will appear twice as rare as ACTION_PERFORM_RATE ) to make sure there is always a way out for your car during the game.

You can also change the environment by uploading your own images of cars into variables `MY_CAR_ICON` and `ENEMY_CAR_ICON` ( Note: for proper gaming experience make sure the image has sizes of 40px vs 80px )

You can change the background of the screen as well as the white vertical lines.
`BLACK = (0, 0, 0)` stands for the color of background. Simply pick your favorite color and write its RGB code in the corresponding fields. `GREY = (150, 150, 150)` stands for vertical lines that separate the road lines