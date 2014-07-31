from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket

feedrate = 22.0

width = 2*5.5
height = 3.4
stockThickness = 0.5250
desiredThickness = 0.45
cutDepth = stockThickness - desiredThickness

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


param = {
        'centerX'       : 0.0,
        'centerY'       : 0.0,
        'width'         : width,
        'height'        : height,
        'depth'         : cutDepth,
        'startZ'        : 0.0,
        'safeZ'         : 0.25,
        'overlap'       : 0.3,
        'overlapFinish' : 0.5,
        'maxCutDepth'   : 0.05,
        'toolDiam'      : 0.375,
        'cornerCut'     : False,
        'direction'     : 'ccw',
        'startDwell'  : 2.0,
        }

pocket = cnc_pocket.RectPocketXY(param)
prog.add(pocket)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
prog.write(fileName)
