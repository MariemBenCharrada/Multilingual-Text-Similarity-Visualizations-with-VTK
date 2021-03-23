# -*- coding: utf-8 -*-
"""
Created on Mon Mar 01 19:03:37 2021

@author: mariem.ben_charrada
"""
from __future__ import division
import numpy as np
import pandas as pd
import vtk

def calculate_angle(idx, pair):
    angle = np.arccos(float(pair[0])/5)*180/np.pi
    return angle


def main():
    colors = vtk.vtkNamedColors()
    
    sts_data = pd.read_csv('sts.csv', header=None)
    index = 10
    pair = sts_data.loc[index].tolist()
    angle = calculate_angle(index, pair)
    
   

    # Create the axes and the associated mapper and actor.
    axes = vtk.vtkAxes()
    axes.SetOrigin(0, 0, 0)
    axesMapper = vtk.vtkPolyDataMapper()
    axesMapper.SetInputConnection(axes.GetOutputPort())
    axesActor = vtk.vtkActor()
    axesActor.SetMapper(axesMapper)


    # Create the Renderer, RenderWindow, and RenderWindowInteractor.
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(640, 480)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)

    style = vtk.vtkInteractorStyleTrackballCamera()
    interactor.SetInteractorStyle(style)

    # Add the actors to the renderer.
    renderer.AddActor(axesActor)

    renderer.SetBackground(colors.GetColor3d('Silver'))
    
    # Create arrow
    source = vtk.vtkArrowSource()
    source.SetShaftResolution(30)
    source.SetTipResolution(30)
    source.SetTipLength(0.15)
    source.SetShaftRadius(0.01)
    source.SetTipRadius(0.05)

    # Create a transform that rotates the arrow 
    transform1 = vtk.vtkTransform()
    transform1.RotateWXYZ(30, 0, 0, 1)
    transform1.RotateWXYZ(330, 0, 1, 0)
    transformFilter1 = vtk.vtkTransformPolyDataFilter()
    transformFilter1.SetTransform(transform1)
    transformFilter1.SetInputConnection(source.GetOutputPort())
    transformFilter1.Update()
    
    # Create another transform that rotates the arrow 
    transform2 = vtk.vtkTransform()
    transform2.RotateWXYZ(30+angle, 0, 0, 1)
    transform2.RotateWXYZ(330, 0, 1, 0)
    transformFilter2 = vtk.vtkTransformPolyDataFilter()
    transformFilter2.SetTransform(transform2)
    transformFilter2.SetInputConnection(source.GetOutputPort())
    transformFilter2.Update()

    # Mapper for the original arrow
    coneMapper1 = vtk.vtkPolyDataMapper()
    coneMapper1.SetInputConnection(transformFilter1.GetOutputPort())

    # Another mapper for the rotated arrow
    coneMapper2 = vtk.vtkPolyDataMapper()
    coneMapper2.SetInputConnection(transformFilter2.GetOutputPort())

    # Actor for original arrow
    actor1 = vtk.vtkActor()
    actor1.SetMapper(coneMapper1)

    # Actor for rotated arrow
    actor2 = vtk.vtkActor()
    actor2.SetMapper(coneMapper2)

    # Color the original arrow
    actor1.GetProperty().SetColor(colors.GetColor3d('LightCoral'))
    # Color rotated arrow
    actor2.GetProperty().SetColor(colors.GetColor3d('PaleTurquoise'))

    # Assign actor to the renderer
    renderer.AddActor(actor1)
    renderer.AddActor(actor2)

    #######
    sent1 = vtk.vtkVectorText()
    sent1.SetText(pair[1])
    sentMapper1 = vtk.vtkPolyDataMapper()
    sentMapper1.SetInputConnection(sent1.GetOutputPort())
    sentActor1 = vtk.vtkFollower()
    sentActor1.SetMapper(sentMapper1)
    sentActor1.SetScale(0.03, 0.03, 0.03)
    sentActor1.AddPosition(0.8, 0.5, 0.6)
    sentActor1.GetProperty().SetColor(colors.GetColor3d('Black'))
    renderer.AddActor(sentActor1)
    
    sent2 = vtk.vtkVectorText()
    sent2.SetText(pair[2])
    sentMapper2 = vtk.vtkPolyDataMapper()
    sentMapper2.SetInputConnection(sent2.GetOutputPort())
    sentActor2 = vtk.vtkFollower()
    sentActor2.SetMapper(sentMapper2)
    sentActor2.SetScale(0.03, 0.03, 0.03)
    if 0<=angle<=10: 
        sentActor2.AddPosition(0.5, 0.6, 0.4)
    elif 10<angle<=30:
        sentActor2.AddPosition(0.5, 0.7, 0.4)
    elif 30<angle<60:
        sentActor2.AddPosition(0.1, 0.9, 0.1)
    elif 60<=angle<65:
        sentActor2.AddPosition(0, 0.9, 0.5)
    elif 65<=angle<80:
        sentActor2.AddPosition(-0.2, 0.9, 0.5)
    else:
        sentActor2.AddPosition(-0.4, 0.8, 0.5)
    sentActor2.GetProperty().SetColor(colors.GetColor3d('Black'))
    renderer.AddActor(sentActor2)
    #####


    # Zoom in closer.
    renderer.ResetCamera()
    renderer.GetActiveCamera().Zoom(1.6)

    renderer.SetBackground(colors.GetColor3d('Silver'))

    # Reset the clipping range of the camera; set the camera of the follower; render.
    renderer.ResetCameraClippingRange()
    sentActor1.SetCamera(renderer.GetActiveCamera())
    sentActor2.SetCamera(renderer.GetActiveCamera())

    interactor.Initialize()
    renderWindow.SetWindowName('SentenceEmbeddings')
    renderWindow.Render()
    interactor.Start()


if __name__ == '__main__':
    main()