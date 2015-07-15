import os
from py2gcode import gcode_cmd
from py2gcode import cnc_drill
from param import param

def createNGCFile(display=False):
    """
    Generate center drill .ngc cutting file.
    """
    motorParam = param['motorDrill']
    standoffParam = param['standoffDrill']
    
    prog = gcode_cmd.GCodeProg()
    prog.add(gcode_cmd.GenericStart())
    prog.add(gcode_cmd.Space())
    
    for x0, y0 in param['partPos']:
        # Motor mount holes
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Motor mount holes, partPos = ({0},{1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.FeedRate(motorParam['feedRate']))
        for i in (-1,1):
                x = x0 + i*0.5*motorParam['holeSpacing']
                drillDict = {
                        'centerX'    : x,
                        'centerY'    : y0,
                        'startZ'     : motorParam['startZ'],
                        'stopZ'      : motorParam['stopZCent'],
                        'safeZ'      : motorParam['safeZ'],
                        'startDwell' : motorParam['startDwell'],
                        }
                drill = cnc_drill.SimpleDrill(drillDict)
                prog.add(drill)
                prog.add(gcode_cmd.Space())
        
        # Standoff holes
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Standoff holes, partPos = ({0},{1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.FeedRate(standoffParam['feedRate']))
        for i in (-1,1):
            for j in (-1,1): 
                x = x0 + i*0.5*standoffParam['holeSpacing']
                y = y0 + j*0.5*standoffParam['holeSpacing']
                drillDict = {
                        'centerX'    : x,
                        'centerY'    : y,
                        'startZ'     : standoffParam['startZ'],
                        'stopZ'      : standoffParam['stopZCent'],
                        'safeZ'      : standoffParam['safeZ'],
                        'startDwell' : standoffParam['startDwell'],
                        }
                drill = cnc_drill.SimpleDrill(drillDict)
                prog.add(drill)
                prog.add(gcode_cmd.Space())
        
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

    createNGCFile(display=False)
