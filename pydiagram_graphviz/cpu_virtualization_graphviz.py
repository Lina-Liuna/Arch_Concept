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


data_struct_1 = {
    'c' : 'Process',
    "n" : ["process create", "process state", "process tools", "process control"],
    'sub' :  [{
    'c': 'API',
    'sub' :  [{
    'c' : "System Call",
    'n' : ['fork()', 'wait()', 'exec()']
}]}]

}
data_struct_2 = {
    'c' : 'Mechanism',
    'sub' : [{
        'c' : 'technique',
        'n' :['limited direct execution']
    },
    {
        'c': 'Problem',
        'n':["restricted operations", 'swtiching between process']
    }]


}
data_struct_3 = {
    'c' : 'Scheduling',
    'sub':[
        {
            'c': 'introduction',
            'n': ['workload']
        },
        {
            'c': 'MLFQ',
            'n':['basic rules']

        },
    ]


}
data_struct = {
   'g': 'CPU Virtualization',
    'sub':[data_struct_1,
           data_struct_2,
           data_struct_3,


    ]

}
def sub_diagram(label_ds, graph, sub_name):
    with graph.subgraph(name=sub_name) as c:
        c.attr(fillcolor=random_color(), label=label_ds['c'], fontcolor='white',
               style='filled', gradientangle='370',rankdir='TB')
        if 'n' in label_ds:
            for item in label_ds['n']:
                c.attr('node', shape='box', fillcolor=random_color(),
                    style='filled', gradientangle='20',rankdir='TB')
                c.node(item)
        if 'sub' in label_ds:
            count = 0
            for sub_ds in label_ds['sub']:
                print(f'{count} : {sub_ds}')
                sub_diagram(sub_ds, c, 'Cluster' + str(count))
                count += 1

def diagram(label_ds, file_name):
    g = graphviz.Graph('G', filename= file_name)
    g.attr(bgcolor=random_color(), label=label_ds['g'], fontcolor='white', style='filled',rankdir='TB')
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