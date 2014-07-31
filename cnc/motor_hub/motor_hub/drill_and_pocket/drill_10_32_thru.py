from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

safeZ = 0.15
startZ = 0.0
stopZ = -(params['partDepth'] + 0.08)
stepZ = 0.02
feedrate = 2.0
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

for xPosLayout, yPosLayout in zip(params['xPosList'],params['yPosList']):
    for drill in params['drillHoleList']:

        if not drill['size'] == '10-32,thru':
            continue

        prog.add(gcode_cmd.Space())
        prog.add(gcode_cmd.Comment(drill['name']))
    
        for xPosRel, yPosRel in zip(drill['xPosList'],drill['yPosList']):

            xPos = xPosLayout + xPosRel
            yPos = yPosLayout + yPosRel

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
