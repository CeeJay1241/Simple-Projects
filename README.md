# Python Projects Portfolio

A collection of Python mini-projects built while learning core programming concepts. Each project applies one or more skills in a practical context — games, automation, data analysis, and more.

---

## Python Concepts Covered

### Data Structures
- Dictionaries (flat and nested)
- Lists
- Tuples
- List comprehensions
- Dictionary comprehensions

### Control Flow
- `while` loops and `for` loops
- `if / elif / else`
- `break` and `continue`
- Nested loops

### Functions
- Function definitions and return values
- Multiple return values (tuples)
- Type hints
- `*args` / `**kwargs` patterns
- Lambda functions
- Global variables

### Object-Oriented Programming (OOP)
- Class definitions
- `__init__` constructors
- Instance variables and class variables
- Methods
- Inheritance (`super()`)
- Class composition (objects containing other objects)
- Single responsibility principle

### String Operations
- f-strings
- `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.title()`
- String iteration (looping over characters)
- `ord()` and `chr()` for ASCII manipulation
- `.join()` to convert lists to strings
- String multiplication

### File I/O
- `open()` with `read()`, `readlines()`, `write()`
- Context managers (`with` statement)
- Template substitution (replace placeholder with value)
- pathlib `Path` for file paths

### Error Handling
- `try / except` blocks
- `ValueError` handling
- Input validation loops

### Algorithms & Math
- Modulo arithmetic (wrap-around, Caesar cipher shifts)
- Coordinate-based positioning
- Collision detection (distance checks)
- Probability-based event triggering (`random.randint`)

### Libraries
| Library | Usage |
|---|---|
| `turtle` | Graphics, shapes, movement, text, event handling |
| `pandas` | CSV reading, DataFrames, filtering, `iterrows()`, `to_csv()` |
| `random` | `randint()`, `choice()` |
| `time` | `sleep()` for game loop timing |
| `pathlib` | File path handling, reading/writing files |
| `string` | Character constants |

### Design Patterns
- **Game loop** — update, detect, respond
- **Event-driven programming** — keyboard/click handlers
- **MVC separation** — logic classes separated from main loop
- **Factory pattern** — dynamically creating objects (cars, snake segments)
- **Template method** — file templates with placeholder substitution
- **State management** — tracking game/app state with variables
- **Module-level constants** — configuration at the top of files

---

## Projects

### 1. Coffee Machine (Procedural)
`coffee_machine/`
A command-line coffee machine simulator. Takes drink orders, processes coin payments, tracks resources, and dispenses drinks.
**Key concepts:** Dictionaries, functions, exception handling, loop control

---

### 2. Coffee Machine (OOP)
`coffee_machine_oop/`
A refactored version of the coffee machine using object-oriented design with separate `Menu`, `CoffeeMaker`, and `MoneyMachine` classes.
**Key concepts:** Classes, inheritance, composition, single responsibility

---

### 3. Quiz App
`quiz_project/`
A true/false quiz that loads questions from a data file and scores the user.
**Key concepts:** Classes (`Question`, `QuizBrain`), list of objects, module imports, OOP composition

---

### 4. Caesar Cipher
`ceaser_cypher/`
Encrypts and decrypts messages using a character shift. Handles non-alpha characters and wraps around the alphabet.
**Key concepts:** `ord()` / `chr()`, modulo arithmetic, input validation, exception handling

---

### 5. Secret Auction
`auction/`
Multiple bidders enter their names and bids secretly, and the highest bidder is revealed at the end.
**Key concepts:** Dictionaries, `max()` with `key=`, while loops, type conversion

---

### 6. Snake Game
`snake_game/`
A fully playable Snake game with a scoreboard, high score persistence, food, collision detection, and a no-wall variant.
**Key concepts:** OOP, inheritance, list operations, file I/O with `pathlib`, game loop, event handling

---

### 7. Pong Game
`pong_game/`
A two-player Pong game with paddles, a bouncing ball, and a live scoreboard.
**Key concepts:** OOP, inheritance, global state, keyboard event handlers, collision detection, speed progression

---

### 8. Turtle Crossing
`turtle_crossing_capstone_project/`
Cross the road without getting hit by cars. Difficulty increases each level.
**Key concepts:** Dynamic object creation, `random.choice()` / `randint()`, level progression, collision detection, game loop

---

### 9. Mail Merge
`mail_merge_project/`
Reads a list of names and a letter template, then generates a personalized letter for each person.
**Key concepts:** File I/O, `readlines()`, `strip()`, `replace()`, context managers, nested file operations

---

### 10. U.S. States Game
`us_state_game/`
A geography quiz where you type U.S. state names and they appear on a map. Missed states are saved to a CSV at the end.
**Key concepts:** `pandas`, DataFrames, `turtle` image backgrounds, `iterrows()`, `iloc`, `to_csv()`, GUI text input

---

### 11. NATO Alphabet Translator
`NATO_alphabet_project/`
Converts any word into its NATO phonetic alphabet equivalent (e.g. "Hello" → `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']`).
**Key concepts:** `pandas`, dictionary comprehension with `iterrows()`, list comprehension, string iteration
