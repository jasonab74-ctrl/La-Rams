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

# Trusted Rams feeds bypass strict filter (prevents empty results)
FEEDS = [
    {"name": "\"Los Angeles Rams\" — Google News",
     "url": "https://news.google.com/rss/search?q=%22Los+Angeles+Rams%22&hl=en-US&gl=US&ceid=US:en",
     "trusted": False},

    {"name": "Bing News — Los Angeles Rams",
     "url": "https://www.bing.com/news/search?q=Los+Angeles+Rams&format=rss",
     "trusted": False},

    {"name": "therams.com",
     "url": "https://www.therams.com/rss",
     "trusted": True},

    {"name": "NFL.com — Los Angeles Rams",
     "url": "https://www.nfl.com/rss/team/ram",
     "trusted": True},

    {"name": "Rams Wire (USA Today)",
     "url": "https://theramswire.usatoday.com/feed/",
     "trusted": True},

    {"name": "ESPN — Los Angeles Rams Blog",
     "url": "https://www.espn.com/blog/los-angeles-rams/rss",
     "trusted": True},

    {"name": "NBC Sports — Los Angeles Rams",
     "url": "https://www.nbcsports.com/rss/team/los-angeles-rams",
     "trusted": True},

    {"name": "Bleacher Report — Los Angeles Rams",
     "url": "https://bleacherreport.com/articles/feed?tag_id=2607",
     "trusted": True},

    {"name": "Yahoo Sports — Los Angeles Rams",
     "url": "https://sports.yahoo.com/nfl/teams/lar/rss/",
     "trusted": True},

    {"name": "Reddit — r/LosAngelesRams",
     "url": "https://www.reddit.com/r/LosAngelesRams/.rss",
     "trusted": True},
]

# Buttons row
STATIC_LINKS = [
    {"label": "Schedule", "url": "https://www.therams.com/schedule/"},
    {"label": "Roster", "url": "https://www.therams.com/team/players-roster/"},
    {"label": "Reddit", "url": "https://www.reddit.com/r/LosAngelesRams/"},
    {"label": "Fan Zone", "url": "https://www.therams.com/fans"},
    {"label": "Bleacher Report", "url": "https://bleacherreport.com/los-angeles-rams"},
    {"label": "NFL Power Rankings", "url": "https://www.nfl.com/news/power-rankings"},
    {"label": "Stats", "url": "https://www.espn.com/nfl/team/stats/_/name/lar/los-angeles-rams"},
    {"label": "Depth Chart", "url": "https://www.ourlads.com/nfldepthcharts/depthchart/LA"},
    {"label": "Standings", "url": "https://www.nfl.com/standings/league/2025/REG"},
    {"label": "ESPN Team", "url": "https://www.espn.com/nfl/team/_/name/lar/los-angeles-rams"},
]
