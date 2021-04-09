# python-diceware

Simple Python script that gives you a secure password.

For a more thorough explanation, please see https://theworld.com/~reinhold/diceware.html

## How the script works...

The script emulates `n` amount of dice rolls (five digits each). 

1. The script gets a five digit number and matches that number to a word in the provided wordlist.
2. It adds a random ASCII punctuation character which becomes the delimeter.
3. It also adds a random number (1-4 in length) to the end.
4. Finally, it has a 50/50 chance of capitalizing the word.

### Example

  ```
  $ python3 dice.py 5
  Password = Faculty=taunt;retread=Posted%Chapped8
  ```

## Usage

`$ python3 dice.py -h` Displays the help message.

`$ python3 dice.py n` Replace `n` with the amount of words you want in your password

## Credits

If you have any suggestions to make the program better, let me know.

GitHub https://github.com/majesticflo
