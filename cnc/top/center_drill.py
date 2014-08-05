from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

safeZ = 0.15
startZ = 0.0
stepZ = 0.02
stopZ = -0.09
feedrate = 15 
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

for cx, cy in params['partPosList']:
    for i in (-1,1):
        for j in (-1,1):
            xPos = 0.5*i*params['mountHole']['spacing'] + cx
            yPos = 0.5*j*params['mountHole']['spacing'] + cy
            drillDict =  { 
                    'centerX'    : xPos,
                    'centerY'    : yPos,
                    'startZ'     : startZ,
                    'stopZ'      : stopZ,
                    'safeZ'      : safeZ,
                    'stepZ'      : stepZ,
                    'startDwell' : startDwell,
                    }
            drill = cnc_drill.PeckDrill(drillDict)
            prog.add(drill)
            prog.add(gcode_cmd.Space())

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
prog.write(fileName)
