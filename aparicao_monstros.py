# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:13:15 2019

@author: User
"""

### APARARIÇÃO DE MONSTROS ###
def aparece_monstro(cenario_atual):
    if cenario_atual == cenario_atual:
        chance = random.randint(1,10)
        if chance <= 4:
            print('Meu Deus! Um monstro apareceu!')
            combate()
            
            