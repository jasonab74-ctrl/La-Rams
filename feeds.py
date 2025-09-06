# feeds.py — Los Angeles Rams

TEAM_NAME = "Los Angeles Rams Football"
TEAM_SLUG = "los-angeles-rams"

TEAM_COLORS = {
    "primary": "#003594",
    "secondary": "#FFD100",
    "text": "#111111",
}

TEAM_KEYWORDS = [
    "Los Angeles Rams", "LA Rams", "L.A. Rams", "Rams",
    "SoFi Stadium", "Sean McVay",
    "Matthew Stafford", "Cooper Kupp", "Puka Nacua",
    "Kyren Williams", "Byron Young", "Ernest Jones",
]

SPORT_TOKENS = ["NFL", "football", "National Football League", "Rams"]

EXCLUDE_TOKENS = [
    "women", "basketball", "baseball", "softball", "soccer",
    "hockey", "volleyball", "college", "NCAA",
    "Ramsgate", "Ramadan",
]

# -------- Feeds (populate Sources dropdown) --------
FEEDS = [
    {"name": "\"Los Angeles Rams\" — Google News",
     "url": "https://news.google.com/rss/search?q=%22Los+Angeles+Rams%22&hl=en-US&gl=US&ceid=US:en"},

    {"name": "Bing News — Los Angeles Rams",
     "url": "https://www.bing.com/news/search?q=Los+Angeles+Rams&format=rss"},

    {"name": "therams.com",
     "url": "https://www.therams.com/rss"},

    {"name": "NFL.com — Los Angeles Rams",
     "url": "https://www.nfl.com/rss/team/ram"},

    {"name": "Rams Wire (USA Today)",
     "url": "https://theramswire.usatoday.com/feed/"},

    {"name": "ESPN — Los Angeles Rams Blog",
     "url": "https://www.espn.com/blog/los-angeles-rams/rss"},

    {"name": "NBC Sports — Los Angeles Rams",
     "url": "https://www.nbcsports.com/rss/team/los-angeles-rams"},

    {"name": "Bleacher Report — Los Angeles Rams",
     "url": "https://bleacherreport.com/articles/feed?tag_id=2607"},

    {"name": "Yahoo Sports — Los Angeles Rams",
     "url": "https://sports.yahoo.com/nfl/teams/lar/rss/"},

    {"name": "Reddit — r/LosAngelesRams",
     "url": "https://www.reddit.com/r/LosAngelesRams/.rss"},
]

# -------- Quick Links (buttons at the top) --------
STATIC_LINKS = [
    {"label": "Schedule", "url": "https://www.therams.com/schedule/"},
    {"label": "Roster", "url": "https://www.therams.com/team/players-roster/"},
    {"label": "Depth Chart", "url": "https://www.ourlads.com/nfldepthcharts/depthchart/LA"},
    {"label": "Standings", "url": "https://www.nfl.com/standings/league/2025/REG"},

    # Requested buttons
    {"label": "Reddit Rams", "url": "https://www.reddit.com/r/LosAngelesRams/"},
    {"label": "Fan Zone", "url": "https://www.therams.com/fans"},
    {"label": "Bleacher Report", "url": "https://bleacherreport.com/los-angeles-rams"},
    {"label": "NFL Power Rankings", "url": "https://www.nfl.com/news/power-rankings"},
    {"label": "Stats", "url": "https://www.espn.com/nfl/team/stats/_/name/lar/los-angeles-rams"},
    {"label": "ESPN Team", "url": "https://www.espn.com/nfl/team/_/name/lar/los-angeles-rams"},
]
