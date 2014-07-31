import math
import scipy

params = {}

# Plate parameters
params['plate'] = { 
        'width'       : 10.0,
        'height'      : 1.8,
        'thickness'   : 0.379,
        'radius'      : 5/64.0,
        'numParts'    : 5, 
        'partSpacing' : 2.0,
        }
totalLength = (params['plate']['numParts']-1)*params['plate']['partSpacing']
xPosArray = scipy.linspace(0,totalLength,params['plate']['numParts']) 
xPosArray = xPosArray - 0.5*totalLength
params['plate']['xPosArray'] = xPosArray


partMountDistToYEdge = 0.4
partMountYPos = 0.5*params['plate']['height'] - partMountDistToYEdge

blockMountDistToEdge = 0.25
blockMountYPos = -(0.5*params['plate']['height'] - blockMountDistToEdge)

        
# Part mount holes
params['partMountHoles'] = {
        'holeSpacing'   : 0.75*math.cos(math.pi/4),
        'yMidPos'      : partMountYPos,
        }

# Block mount holes
params['blockMountHoles'] = {
        'holeSpacing'  : 2.0,
        'blockSpacing' : 5*1.16,
        'yPos'         : blockMountYPos,
        }

# Pocket params
params['partPocket'] = { 
        'diameter' : 0.505,
        'depth'    : 0.15,
        'yPos'     : partMountYPos, 
        }


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print(params)

