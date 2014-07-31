from __future__ import print_function
import math
import scipy

magnetHoleSep = 0.75
fixtureHoleSep = 0.75
partDiameter = 1.4
partDepth = 0.45


# Basic layout parameters
params = {}
params['numParts'] = 5 
params['partSpacing'] = 2.0 
layoutLen = (params['numParts']-1)*params['partSpacing']
xPosArray = scipy.linspace(-0.5*layoutLen, 0.5*layoutLen,params['numParts'])
yPosArray = scipy.zeros(xPosArray.size)
params['xPosList'] = list(xPosArray)
params['yPosList'] = list(yPosArray)
params['partDiamter'] = partDiameter
params['partDepth'] = partDepth

# Define drill holes  
# Note hole positions are give relative to part layout position
params['drillHoleList'] = []

shaftHoles = {}
shaftHoles['name'] = 'motorShaftHoles'
shaftHoles['size'] = '2mm,thru'
shaftHoles['xPosList'] = [0.0,] 
shaftHoles['yPosList'] = [0.0,] 
params['shaftHOles'] = shaftHoles
params['drillHoleList'].append(shaftHoles)

magnetHoles = {}
magnetHoles['name'] = 'magnetHoles'
magnetHoles['size'] = '6-32,tap'
magnetHoles['xPosList'] = [-0.5*magnetHoleSep, 0.5*magnetHoleSep]
magnetHoles['yPosList'] = [0.0, 0.0]
params['magnetHoles'] = magnetHoles
params['drillHoleList'].append(magnetHoles)

fixtureHoles = {}
fixtureHoles['name'] = 'fixtureHoles'
fixtureHoles['size'] = '10-32,thru'
fixtureHoles['xPosList'] = [0.0, 0.0]
fixtureHoles['yPosList'] = [-0.5*fixtureHoleSep, 0.5*fixtureHoleSep]
params['fixtureHoles'] = fixtureHoles
params['drillHoleList'].append(fixtureHoles)

# Pocketing
rectThickness = 0.3
rectInnerSize = partDiameter + 0.25
rectOuterSize = rectInnerSize + 2*rectThickness 
outerRadius = rectInnerSize/math.sqrt(2) + 0.25*rectThickness

# Annulus Pocket cut
annulusCut = {}
annulusCut['xPos'] = 0.0
annulusCut['yPos'] = 0.0
annulusCut['outerRadius'] = outerRadius 
annulusCut['innerRadius'] = 0.25
annulusCut['depth'] = 0.1
params['annulusCut'] = annulusCut

# Rectangular pocket cut
rectCut = {}
rectCut['xPos'] = 0.0
rectCut['yPos'] = 0.0
rectCut['innerSize'] = rectInnerSize
rectCut['outerSize'] = rectOuterSize
rectCut['depth'] = 0.2
params['rectCut'] = rectCut



# -----------------------------------------------------------------------------
if __name__ == '__main__':
    for k,v in params.iteritems():
        print(k,v)







