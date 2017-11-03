import urllib2
import json

base_url = 'https://publish.twitter.com/oembed?url={}?&hide_media=true&hide_thread=true&omit_script=true'

urls = open('tweets.txt').read().split()

left = []
right = []
i = 0
for i in range(0, len(urls)):
    url = base_url.format(urls[i])
    print url
    resp = urllib2.urlopen(url)
    markup = json.load(resp)['html']
    markup = markup.replace('class="twitter-tweet"', 'class="twitter-tweet tw-align-center"')
    if not i%2:
        left.append(markup)
    else:
        right.append(markup)

print u'''
<div class="row">
<div class="six columns">
{}
</div>
<div class="six columns">
{}
</div>
</div>
'''.format(''.join(left).strip(), ''.join(right).strip())
