#!/usr/bin/env/python3

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def len_of_song(self):
        print(len(self.lyrics))

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

mr_brownstone = Song(["I get up around seven",    
                    "Get outta bed around nine",
                    "And I don't worry about nothin' no",
                    "Cause worryin's a waste of my...time"])

happy_bday.sing_me_a_song()
print()
bulls_on_parade.sing_me_a_song()
print()
mr_brownstone.sing_me_a_song()
print()
mr_brownstone.len_of_song()