# -*- coding: utf-8 -*-
"""
Created on Fri Mar 05 13:41:53 2021

@author: mariem.ben_charrada
"""
from __future__ import division
import vtk
import pandas as pd

def rgb(sim, color):
    if 4.5<=sim<=5:
        if color=='Red':
            r, g, b = 102, 0, 0
        elif color=='Orange':
            r, g, b = 102, 51, 0
        elif color=='Yellow':
            r, g, b =  102, 102, 0
        elif color=='Green':
            r, g, b =  51, 102, 0
        elif color=='Blue':
            r, g, b =  0, 51, 102
        elif color=='Purple':
            r, g, b =  51, 0, 102
        elif color=='Pink':
            r, g, b =  102, 0, 51
        elif color=='Grey':
            r, g, b =  32, 32, 32
    elif 4<=sim<4.5:
        if color=='Red':
            r, g, b = 153, 0, 0
        elif color=='Orange':
            r, g, b = 153, 76, 0
        elif color=='Yellow':
            r, g, b =  153, 153, 0
        elif color=='Green':
            r, g, b =  76, 153, 0
        elif color=='Blue':
            r, g, b =  0, 76, 153
        elif color=='Purple':
            r, g, b =  76, 0, 153
        elif color=='Pink':
            r, g, b =  153, 0, 76
        elif color=='Grey':
            r, g, b =  64, 64, 64
    elif 3.5<=sim<4:
        if color=='Red':
            r, g, b = 204, 0, 0
        elif color=='Orange':
            r, g, b = 204, 102, 0
        elif color=='Yellow':
            r, g, b =  204, 204, 0
        elif color=='Green':
            r, g, b =  102, 204, 0
        elif color=='Blue':
            r, g, b =  0 ,102, 204
        elif color=='Purple':
            r, g, b =  102, 0, 204
        elif color=='Pink':
            r, g, b =  204, 0, 102
        elif color=='Grey':
            r, g, b = 96, 96, 96 
    elif 3<=sim<3.5:
        if color=='Red':
            r, g, b = 255, 0, 0
        elif color=='Orange':
            r, g, b = 255, 128, 0
        elif color=='Yellow':
            r, g, b =  255, 255, 0
        elif color=='Green':
            r, g, b =  128, 255, 0
        elif color=='Blue':
            r, g, b =  0, 128, 255
        elif color=='Purple':
            r, g, b =  127, 0, 255
        elif color=='Pink':
            r, g, b =  255, 0, 127
        elif color=='Grey':
            r, g, b =  128, 128, 128
    elif 2.5<=sim<3:
        if color=='Red':
            r, g, b = 255, 51, 51
        elif color=='Orange':
            r, g, b = 255, 153, 51
        elif color=='Yellow':
            r, g, b =  255, 255, 51
        elif color=='Green':
            r, g, b =  153, 255, 51
        elif color=='Blue':
            r, g, b =  51, 153, 255
        elif color=='Purple':
            r, g, b =  153, 51, 255
        elif color=='Pink':
            r, g, b =  255, 51, 153
        elif color=='Grey':
            r, g, b =  160, 160, 160
    elif 2<=sim<2.5:
        if color=='Red':
            r, g, b = 255, 102, 102
        elif color=='Orange':
            r, g, b = 255, 102, 102
        elif color=='Yellow':
            r, g, b =  255, 255, 102
        elif color=='Green':
            r, g, b =  178, 255, 102
        elif color=='Blue':
            r, g, b =  102, 178, 255
        elif color=='Purple':
            r, g, b =  178, 102, 255
        elif color=='Pink':
            r, g, b =  255, 102, 178
        elif color=='Grey':
            r, g, b =  192, 192, 192
    elif 1<=sim<2:
        if color=='Red':
            r, g, b = 255, 153, 153
        elif color=='Orange':
            r, g, b = 255, 204, 153
        elif color=='Yellow':
            r, g, b =  255, 255, 153
        elif color=='Green':
            r, g, b =  204, 255, 153
        elif color=='Blue':
            r, g, b =  153, 204, 255
        elif color=='Purple':
            r, g, b =  204, 153, 255
        elif color=='Pink':
            r, g, b =  255, 153, 204
        elif color=='Grey':
            r, g, b =  224, 224, 224
    else:
        if color=='Red':
            r, g, b = 255, 204, 204
        elif color=='Orange':
            r, g, b = 255, 229, 204
        elif color=='Yellow':
            r, g, b =  255, 255, 204
        elif color=='Green':
            r, g, b =  229, 255, 204
        elif color=='Blue':
            r, g, b =  204, 229, 255
        elif color=='Purple':
            r, g, b =  229, 204, 255
        elif color=='Pink':
            r, g, b =  255, 204, 229
        elif color=='Grey':
            r, g, b =  255, 255, 255
    return [r/255, g/255, b/255]

def MakeLUT(tableSize, similarity, color):
    lut = vtk.vtkLookupTable()
    lut.SetNumberOfTableValues(tableSize)
    lut.Build()
    
    lut.SetTableValue(4, rgb(similarity, color)+[1])
    lut.SetTableValue(1, rgb(similarity, color)+[1])
    
    lut.SetTableValue(2, rgb(5, color)+[1])
    lut.SetTableValue(3, rgb(5, color)+[1])

    return lut


def MakeCellData(tableSize, lut, colors):
    """
    Create the cell data using the colors from the lookup table.
    :param: tableSize - The table size
    :param: lut - The lookup table.
    :param: colors - A reference to a vtkUnsignedCharArray().
    """
    for i in range(1, tableSize):
        rgb = [0.0, 0.0, 0.0]
        lut.GetColor(float(i) / (tableSize - 1), rgb)
        ucrgb = list(map(int, [x * 255 for x in rgb]))
        colors.InsertNextTuple3(ucrgb[0], ucrgb[1], ucrgb[2])
        s = '[' + ', '.join(['{:0.6f}'.format(x) for x in rgb]) + ']'
        #print(s, ucrgb)


def main():
    """
    :return: The render window interactor.
    """
    sts_data = pd.read_csv('sts.csv')
    idx = 12
    selected_pair = sts_data.loc[idx].tolist()
    print selected_pair

    nc = vtk.vtkNamedColors()

    # Provide some geometry
    resolution = 2

    plane11 = vtk.vtkPlaneSource()
    plane11.SetXResolution(resolution)
    plane11.SetYResolution(resolution)

    tableSize = resolution * resolution + 1

    #  Force an update so we can set cell data
    plane11.Update()

    #  Get the lookup tables mapping cell data to colors
    lut1 = MakeLUT(tableSize, selected_pair[0], color='Pink')

    colorData1 = vtk.vtkUnsignedCharArray()
    colorData1.SetName('colors')  # Any name will work here.
    colorData1.SetNumberOfComponents(3)
    MakeCellData(tableSize, lut1, colorData1)
    # Then use SetScalars() to add it to the vtkPolyData structure,
    # this will then be interpreted as a color table.
    plane11.GetOutput().GetCellData().SetScalars(colorData1)

    # Set up actor and mapper
    mapper11 = vtk.vtkPolyDataMapper()
    mapper11.SetInputConnection(plane11.GetOutputPort())
    # Now, instead of doing this:
    # mapper11.SetScalarRange(0, tableSize - 1)
    # mapper11.SetLookupTable(lut1)
    # We can just use the color data that we created from the lookup table and
    # assigned to the cells:
    mapper11.SetScalarModeToUseCellData()
    mapper11.Update()

    actor11 = vtk.vtkActor()
    actor11.SetMapper(mapper11)

    # Set up the renderers.
    ren11 = vtk.vtkRenderer()
    
    colors = vtk.vtkNamedColors()
    
    sim_val = (selected_pair[0]/5)*100
    
    # Create the 3D text 
    sim1 = vtk.vtkVectorText()
    sim1.SetText('100%')
    textMapper1 = vtk.vtkPolyDataMapper()
    textMapper1.SetInputConnection(sim1.GetOutputPort())
    textActor1 = vtk.vtkFollower()
    textActor1.SetMapper(textMapper1)
    textActor1.SetScale(0.1, 0.1, 0.1)
    textActor1.AddPosition(0.05, -0.3, 0)
    textActor1.GetProperty().SetColor(colors.GetColor3d('White'))
    
    sim2 = vtk.vtkVectorText()
    sim2.SetText('100%')
    textMapper2 = vtk.vtkPolyDataMapper()
    textMapper2.SetInputConnection(sim2.GetOutputPort())
    textActor2 = vtk.vtkFollower()
    textActor2.SetMapper(textMapper2)
    textActor2.SetScale(0.1, 0.1, 0.1)
    textActor2.AddPosition(-0.45, 0.22, 0)
    textActor2.GetProperty().SetColor(colors.GetColor3d('White'))
    
    sim3 = vtk.vtkVectorText()
    sim3.SetText(str(int(sim_val))+'%')
    textMapper3 = vtk.vtkPolyDataMapper()
    textMapper3.SetInputConnection(sim3.GetOutputPort())
    textActor3 = vtk.vtkFollower()
    textActor3.SetMapper(textMapper3)
    textActor3.SetScale(0.1, 0.1, 0.1)
    textActor3.AddPosition(0.06, 0.22, 0)
    textActor3.GetProperty().SetColor(colors.GetColor3d('White'))
    
    sim4 = vtk.vtkVectorText()
    sim4.SetText(str(int(sim_val))+'%')
    textMapper4 = vtk.vtkPolyDataMapper()
    textMapper4.SetInputConnection(sim4.GetOutputPort())
    textActor4 = vtk.vtkFollower()
    textActor4.SetMapper(textMapper4)
    textActor4.SetScale(0.1, 0.1, 0.1)
    textActor4.AddPosition(-0.45, -0.3, 0)
    textActor4.GetProperty().SetColor(colors.GetColor3d('White'))
    
    
    # Add sentences to the LUT
    sent1 = vtk.vtkVectorText()
    sent1.SetText(selected_pair[1])
    sentMapper1 = vtk.vtkPolyDataMapper()
    sentMapper1.SetInputConnection(sent1.GetOutputPort())
    sentActor1 = vtk.vtkFollower()
    sentActor1.SetMapper(sentMapper1)
    sentActor1.SetScale(0.05, 0.05, 0.05)
    sentActor1.AddPosition(-0.35, 0.55, 0)
    sentActor1.RotateWXYZ(45, 0, 0, 1)
    sentActor1.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    sent2 = vtk.vtkVectorText()
    sent2.SetText(selected_pair[2])
    sentMapper2 = vtk.vtkPolyDataMapper()
    sentMapper2.SetInputConnection(sent2.GetOutputPort())
    sentActor2 = vtk.vtkFollower()
    sentActor2.SetMapper(sentMapper2)
    sentActor2.SetScale(0.05, 0.05, 0.05)
    sentActor2.AddPosition(0.2, 0.55, 0)
    sentActor2.RotateWXYZ(45, 0, 0, 1)
    sentActor2.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    sent3 = vtk.vtkVectorText()
    sent3.SetText(selected_pair[1])
    sentMapper3 = vtk.vtkPolyDataMapper()
    sentMapper3.SetInputConnection(sent3.GetOutputPort())
    sentActor3 = vtk.vtkFollower()
    sentActor3.SetMapper(sentMapper3)
    sentActor3.SetScale(0.05, 0.05, 0.05)
    sentActor3.AddPosition(0.55, 0.25, 0)
    sentActor3.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    sent4 = vtk.vtkVectorText()
    sent4.SetText(selected_pair[2])
    sentMapper4 = vtk.vtkPolyDataMapper()
    sentMapper4.SetInputConnection(sent4.GetOutputPort())
    sentActor4 = vtk.vtkFollower()
    sentActor4.SetMapper(sentMapper4)
    sentActor4.SetScale(0.05, 0.05, 0.05)
    sentActor4.AddPosition(0.55, -0.25, 0)
    sentActor4.GetProperty().SetColor(colors.GetColor3d('Black'))

    # Setup the render windows
    renWin = vtk.vtkRenderWindow()
    renWin.SetSize(800, 800)
    renWin.SetWindowName('AssignCellColorsFromLUT');

    renWin.AddRenderer(ren11)
    ren11.SetBackground(nc.GetColor3d('Grey'))
    ren11.AddActor(actor11)
    
    ren11.AddActor(textActor1)
    ren11.AddActor(textActor2)
    ren11.AddActor(textActor3)
    ren11.AddActor(textActor4)
    
    ren11.AddActor(sentActor1)
    ren11.AddActor(sentActor2)
    ren11.AddActor(sentActor3)
    ren11.AddActor(sentActor4)
    
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)
    renWin.Render()

    return iren


if __name__ == '__main__':
    requiredMajorVersion = 6
    #print(vtk.vtkVersion().GetVTKMajorVersion())
    if vtk.vtkVersion().GetVTKMajorVersion() < requiredMajorVersion:
        print("You need VTK Version 6 or greater.")
        print("The class vtkNamedColors is in VTK version 6 or greater.")
        exit(0)
    iren = main()
    iren.Start()

