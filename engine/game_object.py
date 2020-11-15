from engine.constants import *
from engine.transform import Transform
from engine.behaviour import Behaviour

class GameObject():
    id_tracker = 0
    def __init__(self, name_ = "", layer = -1):
        self.name = name_
        self._id = GameObject.id_tracker
        GameObject.id_tracker += 1
        
        self._layer = layer
        self._parent = None

        self.is_started = False
        self.is_active = True

        self._behaviours = {}
        self._children = {}

        self.transform = Transform()
        
    def start(self):
        for b_name in self._behaviours.keys():
            if not self._behaviours[b_name].is_started:
                self._behaviours[b_name].start()
                    
        for c_name in self._children.keys():
            if not self._children[c_name].is_started:
                self._children[c_name].start()
        self.is_started = True

    def update(self, delta):
        for b_name in self._behaviours.keys():
            if self._behaviours[b_name].is_active:
                self._behaviours[b_name].update(delta)
                
        for c_name in self._children.keys():
            if self._children[c_name].is_active:
                self._children[c_name].update(delta)

    def render(self):
        for b_name in self._behaviours.keys():
            if self._behaviours[b_name].is_active:
                self._behaviours[b_name].render()
                
        for c_name in self._children.keys():
            if self._children[c_name].is_active:
                self._children[c_name].render()

    #Self-management functionality:
    def set_layer(self, layer):
        if not self._parent:
            if layer == BACKGROUND or\
               layer == GAMELAYER or\
               layer == UI:
                self._layer = layer
                for child in self._children:
                    child.check_layer()
            else:
                raise ValueError("Invalid layer")
        else:
            raise ValueError("Cannot change layer of GameObject with parent."+\
                             "\nChange parent GameObject layer instead.")

    def check_layer(self):
        if self._parent and self._parent.get_layer() != self.layer:
            self._layer = self._parent.get_layer()
            for child in self.children:
                child.check_layer()
        return self._layer
                
    def set_parent(self, new_parent):
        if isinstance(new_parent, GameObject):
            if not self._parent:
                new_parent.add_game_object(self)
            else:
                raise ValueError("Cannot set parent of parented object."+\
                                 "\nDetatch it before adding it to a new parent.")
        else:
            raise TypeError("Not a GameObject")

    def has_parent(self):
        return self._parent != None
    
    def detach_parent(self):
        if self._parent:
            return self.parent.detatch_child(self._name)

    def get_layer(self):
        return self._layer

    def get_parent(self):
        return self._parent

    def get_id(self):
        return self._id

    #Behaviour management
    def add_behaviour(self, new_behaviour):
        if isinstance(new_behaviour, Behaviour):
            if new_behaviour.game_object:
                raise ValueError("This "+new_behaviour.name+\
                                 " already has a parent.")
            if isinstance(new_behaviour.name, str):
                if new_behaviour.name == "Transform" or\
                   new_behaviour.name in self._behaviours.keys():
                    raise ValueError(new_behaviour.name+" already attached")
                if new_behaviour.name == "":
                    raise ValueError("Cannot attach empty-named Behaviour")
            else:
                raise TypeError("Behaviour name must be str.")
                
            new_behaviour.game_object = self
            self._behaviours[new_behaviour.name] = new_behaviour
            if not self._behaviours[new_behaviour.name].is_started:
                self._behaviours[new_behaviour.name].start()
            return
        else:
            raise TypeError(new_behaviour.name+" is not a valid Behaviour")

    def remove_behaviour(self, rem_bev):
        name = ""
        if isinstance(rem_bev, Behaviour):
            name = rem_bev.name
        elif isinstance(rem_bev, str):
            name = rem_bev
        else:
            raise TypeError("Not a valide Behaviour or str argument.")
        if name in self._behaviours.keys():
            self._behaviours[name].game_object = None
            return self._behaviours.pop(name)
        else:
            raise ValueError("not found...")

    def get_behaviour(self, behaviour_name):
        if isinstance(behaviour_name, str):
            if behaviour_name == "Transform":
                return self.transform
            if behaviour_name in self._behaviours.keys():
                return self._behaviours[behaviour_name]
            else:
                return None
        else:
            raise TypeError("Not a valid behaviour name")

    def has_behaviour(self, behaviour_name):
        if isinstance(behaviour_name, str):
            return behaviour_name in self._behaviours.keys()
        else:
            raise TypeError("Not a valid behaviour name")

    #Children management
    def add_child(self, child):        
        if isinstance(child, GameObject):
            if child.name == "":
                raise ValueError("Cannot add nameless child.")
            elif child.name not in self._children.keys():
                self._children[child.name] = child
                return self._children[child_name]
            elif child_name in self._children.keys():
                raise ValueError(child.name + " is already a child.")
        else:
            raise TypeError("Not a valid GameObject")

    def get_child(self, child_name):
        if isinstance(child_name, str):
            if child_name in self._children.keys():
                return self._children[child_name]
            else:
                return None
        else:
            raise TypeError("Not a valid GameObject name")

    def has_child(self, child_name):
        if isinstance(child_name, str):
            if child_name == "":
                raise ValueError("Empty-named GameObjects are not valid")
            else:
                return child_name in self._children.keys()
        else:
            raise TypeError("Not a valid GameObject name")
        
    def detach_child(self, child_name):
        if self.has_child(child_name):
            self._children[child_name]._parent = None
            return self._children.pop(child_name)
