#############################

# Generic Tree Youtube Practice

#############################

class TreeNode:
    
    def __init__(self,data):
        self.data = data 
        self.children = [] 
        self.parent = None 
        
    def add_child(self,child):
        child.parent = self # child is a instance of tree node class, it will have a parent property and set it to self
        self.children.append(child)
    
    def print_tree(self):
        spaces = ' ' *self.get_level() * 3 # spaces gives each level a indention for cleaner output
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+ self.data)
        if len(self.children) > 0:
            
            for child in self.children:
                child.print_tree() # recursion! recur the function and print the subtrees
    
    def get_level(self): # Treen level so level 0 is parent, 1 is child of root etc
        level = 0
        p = self.parent 
        while p:
            level +=1 
            p = p.parent       
        return level


def build_product_tree():
    root = TreeNode("Electronics") # top of the tree...
    
    laptop =TreeNode("Laptop") # child of the root, with its own child nodes
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Google"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("IPhone"))
    cellphone.add_child(TreeNode("Galaxy"))
    cellphone.add_child(TreeNode("Google"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Vizio"))
    tv.add_child(TreeNode("Apple"))
    
    
    root.add_child(laptop) # we are adding all those children nodes under root node 
    root.add_child(cellphone)
    root.add_child(tv)
    
    #   (Root = Electronics)
    #     /      |       \
    #   laptop   cell    tv
    #  below laptop/cell/tv, is the brands (Mac.Galaxy...)
    
    return root
    
    
    
if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_level()) # level 0 as expected 
    
    root.print_tree()
