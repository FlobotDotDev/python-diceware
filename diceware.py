import random, string

def generate_password():
    passwd = []
    num = 3

    # Generate a random number between 1 and 999
    rand_num = str(random.randint(1, 999))

    for w in range(num):
        # Generate 5 random numbers between 1 and 6
        roll = ''.join([str(random.randint(1, 6)) for _ in range(5)])
        word = wl_dict[roll]

        # Randomly capitalizes the current word
        if random.randrange(2) == 1:
            word = word.capitalize()

        # Appends word to array
        passwd.append(word)

        # Generate a random special character
        passwd.append(random.choice(string.punctuation))

    # Concatenate the words, number, and special character to form the password
    final_pw = ''.join(passwd) + rand_num

    return final_pw

# Load the diceware wordlist
with open("diceware.txt", "r") as f:
    wl = [line.strip() for line in f]
    
wl_dict = {}
for line in range(len(wl)):
    l = wl[line].split("\t")
    wl_dict[l[0]] = l[1]

print("Password = " + generate_password())
