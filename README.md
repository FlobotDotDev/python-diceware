# diceware

Simple Python script that gives you a secure password.

For a more thorough explanation, please see https://theworld.com/~reinhold/diceware.html

OR

Check out my blog https://jamesflores.dev/posts/diceware/

## How the script works...

The script emulates `n` amount of die rolls (five digits each). The default is three words.

1. The script gets a five digit number and matches that number to a word in the provided wordlist.
2. It adds a random ASCII punctuation character which becomes the delimeter.
3. It also adds a random number (1-3 in length) to the end.
4. Finally, it has a 50/50 chance of capitalizing the word.

## Try it out!

<iframe loading="lazy" src="https://diceware.streamlit.app/?embed=true" scrolling="No" height="350px" width="100%" style="border: none;"></iframe>

### Example

  ```
  $ python3 diceware.py
  Password = Junkie~undivided%Disorder#943
  ```
