import os
from py2gcode import gcode_cmd
from py2gcode import cnc_pocket
from param import param

def createNGCFile(display=False):
    standoffParam = param['standoffPocket']
    motorPocketParam = param['motorPocket']
    motorHoleParam = param['motorHole']
    boundaryParam = param['boundaryCut']
    
    prog = gcode_cmd.GCodeProg()
    prog.add(gcode_cmd.GenericStart())
    prog.add(gcode_cmd.Space())
    
    for x0, y0 in param['partPos']:
    
        # Standoff pockets
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Standoff pocket, partPos = ({0}, {1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.FeedRate(standoffParam['feedRate']))
        for i in (-1,1):
            for j in (-1,1): 
                x = x0 + i*0.5*standoffParam['holeSpacing']
                y = y0 + j*0.5*standoffParam['holeSpacing']
                pocketDict = { 
                        'centerX'        : x, 
                        'centerY'        : y,
                        'radius'         : 0.5*standoffParam['holeDiam'],
                        'depth'          : standoffParam['depth'],
                        'startZ'         : standoffParam['startZ'],
                        'safeZ'          : standoffParam['safeZ'],
                        'overlap'        : standoffParam['overlap'],
                        'overlapFinish'  : standoffParam['overlapFinish'],
                        'maxCutDepth'    : standoffParam['maxCutDepth'], 
                        'toolDiam'       : standoffParam['toolDiam'],
                        'direction'      : standoffParam['direction'], 
                        'startDwell'     : standoffParam['startDwell'],
                        }
        
                pocket = cnc_pocket.CircPocketXY(pocketDict)
                prog.add(pocket)
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
    
