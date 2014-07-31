from __future__ import print_function
import os
import scipy
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from py2gcode import cnc_boundary
from params import params

# Cutting parameters
safeZ = 0.5
startZ = 0.0
overlap = 0.4
overlapFinish = 0.6
maxCutDepth = 0.03
toolDiam = 0.25
direction = 'ccw'
startDwell = 2.0
feedrate = 22.0
cutThruMargin = 0.04

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))
prog.add(gcode_cmd.Space())

for i,posLayout in enumerate(zip(params['xPosList'],params['yPosList'])):

    xPosLayout, yPosLayout = posLayout

    if 1:

        # Magnet pocket 
        magnetParams = params['magnetCut']
        for xPosRel, yPosRel in zip(magnetParams['xPosList'], magnetParams['yPosList']):
            xPos = xPosLayout + xPosRel
            yPos = yPosLayout + yPosRel
            pocketDict = { 
                    'centerX'        : xPos, 
                    'centerY'        : yPos,
                    'radius'         : 0.5*magnetParams['diameter'],
                    'depth'          : magnetParams['depth'],
                    'startZ'         : startZ,
                    'safeZ'          : safeZ,
                    'overlap'        : overlap,
                    'overlapFinish'  : overlapFinish,
                    'maxCutDepth'    : maxCutDepth,
                    'toolDiam'       : toolDiam,
                    'direction'      : direction,
                    'startDwell'     : startDwell,
                    }
            pocket = cnc_pocket.CircPocketXY(pocketDict)
            prog.add(pocket)

    if 1:
        if i == (params['numParts'] - 1):
            prog.add(gcode_cmd.Space())
            prog.add(gcode_cmd.Comment('Pause'))
            prog.add(gcode_cmd.Pause())
            prog.add(gcode_cmd.Space())

        # Part boundary
        boundaryParams = params['boundaryCut']
        boundaryDict = { 
                'centerX'      : xPosLayout,
                'centerY'      : yPosLayout,
                'radius'       : boundaryParams['radius'],
                'depth'        : boundaryParams['depth'] + cutThruMargin,
                'startZ'       : startZ,
                'safeZ'        : safeZ,
                'toolDiam'     : toolDiam,
                'toolOffset'   : 'outside',
                'direction'    : direction,
                'maxCutDepth'  : maxCutDepth,
                'startDwell'   : startDwell,
                }
        boundary = cnc_boundary.CircBoundaryXY(boundaryDict)
        prog.add(boundary)


prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
prog.write(fileName)
