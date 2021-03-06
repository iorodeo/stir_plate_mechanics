"""
Creates an enclosure
"""
from py2scad import *

# Inside dimensions
x,y,z = 6*INCH2MM, 3.5*INCH2MM, 1.75*INCH2MM

topHoleSize = 0.116*INCH2MM
botHoleSize = 0.089*INCH2MM
holeOffset = 3.0 + 0.25*0.5

holeList = []
for i in (-1,1):
    for j in (-1,1):
        holeX = i*(0.5*x + holeOffset)
        holeY = j*(0.5*y + holeOffset)
        hole = {
                'type' : 'round',
                'panel': 'top',
                'size' : topHoleSize,
                'location' : (holeX,holeY)
                }
        holeList.append(hole)
        hole = {
                'type' : 'round',
                'panel': 'bottom',
                'size' : botHoleSize,
                'location' : (holeX,holeY)
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
        'lid2front_tabs'          : (0.2,0.5,0.8),
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
