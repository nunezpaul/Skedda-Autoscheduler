import argparse


class Config(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Parameters for training model.')
        parser.add_argument('--username', type=str, default=None,
                            help='Username to be used to log into Skedda.')
        parser.add_argument('--password', type=str, default=None,
                            help='Password to be used to log into Skedda.')
        parser.add_argument('--title', type=str, default='West Coast Swing Dance Social',
                            help='Title of the event that is to be posted.')
        parser.add_argument('--body', type=str, default='Come dance the California state dance with us!',
                            help='Body of the event that is to be posted.')
        parser.add_argument('--num_weeks_away', type=int, default=4,
                            help='Number of weeks from today in which the room is to be scheduled. Additive with days.')
        parser.add_argument('--num_days_away', type=int, default=1,
                            help='Number of days from today in which the room is to be scheduled. Additive with weeks.')
        parser.add_argument('--debug', action='store_true', default=False,
                            help='Will take screenshots of each step. Helpful for debugging.')
        parser.add_argument('--display', action='store_true', default=False,
                            help='Will run in headless mode.')
        parser.add_argument('--submit', action='store_true', default=False,
                            help='Will submit the post to skedda for scheduling. Must include this flag to post.')
        self.params = vars(parser.parse_args())


if __name__ == '__main__':
    config = Config()
    print(config.params)