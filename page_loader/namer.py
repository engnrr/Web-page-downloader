"""Module for getting names depending on the URL of the page."""
import re
import os
from urllib.parse import urlparse


def get_filename(url, ext='.html'):

    '''
    TODO: ограничить максимальную длину имени
    '''
    u = urlparse(url)
    parsed_url = u.hostname + u.path
    url_head, url_tail = os.path.splitext(parsed_url)

    if url_tail == ext:
        return f'{filename_convert(url_head)}{ext}'

    return f'{filename_convert(parsed_url)}{ext}'


def filename_convert(filename):
    return re.sub(f'\W', '-', filename)