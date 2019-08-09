#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def open_xyz(filename):
    """ Opens a file and provides two files one with symbols and one with coordinates"""
    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(numpy.float)
    return symbols,coordinates

def bond_check(distance, minimum_length =0, maximum_length =1.5):
    if distance > minimum_length and distance<maximum_length:
        return True
    else:
        return False
    
    
def calculate_distance(atom1_coord, atom2_coord):
    """docstring"""
    
    x_distance =atom1_coord[0]-atom2_coord[0]
    y_distance = atom1_coord[1]-atom2_coord[1]
    z_distance = atom1_coord[2]-atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return bond_length_12

file_location =os.path.join('data','data', 'water.xyz')
symbols, coord = open_xyz(file_location)
num_atoms = len(symbols)
for num1 in range(0, num_atoms):
    for num2 in range(0,num_atoms):
        if num1<num2:
            bond_lenght_12 =calculate_distance(coord[num1], coord[num2])
            if bond_check(bond_lenght_12) is True:
                print(F'{symbols[num1]} to {symbols[num2]}: {bond_lenght_12:.3f}')

