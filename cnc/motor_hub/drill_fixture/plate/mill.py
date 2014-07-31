import os
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from py2gcode import cnc_boundary
from params import params

startZ = 0.0
safeZ = 0.15
feedrate = 24.0
overlap = 0.3
overlapFinish = 0.5
normalMaxCutDepth = 0.03   # maximum cut depth
removeMaxCutDepth = 0.015  # part removal (light) cut depth
removeUnderCut = 0.03      # sets where light passes start
removeOverCut = 0.05       # extra cut depth to ensure part removal

toolDiam = 0.25
direction = 'ccw'
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

# Cut part pockets
if 1:
    for xPos in params['plate']['xPosArray']:
    
        pocketDict = { 
                'centerX'        : xPos, 
                'centerY'        : params['partPocket']['yPos'],
                'radius'         : 0.5*params['partPocket']['diameter'],
                'depth'          : params['partPocket']['depth'],
                'startZ'         : startZ,
                'safeZ'          : safeZ,
                'overlap'        : overlap,
                'overlapFinish'  : overlapFinish,
                'maxCutDepth'    : normalMaxCutDepth,
                'toolDiam'       : toolDiam,
                'direction'      : direction,
                'startDwell'     : startDwell,
                }
        pocket = cnc_pocket.CircPocket(pocketDict)
        prog.add(pocket)

# Cut boundary  
depthNormalCut = params['plate']['thickness'] - removeUnderCut
depthRemoveCut = removeUnderCut + removeOverCut

if 1:
    # Normal boundary cut - maximum cut depth per pass
    normalBoundaryDict = { 
            'centerX'      : 0.0,
            'centerY'      : 0.0,
            'width'        : params['plate']['width'],
            'height'       : params['plate']['height'],
            'depth'        : depthNormalCut,
            'radius'       : params['plate']['radius'],
            'startZ'       : startZ,
            'safeZ'        : safeZ,
            'toolDiam'     : toolDiam,
            'toolOffset'   : 'outside',
            'direction'    : direction,
            'maxCutDepth'  : normalMaxCutDepth,
            }
    normalBoundary = cnc_boundary.RectBoundaryXY(normalBoundaryDict)
    prog.add(normalBoundary)

if 1:
    # Part removal boundary cut - light cut depth
    removeBoundaryDict = {
            'centerX'      : 0.0,
            'centerY'      : 0.0,
            'width'        : params['plate']['width'],
            'height'       : params['plate']['height'],
            'depth'        : depthRemoveCut,
            'radius'       : params['plate']['radius'],
            'startZ'       : startZ-depthNormalCut,
            'safeZ'        : safeZ,
            'toolDiam'     : toolDiam,
            'toolOffset'   : 'outside',
            'direction'    : direction,
            'maxCutDepth'  : removeMaxCutDepth,
            }
    removeBoundary = cnc_boundary.RectBoundaryXY(removeBoundaryDict)
    prog.add(removeBoundary)



prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
