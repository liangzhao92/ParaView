from vtk import *
#from libvtkMantaPython import *
cone = vtkConeSource()
cone.SetHeight( 3.0 )
cone.SetRadius( 1.0 )
cone.SetResolution( 10 )
coneMapper = vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtkActor()
coneActor.SetMapper(coneMapper)
ren1 = vtkRenderer()
ren1.AddActor(coneActor)
ren1.SetBackground(0.1, 0.2, 0.4)
renWin = vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)
renWin.Render()
#ren1.Render()
iren.Initialize()
iren.Start()

