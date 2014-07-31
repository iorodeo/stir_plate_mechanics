from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

# 10-32 through tap holes

safeZ = 0.15
stepZ = 0.04
startZ = 0.0
stopZ = -0.24
feedrate = 2.0
startDwell = 2.0
holeSpacing = params['block2fixture_hole_spacing']
 
prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

for i in (-1,1):
    xPos = i*0.5*holeSpacing
    yPos = 0.0
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
prog.write('block2fixture_center_drill.ngc')
