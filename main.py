from sys import exit
from random import randint
from textwrap import dedent
from death import Death
from planet import Planet
from scene import Scene
from corridor import CentralCorridor
from armory import Armory
from bridge import Bridge
from pod import EscapePod


# class Scene(object):
#     def enter(self):   
#         print("This scene is not yet configured.")
#         print("Subclass it and implement enter().")
#         exit(0)


class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()



# class CentralCorridor(Scene):

#     def enter(self):
#         print(dedent("""
#             The Gothons of Planet Percal #25 have invaded your ship and
#             destroyed your entire crew.
#             member and your last mission is to get the neutron destruct
#             bomb from the Weapons Armory, put it in the bridge, and
#             blow the ship up after getting into an escape pod.
#             You are the last surviving
            
#             You're running down the central corridor to the Weapons
#             Armory when a Gothon jumps out, red scaly skin, dark grimy
#             teeth, and evil clown costume flowing around his hate
#             filled body. He's blocking the door to the Armory and
#             about to pull a weapon to blast you.
#             """))
#         print("Choose between shoot, dodge, tell a joke")

#         action = input("---->")

#         if action == "shoot":
#             print(dedent("""
#                 Quick on the draw you yank out your blaster and fire
#                 it at the Gothon.
#                 moving around his body, which throws off your aim.
#                 Your laser hits his costume but misses him entirely.
#                 This completely ruins his brand new costume his mother
#                 bought him, which makes him fly into an insane rage
#                 and blast you repeatedly in the face until you are
#                 dead.
#                 """))
#             return "death"
        
#         elif action == "dodge":
#             print(dedent("""
#                 Like a world class boxer you dodge, weave, slip and
#                 slide right as the Gothon's blaster cranks a laser
#                 past your head.
#                 your foot slips and you bang your head on the metal
#                 wall and pass out.
#                 die as the Gothon stomps on your head and eats you.
#                 In the middle of your artful dodge
#                 You wake up shortly after only to see your death
#                 """))
#             return "death"

#         elif action == "tell a joke":
#             print(dedent("""
#                 Lucky for you they made you learn Gothon insults in
#                 the academy. You tell the one Gothon joke you know:
#                 Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
#                 fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
#                 not to laugh, then busts out laughing and can't move.
#                 While he's laughing you run up and shoot him square in
#                 the head putting him down, then jump through the
#                 Weapon Armory door.
#                 """))
#             return "armory"

#         else:
#             print("Does not Compute!")
#             return "central_corridor"


# class Armory(Scene):

#     def enter(self):
#         print(dedent("""
#             You do a dive roll into the Weapon Armory, crouch and scan
#             the room for more Gothons that might be hiding.
#             quiet, too quiet. Find
#             the room and find the neutron bomb in its container.
#             There's a keypad lock on the box and you need the code to
#             It's dead
#             You stand up and run to the far side of
#             get the bomb out.
#             If you get the code wrong 10 times then
#             the lock closes forever and you can't get the bomb.
#             code is 3 digits.
#             """))
        
#         code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
#         count = 0
        
#         while count < 10:
#             guess = input("ENTER your CHOICE")

#             if guess == code:
#                 print(dedent("""
#                 The container clicks open and the seal breaks, letting
#                 gas out. You grab the neutron bomb and run as fast as
#                 you can to the bridge where you must place it in the
#                 right spot.
#                 """))
#                 return "bridge"
            
#             print("BUZZZZZZED")
#             count+=1
#         else:
#             print(dedent("""
#             The lock buzzes one last time and then you hear a
#             sickening melting sound as the mechanism is fused
#             together. You decide to sit there, and finally the
#             Gothons blow up the ship from their ship and you die.
#             """))
#             return "death"
            

# class Bridge(Scene):

#     def enter(self):
#         print(dedent("""
#             You burst onto the Bridge with the netron destruct bomb
#             under your arm and surprise 5 Gothons who are trying to
#             take control of the ship. Each of them has an even uglier
#             clown costume than the last. They haven't pulled their
#             weapons out yet, as they see the active bomb under your
#             arm and don't want to set it off.
#             """))
#         print("Choose one \"Throw bomb\" \"Slowly place the bomb\" ")

#         action = input("---->")

#         if action == "Throw bomb":
#             print(dedent("""
#             He notice you. You are dead now.
#             """))
#             return "death"

#         elif action == "Slowly place the bomb":
#             print(dedent("""
#             You point your blaster at the bomb under your arm and
#             the Gothons put their hands up and play to sweat.
#             You inch backward to the door, open it, and then
#             carefully place the bomb on the floor, pointing your
#             blaster at it. You then jump back through the door,
#             punch the close button and blast the lock so the
#             Gothons can't get out. Now that the bomb is placed
#             you run to the escape pod to get off this tin can.
#             """))
#             return "finished"

#         else:
#             print("Does not Compute!")
#             return "bridge"

    
# class EscapePod(Scene):

#     def enter(self):
#         pass


# class Planet(Scene):

#     def enter(self):
#         print("You won! Good job.")
#         return "finished"


# class Death(Scene):

#     quips = [
#         "You died",
#         "You kinda suck at this.",
#         "Your Mom would be proud...if she were smarter.",
#         "Such a luser.",
#         "I have a small puppy that's better at this.",
#         "You're worse than your Dad's jokes."
#     ]

#     def enter(self):
#         print(Death.quips[randint(0, len(self.quips)-1)])
#         exit(1)


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'death': Death(),
        'finished': Planet(),
        'armory': Armory(),
        'bridge': Bridge(),
        'pod': EscapePod()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()