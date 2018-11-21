import string
import collections
import queue
import sys


def hashing(word):
    sum = 0
    for character in word.rstrip():
        sum += alpha_list[character]
    #print(sum)
    return sum

def gen_dict():
    values = {}
    i = 1
    for index, letter in enumerate(string.ascii_lowercase):
        #print(letter)
        values[letter] = 11**i + 13**i
        i = i + 1
    return values

def children(value, h_map):
    child_nodes = []
    for entry in alpha_list:
        
        if entry in h_map[value][0]:
            new_val_sub = value - alpha_list[entry]
            if new_val_sub in h_map:
                if len(h_map[new_val_sub][0]) == len(h_map[value][0]) - 1:
                    child_nodes.append(new_val_sub)
                    
        new_val_add = value + alpha_list[entry]
        if new_val_add in h_map:
            if len(h_map[new_val_add][0]) == len(h_map[value][0]) + 1:
                child_nodes.append(new_val_add)
        
    return child_nodes

def bfs(start,goal):
    visited = set([start])
    prev_node = {}
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        cur_node = q.get()
        if cur_node==goal:
            ans = []
            while cur_node: ans.append(cur_node);cur_node = prev_node.get(cur_node)
            return ans[::-1]
        for m in children(cur_node,hash_map):
            if m not in visited:
                visited.add(m)
                q.put(m)
                prev_node[m] = cur_node

                
def ladders(start_word, goal_word):
        
    solution = bfs(hashing(start_word),hashing(goal_word))	
    file_string =[]

    for s in solution:
        if start_word in hash_map[s]:
            file_string.append(start_word+'\n')
        elif goal_word in hash_map[s]:
            file_string.append(goal_word+'\n')
        else:
            file_string.append(hash_map[s][0]+'\n')
			
    fh = open("output.txt", "w")
    fh.writelines(file_string)
    fh.close()

first_arg = sys.argv[1]
second_arg = sys.argv[2]

#first_arg = 'croissant'
#second_arg = 'baritone'

word_list = []
for line in open('wordList.txt', 'r'):
	word_list.append(line.rstrip())

alpha_list = gen_dict()
hash_map = collections.defaultdict(list)

for word in word_list:
	hash_map[hashing(word)].append(word)
    
try_symb = 1
if(try_symb == 1):
	ladders(first_arg,second_arg)

