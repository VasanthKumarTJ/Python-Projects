with open("story.txt", 'r') as file:
    story = file.read()

words = set()
start_of_word = -1

target_first = "<"
target_last = ">"

for i, char in enumerate(story):
    if char == target_first:
        start_of_word = i
    
    if char == target_last and start_of_word != -1:
        words.add(story[start_of_word:i +1])
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"please enter a input for the word {word}: ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])

print("/n", story)
