#!/usr/bin/python3
#
# Spaceration - Jogo de exploração espacial.
#
# Site      : https://github.com/linuxjeff
# Autor     : Jefferson Santana <computadores.rp@gmail.com>
#
# -----------------------------------------------------------------------------
#   Descrição: Jogo de exploração espacial e RPG.
#
# -----------------------------------------------------------------------------
#
#
# Histórico:
#
#  v0.0.1 02-11-2023, Jefferson Santana
#   - Versão inicial
#   - Criado o cabeçalho
#   - Criada área de importação de bibliotecas
#   - Criada área de variáveis iniciais
#   - Criado menu inicial do jogo
#   - Criada a opção de sair do jogo
#
# Licença: MIT.
#

# Impotando bibliotecas

from os import system
from time import sleep

# Impotando bibliotecas ###
# Variáveis iniciais.

PlayerOne = str('PlayerOne')

MenuCH = int(0)

MenuOpcao = str('')



# Variáveis íniciais. ###
# Menu ínicial
while True:
    # Limpa a tela
    system('export TERM=xterm ; clear') or None
    MenuOpcao = str(input('1 - Iniciar Jogo\n2 - Carregar Jogo(Não implementado)\n3 - Opções(Não implementado)'
                          '\n4 - Sair\n>>> '))
    if MenuOpcao == '1':
        MenuCH = int(1)
    elif MenuOpcao == '4':
        system('export TERM=xterm ; clear') or None
        break
    else:
        # Limpa a tela
        system('export TERM=xterm ; clear') or None
        print('Opção inválida!')
        sleep(2)
# Menu ínicial ###
#


