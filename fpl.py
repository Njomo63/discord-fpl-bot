import requests, json
from pprint import pprint
import pandas as pd
import sqlite3

BASE_URL = "https://fantasy.premierleague.com/api/"


def get_player_id(name):
    conn = sqlite3.connect("fpl.db")
    cur = conn.cursor()
    cur.execute("SELECT ID FROM players WHERE name=?", (name,))
    res = cur.fetchall()
    conn.close()
    if not res:
        return "Incorrect entry."
    return res[0][0]

# def get_fixtures():
#     r = requests.get(BASE_URL+"fixtures?future=1").json()
#     return r

def get_player_hist_data(name, season):
    id = get_player_id(name)
    if id == "Incorrect entry.":
        return "Incorrect entry."
    URL = BASE_URL + f"element-summary/{id}/"
    r = requests.get(url=URL).json()
    try:
        res = r["history_past"][-season]
        return f"Season Name: {res['season_name']}, Goals: {res['goals_scored']}, Assists: {res['assists']}, Total Points: {res['total_points']}"
    except IndexError:
        return "Player not present in that season"


def get_player_data(name):
    id = get_player_id(name)
    if id == "Incorrect entry.":
        return "Incorrect entry."
    URL = BASE_URL + "bootstrap-static/"
    r = requests.get(url=URL).json()
    players = r["elements"]
    for res in players:
        if res["id"] == id:
            if res["element_type"] == 1: #Goalkeeper
                msg = (f"Cleansheets: {res['clean_sheets']}, "
                    f"Saves: {res['saves']}, "
                    f"Goals Conceded: {res['goals_conceded']}, " 
                    f"Penalties Saved: {res['penalties_saved']}, "
                    f"Yellow Cards: {res['yellow_cards']}, " 
                    f"Red Cards: {res['red_cards']}, " 
                    f"Points per game: {res['points_per_game']}")
            
            elif res["element_type"] == 2: #Defender
                msg = (f"Cleansheets: {res['clean_sheets']}, "
                    f"Goals Conceded: {res['goals_conceded']}, " 
                    f"Goals Scored: {res['goals_scored']}, "
                    f"Assists: {res['assists']}, "
                    f"Yellow Cards: {res['yellow_cards']}, " 
                    f"Red Cards: {res['red_cards']}, "
                    f"Points per game: {res['points_per_game']}")
            
            elif res["element_type"] == 2: #Midfielder
                msg = (f"Cleansheets: {res['clean_sheets']}, "
                    f"Goals Scored: {res['goals_scored']}, "
                    f"Assists: {res['assists']}, "
                    f"Yellow Cards: {res['yellow_cards']}, " 
                    f"Red Cards: {res['red_cards']}, " 
                    f"Points per game: {res['points_per_game']}")
            else:    #Striker
                msg = (f"Goals Scored: {res['goals_scored']}, "
                    f"Assists: {res['assists']}, "
                    f"Yellow Cards: {res['yellow_cards']}, " 
                    f"Red Cards: {res['red_cards']}, " 
                    f"Points per game: {res['points_per_game']}")
    return msg