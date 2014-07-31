from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_surface
from params import params

feedrate = 20.0
side = '+'
startZ = 0.0
safeZ = 0.5
depthZ = 0.41
depthY = 0.01
toolDiam = 0.25 
maxCutDepth = 0.025
cutDirection = '-'
returnDist = 0.1
startDwell = 2.0


minimumX = -0.5*params['plate']['width'] - toolDiam
maximumX = 0.5*params['plate']['width'] + toolDiam


prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


param = { 
        'side'            : side,       
        'positionY'       : -depthY,
        'minimumX'        : minimumX,
        'maximumX'        : maximumX,
        'startZ'          : startZ,
        'depth'           : depthZ,
        'returnDist'      : returnDist,
        'safeZ'           : safeZ,
        'toolDiam'        : toolDiam,
        'maxCutDepth'     : maxCutDepth,
        'cutDirection'    : cutDirection,
        'startDwell'      : startDwell,
        }

print(param)
surface = cnc_surface.SurfaceRasterXZ(param)
prog.add(surface)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
