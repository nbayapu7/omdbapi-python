from omdb import OMDBClient
import sys, getopt, os
import json


def help():
    print """\nomdbapi.py [options]
Options:
-t | --title  "Movie Title"
-h | --help   "Print help message"
"""


def main(argv):
    argv1 = ["-h", "--help", "-t", "--title"]

    try:
        if os.environ['OMDB_API_KEY'] != "":
            pass
    except:
        print "Error: Bash: Export 'OMDB_API_KEY'"
        sys.exit(2)

    if len(sys.argv) < 2:
        print "Error: Insufficient arguments "
        help()
        sys.exit(2)
    elif len(sys.argv) > 3:
        print "Error: More arguments "
        help()
        sys.exit(2)

    if sys.argv[1] in argv1:
        pass
    else:
        print ("Error: Invalid option {0}").format(sys.argv[1])
        help()
        sys.exit(2)

    if len(sys.argv) == 2:
        if sys.argv[1] == "-t" or sys.argv[1] == "--title":
            print ("Error: Title is missing")
            help()
            sys.exit(2)

    title_name = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:t:",["help=","title="])
    except:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit()
        elif opt in ("-t", "--title"):
            title_name = arg
        else:
            print "Error: invalid input"
            help()
    client = OMDBClient(apikey=os.environ['OMDB_API_KEY'])
    for title in client.search(title_name, timeout=5, tomatoes=True):
        if title['type'] == 'movie':
            print ("Title: {0}").format(title['title'])
            print '------------------------------------------'
            print (json.dumps(title, ensure_ascii=True, indent=4))


            
if __name__ == "__main__":
    main(sys.argv[1:])
