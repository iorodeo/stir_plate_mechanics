from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_boundary
from params import params

safeZ = 0.15
toolDiam = 0.25
feedrate = 22.0 
direction = 'ccw'
offset = 'outside'
startDwell = 2.0

startZDeep = 0.0
removalMargin = 0.03
removalOverCut = 0.01
maxCutDepthDeep = 0.04
depthDeep = params['partDepth'] - removalMargin 
startZLite = startZDeep - depthDeep
depthLite = removalMargin + removalOverCut 
maxCutDepthLite = 0.02


prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

boundaryParams = params['boundaryCut']

cnt = 0

for xPosLayout, yPosLayout in zip(params['xPosList'], params['yPosList']):

    cnt += 1
    if cnt < 4:
        continue

    if 0:
        cutDictDeep = { 
                'centerX'      : xPosLayout + boundaryParams['xPos'],
                'centerY'      : yPosLayout + boundaryParams['yPos'],
                'radius'       : boundaryParams['radius'],
                'depth'        : depthDeep,
                'startZ'       : startZDeep,
                'safeZ'        : safeZ,
                'toolDiam'     : toolDiam,
                'toolOffset'   : offset,
                'direction'    : direction,
                'maxCutDepth'  : maxCutDepthDeep,
                'startDwell'   : startDwell,
                }
        boundaryDeep = cnc_boundary.CircBoundaryXY(cutDictDeep)
        prog.add(boundaryDeep)


    if 1:
        cutDictLite = { 
                'centerX'      : xPosLayout + boundaryParams['xPos'],
                'centerY'      : yPosLayout + boundaryParams['yPos'],
                'radius'       : boundaryParams['radius'],
                'depth'        : depthLite,
                'startZ'       : startZLite,
                'safeZ'        : safeZ,
                'toolDiam'     : toolDiam,
                'toolOffset'   : offset,
                'direction'    : direction,
                'maxCutDepth'  : maxCutDepthLite,
                'startDwell'   : startDwell,
                }
        boundaryLite = cnc_boundary.CircBoundaryXY(cutDictLite)
        prog.add(boundaryLite)


prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
prog.write(fileName)
