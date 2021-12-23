import argparse
from dotenv import load_dotenv
from job.ingestion.ingestion_job import IngestionJob
from job.processing.procesing_job import ProcessingJob
from job.spark_job_base import SparkBaseJob


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--job-type', type=str, required=True)
    parser.add_argument('--config-file', type=str, required=True)
    parser.add_argument('--env', type=str, default="dev")
    parser.add_argument('--app-name', type=str, default="my_job")
    return parser


def get_job_type(args: argparse.Namespace) -> SparkBaseJob:
    if "processing" in args.job_type:
        return ProcessingJob(args)
    elif "ingestion" in args.job_type:
        return IngestionJob(args)


if __name__ == '__main__':
    load_dotenv()
    parser = get_parser()
    args = parser.parse_args()

    job = get_job_type(args)
    job.process()

