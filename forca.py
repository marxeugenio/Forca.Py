def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = "python"  # Palavra a ser adivinhada
    guessed_letters = []
    attempts = 6  # Número de tentativas antes de perder o jogo

    print("Bem-vindo ao Jogo da Forca!")
    
    while True:
        print("\nPalavra:", display_word(word, guessed_letters))
        guess = input("Digite uma letra: ").lower()

        if guess in guessed_letters:
            print("Você já tentou essa letra. Tente novamente.")
            continue
        
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"A letra '{guess}' não está na palavra. Você tem {attempts} tentativas restantes.")
            if attempts == 0:
                print("Você perdeu! A palavra era:", word)
                break
        else:
            if "_" not in display_word(word, guessed_letters):
                print("Parabéns! Você ganhou!")
                break

if __name__ == "__main__":
    hangman()
