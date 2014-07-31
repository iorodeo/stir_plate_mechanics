from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

safeZ = 0.15
stepZ = 0.1
startZ = 0.0
stopZ = -0.2 
feedrate = 4.0
startDwell = 2.0

holeParams = params['toolingPlateHoles']

# Split into 'upper' and 'lower' y holes in order to move clamps
yHalf = 'lower'

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


for xSign in (-1,1):
    ySign = 1 if yHalf == 'upper' else -1
    xPos = 0.5*xSign*holeParams['xSpacing']
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
prog.write('tooling_plate_center_drill.ngc')

