class Summary:
    """Class that represents a laserforce account's mission Summary. This class gives you a mission summary of a member. You can also initalize this class with kwargs."""
    def __init__(self, content, **kw):
        content = content["centre"]
        try:
            content = content[0]
        except IndexError:
            raise ValueError
        content = content["summary"]
        self.content = content
        try: self.standard = kw["standard"]
        except: pass
        try: self.other = kw["other"]
        except: pass
        try: self.counter_strike = kw["counter_strike"]
        except: pass
        try: self.space_marines = kw["space_marines"]
        except: pass
        try: self.ctf = kw["ctf"]
        except: pass

    @property
    def standard(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[0]

    @property
    def other(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[1]

    @property
    def counter_strike(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[2]

    @property
    def space_marines(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[3]

    @property
    def ctf(self):
        """Returns list [gameType, #missions, dateLastPlayed, highScore, averageScore]"""
        return self.content[4]
        