import graphviz

g = graphviz.Graph('G', filename='g_c_n.gv')
g.attr(bgcolor='blue:green', label='Process', fontcolor='white')

with g.subgraph(name='clusterC') as c:
    c.attr(fillcolor='pink:cyan', label='API', fontcolor='white',
           style='filled', gradientangle='370')
    c.attr('node', shape='box', fillcolor='green:yellow',
               style='filled', gradientangle='20')
    c.node("Creation")
    c.attr('node', shape='box', fillcolor='green:yellow',
               style='filled', gradientangle='20')
    c.node("States")
    c.attr('node', shape='box', fillcolor='green:yellow',
               style='filled', gradientangle='20')
    c.node("Tools")
    with c.subgraph(name='clusterD') as d:
        d.attr(fillcolor='blue:pink', label='System Call', fontcolor='white',
           style='filled', gradientangle='200')
        d.attr('node', shape='box', fillcolor='green:yellow',
               style='filled', gradientangle='30')
        d.node('fork()')
        d.attr('node', shape='box', fillcolor='green:yellow',
               style='filled', gradientangle='30')
        d.node('wait()')
        d.attr('node', shape='box', fillcolor='green:yellow',
               style='filled', gradientangle='30')
        d.node('exec()')

g.view()