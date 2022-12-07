#--- Day 7: No Space Left On Device ---
# contain tree of files
# outermost -> /
# lines beginning with $ are commands executed
# cd x -> move into x
# cd .. -> move out of cwd
# cd / -> move to outermost
# ls -> list all files & dirs
#   123 abc -> a file called "abc" w/ size 123
#   dir xyz -> a dir called "xyz"
# steps:
# find dirs for deletion
# find total dirs w/ size at most 100K
import sys

class Node:
    """
        Parent-Children relationship
    """
    def __init__(self, name, parent=None, size=0) -> None:
        self.children = []
        self.name = name
        self.size = size
        self.parent = parent

    def insert(self, child_node):
        self.children.append(child_node)

    def printTree(self, t:int=0):
        """Prints file tree, [t] is tab count"""
        print('\t'*t, self.name, end='')
        if self.size == 0:
            print(" (dir)")
            if len(self.children):
                for c in self.children:
                    c.printTree(t+1)
                t-=1
        else:
            print(f" (file, size={self.size})")

    def getSize(self, store_ls:list):
        """ Get size of directory; If is not a dir, return file size """
        total_size = 0
        for c in self.children:
            if c.size != 0:
                total_size+=c.size
            else:
                total_size += c.getSize(store_ls)
        if self.size == 0:
            # print(self.name, total_size)
            store_ls.append(total_size)
        return total_size

cmds = []
with open(sys.argv[1], 'r') as f:
    cmds = f.read().split('$')

cmds.remove('')
# print(commands)

root = Node('/')
cwd = root
i = 0
while i < len(cmds):
    args = cmds[i].split('\n')
    if '' in args:
        args.remove('')
    # print(i, "args", args)
    
    if "cd" in args[0]:
        dir_name = args[0].strip().split()[-1]
        # child = Node(dir_name, cwd)
        # cwd.insert(child)
        if dir_name == "..":
            cwd = cwd.parent
            pass
        else:
            for c in cwd.children:
                if dir_name == c.name:
                    cwd = c
                    break
    elif "ls" in args[0]:
        j = 1
        while j < len(args):
            if "dir" in args[j]:
                c_dir_name = args[j].split()[-1]
                c_child = Node(c_dir_name, cwd)
            else:
                fsize, fname = args[j].split()
                c_child = Node(fname, parent=cwd, size=int(fsize))
            cwd.insert(c_child)
            j += 1

    # print('cwd', cwd.name)
    i += 1

root.printTree()
cwd = root
size_sum = 0
store_ls = []
# root.getSize(store_ls)
# print(*store_ls, sep='\n')

# filter out size < 100K
less100 = [i for i in store_ls if i<=100000]
# print(*less100, sep='\n')
print("Part 1", sum(less100))

maxsize = 70000000  # 70M
# unused must be >= 30000000 or 30M
unused = maxsize - max(store_ls)
del_opt = [s for s in store_ls if s >= 30000000-unused]
to_del = min(del_opt)
print("Part 2", to_del)