MAX_DEPTH = 10  # maximum click depth
MIN_DEPTH = 3 # minimum click depth
MAX_WAIT = 10  # maximum amount of time to wait between HTTP requests
MIN_WAIT = 5  # minimum amount of time allowed between HTTP requests
DEBUG = False  # set to True to enable useful console output

# use this single item list to test how a site responds to this crawler
# be sure to comment out the list below it.
#ROOT_URLS = ["https:///digg.com/"]

ROOT_URLS = [
	"https://paid2play.co/share/inyongnation3969i",
	"https://paid2play.co/share/inyongnation6523i",
	"https://paid2play.co/share/chaeriyahmaddu3270c",
	"https://paid2play.co/share/digitalhanddrawing2582d",
	"https://paid2play.co/share/sbp1407806115s",
	"https://paid2play.co/share/panjulkerenbro5857p"
	]


# items can be a URL "https://t.co" or simple string to check for "amazon"
blacklist = [
	"https://t.co", 
	"t.umblr.com", 
	"messenger.com", 
	"itunes.apple.com", 
	"l.facebook.com", 
	"bit.ly", 
	"mediawiki", 
	".css", 
	".ico", 
	".xml", 
	"intent/tweet", 
	"twitter.com/share", 
	"signup", 
	"login", 
	"dialog/feed?", 
	".png", 
	".jpg", 
	".json", 
	".svg", 
	".gif", 
	"zendesk",
	"clickserve"
	]  

# must use a valid user agent or sites will hate you
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) ' \
	'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
