import struct
import numpy as np
import os
import pathlib
from dataclasses import dataclass

#class containing all aspects of a file
@dataclass
class Data():
  name: str
  output: str
  variable: str
#   data: list
  #timestep: int

#list containing all categorized files
options = []
materials =[]
variables = []

#location of directory contining all files
directory = '/Users/vli/Desktop/test_datacopy'


#categorize all files into the class
for file in os.listdir(directory):
	fname = 'test_datacopy/{}'.format(file)
	split1 = fname.split('.')
	split2 = split1[2].rsplit('_', 1)

	nx,nz = 14,30
	bytes_total = os.path.getsize(fname)
	f           = open(fname,'rb')
	bytes_read   = 80+80+4+80+4
	bytes_remain = bytes_total - bytes_read
	num_elems    = bytes_remain/4
	format       = str(int(num_elems))+'f'
	raw_data     = struct.unpack(format,f.read(bytes_remain)) # n x float
	f.close()
	
	data = np.array(raw_data)
	data = data.reshape(nx,nz)
	
	materialone = Data((split2[1][:-4]), split1[1], split2[0])
	options.append(materialone)
	
# print(options)

for i in options:
	materials.append(i.name)
	variables.append(i.variable)


@dataclass 
class Dumpdata():
	# create a dictionary for each material with arrays for each variable
	for material in materials:
		material : {}
		
	for key in variables:
		material[key] : {}
