import re
from requesting_urls import get_html


def find_urls(content, base_url='', output=None):
    """
    Find a href links in body of html document.
    :param content: html content
    :type content: str
    :param base_url: Optional argument, if provided, it is appended to each relative link.
    :type base_url: str
    :param output: Path to the file where the links will be saved
    :type output: str
    :return: List of links found in the content
    :rtype: lst[str]
    """
    # Everything between <body> </body> tags.
    body_regex = re.compile(r"<body[^\>]*>(?P<body>[\s\S]*)<\/body>")

    # <a followed by spaces and any characters followed by href then single or double quotes, then any characters
    # (witch is a matched named group) and again followed by single or double quotes.
    href_regex = re.compile(r"<a\s+.*?href\s*=\s*['\"](?P<path>.*?)['\"]")

    # Matches everything from the beginning of string but #
    remove_fragment_regex = re.compile(r"^[^#]*")

    # Matches strings that begin only with a single slash.
    single_slash_regex = re.compile(r"^/[^/].*")

    body_match = body_regex.search(content)
    body = body_match.group('body') if body_match is not None else ''
    links = [link for link in href_regex.findall(body) if not link.startswith('#')]
    links = [remove_fragment_regex.search(link).group() for link in links]

    if base_url != '':
        for i, link in enumerate(links):
            if single_slash_regex.match(link) is not None:
                links[i] = f'{base_url}{link}'

    if output is not None:
        with open(output, 'w') as out_file:
            for link in links:
                out_file.write(f'{link}\n')
    return links


def find_articles(content, output=None):
    # Matches strings that optionally begin with https// optionally followed by @ then by www. then optionally
    # have a two letter subdomain e.g. en. followed by wikipedia.org
    wiki_regex = re.compile(r"^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?(?P<domain>[^:\/\n?]+[\w{2}]?\.wikipedia\.org)")
    links = find_urls(content)
    links = [link for link in links if wiki_regex.match(link) is not None]

    if output is not None:
        with open(output, 'w') as out_file:
            for link in links:
                out_file.write(f'{link}\n')
    return links


if __name__ == '__main__':
    batch_1 = [
        'https://en.wikipedia.org/wiki/Nobel_Prize',
        'https://en.wikipedia.org/wiki/Bundesliga',
        'https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup'
    ]
    for url, idx in zip(batch_1, range(len(batch_1))):
        file_name = f'./filter_urls/output_1_0{idx}.txt'
        html = get_html(url)
        find_articles(html, file_name)
