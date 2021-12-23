import argparse
from cli.cmd.loadCSV import load_from_csv
from cli.cmd.loadCSV import load_all_csv
from cli.cmd.clearDatabase import clear_database
from cli.cmd.ETL import create_dwh_tables
parser = argparse.ArgumentParser()
 
subparser = parser.add_subparsers()
printer = subparser.add_parser('load_csv', help="load_csv")
printer.set_defaults(which='load_csv')
printer.add_argument('path')

printer = subparser.add_parser('load_all_csv', help="load_all_csv")
printer.set_defaults(which='load_all_csv')

printer = subparser.add_parser('run_etl', help="run_etl")
printer.set_defaults(which='run_etl')

printer = subparser.add_parser('clear_db', help="clear_db")
printer.set_defaults(which='clear_db')

 
args = parser.parse_args()

if hasattr(args, 'which'):
    if args.which == 'load_csv':
        load_from_csv(args.path)
        print(args.which)
    if args.which == 'load_all_csv':
        load_all_csv()
        print(args.which)
    if args.which == 'run_etl':
        create_dwh_tables()
        print(args.which)                      
    if args.which == 'clear_db':
        clear_database()


        