# Receives the friendship status to determine the cost of trade
# Use easygui to display information
# Based off of data from 'https://i.redd.it/zw086dsi9n511.png'

from easygui import *

friend = False
good_friend = False
great_friend = False
ultra_friend = False
best_friend = False
player1_have_player2 = False
player2_have_player1 = False
special_trade = False
regional = False
player1_name = ""
player2_name = ""
player1_pokemon = ""
player2_pokemon = ""
player1_pokemon_shiny = False
player2_pokemon_shiny = False
mythical = False
owned = False
cost = 0
title = "Trade Stardust Calculator (Updated September 9, 2018)"

def get_names():
    global title, player1_name, player2_name
    player1_name = enterbox("What is the name of Player One?", title)
    player2_name = enterbox("What is the name of Player Two?", title)

def get_friendship_level():
    global title, friendship_level, friend, good_friend, great_friend, ultra_friend, best_friend
    friendship_level = choicebox("What is the current friendship level?",
                                 title, ["Friends", "Good Friends",
                                         "Great Friends", "Ultra Friends",
                                         "Best Friends"])
    if friendship_level == "Friends":
        friend = True
    elif friendship_level == "Good Friends":
        good_friend = True
    elif friendship_level == "Great Friends":
        great_friend = True
    elif friendship_level == "Ultra Friends":
        ultra_friend = True
    elif friendship_level == "Best Friends":
        best_friend = True

def get_pokemon():
    global title, player1_name, player2_name, player1_pokemon, player2_pokemon, player1_have_player2, player2_have_player1, regional, owned
    player1_pokemon = enterbox("Which pokemon does " + player1_name + " want to give away? \n Please type exactly as it is (i.e. Farfetch'd, Mr. Mime, Porygon2)", title)
    player2_pokemon = enterbox("Which pokemon does " + player2_name + " want to give away? \n Please type exactly as it is (i.e. Farfetch'd, Mr. Mime, Porygon2)", title)
    player1_pokemon_shiny = ynbox("Is " + player1_pokemon + " a shiny?", title)
    player2_pokemon_shiny = ynbox("Is " + player2_pokemon + " a shiny?", title)
    player1_have_player2 = ynbox("Does " + player1_name + " have " + player2_pokemon + " registered in their pokedex?", title)
    player2_have_player1 = ynbox("Does " + player2_name + " have " + player1_pokemon + " registered in their pokedex?", title)
    if player1_have_player2 or player2_have_player1:
        special_trade = True
    if player1_pokemon_shiny or player2_pokemon_shiny:
        special_trade = True
    if player2_have_player1 or player1_have_player2:
        owned = True
    if player1_pokemon or player2_pokmeon == "Articuno" or "Zapdos" or "Moltres" or "Mewtwo" or "Raikou" or "Entei" or "Suicune" or "Lugia" or "Ho-oh" or "Regice" or "Registeel" or "Regirock" or "Latios" or "Latias" or "Kyogre" or "Groudon" or "Rayquaza":
        special_trade = True
    if player1_pokemon or player2_pokmeon == "Mew" or "Celebi":
        mythical = True
    if player1_pokemon or player2_pokemon == "Tropius" or "Volbeat" or "Illumise" or "Relicanth" or "Lunatone" or "Solrock" or "Seviper" or "Zangoose" or "Torkoal" or "Corsola" or "Heracross" or "Tauros" or "Mr. Mime" or "Kangaskhan" or "Farfetch'd":
        regional = True

def get_price():
    global title, cost, owned, player1_name, player2_name, player1_pokemon, player2_pokemon, player1_have_player2, player2_have_player1, mythical, special_trade, regional, friend, good_friend, great_friend, ultra_friend, best_friend
    if friend:
        if special_trade or regional:
            cost = 33
        else:
            if owned:
                cost = 100
            else:
                cost = 20,000
    elif good_friend:
        if owned:
            if special_trade:
                cost = 20,000
            else:
                cost = 100
        else:
            if special_trade:
                cost = 1,000,000
            else:
                cost = 20,000
    elif great_friend:
        if owned:
            if special_trade:
                cost = 16,000
            else:
                cost = 80
        else:
            if special_trade:
                cost = 800,000
            else:
                cost = 16,000
    elif ultra_friend:
        if owned:
            if special_trade:
                cost = 1,600
            else:
                cost = 8
        else:
            if special_trade:
                cost = 80,000
            else:
                cost = 1,600
    elif best_friend:
        if owned:
            if special_trade:
                cost = 800
            else:
                cost = 4
        else:
            if special_trade:
                cost = 40,000
            else:
                cost = 800
    
def final_text():
    global title, player1_name, player2_name, player1_pokemon, player2_pokemon, cost, mythical, friend, good_friend, great_friend, ultra_friend, best_friend
    if mythical:
        msgbox("Mythical pokemon cannot be traded!", title)
        exit()
    else:
        if cost == 33:
            msgbox("Inadequate friendship levels \n Trade is not possible", title)
        else:
            if friend:
                msgbox("As friends, trading " + str(player1_name) + "'s " + str(player1_pokemon) + " for " + str(player2_name) + "'s " + str(player2_pokemon) + " will cost " + str(cost) + " stardust", title)
            elif good_friend:
                msgbox("As good friends, trading " + str(player1_name) + "'s " + str(player1_pokemon) + " for " + str(player2_name) + "'s " + str(player2_pokemon) + " will cost " + str(cost) + " stardust", title)
            elif great_friend:
                msgbox("As great friends, trading " + str(player1_name) + "'s " + str(player1_pokemon) + " for " + str(player2_name) + "'s " + str(player2_pokemon) + " will cost " + str(cost) + " stardust", title)
            elif ultra_friend:
                msgbox("As ultra friends, trading " + str(player1_name) + "'s " + str(player1_pokemon) + " for " + str(player2_name) + "'s " + str(player2_pokemon) + " will cost " + str(cost) + " stardust", title)
            elif best_friend:
                msgbox("As best friends, trading " + str(player1_name) + "'s " + str(player1_pokemon) + " for " + str(player2_name) + "'s " + str(player2_pokemon) + " will cost " + str(cost) + " stardust", title)

def final_code():
    get_names()
    get_friendship_level()
    get_pokemon()
    get_price()
    final_text()

final_code()
