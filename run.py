def remove_lines_from_bottom(file_path, num_lines):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = lines[:-num_lines]

    with open(file_path, 'w') as file:
        file.writelines(lines)

def count_duplicate_sentences(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Menghitung kemunculan setiap kalimat
    sentence_count = {}
    for index, line in enumerate(lines, start=1):
        sentence = line.strip()
        if sentence in sentence_count:
            sentence_count[sentence].append(index)
        else:
            sentence_count[sentence] = [index]

    # Mencetak hasil
    print("\nKalimat yang sama di antara baris:")
    for sentence, indexes in sentence_count.items():
        if len(indexes) > 1:
            print(f"Kalimat '{sentence}' muncul pada baris {', '.join(map(str, indexes))}")

    if all(len(indexes) == 1 for indexes in sentence_count.values()):
        print("Tidak ada kalimat yang sama di antara baris.")

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

    sentence_to_remove = input("Masukkan kalimat yang ingin Anda hapus: ")
    lines = remove_specific_sentence(lines, sentence_to_remove)

    with open(file_path, 'w') as file:
        file.writelines(lines)

def add_sentence_to_lines(lines, sentence, position):
    if position == "awal":
        return [sentence.strip() + line for line in lines]
    elif position == "akhir":
        return [line.strip() + sentence + "\n" for line in lines]

def add_sentence_to_file(file_path, sentence, position):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = add_sentence_to_lines(lines, sentence, position)

    with open(file_path, 'w') as file:
        file.writelines(lines)

def main():
    file_path = "proxy_list.txt"  # Ganti dengan path file teks Anda

    while True:
        # Menu
        print("\nMenu:")
        print("1. Tambahkan Kata ke setiap baris")
        print("2. Hapus Kata")
        print("3. Hapus baris dari bawah")
        print("4. Check kata yang sama di antara baris")
        print("5. Keluar")
        choice = input("Pilih menu (1/2/3/4/5): ")

        if choice == "1":
            sentence = input("Masukkan kalimat yang ingin Anda tambahkan: ")
            position = input("Pilih posisi untuk menambahkan kalimat (awal/akhir): ")
            add_sentence_to_file(file_path, sentence, position)
            print(f"Kalimat '{sentence}' telah ditambahkan ke file pada posisi {position}.")
        elif choice == "2":
            remove_socks5_prefix(file_path)
            print("Kalimat yang Anda pilih telah dihapus dari file.")
        elif choice == "3":
            num_lines = int(input("Masukkan jumlah baris yang ingin dihapus dari bawah: "))
            remove_lines_from_bottom(file_path, num_lines)
            print(f"{num_lines} baris telah dihapus dari bawah file.")
        elif choice == "4":
            count_duplicate_sentences(file_path)
        elif choice == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
