import sys
import twitteranalyzer

def main(args):
    twitteranalyzer.main(args[1])
    twitteranalyzer.main(args[2])

if __name__ == '__main__':
    main(sys.argv)
