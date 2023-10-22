import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    model = models.user.User(name="admin", username="admin", password="admin", role="admin")
    dbsession.add(model)
    
    # create 10 data movies
    movies = [
        {
            "title" : "Money Heist",
            "genre" : "Crime",
            "synopsis" : "A criminal mastermind who goes by 'The Professor' has a plan to pull off the biggest heist in recorded history -- to print billions of euros in the Royal Mint of Spain. To help him carry out the ambitious plan, he recruits eight people with certain abilities and who have nothing to lose. The group of thieves take hostages to aid in their negotiations with the authorities, who strategize to come up with a way to capture The Professor. As more time elapses, the robbers prepare for a showdown with the police.",
        },
        {
            "title": "The Witcher",
            "genre": "Fantasy",
            "synopsis": "Geralt of Rivia, a solitary monster hunter, struggles to find his place in a world where people often prove more wicked than beasts."
        },
        {
            "title": "The Mandalorian",
            "genre": "Sci-Fi",
            "synopsis": "After the fall of the Galactic Empire, lawlessness has spread throughout the galaxy. A lone gunfighter makes his way through the outer reaches, earning his keep as a bounty hunter."
        },
        {
            "title": "Game of Thrones",
            "genre": "Fantasy",
            "synopsis": "Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss for HBO. It is an adaptation of A Song of Ice and Fire, George R. R. Martin's series of fantasy novels, the first of which is A Game of Thrones. The show was shot in the United Kingdom, Canada, Croatia, Iceland, Malta, Morocco, and Spain. It premiered on HBO in the United States on April 17, 2011, and concluded on May 19, 2019, with 73 episodes broadcast over eight seasons."
        },
        {
            "title": "The Walking Dead",
            "genre": "Horror",
            "synopsis": "-"
        },
        {
            "title": "The Flash",
            "genre": "Sci-Fi",
            "synopsis": "-"
        },
        {
            "title": "Arrow",
            "genre": "Sci-Fi",
            "synopsis": "-"
        },
        {
            "title": "The Big Bang Theory",
            "genre": "Comedy",
            "synopsis": "-"
        },
        {
            "title": "The Good Doctor",
            "genre": "Drama",
            "synopsis": "-"
        },
        {
            "title": "The 100",
            "genre": "Sci-Fi",
            "synopsis": "-"
        }
    ]

    for movie in movies:
        model = models.movie.Movie(title=movie['title'], genre=movie['genre'], synopsis=movie['synopsis'])
        dbsession.add(model)






def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
