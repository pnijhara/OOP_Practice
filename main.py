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