# Built in library imports
import re
import urllib
import urllib2

# JSON decoder
try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("Need a json decoder")


# Embed.ly Multi Provider API Endpoint
OEMBED_API_ENDPOINT = 'http://api.embed.ly/v1/api/oembed'

# URL Schemes Supported
URL_SCHEMES_RE = (
    r'^http://www\.5min\.com/Video/.*',
    r'^http://.*\.viddler\.com/explore/.*/videos/.*',
    r'^http://qik\.*/video/.*',
    r'^http://www\.hulu\.com/watch/.*',
    r'^http://.*\.revision3\.com/.*',
    r'^http://.*nfb\.ca/film/.*',
    r'^http://.*dailymotion\.com/video/.*',
    r'^http://blip\.tv/file/.*',
    r'^http://.*\.scribd\.com/doc/.*',
    r'^http:/.*\.movieclips\.com/watch/.*',
    r'^http://screenr.com/.+',
    r'^http://twitpic\.com/.*',
    r'^http://.*\.youtube\.com/watch.*',
    r'^http://.*\.youtube\.com/v.*',
    r'^http://yfrog.com.*',
    r'^http://.*amazon.*/gp/product/.*$',
    r'^http://.*amazon\..*/.*/dp/.*$',
    r'^http://.*flickr.com/.*',
    r'^http://.*vimeo\.com/groups/.*/videos/.*',
    r'^http://.*vimeo\.com/.*',
    r'^http://tweetphoto\.com/.*',
    r'^http://www\.collegehumor\.com/video:.*',
    r'^http://www\.funnyordie\.com/videos/.*',
    r'^http://video\.google\.com/videoplay?.*',
    r'^http://www\.break\.com/.*/.*',
    r'^http://www\.slideshare\.net/.*/.*',
    r'^http://www\.ustream\.tv/recorded/.*',
    r'^http://www\.ustream\.tv/channel/.*',
    r'^http://www\.twitvid\.com/.*',
    r'^http://www\.justin.tv/clip/.*',
    r'^http://www\.justin.tv/.*',
    r'^http://vids\.myspace\.com/index.cfm.*$',
    r'^http://www\.metacafe\.com/watch/.*',
    r'^http://.*crackle\.com/c/.*',
    r'^http://www\.veoh\.com/.*/watch/.*',
    r'^http://www\.fancast\.com/.*/.*/videos',
    r'^http://.*imgur\.com/.*$',
    r'^http://.*imgur\.com/.*$',
)


def is_pattern_match(url):
    for pat_re in URL_SCHEMES_RE:
        if re.search(pat_re, url):
            return True
    return False

# returns a dictionary of the oembed object
def get_oembed(url, format='json', maxwidth=None, maxheight=None):

    # make sure embed.ly supports the url scheme
    if not is_pattern_match(url):
       return None

    # gather url, format, maxwidth or maxheight options for embed sizing
    params = {"url": url}
    if maxwidth is not None:
        params['maxwidth'] = maxwidth
    if maxheight is not None:
        params['maxheight'] = maxwidth
    if format is not None:
        params['format'] = format
    
    # generate query string
    query = urllib.urlencode(params)

    # api endpoint url
    fetch_url = "%s?%s" %(OEMBED_API_ENDPOINT,query)

    try:
        r = urllib2.urlopen(fetch_url).read()
        obj = json.loads(r)
    except urllib2.HTTPError, e:
        return None
    except urllib2.URLError:
        return None

    return obj



