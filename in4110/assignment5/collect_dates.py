import re
from requesting_urls import get_html


def find_dates(content, output=None):
    """
    Collects page from a body of an html document. It looks for dates only in text content of tags. Supported
    formats are e.g. 10 January 2010; January 10, 2010; M/D/YYYY; MM/DD/YYYY; YYYY. Any four digit integers up to
    2030 are considered a year.
    :param content: html document
    :type content: str
    :param output: Optionally, path to the file where the data will be saved.
    :type output: str
    :return:  List of dates found in the document.
    :rtype: lst[str]
    """
    result = set()
    # Matches anything between < > brackets.
    tag_regex = re.compile(r"<(.|[\n\r\t])*?>")

    # Matches anything between <body>
    body_regex = re.compile(r"<body[^\>]*>(?P<body>[\s\S]*)<\/body>")

    # Month, space, digit from 1 to 9 or digit beginning from 0 with a second digit from 1 to 9, or digit beginning
    # from 1 or 2 with second element from 0 to 9, or digit that begins with 3 and ends with 0 or 1 followed by
    # four digits
    text_month_regex = re.compile(r"(?P<month>January|February|March|April|May|June|July|August|September|October|"
                                  r"November|December)\s+(?P<day>[1-9]|0[1-9]|[12][0-9]|3[01]),\s+(?P<year>\d{4})")

    # Similar as previous but day and month as swapped.
    text_month_regex_2 = re.compile(r"(?P<day>[1-9]|0[1-9]|[12][0-9]|3[01])\s+(?P<month>January|February|March|April|"
                                    r"May|June|July|August|September|October|November|December)\s+(?P<year>\d{4})")

    # Same patter as the two previous ones but months are encoded digitally.
    date_regex = re.compile(r"(?P<month>0[1-9]|1[012])[- /.](?P<day>[1-9]|0[1-9]|[12][0-9]|3[01])[- /.](?P<year>\d{4})")
    year_regex = re.compile(r"\b\d{4}\b")

    map_months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
                  'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

    body_match = body_regex.search(content)
    body = body_match.group('body') if body_match is not None else ''
    body = re.sub(tag_regex, '', body)

    text_dates = [date for date in text_month_regex.findall(body)]
    if len(text_dates) > 0:
        body = re.sub(text_month_regex, '', body)
        for date in text_dates:
            day = date[1] if len(date[1]) > 1 else f'0{date[1]}'
            date_string = f'{date[2]}/{map_months[date[0]]}/{day}'
            result.add(date_string)

    text_dates_2 = [date for date in text_month_regex_2.findall(body)]
    if len(text_dates_2) > 0:
        body = re.sub(text_month_regex_2, '', body)
        for date in text_dates_2:
            day = date[0] if len(date[0]) > 1 else f'0{date[0]}'
            date_string = f'{date[2]}/{map_months[date[1]]}/{day}'
            result.add(date_string)

    numerical_dates = [date for date in date_regex.findall(body)]
    if len(numerical_dates) > 0:
        body = re.sub(date_regex, '', body)
        for date in numerical_dates:
            day = date[1] if len(date[1]) > 1 else f'0{date[1]}'
            date_string = f'{date[2]}/{date[0]}/{day}'
            result.add(date_string)

    years = [date for date in year_regex.findall(body)]
    for date in years:
        if int(date) < 2030:
            result.add(date)

    if output is not None:
        with open(output, 'w') as out_file:
            for i in result:
                out_file.write(f'{i}\n')

    return list(result)


if __name__ == '__main__':
    batch_1 = [
        'https://en.wikipedia.org/wiki/Linus_Pauling',
        'https://en.wikipedia.org/wiki/Rafael_Nadal',
        'https://en.wikipedia.org/wiki/J._K._Rowling',
        'https://en.wikipedia.org/wiki/Richard_Feynman',
        'https://en.wikipedia.org/wiki/Hans_Rosling'
    ]
    for i, idx in zip(batch_1, range(len(batch_1))):
        file_name = f'./filter_dates_regex/output_1_0{idx}.txt'
        html = get_html(i)
        find_dates(html, file_name)
