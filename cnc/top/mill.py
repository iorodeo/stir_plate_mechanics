from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from py2gcode import cnc_boundary
from params import params

# Cutting parameters
safeZ = 0.5
startZ = 0.0
overlap = 0.3
overlapFinish = 0.6
maxCutDepth = 0.05
maxCutDepthRemoval = 0.02
toolDiam = 0.25
direction = 'ccw'
startDwell = 2.0
feedrate = 22.0
cutThruMargin = 0.04

includeMainPocket = True
includeStandoffPocket = True
includeHubPocket = True
includeBoundary = True
includeBoundaryRemoval = True

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

if includeMainPocket:
    # Cut main pocket
    mainPocketDict = {
            'centerX'       : 0.0,
            'centerY'       : 0.0,
            'width'         : params['mainPocket']['width'],
            'height'        : params['mainPocket']['height'], 
            'depth'         : params['mainPocket']['depth'],
            'startZ'        : startZ,
            'safeZ'         : safeZ,
            'overlap'       : overlap,
            'overlapFinish' : overlapFinish,
            'maxCutDepth'   : maxCutDepth,
            'toolDiam'      : toolDiam,
            'cornerCut'     : False,
            'direction'     : direction,
            'startDwell'    : startDwell,
            }
    
    mainPocket = cnc_pocket.RectPocketXY(mainPocketDict)
    prog.add(mainPocket)

if includeStandoffPocket:
    # Cut standoff screw head pockets
    for i in (-1,1):
        for j in (-1,1):
            xPos = 0.5*i*params['standoffPocket']['spacing']
            yPos = 0.5*j*params['standoffPocket']['spacing']
            standoffPocketStartZ = startZ - params['mainPocket']['depth']
            standoffPocketDict = { 
                    'centerX'        : xPos, 
                    'centerY'        : yPos,
                    'radius'         : params['standoffPocket']['radius'],
                    'depth'          : params['standoffPocket']['depth'],
                    'startZ'         : standoffPocketStartZ,
                    'safeZ'          : safeZ,
                    'overlap'        : overlap,
                    'overlapFinish'  : overlapFinish,
                    'maxCutDepth'    : maxCutDepth,
                    'toolDiam'       : toolDiam,
                    'direction'      : direction,
                    'startDwell'     : startDwell,
                    }
            standoffPocket = cnc_pocket.CircPocketXY(standoffPocketDict)
            prog.add(standoffPocket)

if includeHubPocket:
    # Hub pocket 
    hubPocketStartZ = startZ - params['mainPocket']['depth']
    hubPocketDict = {
            'centerX'       : 0.0,
            'centerY'       : 0.0,
            'width'         : params['hubPocket']['width'],
            'height'        : params['hubPocket']['height'], 
            'depth'         : params['hubPocket']['depth'],
            'startZ'        : hubPocketStartZ,
            'safeZ'         : safeZ,
            'overlap'       : overlap,
            'overlapFinish' : overlapFinish,
            'maxCutDepth'   : maxCutDepth,
            'toolDiam'      : toolDiam,
            'cornerCut'     : False,
            'direction'     : direction,
            'startDwell'    : startDwell,
            }
    
    hubPocket = cnc_pocket.RectPocketXY(hubPocketDict)
    prog.add(hubPocket)


if includeBoundary:
    # Boundary cut - normal deep cuts 
    boundaryDict = { 
            'centerX'      : 0.0,
            'centerY'      : 0.0,
            'width'        : params['width'],
            'height'       : params['height'],
            'depth'        : params['thickness'] - cutThruMargin,
            'radius'       : params['radius'],
            'startZ'       : startZ,
            'safeZ'        : safeZ,
            'toolDiam'     : toolDiam,
            'toolOffset'   : 'outside',
            'direction'    : direction,
            'maxCutDepth'  : maxCutDepth,
            'startDwell'   : startDwell,
            }
    boundary = cnc_boundary.RectBoundaryXY(boundaryDict)
    prog.add(boundary)
    

if includeBoundaryRemoval:

    prog.add(gcode_cmd.Space())
    prog.add(gcode_cmd.Comment('Pause before removal boundary cut'))
    prog.add(gcode_cmd.Pause())
    prog.add(gcode_cmd.Space())

    # Boundary cut - shallow removal cuts
    boundaryRemovalDict = { 
            'centerX'      : 0.0,
            'centerY'      : 0.0,
            'width'        : params['width'],
            'height'       : params['height'],
            'depth'        : 2*cutThruMargin,
            'radius'       : params['radius'],
            'startZ'       : startZ - (params['thickness'] - cutThruMargin),
            'safeZ'        : safeZ,
            'toolDiam'     : toolDiam,
            'toolOffset'   : 'outside',
            'direction'    : direction,
            'maxCutDepth'  : maxCutDepth,
            'startDwell'   : startDwell,
            }
    boundaryRemoval = cnc_boundary.RectBoundaryXY(boundaryRemovalDict)
    prog.add(boundaryRemoval)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
prog.write(fileName)
