import config
import requests
import random
import time
from utils import create_folder, extract_link, get_name, LOG

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


create_folder([config.LYRICS_FOLDER])


def get_lyrics(url):
    resp = requests.get(url)
    parsed_html = BeautifulSoup(resp.content, features="html.parser")
    text = parsed_html.select('.col-xs-12.col-lg-8.text-center')[0].text
    return text


def crawler():
    counter = 1
    for url_ref in config.FULL_URLS:
        resp = requests.get(url_ref)
        if resp.status_code == 200:
            _, name = get_name(url_ref)
            # Ensure folder exists
            folter_path = create_folder([config.LYRICS_FOLDER, name])
            # Get all links
            parsed_html = BeautifulSoup(resp.content, features='html.parser')
            lyrics_links = parsed_html.select('.listalbum-item a')
            LOG.info(f"Number of {name.upper()} songs: {len(lyrics_links)}")

            lyric_paths = [extract_link(link) for link in lyrics_links]

            for lyric_path in lyric_paths:

                try:
                    writer, song_name = get_name(lyric_path)
                    if name != writer:
                        alt_folder = create_folder([config.LYRICS_FOLDER, writer])
                        lyrics_file = alt_folder.joinpath(song_name + '.txt')
                        file_found = lyrics_file.is_file()
                    else:
                        writer = name
                        lyrics_file = folter_path.joinpath(song_name + '.txt')
                        file_found = lyrics_file.is_file()

                    if not file_found:
                        # url = config.BASE_URL + lyric_path
                        text = get_lyrics(lyric_path).strip()
                        LOG.info("Downloading (" + str(counter).zfill(3) +
                                 f") [{writer}]: {song_name}")
                        counter += 1

                        with open(lyrics_file, "w") as f:
                            f.write(text)
                        time.sleep(config.CRAWLER_WAIT + config.CRAWLER_WAIT * random.random())

                except IndexError:
                    LOG.error(f"Access denied while scraping: {lyric_path} \n"
                              f"Try increasing the waiting time.\n"
                              f"Finishing the scrapping for the moment. Try to access on your browser to unblock access")
                    return
                except Exception as err:
                    print(f"ERROR: {lyric_path}: {err}")

        else:
            LOG.warning(f"Unable to load: {url_ref}")


if __name__ == '__main__':
    crawler()
