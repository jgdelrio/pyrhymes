from logging import INFO
import pathlib


# Folders
ROOT = pathlib.Path(__file__).parents[1]
LYRICS_FOLDER = 'lyrics'

# Logging settings
LOG_LEVEL = INFO
LOGGER_FORMAT = "%(asctime)s %(message)s"
LOG_FOLDER = ROOT.joinpath('logs')

# References
BASE_URL = "https://www.azlyrics.com/"
# Artists
ARTISTS = ["k/kendricklamar.html", "n/nas.html", "n/notorious.html", "r/rakim.html"]
ARTISTS_DONE = ["a/andre3000.html", "e/eminem.html", "g/ghostface.html", "h/hill.html", "i/icecube.html",
                "j/jayz.html"]

FULL_URLS = [BASE_URL + art for art in ARTISTS]

# Settings
CRAWLER_WAIT = 16
MAX_LENGTH = int(10000)
VERBOSE = 1
