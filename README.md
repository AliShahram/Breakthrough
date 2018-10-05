# Breakthrough
Breakthrough game, AI agents playing.

# Contributors
Ali Shahram Musavi, Swomma Roy and Sirajus Salekin

# How To Play
 1. Make sure you have `python 3` installed.
 2. Run `python game.py` and follow the instructions.
 3. If you want to play with Evasive and House Lannister, type `1 3` when
prompted
    1. Evasive
    2. Conquerer
    3. House Lannister
    4. House Stark

# Unit Testing
Simply run the `testTransition.py` file:

```python testTransition.py```

# Progress
* Finished implementing `Board` Class methods

    * `get_moves(position)`
    * `is_valid(source, destination)`
    * `get_sym(position)`
    * `get_direction(position)`
    * Integrated `display_state()`
    * Integrated `terminal_state()`
    * Add `self.turn` to the `Board` and check before moving 
      any piece to ensure the integrity of the game
    * Implement `move_generator(player)` method that will provide
      all the moves for a particular player

* Test coverage for finished methods
    
    - [x] `get_moves(position)`
    - [x] `is_valid(source, destination)`
    - [x] `all_moves(player)`
    - [x] `move(position, direction)`
    - [ ] `get_sym(position)`
    - [ ] `get_direction(position)`
    - [ ] `display_state()`
    - [ ] `terminal_state()`

# ToDo 
- [ ] Finish implementing the `Agent` class
- [x] Decide whether to implement a function or class for `Game`
- [x] Finish `minimax` tree
- [ ] Implement `conquerer` and 2 more utility functions

