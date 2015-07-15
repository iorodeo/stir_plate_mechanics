"""
Parameters for cutting the strir bar motor mount plate.

"""
from __future__ import print_function
numPart = 8
#partPosStartX = -4.0
partPosStartX = 2.5 
partPosStartY = 1.18
partPosStep = 2.5
partPos = [(partPosStartX + partPosStep*i, partPosStartY) for i in range(numPart)]

motorHoleSpacing = 0.866
standoffHoleSpacing = 1.8
rawThickness = 0.27
partThickness = 0.25

surfaceToolDiam = 0.5
surfaceDepth = rawThickness - partThickness 
surfaceXYMargin = 0.4

boundaryPad = 0.1

startDwell = 2.0

drillFeedRate = 22.0 
centDrillDepth = -0.12
#thruDrillDepth = -(partThickness + 0.1) 
thruDrillDepth = -(rawThickness + 0.1) 
drillSafeZ = 0.15
drillStartZ = 0.0
drillStepZ = 0.05

endMillDiam = 0.125
millFeedRate = 60.0
millDirection = 'ccw'
millSafeZ = 0.25
millOverlap = 0.5
millFinishOverlap = 0.6
millNormMaxCutDepth = 0.08
millSepMaxCutDepth = 0.02
millSepMargin = 0.03
millThruMargin = 0.03

param = {}
param['partPos'] = partPos 
param['numPart'] = numPart 

param['motorDrill'] = { 
        'feedRate'     : drillFeedRate,
        'holeSpacing'  : motorHoleSpacing,
        'startZ'       : drillStartZ,
        'stopZCent'    : centDrillDepth,
        'stopZThru'    : thruDrillDepth,
        'safeZ'        : drillSafeZ,
        'stepZ'        : drillStepZ,
        'startDwell'   : startDwell,
        }

param['standoffDrill'] = { 
        'feedRate'     : drillFeedRate,
        'holeSpacing'  : standoffHoleSpacing,
        'startZ'       : drillStartZ,
        'stopZCent'    : centDrillDepth,
        'stopZThru'    : thruDrillDepth,
        'safeZ'        : drillSafeZ,
        'stepZ'        : drillStepZ,
        'startDwell'   : startDwell,
        }

param['standoffPocket'] = {
        'toolDiam'       : endMillDiam,
        'feedRate'       : millFeedRate,
        'holeSpacing'    : standoffHoleSpacing,
        'holeDiam'       : 0.26,
        'depth'          : 0.075,
        'startZ'         : 0.0,
        'safeZ'          : millSafeZ,
        'overlap'        : millOverlap,
        'overlapFinish'  : millFinishOverlap,
        'maxCutDepth'    : millNormMaxCutDepth,
        'direction'      : millDirection,
        'startDwell'     : startDwell,
        }

param['motorPocket'] = { 
        'toolDiam'       : endMillDiam,
        'feedRate'       : millFeedRate,
        'radius'         : 0.5*1.26,
        'depth'          : partThickness - 0.1,
        'startZ'         : 0.0,
        'safeZ'          : millSafeZ,
        'overlap'        : millOverlap,
        'overlapFinish'  : millFinishOverlap,
        'maxCutDepth'    : millNormMaxCutDepth,
        'direction'      : millDirection,
        'startDwell'     : startDwell,
        }

param['motorHole'] = {
        'toolDiam'       : endMillDiam,
        'feedRate'       : millFeedRate,
        'radius'         : 0.5*0.255,
        'depth'          : partThickness - param['motorPocket']['depth'] + millThruMargin,
        'startZ'         : -param['motorPocket']['depth'],
        'safeZ'          : millSafeZ,
        'overlap'        : millOverlap,
        'overlapFinish'  : millFinishOverlap,
        'maxCutDepth'    : millNormMaxCutDepth,
        'direction'      : millDirection,
        'startDwell'     : startDwell,
        }

boundaryDim = standoffHoleSpacing 
boundaryDim += param['standoffPocket']['holeDiam']  
boundaryDim += 1.0*endMillDiam
boundaryDim += 2.0*boundaryPad

param['boundaryCut'] = {
        'toolDiam'           : endMillDiam,
        'feedRate'           : millFeedRate,
        'width'              : boundaryDim,
        'height'             : boundaryDim,
        'thickness'          : endMillDiam,
        'normDepth'          : partThickness - millSepMargin,
        'sepDepth'           : partThickness + millThruMargin,
        'normStartZ'         : 0.0,
        'safeZ'              : millSafeZ,
        'overlap'            : millOverlap,
        'overlapFinish'      : millFinishOverlap,
        'normMaxCutDepth'    : millNormMaxCutDepth,
        'sepMaxCutDepth'     : millSepMaxCutDepth,
        'cornerCut'          : False,
        'direction'          : millDirection,
        'startDwell'         : startDwell,
        }

surfaceX0 = min([x for x,y in partPos]) 
surfaceX0 -= 0.5*param['boundaryCut']['width']
surfaceX0 -= surfaceXYMargin

surfaceX1 = max([x for x,y in partPos]) 
surfaceX1 += 0.5*param['boundaryCut']['width']
surfaceX1 += surfaceXYMargin

param['surface'] = {
        'centerX'        : 0.5*(surfaceX0 + surfaceX1),
        'centerY'        : partPosStartY,
        'feedRate'       : millFeedRate,
        'width'          : surfaceX1 - surfaceX0,
        'height'         : param['boundaryCut']['height'] + 2*surfaceXYMargin,
        'depth'          : surfaceDepth,
        'startZ'         : 0.0,
        'safeZ'          : millSafeZ,
        'overlap'        : millOverlap,
        'overlapFinish'  : millFinishOverlap,
        'maxCutDepth'    : millNormMaxCutDepth,
        'cornerCut'      : False,
        'direction'      : millDirection,
        'toolDiam'       : surfaceToolDiam,
        'startDwell'     : startDwell,
        }

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    for k,v in param['boundaryCut'].iteritems():
        print(k,v)
