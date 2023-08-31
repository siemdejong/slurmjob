import argparse
from . import create_interactive, run_interactive, set_config

def main():
    parser = argparse.ArgumentParser(description="Manage Slurm jobs.")
    subparsers = parser.add_subparsers(dest="command")

    parser_config = subparsers.add_parser("config", help="Configure Slurm settings.")
    
    parser_create = subparsers.add_parser("create", help="Create a new interactive Slurm job.")
    
    parser_run = subparsers.add_parser("run", help="Run a Slurm job.")
    parser_run.add_argument("name", type=str, help="Name of the job to run.")

    args = parser.parse_args()

    if args.command == "config":
        set_config.main()
    elif args.command == "create":
        create_interactive.main()
    elif args.command == "run":
        run_interactive.main(args.name)