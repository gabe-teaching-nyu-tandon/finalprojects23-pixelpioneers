import logging

from pixelpioneers.exceptions import ActionError
from pixelpioneers.actions.unified_actions import UnifiedActions
from pixelpioneers.cli_parser import args
from pixelpioneers.image_io.unified_io import UnifiedIO
from pixelpioneers.utils import get_output_paths

logging.basicConfig(level=args.loglevel)
logger = logging.getLogger(__name__)


def main():
    logger.info("In CLI: main()")

    action_name = args.action
    action_args = args.action_args

    input_paths = args.images
    output_dir = args.dest
    try:
        action_ob = UnifiedActions.get_action_instance(action_name, action_args)
        output_paths = get_output_paths(input_paths, output_dir, action_name)
    except ActionError as ae:
        logger.error(ae, exc_info=False)

    for input_path, output_path in zip(input_paths, output_paths):
        try:
            image = UnifiedIO.read(input_path)
            image_transformed = action_ob.apply(image)
            UnifiedIO.write(output_path, image_transformed)
        except Exception as e:
            logger.error(e, exc_info=False)


if __name__ == "__main__":
    main()
