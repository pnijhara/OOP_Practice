from scene import Scene

class Planet(Scene):

    def enter(self):
        print("You won! Good job.")
        return "finished"