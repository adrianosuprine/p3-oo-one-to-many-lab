class Pet:
    all = []
    PET_TYPES =  ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self,name,pet_type,owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError("pet_type must be in Pet.PET_TYPES")
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)
        
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner class")
        self._owner = value
    
        

class Owner:
    def __init__(self,name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self ]
    
    
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
            raise TypeError("ub")
        pet.owner = self
        
    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet: pet.name, reverse=False)
