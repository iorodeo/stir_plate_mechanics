import scipy

# Basic layout parameters
params = {}
params['numParts'] = 5
params['partSpacing'] = 2.0 
layoutLen = (params['numParts']-1)*params['partSpacing']
xPosArray = scipy.linspace(-0.5*layoutLen, 0.5*layoutLen,params['numParts'])
yPosArray = scipy.zeros(xPosArray.size)
params['xPosList'] = list(xPosArray)
params['yPosList'] = list(yPosArray)

params['xPosRelDrill'] = 0.0
params['yPosRelDrill'] = -0.1


