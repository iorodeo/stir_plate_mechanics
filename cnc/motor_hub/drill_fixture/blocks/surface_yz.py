from __future__ import print_function
from py2gcode import gcode_cmd
from py2gcode import cnc_surface
from params import params

feedrate = 20.0
blockWidth = params['blockWidth'] 
blockLength = params['blockLength'] 
startZ = 0.0
safeZ = 0.5
depth = 0.55
toolDiam = 5.0/16.0
maxCutDepth = 0.025
returnDist = 0.1
startDwell = 2.0


minimumY = -0.5*blockWidth - toolDiam
maximumY = 0.5*blockWidth + toolDiam


prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


for side in ('+', '-'):
    if side == '+':
        cutDirection = '+'
        positionX = 0.5*blockLength
    else:
        cutDirection = '-'
        positionX = -0.5*blockLength

    param = { 
            'side'            : side,       
            'positionX'       : positionX,
            'minimumY'        : minimumY,
            'maximumY'        : maximumY,
            'startZ'          : startZ,
            'depth'           : depth,
            'returnDist'      : returnDist,
            'safeZ'           : safeZ,
            'toolDiam'        : toolDiam,
            'maxCutDepth'     : maxCutDepth,
            'cutDirection'    : cutDirection,
            'startDwell'      : startDwell,
            }

    print(param)
    surface = cnc_surface.SurfaceRasterYZ(param)
    prog.add(surface)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
prog.write('surface_yz.ngc')
