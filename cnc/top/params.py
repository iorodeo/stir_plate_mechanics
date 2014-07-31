params = {}

params['width'] = 4.5
params['height'] = 4.5
params['radius'] = 0.25
params['thickness'] = 0.514

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




