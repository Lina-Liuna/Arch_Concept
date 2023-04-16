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

ds_1 = {
    'c' : 'Address',
    'sub':[
        {
            'c': 'Address Space',
            'n':['goals','Address Spce', 'Multiprogramming and Time Sharing']
        },
        {
            'c': 'Address Translation',
            'n': ['an example', 'Dynamic(Hardware-based) Relocation',
                  'Hardware support', "Operating system issues"]
        }
    ]
}
ds_2 = {
    'c' : 'Memory API',
    'n' : ['free() call','malloc() call','other calls','Type of Memory','underlying OS support'],
}


ds_4 = {
    'c' : 'Segmentaion',
    'n' : ['Generalized Base Bounds', 'which segment are we referring to',
           'what about the Stack', 'support for Sharing',
           "Fine grained vs. Coarse grained Segmentation",
           'OS Support']


}
ds_5 = {
    'c' : 'Free Space Management',
    'n' : ['low level mechanism', 'baisc strategies', 'other approaches'],

}
ds_6 = {
    'c' : 'Paging',
    'sub':[
        {
            'c': 'Introduction',
            'n':['a simple example', 'where are Page Tables Stored'
                 'Whats Actually In the Page Table',
                 "Paging Also Too Slow",
                 'A memory Trace']
        },
        {
            'c': 'Faster Translation(TLBs)',
            'n':[
                "TLB Bsic Algorithm", 'Example Accessing An Arrary',
                "Who handles The TLB Miss ", "TLB Contents Whats In There ",
                "TLB Issue Context Switches",
                "Issue Replacement Policy",
                "A Real TLB Entry"
            ]
        },
        {
            'c': "Small Tables",
            'n': ['Simple Solution Bigger Pages',
                  "Hybrid Approach Paging and Segments",
                  "Multi level Page Tables",
                  'Inverted Page Tables',
                  'Swapping the Page Tables to Disk']
        }
    ]
}
ds_7 = {
    'c' : 'Beyond Physical Memory',
    'n' : '',
    'sub':[
        {
            'c': 'Mechanisms',
            'n':[
                "Swap space", 'The present Bit', 'The Page Fault',
                'What if Memory is Full', 'Page Fault Control Flow',
                'When Replacements Really Occur'
            ]
        },
        {
           'c': 'Policies',
            'n':[
                'Cache Management', "The Optimal Replacement Policy",
                "A simple Policy FIFO", 'A Simple Policy Random',
                "Uing History LRU", "workload examples",
                "Implementing Historical Algorithms",
                "Approximating LRU",
                "Consider Dirty Pages",
                "Other VM Policies",
                'Thrashing'
            ]
        }
    ]
}
ds_8 = {
    'c' : 'Complete Virtual Memory System',
    'n' : ['VAX VMS Virtual Memory', 'The Linux Virtual memory System'],

}

data_struct = {
   'g': 'Memory Virtualization',
    'sub':[ ds_1,
             ds_2, ds_4, ds_5, ds_8,
              ds_7,
          ds_6
    ]

}


def sub_diagram(label_ds, graph, sub_name):

    with graph.subgraph(name=sub_name) as c:
        c.attr(rankdir='TB')
        c.attr(fillcolor=random_color(), label=label_ds['c'], fontcolor='black',
               style='filled', gradientangle='100',rankdir='TB')
        first_node = 'None'
        if 'n' in label_ds:
            for item in label_ds['n']:
                c.attr(rankdir='TB')
                c.attr('node', shape='box', fillcolor=random_color(),
                    style='filled', gradientangle='20',rankdir='TB')
                c.attr(rankdir='TB')
                c.node(item)
                if first_node != 'None':
                    c.edge(first_node, item, penwidth='0.0', len='0.1')
                first_node = item

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