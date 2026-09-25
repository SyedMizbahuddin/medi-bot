from src.config.container import AppContainer
import argparse
import logging


def main() -> None:
    """Configure logging, parse CLI options, and run ingestion."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)-32s | %(message)s",
    )

    for logger_name in ("httpx", "httpcore", "huggingface_hub", "transformers", "sentence_transformers"):
        logging.getLogger(logger_name).setLevel(logging.WARNING)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force",
        action="store_true",
        help="Use without force to use the cache",
    )

    args = parser.parse_args()

    container = AppContainer()
    if args.force:
        container.file_store().clear_cache()

    pipeline = container.ingestion_pipeline()

    pipeline.process()


if __name__ == "__main__":
    main()
