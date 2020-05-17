from logging import INFO
import pathlib


ROOT = pathlib.Path(__file__).parents[1]
LYRICS_FOLDER = 'lyrics'

# Logging settings
LOG_LEVEL = INFO
LOGGER_FORMAT = "%(asctime)s %(message)s"
LOG_FOLDER = ROOT.joinpath('logs')

# References
BASE_URL = "https://www.azlyrics.com/"
# Artists
ARTISTS = ["a/andre3000.html", "e/eminem.html", "g/ghostface.html", "h/hill.html", "i/icecube.html",
           "j/jayz.html", "k/kendricklamar.html", "n/nas.html", "n/notorious.html", "r/rakim.html"]

FULL_URLS = [BASE_URL + art for art in ARTISTS]

CRAWLER_WAIT = 10
VERBOSE = 1
