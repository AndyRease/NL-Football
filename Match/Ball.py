class Ball:
    '''
    The ball has a position and a controller, and both of these attributes
    changes constantly during a matchself.
    The position references a spot on the field and the controller references
    the actor currently running with the ball. If there is no actor in control
    of the ball, it should have 'None' value.

    As a side note, the controller input is an Actor object and should possibly
    be notified as such.
    '''

    def __init__(position, controller=None):
        self.position = position
        self.controller = controller

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_controller(self):
        return self.controller

    def set_controller(self, controller):
        self.controller = controller
