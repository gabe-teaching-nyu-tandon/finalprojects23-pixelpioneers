import argparse
import logging

parser = argparse.ArgumentParser()

logging_arg_group = parser.add_mutually_exclusive_group(required=False)
logging_arg_group.add_argument(
    '-d', '--debug',
    help="Print lots of debugging statements",
    action="store_const", dest="loglevel", const=logging.DEBUG,
    default=logging.WARNING,
)
logging_arg_group.add_argument(
    '-v', '--verbose',
    help="Be verbose",
    action="store_const", dest="loglevel", const=logging.INFO,
)

args = parser.parse_args()

logging.basicConfig(level=args.loglevel)
logger = logging.getLogger(__name__)


def main():
    logger.info("In CLI: main()")


if __name__ == "__main__":
    main(args)
