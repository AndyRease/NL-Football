class Field(object):
    '''
    The field in wich a match is played. The actors (players) will interact with
    other actors and the ball.
    '''

    def __init__(self, height=90, width=60):
        self.height = height
        self.width = width

    def draw(self):
        
