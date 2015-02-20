from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from params import params

safeZ = 0.15
startZ = 0.0
overlap = 0.3
overlapFinish = 0.6
maxCutDepth = 0.04
toolDiam = 0.25
direction = 'ccw'
startDwell = 2.0
feedrate = 60.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

cnt = 0
for xPosLayout, yPosLayout in zip(params['xPosList'],params['yPosList']):

    cnt+=1
    if cnt == 1:
        continue

    if 1:
        # Annulus pocket
        xPos = params['annulusCut']['xPos'] + xPosLayout
        yPos = params['annulusCut']['yPos'] + yPosLayout
        outerRadius = params['annulusCut']['outerRadius']
        innerRadius = params['annulusCut']['innerRadius']
        thickness = outerRadius - innerRadius
        depth = params['annulusCut']['depth']
        annulusDict = { 
                'centerX'        : xPos, 
                'centerY'        : yPos,
                'radius'         : outerRadius,
                'thickness'      : thickness,
                'depth'          : depth,
                'startZ'         : startZ,
                'safeZ'          : safeZ,
                'overlap'        : overlap,
                'overlapFinish'  : overlapFinish,
                'maxCutDepth'    : maxCutDepth,
                'toolDiam'       : toolDiam,
                'direction'      : direction,
                'startDwell'     : startDwell,
                }
        annulus = cnc_pocket.CircAnnulusPocketXY(annulusDict)
        prog.add(annulus)

    if 1:
        # Rectangular pocket
        xPos = params['rectCut']['xPos'] + xPosLayout
        yPos = params['rectCut']['yPos'] + yPosLayout
        outerSize = params['rectCut']['outerSize']
        innerSize = params['rectCut']['innerSize']
        thickness = 0.5*(outerSize - innerSize)
        depth = params['rectCut']['depth']
        rectDict = {
                'centerX'       : xPos,
                'centerY'       : yPos,
                'width'         : outerSize,
                'height'        : outerSize,
                'thickness'     : thickness, 
                'depth'         : depth,
                'startZ'        : startZ, 
                'safeZ'         : safeZ,
                'overlap'       : overlap,
                'overlapFinish' : overlap, 
                'maxCutDepth'   : maxCutDepth,
                'toolDiam'      : toolDiam,
                'cornerCut'     : False,
                'direction'     : direction,
                'startDwell'    : startDwell,
                }
        rect = cnc_pocket.RectAnnulusPocketXY(rectDict)
        prog.add(rect)


prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
prog.write(fileName)
