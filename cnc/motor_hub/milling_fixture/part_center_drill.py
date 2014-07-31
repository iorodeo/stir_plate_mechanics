from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

safeZ = 0.15
stepZ = 0.1
startZ = 0.0
stopZ = -0.2 
feedrate = 2.0
startDwell = 2.0

xPosArray = params['fixture']['xPosArray']
holeParams = params['partMountHoles']

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


for xPos in xPosArray:
    for ySign in (-1,1):
        yPos = 0.5*ySign*holeParams['ySpacing']
        drillDict =  { 
                'centerX'    : xPos,
                'centerY'    : yPos,
                'startZ'     : startZ,
                'stopZ'      : stopZ,
                'safeZ'      : safeZ,
                'stepZ'      : stepZ,
                'startDwell' : startDwell,
                }
        drill = cnc_drill.PeckDrill(drillDict)
        prog.add(drill)
        prog.add(gcode_cmd.Space())


prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
prog.write('part_center_drill.ngc')
