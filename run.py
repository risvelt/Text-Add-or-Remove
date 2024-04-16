def remove_lines_from_bottom(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = lines[:-num_lines]

    with open(file_path, 'w') as file:
        file.writelines(lines)

def count_duplicate_sentences(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Counting occurrences of each sentence
    sentence_count = {}
    for index, line in enumerate(lines, start=1):
        sentence = line.strip()
        if sentence in sentence_count:
            sentence_count[sentence].append(index)
        else:
            sentence_count[sentence] = [index]

    # Printing the result
    print("\nDuplicate sentences between lines:")
    for sentence, indexes in sentence_count.items():
        if len(indexes) > 1:
            print(f"Sentence '{sentence}' appears on lines {', '.join(map(str, indexes))}")

    if all(len(indexes) == 1 for indexes in sentence_count.values()):
        print("There are no duplicate sentences between lines.")

def remove_lines(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = lines[:-num_lines]

    with open(file_path, 'w') as file:
        file.writelines(lines)

def remove_specific_sentence(lines, sentence):
    return [line.replace(sentence, "").strip() + "\n" for line in lines]

def remove_socks5_prefix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sentence_to_remove = input("Enter the sentence you want to remove: ")
    lines = remove_specific_sentence(lines, sentence_to_remove)

    with open(file_path, 'w') as file:
        file.writelines(lines)

def add_sentence_to_lines(lines, sentence, position):
    if position == "start":
        return [sentence.strip() + line for line in lines]
    elif position == "end":
        return [line.strip() + sentence + "\n" for line in lines]

def add_sentence_to_file(file_path, sentence, position):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = add_sentence_to_lines(lines, sentence, position)

    with open(file_path, 'w') as file:
        file.writelines(lines)

def main():
    file_path = "proxy_list.txt"  # Replace with your text file path

    while True:
        # Menu
        print("\nMenu:")
        print("1. Add Word to Each Line")
        print("2. Delete Word")
        print("3. Delete Lines from Bottom")
        print("4. Check Same Words Between Lines")
        print("5. Exit")
        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            sentence = input("Enter the sentence you want to add: ")
            position = input("Choose position to add the sentence (start/end): ")
            add_sentence_to_file(file_path, sentence, position)
            print(f"Sentence '{sentence}' has been added to the file at position {position}.")
        elif choice == "2":
            remove_socks5_prefix(file_path)
            print("The selected sentence has been removed from the file.")
        elif choice == "3":
            num_lines = int(input("Enter the number of lines you want to delete from the bottom: "))
            remove_lines_from_bottom(file_path, num_lines)
            print(f"{num_lines} lines have been deleted from the bottom of the file.")
        elif choice == "4":
            count_duplicate_sentences(file_path)
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
