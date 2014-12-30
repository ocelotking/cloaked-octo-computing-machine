#!usr/bin/env python

import praw

def main():
    r=praw.Reddit(user_agent='ocelottree')
    r.login('ocelottree', 'treeocelot') 
    r.send_message('mitchmindtree', 'Testmessage', 'I hope this works all my balls will fall off')

if __name__=="__main__":
    main()
