URL = "https://www.coindesk.com/search?s=bitcoin"

PAGES = 3

DELAY = 3

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'AKA_A2=A; querylyvid=1268140894',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'If-Modified-Since': 'Sun, 21 May 2023 13:06:48 GMT',
    'If-None-Match': 'W/"56249-9GmoH8PPKCO3amsTElxLQNWZIvs"',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
