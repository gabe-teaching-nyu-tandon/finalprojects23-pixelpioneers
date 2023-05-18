import argparse
import logging


class MyArgumentParser(argparse.ArgumentParser):
    def parse_args(self, *args, **kw):
        res = argparse.ArgumentParser.parse_args(self, *args, **kw)
        from argparse import _HelpAction, _SubParsersAction
        for x in parser._subparsers._actions:
            if not isinstance(x, _SubParsersAction):
                continue
            v = x.choices[res.action]  # select the subparser name
            action_args = {}
            for x1 in v._optionals._actions:  # loop over the actions
                if isinstance(x1, _HelpAction):  # skip help
                    continue
                n = x1.dest
                if hasattr(res, n):  # pop the argument
                    action_args[n] = getattr(res, n)
                    delattr(res, n)
            res.action_args = action_args
        return res


parser = MyArgumentParser()

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

parser.add_argument("-i", "--images", nargs="+", required=True, help="List of source images")
parser.add_argument("-dest", required=True, type=str, help="Destination directory")

subparser = parser.add_subparsers(dest="action")

brightness_parser = subparser.add_parser("brightness")
brightness_parser.add_argument("value", type=int, help="Brightness Value, Range = (-255, 255)")

contrast_parser = subparser.add_parser("contrast")
contrast_parser.add_argument("factor", type=float, help="Contrast Factor")

saturation_parser = subparser.add_parser("saturation")
saturation_parser.add_argument("factor", type=float, help="Saturation Factor")

crop_parser = subparser.add_parser("crop")
crop_parser.add_argument("box", type=list, help="Bounding box (x1, y1, x2, y2)")

flip_parser = subparser.add_parser("flip")
flip_parser.add_argument("mode", type=str, choices=["vertical", "horizontal"],
                         help="Flip mode - Horizontal or Vertical")

grayscale_parser = subparser.add_parser("grayscale")

invert_parser = subparser.add_parser("invert")

resize_parser = subparser.add_parser("resize")
resize_parser.add_argument("width", type=int, help="new width")
resize_parser.add_argument("height", type=int, help="new height")

rotate_parser = subparser.add_parser("rotate")
rotate_parser.add_argument("angle", type=int, help="Angle in degrees")

args = parser.parse_args()
