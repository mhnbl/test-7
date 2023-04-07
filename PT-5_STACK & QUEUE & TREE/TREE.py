import os
os.system('cls')
class tree:
    def __init__ (self,data):
        self.data = data
        self.children = []
        self.parent = None

    
    def addChild(self,child):
        child.parent = self
        self.children.append(child)

    def removiChild(self,child):
        if child in self.children:
            self.children.remove(child)
        else:
            print("Data Tidak Ditemukan")

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent

        return level
 
    def printTree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else""
        print(prefix + self.data)
        if self.children: 
            for child in self.children:
                child.printTree()

def build_product_tree():
    root = tree("elektronik")

    laptop = tree("laptop")
    hp = tree("hp")
    tv = tree("tv")

    laptop.addChild(tree("asus"))
    laptop.addChild(tree("axio"))
    laptop.addChild(tree("dell"))

    hp.addChild(tree("samsung"))
    hp.addChild(tree("redmi"))
    hp.addChild(tree("LG"))
    
    tv.addChild(tree("PANASONIC"))
    tv.addChild(tree("TV2"))
    tv.addChild(tree("TV3"))

    root.addChild(laptop)
    root.addChild(hp)
    root.addChild(tv)

    return root

root = build_product_tree()
root.printTree()