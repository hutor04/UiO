from requesting_urls import get_html
from bs4 import BeautifulSoup
from players_data import data
import matplotlib.pyplot as plt


def extract_name(url):
    """
    Extracts name of the team from semifinals column.
    :param url: Path to the wikipage with data about the season.
    :type url: str
    :return: List with the team names.
    :rtype: list[str]
    """
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id='Bracket').parent.find_next_sibling("table")
    data = table.find_all('tr')
    teams = []
    for i in range(4, 42, 12):
        teams.append(data[i].find_all('td')[3])
        teams.append(data[i+2].find_all('td')[3])

    return [team.a.text for team in teams]


def extract_url(url):
    """
    Extracts name of the link to the teams' pages among the teams that made it to semifinal.
    :param url: Path to the wikipage with data about the season.
    :type url: str
    :return: List with the team URLs.
    :rtype: list[str]
    """
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id='Bracket').parent.find_next_sibling("table")
    data = table.find_all('tr')
    teams = []
    for i in range(4, 42, 12):
        teams.append(data[i].find_all('td')[3])
        teams.append(data[i + 2].find_all('td')[3])

    return ['https://en.wikipedia.org/' + team.a['href'] for team in teams]


def extract_player_list(url):
    """
    Extrcacts names of the players and the URLs to their personal profiles.
    :param url: Path to the data about teams seasons with a roster.
    :type url: str
    :return: List of dictionaries where each list item contains a players profile. {name: {url: <url>}}
    :rtype: list
    """
    result = {}
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id='Roster').parent.find_next_sibling("table")
    data = table.find_all('tr')[2].find_all('td')[0].find_all('tr')
    for player in data[1:]:
        player_data = player.find_all('td')[2]
        result[player_data.a.text] = {'url': 'https://en.wikipedia.org' + player_data.a['href']}

    return result


def extract_player_statistics(url):
    """
    Extracts statistics about the player during the season 2019-20
    :param url: Path to the personal page of a player.
    :type url: str
    :return: Points per game, blocks per game, and rebounds per game in the season.
    :rtype: dict
    """
    result = {'PPG': 0, 'BPG': 0, 'RPG': 0}
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        table = soup.find(id=['Regular_season', 'Regular_Season']).parent.find_next_sibling("table")
        data = table.find_all('tr')
        for i in data:
            rows = i.find_all('td')
            if len(rows) > 0:
                if rows[0].text.strip() == '2019–20':
                    result['PPG'] = float(rows[-1].text.strip())
                    result['BPG'] = float(rows[-2].text.strip())
                    result['RPG'] = float(rows[8].text.strip())
                    break
        return result
    except:
        print(f'Error fetching player data from: {url}')
        return result


def extract_data():
    """
    Extracts the following data: team names that got into semi-finals, team urls that got into semi-finals,
    the lists of players that participated in the season, and the performance of each player. The data is then
    saved into a dictionary and it is returned.
    Note: some personal pages of players contain irregularities in their patterns, such players were ignored.
    :return: Data about teams, players, and their performance.
    :rtype: dict
    """
    result = {}
    team_names = extract_name('https://en.wikipedia.org/wiki/2020_NBA_playoffs')
    team_urls = extract_url('https://en.wikipedia.org/wiki/2020_NBA_playoffs')
    for name, url in zip(team_names, team_urls):
        result[name] = {'team_url': url}
        result[name]['players'] = extract_player_list(url)

    for team in result.keys():
        players = result[team]['players']
        for player in players.keys():
            url = players[player]['url']
            print(url)
            statistics = extract_player_statistics(url)
            result[team]['players'][player]['stats'] = statistics

    return result


def plot_charts(data):
    """
    Plots the charts with player data as saves them to files as per requirements.
    :param data: dict object with the list of teams, players, and their statistics.
    :type data: dict
    :return: none
    :rtype: none
    """
    PPG = []
    BPG = []
    RPG = []
    for team, team_data in data.items():
        players = team_data['players']
        for k, v in sorted(players.items(), key=lambda item: item[1]['stats']['PPG'], reverse=True)[0:3]:
            PPG.append((team, k, v['stats']['PPG']))
            BPG.append((team, k, v['stats']['BPG']))
            RPG.append((team, k, v['stats']['RPG']))

    team_colors = {'Milwaukee': 'green', 'Miami': 'red', 'Boston': 'yellow', 'Toronto': 'blue',
                   'LA Lakers': 'purple', 'Houston': 'orange', 'Denver': '#1b458f', 'LA Clippers': '#003399'}

    fig = plt.figure(figsize=(13, 13))
    ax = fig.add_subplot(111)

    for idx, player in enumerate(sorted(PPG, key=lambda item: item[2])):
        team = player[0]
        ax.plot(player[2], player[1], 'o', color=team_colors[team], zorder=3)

    ax.grid(color='white', linewidth=5)

    ax.set_xlabel('PPG')
    ax.set_ylabel('NAME')
    plt.xticks([x for x in range(8, 30, 1)])
    plt.savefig('NBA_player_statistics/players_over_ppg.png')
    fig.clear()

    ax = fig.add_subplot(111)

    for idx, player in enumerate(sorted(BPG, key=lambda item: item[2])):
        team = player[0]
        ax.plot(player[2], player[1], 'o', color=team_colors[team], zorder=3)

    ax.grid(color='white', linewidth=5)

    ax.set_xlabel('BPG')
    ax.set_ylabel('NAME')
    plt.savefig('NBA_player_statistics/players_over_bpg.png')
    fig.clear()

    ax = fig.add_subplot(111)

    for idx, player in enumerate(sorted(RPG, key=lambda item: item[2])):
        team = player[0]
        ax.plot(player[2], player[1], 'o', color=team_colors[team], zorder=3)

    ax.grid(color='white', linewidth=5)

    ax.set_xlabel('RPG')
    ax.set_ylabel('NAME')
    plt.savefig('NBA_player_statistics/players_over_rpg.png')


if __name__ == '__main__':
    # Uncomment line below if you want to re-fetch data
    # data = extract_data()
    plot_charts(data)
