import requests.exceptions
from apps.movie_search_app import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    print('--------------------------------')
    print('        MOVIE SEARCH APP')
    print('--------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}, {}, {}'.format(
                        r.year, r.title, r.imdb_score, r.genres
                    ))
                print()
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print('exiting...')


if __name__ == '__main__':
    main()
