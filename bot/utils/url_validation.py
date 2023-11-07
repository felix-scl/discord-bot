from urllib.parse import urlparse


def url_validation(url, scheme, hostname):
    parsed_url = urlparse(url)

    if parsed_url.scheme == scheme and parsed_url.hostname == hostname:
        return True
    else:
        return False
