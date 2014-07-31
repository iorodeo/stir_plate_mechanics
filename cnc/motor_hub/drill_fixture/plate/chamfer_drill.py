from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

safeZ = 0.5
startZ = 0.0
stopZ = -0.025
feedrate = 2.0
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

if 0:
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
                    'startDwell' : startDwell,
                    }
            drill = cnc_drill.SimpleDrill(drillDict)
            prog.add(drill)
            prog.add(gcode_cmd.Space())

if 1:
    # Block mount holes 10-32 through holes
    blockHoleDict = params['blockMountHoles']
    for i in (-1,1):
        for j in (-1,1):
            xPos = i*0.5*blockHoleDict['blockSpacing']
            xPos += j*0.5*blockHoleDict['holeSpacing']
            yPos = blockHoleDict['yPos']
            drillDict =  { 
                    'centerX'    : xPos,
                    'centerY'    : yPos,
                    'startZ'     : startZ,
                    'stopZ'      : stopZ,
                    'safeZ'      : safeZ,
                    'startDwell' : startDwell,
                    }
            drill = cnc_drill.SimpleDrill(drillDict)
            prog.add(drill)
            prog.add(gcode_cmd.Space())


prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
