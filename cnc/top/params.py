params = {}

# Cutting array parametes

params['numX'] = 4 
params['numY'] = 1
params['offsetX'] = 2.5
params['offsetY'] = 0.0

params['width'] = 4.5
params['height'] = 4.5
params['radius'] = 0.25
params['thickness'] = 0.514
params['toolDiam'] = 0.25
params['partSepX'] = params['width'] + 4.0*params['toolDiam'] 
params['partSepY'] = params['height'] +4.0*params['toolDiam']
params['partPosList'] = [] 
for i in range(params['numX']):
    for j in range(params['numY']):
        x = i*params['partSepX'] + params['offsetX']
        y = j*params['partSepY'] + params['offsetY']
        params['partPosList'].append((x,y)) 

print(0.5*params['partSepX'])

# Central pocket
mainPocket = {}
mainPocket['width'] = 4.25
mainPocket['height'] = 4.25
mainPocket['radius'] = 0.25
mainPocket['depth'] = 0.125
params['mainPocket'] = mainPocket

# Mount holes (4-40 tap)
mountHole = {} 
mountHole['spacing'] = 3.8937
mountHole['depth'] = params['thickness'] - 0.08
params['mountHole'] = mountHole

# Standoff screw head pockets
standoffPocket = {}
standoffPocket['spacing'] = 3.15
standoffPocket['depth'] = 0.15
standoffPocket['radius'] = 0.15
params['standoffPocket'] = standoffPocket

# Hub pocket 
hubPocket = {}
hubPocket['width'] = 2.0
hubPocket['height'] = 2.0
hubPocket['depth'] = 0.3
hubPocket['radius'] = 0.25
params['hubPocket'] = hubPocket




