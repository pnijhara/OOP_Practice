from textwrap import dedent
from scene import Scene

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew.
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.
            You are the last surviving
            
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))
        print("Choose between shoot, dodge, tell a joke")

        action = input("---->")

        if action == "shoot":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon.
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                and blast you repeatedly in the face until you are
                dead.
                """))
            return "death"
        
        elif action == "dodge":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head.
                your foot slips and you bang your head on the metal
                wall and pass out.
                die as the Gothon stomps on your head and eats you.
                In the middle of your artful dodge
                You wake up shortly after only to see your death
                """))
            return "death"

        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            return "armory"

        else:
            print("Does not Compute!")
            return "central_corridor"