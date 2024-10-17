PROTOCOL = "Protocol"
ASTROMECH = "Astromech"
PROTOCOL_PARTS = ["p_head", "p_chassis", "p_left_arm", "p_right_arm",  "p_left_leg", "p_right_leg"]
ASTROMECH_PARTS: ["a_dome", "a_body", "a_left_leg", "a_center_leg", "a_right_leg"]


class Droid:
    __slots__ = ["__serial_num", "__type", "__parts"]
    def __init__(self, serial_num, type=PROTOCOL):
        self.__serial_num = serial_num
        self.__type = type
        self.__installed = 0


        parts_list = PROTOCOL_PARTS
        if self.__type == ASTROMECH:
            parts_list = ASTROMECH_PARTS
        
        self.__parts = {}
        for part in parts_list:
            self.__parts[part] = False
            
    def needs_part(self, part):
        if part in self.__parts:
            return self.__parts[part] is False
        else:
            return False

    def install(self, part):
        if self.needs_part(part):
            self.__parts[part] = True
            self.__installed += 1
        else:
            raise ValueError(part + "is not a valid part")

    def is_complete(self):
        return self.__installed == len(self.__parts)
    
    def __repr__(self):
        string = self.__type+":\n"\
        + "serial Numaber: " + str(self.__serial_num)+"\n"
        
        for part in self.__parts:
            installed = self.__parts[part]
            string += "\n " + part + ": " + str(installed)

        return string
    
    def __str__(self):
        return str(self.__serial_num) + ", completed: " + str(self.is_complete())

def main():
    protocol = Droid("C3PO")
    print(protocol)
    



if __name__ == "__main__":
    main()

