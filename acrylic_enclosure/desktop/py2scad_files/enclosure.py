"""
Creates an enclosure
"""
from __future__ import print_function
from py2scad import *

# Inside dimensions
x,y,z = 3.5*INCH2MM, 3.5*INCH2MM, 1.75*INCH2MM

topHoleSize = 0.116*INCH2MM
botHoleSize = 0.089*INCH2MM
holeOffset = 5.0

print("\ntop mount hole sep (in): ", (x+2*holeOffset)/INCH2MM)

# Add outer edge holes in top
holeList = []
for i in (-1,1):
    for j in (-1,1):
        holeX = i*(0.5*x + holeOffset)
        holeY = j*(0.5*y + holeOffset)
        print("hole (x,y):", holeX/INCH2MM, holeY/INCH2MM)
        hole = {
                'type' : 'round',
                'panel': 'top',
                'size' : topHoleSize,
                'location' : (holeX,holeY)
                }
        holeList.append(hole)


# Add hole in cener of top
hole = {
    'type'     : 'rounded_square',
    'panel'    : 'top',
    'size'     : (2.0*INCH2MM,2.0*INCH2MM,0.25*INCH2MM),
    'location' : (0,0),
    }
holeList.append(hole)

params = {
        'inner_dimensions'        : (x,y,z), 
        'wall_thickness'          : 3.0, 
        'lid_radius'              : 0.25*INCH2MM,  
        'top_x_overhang'          : 0.25*INCH2MM,
        'top_y_overhang'          : 0.25*INCH2MM,
        'bottom_x_overhang'       : 0.25*INCH2MM,
        'bottom_y_overhang'       : 0.25*INCH2MM, 
        'lid2front_tabs'          : (0.25, 0.75),
        'lid2side_tabs'           : (0.25, 0.75),
        'side2side_tabs'          : (0.5,),
        'lid2front_tab_width'     : 0.75*INCH2MM,
        'lid2side_tab_width'      : 0.75*INCH2MM, 
        'side2side_tab_width'     : 0.5*INCH2MM,
        'standoff_diameter'       : 0.25*INCH2MM,
        'standoff_offset'         : 0.05*INCH2MM,
        'standoff_hole_diameter'  : 0.116*INCH2MM, 
        'hole_list'               : holeList 
        }

enclosure = Basic_Enclosure(params)
enclosure.make()


print('\nstandoff hole locations (in)')
for hole in enclosure.standoff_hole_list:
    loc = hole['location']
    print(loc[0]/INCH2MM, loc[1]/INCH2MM)

part_assembly = enclosure.get_assembly(explode=(0,0,0))
part_projection = enclosure.get_projection()

prog_assembly = SCAD_Prog()
prog_assembly.fn = 50
prog_assembly.add(part_assembly)
prog_assembly.write('enclosure_assembly.scad')

prog_projection = SCAD_Prog()
prog_projection.fn = 50
prog_projection.add(part_projection)
prog_projection.write('enclosure_projection.scad')
