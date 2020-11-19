import requests as req


def get_html(url: str, params={}, output=None) -> str:
    """
    Fetch html content of a requested url.
    :param url: URL to be fetched.
    :type url: str
    :param params: Dictionary with parameters to be passed with the request.
    :type params: dict
    :param output: Path to the file where the document should stored.
    :type output: str
    :return: html content of the requested URL
    :rtype: str
    """
    request = req.get(url, params=params)
    response = request.text
    if output is not None:
        with open(output, 'w') as out_file:
            out_file.write(response)
    return response


if __name__ == '__main__':
    batch_1 = [
        'https://en.wikipedia.org/wiki/Studio_Ghibli',
        'https://en.wikipedia.org/wiki/Star_Wars',
        'https://en.wikipedia.org/wiki/Dungeons_ %26_Dragons',
    ]
    batch_2 = [
        'https://en.wikipedia.org/w/index.php',
        'https://en.wikipedia.org/w/index.php',
    ]
    batch_2_params = [
        {'title': 'Main Page', 'action': 'info'},
        {'title': 'Hurricane Gonzalo', 'oldid': '983056166'}
    ]
    for url, idx in zip(batch_1, range(len(batch_1))):
        file_name = f'./requesting_urls/output_1_0{idx}.txt'
        get_html(url, {}, file_name)

    for url, idx, params in zip(batch_2, range(len(batch_2)), batch_2_params):
        file_name = f'./requesting_urls/output_2_0{idx}.txt'
        get_html(url, params, file_name)
