import graphviz
import random

cfn = 'color_list.txt'
def color_data(filename):
    color_dict = dict()
    color_list = list()
    with open(filename, 'r') as f:
        for line in f:
            if 'colors' in line:
                color = line
                color_list = list()
                color_dict[color] = color_list
                continue
            str = line.split('	')[0]
            color_list.append(str)
    print(color_dict.items())
    return color_dict


cd = color_data(cfn)

def random_color():
    color_list = list()
    for key, value in cd.items():
        if key == "Pink colors\n":
            color_list.extend(value[2:])
        if key == "Red colors\n":
            color_list.extend(value[4:])
        if key == "Orange colors\n":
            color_list.extend(value[2:])
        if key == "Green color\n":
            color_list.extend(value[7:])
        if key == "Cyan colors\n":
            color_list.extend(value[8:])
        if key == "Yellow colors\n":
            color_list.extend(value[2:-2])
        if key == "Brown color\n":
            color_list.extend(value[6: -3])
        if key == "Purple, violet, and magenta colors\n":
            color_list.extend(value[9:])
        if key == "Blue colors\n":
            color_list.extend(value[5:])
        if key == "White colors\n":
            color_list.extend(value[0:4])
        if key == "Gray and black colors\n":
            color_list.extend(value[3:])

    c1 = random.choice(color_list)
    c2 = random.choice(color_list)

    return c1 + ":" + c2

intro_ds = {
    'c': 'Introduction',
    'n': [
        '1. Why use Threads?',
        "2. How to create a thread?",
        "3. Why it get worse, because of shared data?",
        '4. The heart of the problem: uncontrolled scheduling',
        '5. One more problem: waiting for another',
        '6. The wish for atomicity',
        "7. why in OS class?"
    ]
}
interlude_ds = {
    'c': 'Interlude: Thread API',
    'n':[
        '1. Thread Creation',
        '2. Thread Completion',
        '3. Locks',
        '4. Condition Variables',
        '5. Compiling and Running'
    ]
}
locks_ds = {
    'c' : 'Locks',
    'n' : [
        '1. The basic idea',
        '2. Pthread Locks',
        '3. Building A Lock',
        '4. Evaluating Locks',
        '5. Controlling Interrupts',
        '6. A Failed Attempt: Just Using Loads Stores',
        '7. Building working spin locks with Test-and-set',
        '8. Evaluating Spin Locks',
        '9. Compare and swap',
        '10. Load-Linked and Store-Conditional',
        '11. Fetch-And-Add',
        '12. Too much spinning, what now?',
        '13. Using Queues: Sleeping instead of Spinning',
        '14. Different OS, different support',
        '15. Two-Phase Locks'
    ]
}
lock_based_concurrent_ds_ds = {
    'c': 'Lock-based Concurrent Data Structures',
    'n':[
        '1. Concurrent Counters',
        '2. Concurrent Linked Lists',
        '3. Concurrent Queues',
        '4. Concurrent Hash Table'
    ]
}

c_v_ds = {
    'c': 'Condition Variables',
    'n':[
        '1. what is condition variable?',
        '2. The routines of condition variable',
        '3. The Producer/Consummer(Bounded Buffer) Problem'
        '4. Convering Conditions'
    ]
}
s_ds = {
    'c': "Semaphores",
    'n' : [
        '1. What is semaphore?',
        '2. Binary Semaphores(Locks)',
        '3. Semaphores for ordering',
        '4. The Producer/Consumer(Bound Buffer) Problem',
        '5. Reader-Writer Locks',
        '6. The Dining Philosophers',
        '7. How to implement Semaphores?',
    ]
}

common_concurrency_ds = {
    'c': 'Common Concurrency Problems',
    'n':[
        '1. What types of bugs exist?',
        '2. Non-Deadlock bugs',
        '3. Deadlock Bugs'
    ]
}

eb_c_ds = {
    'c' :'Event-based Concurrency(Advanced)',
    'n' : [
        '1. The basic idea: an event loop',
        '2. An Important API: select()/poll()',
        '3. using select()',
        '4. Why Simpler? No locks needed',
        '5. A problem: Blocking System Calls',
        '6. A Solution: Asynchronous I/O',
        '7. Another Problem: State management',
        '8. What is still difficult with events'
    ]

}





data_struct = {
   'g': 'Concurrency ',
    'sub':[
       # intro_ds,
       # interlude_ds,
       # locks_ds,
       # lock_based_concurrent_ds_ds,
        c_v_ds,
        s_ds,
        common_concurrency_ds,
        eb_c_ds




    ]

}

def alignment_questions_arr(arr):
    rst_arr = list()
    max_len = max(arr, key=len)
    print(len(max_len))
    for item in arr:
        rst_arr.append((len(max_len) - len(item)))
    return rst_arr

def get_node_label(node_name,arr):
    rst_arr_len= alignment_questions_arr(arr)
    label_str = '{'
    # '{<f0> Data|<f1> Next}'
    for rank, (item, item_len) in enumerate(zip(arr, rst_arr_len), 0):
        print(len(item))
        label_str += f'<f{rank}> {item}'
        label_str += '_' * item_len
        if rank != len(arr) - 1:
            label_str += '|'
        else:
            label_str += '}'
    return label_str

def sub_diagram(label_ds, graph, sub_name):

    with graph.subgraph(name=sub_name) as c:
        c.attr(rankdir='TB')
        c.attr(fontname='Comic Sans MS')
        c.attr(fillcolor=random_color(), label=label_ds['c'], fontcolor='black',
               style='filled', gradientangle='100',rankdir='TB')
        if 'n' in label_ds:
            lstr = get_node_label(label_ds['c'], label_ds['n'])

            c.node(label_ds['c'], shape='record',
                    label= lstr, fontname='Monaco', fontcolor='black')

        if 'sub' in label_ds:
            count = 0
            for sub_ds in label_ds['sub']:
                print(f'{count} : {sub_ds}')
                sub_diagram(sub_ds, c, 'Cluster' + str(count))
                count += 1


def diagram(label_ds, file_name):
    g = graphviz.Graph('G', filename= file_name)
    g.attr(bgcolor=random_color(), label=label_ds['g'], fontcolor='black', style='filled',rankdir='TB')
    g.attr(rankdir='TB')
    g.attr(fontname='Comic Sans MS')
    if 'n' in label_ds:
        for item in label_ds['n']:
            g.attr('node', shape='box', fillcolor=random_color(),
                   style='filled', gradientangle='20',rankdir='TB')
            g.attr(rankdir='TB')
            g.node(item)


    if 'sub' in label_ds:
        count = 0
        for sub_ds in label_ds['sub']:
            print(f'{count} : {sub_ds.items()}')
            sub_diagram(sub_ds, g, 'Cluster'+ str(count))
            count += 1

    g.view()

diagram(data_struct, 'g_c_n.gv')