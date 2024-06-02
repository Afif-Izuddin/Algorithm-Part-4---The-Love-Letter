
def compare_letters(file1, file2):
    word_counts = {}

    # Open and read the contents of the first file
    with open(file1, 'r') as f1:
        letter1_text = f1.read()

    # Split the text of the first file into words
    letter1_words = letter1_text.split()

    # Count the occurrences of words in the first letter
    for word in letter1_words:
        if word in word_counts:
            word_counts[word][0] += 1
        else:
            word_counts[word] = [1, 0]

    # Open and read the contents of the second file
    with open(file2, 'r') as f2:
        letter2_text = f2.read()

    # Split the text of the second file into words
    letter2_words = letter2_text.split()

    # Compare the words in the second letter with the word counts in the dictionary
    differences1 = []
    differences2 = []
    
    for word in letter2_words:
        if word in word_counts:
            if word_counts[word][0] > 0:
                word_counts[word][0] -= 1   
            else:
                print(word)
                differences2.append(word)
        else:
            differences2.append(word)

    for word, counts in word_counts.items():
        if counts[0] > 0:
            differences1.append(word)

    # Print the results
    max_length = max(len(differences1), len(differences2))
    print (max_length)
    for i in range(max_length):
        if len(differences2) <= i:
            print(f"Letter 1 has additional words: '{differences1[i]}'")
        elif len(differences1) <= i:
            print(f"Letter 2 has additional words: '{differences2[i]}'")
        else:
            print(f"Letter 1 uses '{differences1[i]}' while Letter 2 uses '{differences2[i]}'")
        

compare_letters('Letter1.txt', 'Letter2.txt')
