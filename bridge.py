from textwrap import dedent
from scene import Scene

class Bridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. Each of them has an even uglier
            clown costume than the last. They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))
        print("Choose one \"Throw bomb\" \"Slowly place the bomb\" ")

        action = input("---->")

        if action == "Throw bomb":
            print(dedent("""
            He notice you. You are dead now.
            """))
            return "death"

        elif action == "Slowly place the bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and
            the Gothons put their hands up and play to sweat.
            You inch backward to the door, open it, and then
            carefully place the bomb on the floor, pointing your
            blaster at it. You then jump back through the door,
            punch the close button and blast the lock so the
            Gothons can't get out. Now that the bomb is placed
            you run to the escape pod to get off this tin can.
            """))
            return "finished"

        else:
            print("Does not Compute!")
            return "bridge"

    
class EscapePod(Scene):

    def enter(self):
        pass