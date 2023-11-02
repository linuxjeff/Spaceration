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

MenuOpcao = int(0)

# Variáveis íniciais. ###
# Menu ínicial
while MenuCH != 1:
    # Limpa a tela
    system('export TERM=xterm ; clear') or None
    MenuOpcao = int(input('1 - Iniciar\n2 - Carregar(Não implementado)\n3 - Opções(Não implementado)\n>>> '))
    if MenuOpcao == 1:
        MenuCH = int(1)
    else:
        # Limpa a tela
        system('export TERM=xterm ; clear') or None
        print('Opção inválida!')
        sleep(2)
# Menu ínicial ###
#


