# -*- coding: utf-8 -*-

#Hangman - Jogo da forca
#programação orientada a objetos

#import
import random

#Board - tabuleiro

board = ['''

 +---+
 |   |
     |
     |
     |
     |
==========''', '''

 +---+
 |   |
 o   |
     |
     |
     |
==========''', '''
 +---+
 |   |
 o   |
 |   |
     |
     |
==========''', '''
 +---+
 |   |
 o   |
/|   |
     |
     |
==========''', '''

 +---+
 |   |
 o   |
/|\  |
     |
     |
==========''', '''
 +---+
 |   |
 o   |
/|\  |
/    |
     |
==========''', '''
 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
==========''']

#classe

class Hangman:

#método construtor

    def __init__(self, word):
        self.word = word
        self.acerto = ''
        self.erro = ''
        self.count_error = 0
        self.letters = ''
        self.hidden_word = []
        self.guessing = []
        self.letter_guessed = ''
        self.current_board = board[self.count_error]
    #método para adivinhar a letra

    def guess(self, letter):
        j = 0
        self.letters =""
        if self.letter_guessed.upper() in self.hidden_word:
            self.acerto += self.letter_guessed + " "
            while j <= (len(self.hidden_word) - 1):
                if self.hidden_word[j] == self.letter_guessed.upper():
                    self.guessing[j] = self.letter_guessed.upper()
                j += 1
        elif self.letter_guessed.upper() not in self.hidden_word:
            self.erro += self.letter_guessed + " "
            self.count_error += 1
        else:
            return False
        return True


    #método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or self.count_error == 6

    #método para verificar se o jogador venceu
    def hangman_won(self):
        if self.count_error < 6  and self.hidden_word == self.guessing:
            return True
        else:
            return False

    #método para não mostrar a letra no tabuleiro
    def hide_word(self):
        for letter in self.word:
            self.hidden_word.append(letter.upper())
            self.guessing.append("_")
        return self.hidden_word, self.letters
    #método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        self.letters = ""
        print(self.current_board)
        i = 0
        while i <= (len(self.guessing) - 1):
            self.letters += self.guessing[i] + " "
            i += 1
        print('Palavra: {}'.format(self.letters))
        print('\n Letras erradas: {} \n\n Letras certas: {}'.format(self.erro, self.acerto))

#função para ler uma palavra de forma aleatória no banco de palavras

def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()

def main():
    #object
    game=Hangman(rand_word())
    game.hide_word()

    #Enquanto o jogo não tiver terminado, print do status solicita uma letra e faz a leitura do caracter
    while game.count_error < 6 and game.guessing != game.hidden_word:
        while not game.hangman_over():
            game.print_game_status()
            game.letter_guessed = input('\nDigite uma letra: ')
            game.guess(game.letter_guessed)

            #Verifica o status do jogo
            game.print_game_status()

        #De acordo com o status, imprime mensagens na tela para o usuário

    if game.hangman_won():
        print("Parabéns! Você venceu!")
    if game.hangman_over():
        print("Game over! Você perdeu")
        print("A palavra era {word}".format(word=game.word))

    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

#Executa o programa
if __name__== "__main__":
    main()



