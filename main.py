# Webscraping Project for IMDB and MyDramaList
# mvf 20230108
# base on a youtube course by Patrick Loeber on IMDB scraping - https://www.youtube.com/watch?v=FoPPgcpSmNs

import random
import requests
import os
from bs4 import BeautifulSoup


def get_year(show):
    show_details = show.text.split()
    return show_details[-1]


def get_show_IMDB():
    response = requests.get('https://www.imdb.com/chart/top-english-movies')
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    shows = soup.select('td.titleColumn')
    show_titles = soup.select('td.titleColumn a')
    show_ratings = soup.select('td.posterColumn span[name=ir]')

    all_years = [get_year(show) for show in shows]
    all_actors = [show['title'] for show in show_titles]
    all_titles = [show.text for show in show_titles]
    all_ratings = [float(rating['data-value']) for rating in show_ratings]
    i = random.randrange(0, len(all_titles))
    return {'title': all_titles[i], 'year': all_years[i], 'rating': all_ratings[i], 'actors': all_actors[i]}


if __name__ == '__main__':
    ask = 'y'
    while ask.lower() == 'y':
        just = os.system('clear')
        print("Looking for recommendations from IMDB website: https://www.imdb.com/chart/top-english-movies")
        reco = get_show_IMDB()
        print(f"{reco['title']} {reco['year']}, IMDB Rating : {reco['rating']:.1f}   STARRING : {reco['actors']}")
        ask = input('Another recommendation? [press y to continue, any key to exit] ')