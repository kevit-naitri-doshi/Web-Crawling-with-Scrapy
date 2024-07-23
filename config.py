from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


# PROJECT_NAME='plusdagjeuit'
PROJECT_NAME='ranveerbrar'

# SPIDER_NAME='plusdagjeuit'
SPIDER_NAME='ranveerbrar'

# domains=["plusdagjeuit.nl"]
domains=["ranveerbrar.com"]

# complete_url="https://plusdagjeuit.nl/"
complete_url="https://ranveerbrar.com/"

# base_url=[complete_url]
base_url=[complete_url]

# rules = [
#         Rule(
#             LinkExtractor(
#                 canonicalize=True,
#                 unique=True,
#                 allow=('content-partner'),
#                 allow_domains=tuple(domains),

#             ),
#             follow=True,
#             callback="parse_link"
#         ),
#     ]

rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True,
                allow=('recipes','special-recipes'),
                allow_domains=tuple(domains),
                deny=('comment','#','post'),
                deny_domains=('addtoany.com','amazon.in')
            ),
            follow=True,
            callback="parse_link"
        ),
    ]

# urls_to_be_removed=[]
urls_to_be_removed=['jpg', 'png', 'pdf', 'comment', 'post','respond','page','jpeg','#']

path='/home/kevit/Downloads/chromedriver-linux64/chromedriver'