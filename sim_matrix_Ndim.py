# -*- coding: utf-8 -*-
"""
Created on Fri Mar 05 13:41:53 2021

@author: mariem.ben_charrada
"""
from __future__ import division
from  sim_matrix_2dim import rgb
import vtk
import pandas as pd

def process_data(data_file):
    data = pd.read_csv(data_file, header=None)
    scores_list = []
    for i in range(7, -1, -1):
        for j in range(0,8):
            scores_list.append(data.loc[i,j])
    return scores_list
    
def MakeLUT(tableSize, scores, color):
    lut = vtk.vtkLookupTable()
    lut.SetNumberOfTableValues(tableSize)
    lut.Build()
    for i in range (1, 65):
        sim = scores[i-1]*5
        lut.SetTableValue(i, rgb(sim, color)+[1])
    
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
        #s = '[' + ', '.join(['{:0.6f}'.format(x) for x in rgb]) + ']'
        


def main():
    """
    :return: The render window interactor.
    """
    # Multilingual sentences
    multilingual_example = ["Willkommen zu einfachen, aber", "verrassend krachtige", "multilingüe", "comprehension du langage naturel", "malleja.", "Was die Leute meinen" , "Hva folk mener", "a lingua que falam."]
    multilingual_example_in_en =  ["Welcome to simple yet", "surprisingly powerful", "multilingual", "natural language understanding", "models.", "What people mean", "matters more than", "the language they speak."]

    scores = process_data('scores.csv')

    nc = vtk.vtkNamedColors()

    # Provide some geometry
    resolution = 8

    plane11 = vtk.vtkPlaneSource()
    plane11.SetXResolution(resolution)
    plane11.SetYResolution(resolution)

    tableSize = resolution * resolution + 1

    #  Force an update so we can set cell data
    plane11.Update()

    #  Get the lookup tables mapping cell data to colors
    lut1 = MakeLUT(tableSize, scores, color='Blue')

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

    for i in range(len(multilingual_example)):
        sent1 = vtk.vtkVectorText()
        sent1.SetText(multilingual_example_in_en[i])
        sentMapper1 = vtk.vtkPolyDataMapper()
        sentMapper1.SetInputConnection(sent1.GetOutputPort())
        sentActor1 = vtk.vtkFollower()
        sentActor1.SetMapper(sentMapper1)
        sentActor1.SetScale(0.03, 0.03, 0.03)
        sentActor1.AddPosition(-0.45+0.13*i, 0.55, 0)
        sentActor1.RotateWXYZ(45, 0, 0, 1)
        sentActor1.GetProperty().SetColor(colors.GetColor3d('Black'))
        ren11.AddActor(sentActor1)
        
        sent2 = vtk.vtkVectorText()
        sent2.SetText(multilingual_example[i])
        sentMapper2 = vtk.vtkPolyDataMapper()
        sentMapper2.SetInputConnection(sent2.GetOutputPort())
        sentActor2 = vtk.vtkFollower()
        sentActor2.SetMapper(sentMapper2)
        sentActor2.SetScale(0.03, 0.03, 0.03)
        sentActor2.AddPosition(0.55, 0.45-0.13*i, 0)
        sentActor2.GetProperty().SetColor(colors.GetColor3d('Black'))
        ren11.AddActor(sentActor2)
        
        
        
    # Setup the render windows
    renWin = vtk.vtkRenderWindow()
    renWin.SetSize(800, 800)
    renWin.SetWindowName('AssignCellColorsFromLUT');

    renWin.AddRenderer(ren11)
    ren11.SetBackground(nc.GetColor3d('Grey'))
    ren11.AddActor(actor11)

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

