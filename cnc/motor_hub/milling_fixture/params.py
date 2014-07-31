import scipy

params = {}

# Fixture params
params['fixture'] = { 
        'numParts'    : 5, 
        'partSpacing' : 2.0,
        'length'      : 11.0, 
        'width'       : 3.0, 
        'thickness'   : 0.25
        }
totalLength = (params['fixture']['numParts']-1)*params['fixture']['partSpacing']
xPosArray = scipy.linspace(0,totalLength,params['fixture']['numParts']) 
xPosArray = xPosArray - 0.5*totalLength
params['fixture']['xPosArray'] = xPosArray

# Pocket params
params['pocket'] = { 
        'diameter' : 0.505,
        'depth'    : 0.15
        }

# Tooling plate holes
params['toolingPlateHoles'] = {
        'partHole' : False,
        'diameter' : 0.187, # (3/16) 10-32 through hole
        'xSpacing' : 10.44,
        'ySpacing' : 2.32,
        }

# Part mounting holes
params['partMountHoles'] = {
        'partHole' : True,
        'diameter' : 0.156, # 10-32 tap-hole
        'ySpacing' : 0.75,
        }



