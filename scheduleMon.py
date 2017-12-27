from AutoScheduler import scheduleSkedda

#This is to be executed on Tuesday 4 weeks in advance

if __name__ == '__main__':
        #schedule South Cats Room from 7-10pm on Monday
        date = scheduleSkedda(-1,
                              title = 'WCS Dance Show Practice',
                              body = 'West Coast Swing practice for danceshow')
