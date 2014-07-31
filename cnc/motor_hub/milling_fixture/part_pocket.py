from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from params import params

startZ = 0.0
safeZ = 0.15
feedrate = 20.0
overlap = 0.3
overlapFinish = 0.5
maxCutDepth = 0.03
toolDiam = 0.25
direction = 'ccw'
startDwell = 2.0

xPosArray = params['fixture']['xPosArray']
pocketParams = params['pocket']

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

for xPos in xPosArray:
    pocketDict = { 
            'centerX'        : xPos, 
            'centerY'        : 0.0,
            'radius'         : 0.5*pocketParams['diameter'],
            'depth'          : pocketParams['depth'],
            'startZ'         : startZ,
            'safeZ'          : safeZ,
            'overlap'        : overlap,
            'overlapFinish'  : overlapFinish,
            'maxCutDepth'    : maxCutDepth,
            'toolDiam'       : toolDiam,
            'direction'      : direction,
            'startDwell'     : startDwell,
            }
    pocket = cnc_pocket.CircPocket(pocketDict)
    prog.add(pocket)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
prog.write('part_pocket.ngc')
