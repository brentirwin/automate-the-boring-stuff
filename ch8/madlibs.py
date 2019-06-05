import re

madlib = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

# Get an array of parts of speech to be requested
pos_regex = re.compile(r'ADJECTIVE|NOUN|VERB')
pos_arr = pos_regex.findall(madlib)

# For each part of speech in the array
for word in pos_arr:
    prompt = 'Enter a '
    if word == 'ADJECTIVE':
        prompt = 'Enter an '
    prompt += word.lower() + ': '

    # Replace part of speech with user's word
    word = input(prompt)

    # Substitute first instance of regex in string with new word
    madlib = pos_regex.sub(word, madlib, 1)

print(madlib)
