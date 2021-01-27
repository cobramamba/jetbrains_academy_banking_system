class House:
    def __init__(self, floors):
        self.floors = floors
        self.color = None

    # create the method here
    def paint(self, col):
        self.color = col
        # print("The place of {} floors is now {}.".format(self.floors, self.color))


# place = House(2)
# place.paint("red")
