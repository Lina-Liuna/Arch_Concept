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

io_ds = {
    'c': 'I/O Devices',
    'n': [
        '1. System Architecture',
        "2. A Canonical Device",
        "3. THe Canonical Protocol",
        '4. Lowering CPU Overhead with the Interrupts',
        '5. More Efficient Data Movement with DMA',
        '6. Methods of Device Interaction',
        "7. Fitting into the OS: The Device Driver",
        '8. Case Study: A simple IDE Disk Driver',
    ]
}
hard_disk_drives_ds = {
    'c': 'Hard Disk Drives',
    'n':[
        '1. The Interface',
        '2. Basic Geometry',
        '3. A Simple Disk Drive',
        '4. I/O Time, Doing the math',
        '5. Disk Scheduling'
    ]
}
RAID_ds = {
    'c' : 'Redundant Arrays of Inexpensive Disks(RAIDs)',
    'n' : [
        '1. Interface And RAID Internals',
        '2. Fault Model',
        '3. How to Evaluate A RAID',
        '4. RAID Level 0: Striping',
        '5. RAID Level 1: Mirroring',
        '6. RAID Level 4: Saving Space with Parity',
        '7. RAID Level 5: Rotating Parity',
        '8. RAID Comparison: A Summary',
        '9. Other Interesting RAID Issues',
    ]
}
i_files_dirs_ds = {
    'c': 'Interlude: Files and Directories',
    'n':[
        '1. Files and Directories',
        '2. The File System Interface',
        '3. Creating Files',
        '4. Reading and Writing Files',
        '5. Reading and Writing, but not Sequentially',
        '6. Shared File Table Entries: fork() and dup()',
        '7. Writing Immediately with fsync()',
        '8. Renaming Files',
        '9. Getting Information about Files',
        '10. Removing Files',
        '11. Making/Reading/Deleting/ Directories',
        '12. Hard Links',
        '13. Symbolic Links',
        '14. Permission Bits and Access Control Lists',
        '15. Making and Mounting a file system'
    ]
}
fs_implementation_ds = {
    'c': 'File System Implementation',
    'n':[
        '1. The way to think',
        '2. Overall Organization',
        '3. File Organization: The Inode',
        '4. Directory Organization',
        '5. Free Space Management',
        '6. Access Paths: Reading and Writing',
        '7. Caching and Buffering',
    ]
}
lffs_ds = {
    'c': "Locality and The fast file system",
    'n' : [
        '1. The Problem: Poor Performance',
        '2. FFS: Disk Awareness is the solution',
        '3. Organizing Structure: The Cylinder Group',
        '4. Policies: How to Allocate Files and Directories'
        '5. Measuring File Locality',
        '6. The Large-File Exception',
        '7. A Few Other things about FFS',
    ]
}

cc_FSCK_J_ds = {
    'c': 'Crash Consistency: FSCK and Journaling',
    'n':[
        '1. A Detailed Example',
        '2. Solution #1: The File System Checker',
        '3. Solution #2: Journaling(or write-Ahead Logging)',
        '4. Solution #3: Other Approaches'
    ]
}

lsfs_ds = {
    'c' :'Log-structed File Systems',
    'n' : [
        '1. Writing to Disk Sequentially',
        '2. Writing Sequentially And Effectively',
        '3. How much to Buffer?',
        '4. Problem: Finding Inodes',
        '5. Solution Through Indirection: The Inode Map',
        '6. Completing The Solution: The Checkpoint Region',
        '7. Reading a file from Disk: A recap',
        '8. What about directories?',
        '9. A new problem: Garbage Collection',
        '10. Determing Block Liveness',
        '11. A Policy Question: Which Blocks to clean, and when?',
        '12. Crash Recovery And the log'
    ]

}

fb_SSD_ds = {
    'c' : "Flash-based SSDs",
    'n' : [
        '1. Storing a single bit',
        '2. From bits to banks/planes',
        '3. Basic Flash Operations',
        '4. Flash Performance And Reliability',
        '5. From Raw Flash to Flash-Based SSDs',
        '6. FTL Organization: A bad Approach',
        '7. A log-structured FTL',
        '8. Garbage Collection',
        '9. Mapping Table Size',
        '10. Wear Leveling',
        '11. SSD Performance and cost'
    ]
}
data_integrity_ds = {
    'c': "Data Integrity and Protection",
    'n': [
        '1. Disk Failure Modes',
        '2. Handling Latent Sector Errors',
        '3. Detecting Corruption: The Checksum',
        '4. Using Checksums',
        '5. A new Problem: Misdirected Writes',
        '6. One last Problem: Lost Writes',
        '7. Scrubbing',
        '8. Overheads of Checksumming'
    ]
}




data_struct = {
   'g': 'Persistence ',
    'sub':[
# io_ds,
# hard_disk_drives_ds,
# RAID_ds,
# i_files_dirs_ds,
# fs_implementation_ds,
lffs_ds,
cc_FSCK_J_ds,
lsfs_ds,
fb_SSD_ds,
data_integrity_ds,






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