from __future__ import print_function
from py2gcode import gcode_cmd 
from py2gcode import cnc_path

# Parameters
endMillDiam = 0.25
safeHeight = 0.25

length = 11.00
xList  = [-0.5*length, 0.5*length] 
sgnList = ['+', '-']

y0 = -0.1 
y1 = 1.7 

z0 = 0
z1 = -0.3

step = 0.03
retDist = 0.1

startDwell = 2.0
coordSystem = 1
feedrate = 20.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart(coord=coordSystem,feedrate=feedrate))

for x,sgn in zip(xList,sgnList):

    if sgn == '+':
        xCut = x - 0.5*endMillDiam 
        xRet = x - 0.5*endMillDiam - retDist 
        y0Mod, y1Mod = y1, y0
    else:
        xCut = x + 0.5*endMillDiam
        xRet = x + 0.5*endMillDiam + retDist
        y0Mod, y1Mod = y0, y1

    print(xCut)

    prog.add(gcode_cmd.Space())
    prog.add(gcode_cmd.Comment('Move to safe height'))
    prog.add(gcode_cmd.RapidMotion(z=safeHeight))
    
    prog.add(gcode_cmd.Space())
    prog.add(gcode_cmd.Comment('Move to x,y start and dwell for {0} secs'.format(startDwell)))
    prog.add(gcode_cmd.RapidMotion(x=xRet,y=y0Mod))
    prog.add(gcode_cmd.Dwell(startDwell))
    
    prog.add(gcode_cmd.Space())
    prog.add(gcode_cmd.Comment('Surface raster'))
    prog.add(gcode_cmd.LinearFeed(z=z0))
    prog.add(cnc_path.UniDirRasterRectPath((y0Mod,z0),(y1Mod,z1),step,xCut,xRet,plane='yz',direction='y'))

    prog.add(gcode_cmd.Space())
    prog.add(gcode_cmd.Comment('Move to x-return'))
    prog.add(gcode_cmd.RapidMotion(x=xRet))

    
    
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.Comment('Return to safe height'))
prog.add(gcode_cmd.LinearFeed(x=xRet))
prog.add(gcode_cmd.RapidMotion(z=safeHeight))

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.Comment('End program'))
prog.add(gcode_cmd.End())

print(prog)

prog.write('surface_yz.ngc')
