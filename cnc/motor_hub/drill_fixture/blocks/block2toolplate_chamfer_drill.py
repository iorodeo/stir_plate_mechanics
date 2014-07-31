from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from params import params

# 10-32 through holes

safeZ = 0.25
stepZ = 0.02
startZ = 0.0
stopZ = -0.025
feedrate = 1.0
startDwell = 2.0
holeSpacing = params['block2toolplate_hole_spacing']
 
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
prog.write('block2toolplate_chamfer_drill.ngc')
