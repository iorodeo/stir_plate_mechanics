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
    
        # Motor pocket
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Motor pocket, partPos = ({0}, {1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.FeedRate(motorPocketParam['feedRate']))
        pocketDict = dict(motorPocketParam)
        pocketDict['centerX'] = x0
        pocketDict['centerY'] = y0
        pocket = cnc_pocket.CircPocketXY(pocketDict)
        prog.add(pocket)
    
        # Motor hole
        prog.add(gcode_cmd.FeedRate(motorHoleParam['feedRate']))
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Motor hole, partPos = ({0}, {1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        holeDict = dict(motorHoleParam)
        holeDict['centerX'] = x0
        holeDict['centerY'] = y0
        pocket = cnc_pocket.CircPocketXY(holeDict)
        prog.add(pocket)

        # Boundary cut
        prog.add(gcode_cmd.FeedRate(boundaryParam['feedRate']))
        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Boundary cut norm, partPos = ({0}, {1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        boundaryDict = dict(boundaryParam)
        boundaryDict['centerX'] = x0
        boundaryDict['centerY'] = y0
        boundaryDict['depth'] = boundaryParam['normDepth']
        boundaryDict['maxCutDepth'] = boundaryParam['normMaxCutDepth']
        boundaryDict['startZ'] = boundaryParam['normStartZ']
        pocket = cnc_pocket.RectAnnulusPocketXY(boundaryDict)
        prog.add(pocket)

        prog.add(gcode_cmd.Comment('-'*60))
        prog.add(gcode_cmd.Comment('Boundary cut sep, partPos = ({0}, {1})'.format(x0,y0)))
        prog.add(gcode_cmd.Comment('-'*60))
        boundaryDict = dict(boundaryParam)
        boundaryDict['centerX'] = x0
        boundaryDict['centerY'] = y0
        boundaryDict['depth'] = boundaryParam['sepDepth'] - boundaryParam['normDepth']
        boundaryDict['maxCutDepth'] = boundaryParam['sepMaxCutDepth']
        boundaryDict['startZ'] = -boundaryParam['normDepth']
        pocket = cnc_pocket.RectAnnulusPocketXY(boundaryDict)
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

    createNGCFile(display=False)
    
