import scipy

# Basic layout parameters
partDiameter = 1.4
partDepth = 0.45

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

# Magnet pocket
magnetHoleSep = 0.75
magnetDiam = 0.5
magnetDiamMargin = 0.008
magnetThickness = 0.125

magnetCut = {}
magnetCut['diameter'] = magnetDiam + magnetDiamMargin
magnetCut['depth'] = magnetThickness
magnetCut['xPosList'] = [-0.5*magnetHoleSep, 0.5*magnetHoleSep]
magnetCut['yPosList'] = [ 0.0, 0.0]
params['magnetCut'] = magnetCut

# Boundary cut
annulusDepth = 0.1
boundaryCut = {}
boundaryCut['xPos'] = 0.0
boundaryCut['yPos'] = 0.0
boundaryCut['radius'] = 0.5*partDiameter 
boundaryCut['offest'] = 'outside'
boundaryCut['depth'] = partDepth - annulusDepth 
params['boundaryCut'] = boundaryCut
