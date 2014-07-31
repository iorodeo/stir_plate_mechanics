import os
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from param import param

def createNGCFile(display=False):
    surfaceParam = param['surface']
    
    prog = gcode_cmd.GCodeProg()
    prog.add(gcode_cmd.GenericStart())
    prog.add(gcode_cmd.Space())
    
    # Standoff holes
    prog.add(gcode_cmd.Comment('-'*60))
    prog.add(gcode_cmd.Comment("Surface"))
    prog.add(gcode_cmd.Comment('-'*60))
    prog.add(gcode_cmd.FeedRate(surfaceParam['feedRate']))
    pocket = cnc_pocket.RectPocketXY(surfaceParam)
    prog.add(pocket)
    
    prog.add(gcode_cmd.End(),comment=True)
    baseName, ext = os.path.splitext(__file__)
    fileName = '{0}.ngc'.format(baseName)
    if display:
        print(prog)
    else:
        print('creating: {0}'.format(fileName))
    prog.write(fileName)

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    createNGCFile(display=True)
