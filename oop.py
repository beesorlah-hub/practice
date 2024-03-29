class RespectiveAnimalSounds:
    def __init__(self, name, legs, sound,can_fly):
        self.name = name
        self.legs = legs
        self.sound = sound
        self.can_fly = can_fly

    def animal_name(self):
        print(self.name)

    def animal_sound(self):
        print(self.sound)

    def animal_leg(self):
        print(self.legs)

    def animal_locomotion(self):
       if self.can_fly:
           print("You can fly")
       else:
           print("you cannot fly")




animal_sound = RespectiveAnimalSounds("cat", 4, "Meow", False)
animal2_sound = RespectiveAnimalSounds("lion", 4, "Roar", False)
animal3_sound = RespectiveAnimalSounds("cow",4, "Moo", False)
animal4_sound = RespectiveAnimalSounds("Elephant",4, "Trumpet", False)
animal5_sound = RespectiveAnimalSounds("Bird",2, "Chirp", True)
animal_sound.animal_name()
animal_sound.animal_sound()
animal_sound.animal_locomotion()
animal2_sound.animal_name()
animal2_sound.animal_sound()
animal3_sound.animal_name()
animal3_sound.animal_sound()
animal4_sound.animal_name()
animal4_sound.animal_sound()
animal5_sound.animal_name()
animal5_sound.animal_sound()
animal5_sound.animal_locomotion()



