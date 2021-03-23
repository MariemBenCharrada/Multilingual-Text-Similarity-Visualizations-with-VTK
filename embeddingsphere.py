# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:26:52 2021

@author: mariem.ben_charrada
"""

import vtk

def create_actors(sphere_colors, points, words):
    colors = vtk.vtkNamedColors()

    # Create sphere
    # sphere 11
    sphere11 = vtk.vtkSphereSource()
    sphere11.SetCenter(0.25, 0.4, 0.2)
    sphere11.SetRadius(0.02)
    sphere11.SetPhiResolution(11)
    sphere11.SetThetaResolution(21)
    
    # mapper
    sphere11Mapper = vtk.vtkPolyDataMapper()
    sphere11Mapper.SetInputConnection(sphere11.GetOutputPort())
    
    # actor
    sphere11Actor = vtk.vtkActor()
    sphere11Actor.SetMapper(sphere11Mapper)
    sphere11Actor.GetProperty().SetColor(colors.GetColor3d(sphere_colors[0]))
    
    # sphere 12
    sphere12 = vtk.vtkSphereSource()
    sphere12.SetCenter(0.15, 0.25, 0.5)
    sphere12.SetRadius(0.02)
    sphere12.SetPhiResolution(11)
    sphere12.SetThetaResolution(21)
    
    # mapper
    sphere12Mapper = vtk.vtkPolyDataMapper()
    sphere12Mapper.SetInputConnection(sphere12.GetOutputPort())
    
    # actor
    sphere12Actor = vtk.vtkActor()
    sphere12Actor.SetMapper(sphere12Mapper)
    sphere12Actor.GetProperty().SetColor(colors.GetColor3d(sphere_colors[1]))
    
    # sphere 21
    sphere21 = vtk.vtkSphereSource()
    sphere21.SetCenter(0.6, 0.3, 0.2)
    sphere21.SetRadius(0.02)
    sphere21.SetPhiResolution(11)
    sphere21.SetThetaResolution(21)
    
    # mapper
    sphere21Mapper = vtk.vtkPolyDataMapper()
    sphere21Mapper.SetInputConnection(sphere21.GetOutputPort())
    
    # actor
    sphere21Actor = vtk.vtkActor()
    sphere21Actor.SetMapper(sphere21Mapper)
    sphere21Actor.GetProperty().SetColor(colors.GetColor3d(sphere_colors[2]))
     
    # sphere 22
    sphere22 = vtk.vtkSphereSource()
    sphere22.SetCenter(0.5, 0.2, 0.7)
    sphere22.SetRadius(0.02)
    sphere22.SetPhiResolution(11)
    sphere22.SetThetaResolution(21)
    
    # mapper
    sphere22Mapper = vtk.vtkPolyDataMapper()
    sphere22Mapper.SetInputConnection(sphere22.GetOutputPort())
    
    # actor
    sphere22Actor = vtk.vtkActor()
    sphere22Actor.SetMapper(sphere22Mapper)
    sphere22Actor.GetProperty().SetColor(colors.GetColor3d(sphere_colors[3]))

    # Add lines
    
    p11 = points[0]
    p12 = points[1]
    p21 = points[2]
    p22 = points[3]
    
    # Create a vtkPoints object and store the points in it
    pts = vtk.vtkPoints()
    pts.InsertNextPoint(p11)
    pts.InsertNextPoint(p12)
    pts.InsertNextPoint(p21)
    pts.InsertNextPoint(p22)
    
    # Create the first line (between Origin and P0)
    line0 = vtk.vtkLine()
    line0.GetPointIds().SetId(0,0) 
    line0.GetPointIds().SetId(1,2) 
    
    # Create the second line (between Origin and P1)
    line1 = vtk.vtkLine()
    line1.GetPointIds().SetId(0,1) # the second 0 is the index of the Origin in the vtkPoints
    line1.GetPointIds().SetId(1,3) # 2 is the index of P1 in the vtkPoints
    
    # Create a cell array to store the lines in and add the lines to it
    lines = vtk.vtkCellArray()
    lines.InsertNextCell(line0)
    lines.InsertNextCell(line1)
    
    # Create a polydata to store everything in
    linesPolyData = vtk.vtkPolyData()
    
    # Add the points to the dataset
    linesPolyData.SetPoints(pts)
    
    # Add the lines to the dataset
    linesPolyData.SetLines(lines)
    

    # Visualize
    lineMapper = vtk.vtkPolyDataMapper()
    lineMapper.SetInputData(linesPolyData)
    
    lineActor = vtk.vtkActor()
    lineActor.SetMapper(lineMapper)
    
    # Add words
    word11 = vtk.vtkVectorText()
    word11.SetText(words[0])
    wordMapper11 = vtk.vtkPolyDataMapper()
    wordMapper11.SetInputConnection(word11.GetOutputPort())
    wordActor11 = vtk.vtkFollower()
    wordActor11.SetMapper(wordMapper11)
    wordActor11.SetScale(0.05, 0.05, 0.05)
    wordActor11.AddPosition(0.25, 0.45, 0.2)
    wordActor11.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    word12 = vtk.vtkVectorText()
    word12.SetText(words[1])
    wordMapper12 = vtk.vtkPolyDataMapper()
    wordMapper12.SetInputConnection(word12.GetOutputPort())
    wordActor12 = vtk.vtkFollower()
    wordActor12.SetMapper(wordMapper12)
    wordActor12.SetScale(0.05, 0.05, 0.05)
    wordActor12.AddPosition(0.6, 0.35, 0.2)
    wordActor12.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    word21 = vtk.vtkVectorText()
    word21.SetText(words[2])
    wordMapper21 = vtk.vtkPolyDataMapper()
    wordMapper21.SetInputConnection(word21.GetOutputPort())
    wordActor21 = vtk.vtkFollower()
    wordActor21.SetMapper(wordMapper21)
    wordActor21.SetScale(0.05, 0.05, 0.05)
    wordActor21.AddPosition(0, 0.15, 0.6)
    wordActor21.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    word22 = vtk.vtkVectorText()
    word22.SetText(words[3])
    wordMapper22 = vtk.vtkPolyDataMapper()
    wordMapper22.SetInputConnection(word22.GetOutputPort())
    wordActor22 = vtk.vtkFollower()
    wordActor22.SetMapper(wordMapper22)
    wordActor22.SetScale(0.05, 0.05, 0.05)
    wordActor22.AddPosition(0.5, 0.12, 0.7)
    wordActor22.GetProperty().SetColor(colors.GetColor3d('Black'))

    title = vtk.vtkVectorText()
    title.SetText(words[4])
    titleMapper = vtk.vtkPolyDataMapper()
    titleMapper.SetInputConnection(title.GetOutputPort())
    titleActor = vtk.vtkFollower()
    titleActor.SetMapper(titleMapper)
    titleActor.SetScale(0.08, 0.08, 0.08)
    titleActor.AddPosition(0.3, 1, 0.0)
    titleActor.GetProperty().SetColor(colors.GetColor3d('Black'))
    
    return sphere11Actor, sphere21Actor, sphere12Actor, sphere22Actor,\
           lineActor, wordActor11, wordActor12, wordActor21,\
           wordActor22, titleActor
           

def main():
    colors = vtk.vtkNamedColors()
    
    # Create the axes and the associated mapper and actor.
    axes = vtk.vtkAxes()
    axes.SetOrigin(0, 0, 0)
    axesMapper = vtk.vtkPolyDataMapper()
    axesMapper.SetInputConnection(axes.GetOutputPort())
    axesActor = vtk.vtkActor()
    axesActor.SetMapper(axesMapper)
    
    p11 = [0.25, 0.4, 0.2]
    p12 = [0.15, 0.25, 0.5]
    p21 = [0.6, 0.3, 0.2]
    p22 = [0.5, 0.2, 0.7]
    
    points1 = [p11, p12, p21, p22]    
    colors1 = ['Red', 'Red', 'Purple', 'Purple']
    words1 = ['man', 'femme', 'roi', 'queen', 'Male-Female']
    
    sphere11Actor, sphere21Actor, sphere12Actor, sphere22Actor, lineActor,\
    wordActor11, wordActor12, wordActor21, wordActor22, titleActor\
    = create_actors(colors1, points1, words1)
    
    points2 = [p11, p21, p12, p22]    
    colors2 = ['Yellow', 'Orange', 'Yellow', 'Orange']
    words2 = ['walked', 'swam', 'marche', 'nage', 'Verb Tense']
    
    sphere11Actor2, sphere21Actor2, sphere12Actor2, sphere22Actor2, lineActor2,\
    wordActor112, wordActor122, wordActor212, wordActor222, titleActor2\
    = create_actors(colors2, points2, words2)
    
    colors3 = ['Pink', 'White', 'White', 'Pink']
    words3 = ['La Chine', 'Beijing', 'Le Japon', 'Tokyo', 'Country-Capital']
    
    sphere11Actor3, sphere21Actor3, sphere12Actor3, sphere22Actor3, lineActor3,\
    wordActor113, wordActor123, wordActor213, wordActor223, titleActor3\
    = create_actors(colors3, points1, words3)

    # There will be one render window
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(900, 300)
    renderWindow.SetWindowName('ExtractSelectionCells')

    # And one interactor
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    # Define viewport ranges
    # (xmin, ymin, xmax, ymax)
    leftViewport = [0.0, 0.0, 0.33, 1.0]
    centerViewport = [0.33, 0.0, 0.66, 1.0]
    rightViewport = [0.66, 0.0, 1.0, 1.0]

    # Create a camera for all renderers
    camera = vtk.vtkCamera()

    # Setup the renderers
    leftRenderer = vtk.vtkRenderer()
    renderWindow.AddRenderer(leftRenderer)
    leftRenderer.SetViewport(leftViewport)
    leftRenderer.SetBackground(colors.GetColor3d('BurlyWood'))
    leftRenderer.SetActiveCamera(camera)

    centerRenderer = vtk.vtkRenderer()
    renderWindow.AddRenderer(centerRenderer)
    centerRenderer.SetViewport(centerViewport)
    centerRenderer.SetBackground(colors.GetColor3d('Pink'))
    centerRenderer.SetActiveCamera(camera)

    rightRenderer = vtk.vtkRenderer()
    renderWindow.AddRenderer(rightRenderer)
    rightRenderer.SetViewport(rightViewport)
    rightRenderer.SetBackground(colors.GetColor3d('CornflowerBlue'))
    rightRenderer.SetActiveCamera(camera)

    leftRenderer.AddActor(axesActor)
    leftRenderer.AddActor(sphere11Actor)
    leftRenderer.AddActor(sphere21Actor)
    leftRenderer.AddActor(sphere12Actor)
    leftRenderer.AddActor(sphere22Actor)
    leftRenderer.AddActor(lineActor)
    leftRenderer.AddActor(wordActor11)
    leftRenderer.AddActor(wordActor12)
    leftRenderer.AddActor(wordActor21)
    leftRenderer.AddActor(wordActor22)
    leftRenderer.AddActor(titleActor)
    
    centerRenderer.AddActor(axesActor)
    centerRenderer.AddActor(sphere11Actor2)
    centerRenderer.AddActor(sphere21Actor2)
    centerRenderer.AddActor(sphere12Actor2)
    centerRenderer.AddActor(sphere22Actor2)
    centerRenderer.AddActor(lineActor2)
    centerRenderer.AddActor(wordActor112)
    centerRenderer.AddActor(wordActor122)
    centerRenderer.AddActor(wordActor212)
    centerRenderer.AddActor(wordActor222)
    centerRenderer.AddActor(titleActor2)
    
    rightRenderer.AddActor(axesActor)
    rightRenderer.AddActor(sphere11Actor3)
    rightRenderer.AddActor(sphere21Actor3)
    rightRenderer.AddActor(sphere12Actor3)
    rightRenderer.AddActor(sphere22Actor3)
    rightRenderer.AddActor(lineActor3)
    rightRenderer.AddActor(wordActor113)
    rightRenderer.AddActor(wordActor123)
    rightRenderer.AddActor(wordActor213)
    rightRenderer.AddActor(wordActor223)
    rightRenderer.AddActor(titleActor3)

    leftRenderer.ResetCamera()

    renderWindow.Render()
    interactor.Start()


if __name__ == '__main__':
    main()