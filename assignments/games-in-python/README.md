
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman (ahorcado) word-guessing game using Python. Students will practice string manipulation, loops, conditionals, user input handling and random selection.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description
Implement a playable Hangman game that runs in the terminal. The program should randomly select a word from a predefined list and let the player guess letters until they either discover the full word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select words from a predefined list.
- Accept letter guesses and show current progress in a spaced "_ _ _" format for unrevealed letters.
- Track remaining incorrect guesses and show them to the player.
- End the game when the word is fully guessed or attempts are exhausted.
- Display a clear win or lose message and reveal the word when the player loses.

### 🛠️ Optional: Improve the Game

#### Description
Add one or more enhancements to make the game more robust or fun. These are optional but encouraged for extra practice.

#### Requirements (optional)

- Make input case-insensitive and validate single-letter input.
- Prevent counting the same incorrect letter more than once.
- Load the word list from a text file (e.g., `words.txt`) instead of a hardcoded list.
- Add ASCII-art hangman stages, scoring, hints, or the ability to save high scores.

## Example gameplay (simplified)

Player sees:

```
Word: _ _ _ _ _
Guesses remaining: 6
Wrong guesses: a, e
Enter a letter: 
```

After guessing all letters correctly:

```
Congratulations — you guessed the word "apple"!
```

After attempts exhausted:

```
Game over. The word was "apple". Try again!
```

---

Nota: Sigue la plantilla ubicada en `templates/assignment-template.md`. Guarda este archivo como `README.md` dentro de `assignments/games-in-python/`.
- Display win/lose messages
