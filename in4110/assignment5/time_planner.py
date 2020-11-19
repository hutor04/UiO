from bs4 import BeautifulSoup
import requests
import re


def extract_events(url, output=None):
    """
    Extracts events from pages like https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup.
    It reads the table substitutes colspan rowspan and returns the table in the specified Markdown table format.
    :param url: url of the page from which the data should be extracted.
    :type url: str
    :param output: Optional argument, path to the file where the data should be saved.
    :type output: str
    :return: Markdown formatted table.
    :rtype: str.
    """
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id='Calendar').parent.find_next_sibling("table")
    data = table.find_all('tr')[1:]

    row_span = []
    col_span = []

    for idx, tr in enumerate(data):
        for td_idx, content in enumerate(tr.find_all('td')):
            if content.has_attr('colspan'):
                if td_idx == 0:
                    col_span.append((idx, td_idx, int(content['colspan'])))
    for i in col_span:
        for reps in range(1, i[2]):
            tag = soup.new_tag('td')
            tag.string = 'NaN'
            data[i[0]].insert(i[1]+reps, tag)

    for idx, tr in enumerate(data):
        for td_idx, content in enumerate(tr.find_all('td')):
            if content.has_attr('rowspan'):
                row_span.append((idx, td_idx, int(content['rowspan']), content.get_text()))

    results = [[data.get_text() for data in row.find_all('td')] for row in data]

    for i in row_span:
        for reps in range(1, i[2]):
            results[i[0]+reps].insert(i[1], i[3])

    map_months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
                  'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    date_regex = re.compile(r"(?P<day>[1-9]|0[1-9]|[12][0-9]|3[01])\s+(?P<month>\w+)\s+(?P<year>\d{4})")
    type_regex = re.compile(r"(?P<type>[A-Z][A-Z])")

    normalized_results = []
    for result in results:
        date = date_regex.search(result[2])
        if date is not None:
            row = []
            month = map_months[date_regex.search(result[2]).group("month")]
            row.append(f'{month}/{date_regex.search(result[2]).group("month")}/'
                       f'{date_regex.search(result[2]).group("year")}')
            row.append(result[3].strip())
            row.append(type_regex.search(result[4]).group('type'))
            normalized_results.append(row)

    table_header = '| Date | Venue | Discipline | Who Wins? |\n|------|-------|------------|-----------|\n'
    table_content = [f'| {date} | {venue} | {discipline} |  |\n' for date, venue, discipline in normalized_results]
    table_content = ''.join(table_content)
    table = table_header + table_content

    if output is not None:
        with open(output, 'w') as out_file:
            out_file.write(table)

    return table


if __name__ == '__main__':
    path = 'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup'
    extract_events(path, 'datetime_filter/betting_slip_empty.md')
