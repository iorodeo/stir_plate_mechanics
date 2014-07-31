from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

safeZ = 0.15
stepZ = 0.02
startZ = 0.0
stopZ = -(params['plate']['thickness'] + 0.12) 
feedrate = 2.5
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

# Part mount holes 10-32 tap holes
partHoleDict = params['partMountHoles']
for partXPos in params['plate']['xPosArray']:
    for i in (-1,1):
        xPos = partXPos + i*0.5*partHoleDict['holeSpacing']
        yPos = partHoleDict['yMidPos'] + i*0.5*partHoleDict['holeSpacing'] 
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
print(fileName)
prog.write(fileName)
