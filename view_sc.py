# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#from paraview.simple import *
import sys
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

fn = []

pt = str(sys.argv[1])
op = str(sys.argv[2])
for n in range(3,len(sys.argv)):
    fn += [str(sys.argv[n])]

# create a new 'CGNS Series Reader'
test2cgns = CGNSSeriesReader(registrationName='running.cgns', FileNames=[op]) #test2名称可以随意改变，无需拘泥，但要注意名称统一
test2cgns.Bases = ['Base']
test2cgns.PointArrayStatus = []

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
test2cgnsDisplay = Show(test2cgns, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
test2cgnsDisplay.Representation = 'Surface'
test2cgnsDisplay.ColorArrayName = [None, '']
test2cgnsDisplay.SelectTCoordArray = 'None'
test2cgnsDisplay.SelectNormalArray = 'None'
test2cgnsDisplay.SelectTangentArray = 'None'
test2cgnsDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
test2cgnsDisplay.SelectOrientationVectors = 'None'
test2cgnsDisplay.ScaleFactor = 0.24400000572204592
test2cgnsDisplay.SelectScaleArray = 'None'
test2cgnsDisplay.GlyphType = 'Arrow'
test2cgnsDisplay.GlyphTableIndexArray = 'None'
test2cgnsDisplay.GaussianRadius = 0.012200000286102295
test2cgnsDisplay.SetScaleArray = [None, '']
test2cgnsDisplay.ScaleTransferFunction = 'PiecewiseFunction'
test2cgnsDisplay.OpacityArray = [None, '']
test2cgnsDisplay.OpacityTransferFunction = 'PiecewiseFunction'
test2cgnsDisplay.DataAxesGrid = 'GridAxesRepresentation'
test2cgnsDisplay.PolarAxes = 'PolarAxesRepresentation'
test2cgnsDisplay.ScalarOpacityUnitDistance = 0.0646560301389689
test2cgnsDisplay.OpacityArrayName = ['FIELD', 'ispatch']
test2cgnsDisplay.ExtractedBlockIndex = 2

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on test2cgns
test2cgns.PointArrayStatus = ['DPM_Concentration', 'VelocityMagnitude']

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=test2cgns)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [1.2200000286102295, 1.2200000286102295, 1.2200000286102295]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [1.2200000286102295, 1.2200000286102295, 1.2200000286102295]

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = [None, '']
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'DPM_Concentration'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.24400000572204592
slice1Display.SelectScaleArray = 'DPM_Concentration'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'DPM_Concentration'
slice1Display.GaussianRadius = 0.012200000286102295
slice1Display.SetScaleArray = ['POINTS', 'DPM_Concentration']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'DPM_Concentration']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.12454807013273239, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 0.12454807013273239, 1.0, 0.5, 0.0]

# hide data in view
Hide(test2cgns, renderView1)

# Properties modified on renderView1
renderView1.Background = [1.0, 1.0, 1.0]

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'DPM_Concentration'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'DPM_Concentration'
dPM_ConcentrationLUT = GetColorTransferFunction('DPM_Concentration')
dPM_ConcentrationLUT.RGBPoints = [0.0, 0.02, 0.3813, 0.9981, 0.002965430241255533, 0.02000006, 0.424267768, 0.96906969, 0.005930860482511066, 0.02, 0.467233763, 0.940033043, 0.008896290723766598, 0.02, 0.5102, 0.911, 0.011861720965022133, 0.02000006, 0.546401494, 0.872669438, 0.014827151206277665, 0.02, 0.582600362, 0.83433295, 0.017792581447533196, 0.02, 0.6188, 0.796, 0.02075801168878873, 0.02000006, 0.652535156, 0.749802434, 0.023723441930044265, 0.02, 0.686267004, 0.703599538, 0.026688872171299796, 0.02, 0.72, 0.6574, 0.02965430241255533, 0.02000006, 0.757035456, 0.603735359, 0.032619732653810865, 0.02, 0.794067037, 0.55006613, 0.03558516289506639, 0.02, 0.8311, 0.4964, 0.038550593136321934, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 0.04151602337757746, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 0.044481453618832996, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 0.04744688386008853, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 0.050412314101344065, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 0.05337774434259959, 0.6439, 0.9773, 0.0469, 0.05634317458385513, 0.762401813, 0.984669591, 0.034600153, 0.05930860482511066, 0.880901185, 0.992033407, 0.022299877, 0.062274035066366196, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 0.06523946530762173, 0.999402998, 0.955036376, 0.079066628, 0.06820489554887726, 0.9994, 0.910666223, 0.148134024, 0.07117032579013279, 0.9994, 0.8663, 0.2172, 0.07413575603138833, 0.999269665, 0.818035981, 0.217200652, 0.07710118627264387, 0.999133332, 0.769766184, 0.2172, 0.0800666165138994, 0.999, 0.7215, 0.2172, 0.08303204675515492, 0.99913633, 0.673435546, 0.217200652, 0.08599747699641046, 0.999266668, 0.625366186, 0.2172, 0.08896290723766599, 0.9994, 0.5773, 0.2172, 0.09192833747892153, 0.999402998, 0.521068455, 0.217200652, 0.09489376772017706, 0.9994, 0.464832771, 0.2172, 0.0978591979614326, 0.9994, 0.4086, 0.2172, 0.10082462820268813, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 0.10379005844394366, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 0.10675548868519918, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 0.10972091892645472, 0.949903037, 0.116867171, 0.252900603, 0.11268634916771025, 0.903199533, 0.078432949, 0.291800389, 0.1156517794089658, 0.8565, 0.04, 0.3307, 0.11861720965022132, 0.798902627, 0.04333345, 0.358434298, 0.12158263989147686, 0.741299424, 0.0466667, 0.386166944, 0.12454807013273239, 0.6837, 0.05, 0.4139]
dPM_ConcentrationLUT.ColorSpace = 'RGB'
dPM_ConcentrationLUT.NanColor = [1.0, 0.0, 0.0]
dPM_ConcentrationLUT.ScalarRangeInitialized = 1.0
# dPM_ConcentrationLUT.ApplyPreset('Rainbow Uniform', True)

# get opacity transfer function/opacity map for 'DPM_Concentration'
dPM_ConcentrationPWF = GetOpacityTransferFunction('DPM_Concentration')
dPM_ConcentrationPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.12454807013273239, 1.0, 0.5, 0.0]
dPM_ConcentrationPWF.ScalarRangeInitialized = 1

# get color legend/bar for velocityMagnitudeLUT in view renderView1
dPM_ConcentrationLUTColorBar = GetScalarBar(dPM_ConcentrationLUT, renderView1)
dPM_ConcentrationLUTColorBar.Title = 'DPM_Concentration'
dPM_ConcentrationLUTColorBar.ComponentTitle = ''


# change scalar bar placement
dPM_ConcentrationLUTColorBar.WindowLocation = 'AnyLocation'
dPM_ConcentrationLUTColorBar.Position = [0.736753574432296, 0.33911882510013347]
dPM_ConcentrationLUTColorBar.ScalarBarLength = 0.3300000000000002

dPM_ConcentrationLUTColorBar.RangeLabelFormat = '%-#6.2f'

# Properties modified on velocityMagnitudeLUTColorBar
dPM_ConcentrationLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
dPM_ConcentrationLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# set active source
SetActiveSource(None)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1189, 749)

# current camera placement for renderView1
renderView1.CameraPosition = [1.2200000062584877, 1.2200000062584877, -8.72274266440093]
renderView1.CameraFocalPoint = [1.2200000062584877, 1.2200000062584877, 1.2200000286102295]
renderView1.CameraViewUp = [0.0, -1.0, 0.0]
renderView1.CameraParallelScale = 2.1131020347884015

# save screenshot
SaveScreenshot(pt+fn[1]+'.png', renderView1, ImageResolution=[1189, 749])

# set active source
SetActiveSource(slice1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice1.SliceType)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'VelocityMagnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(dPM_ConcentrationLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'VelocityMagnitude'
velocityMagnitudeLUT = GetColorTransferFunction('VelocityMagnitude')
# velocityMagnitudeLUT.RGBPoints = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2]#[0.0, 0.02, 0.3813, 0.9981, 0.020170151810399464, 0.02000006, 0.424267768, 0.96906969, 0.04034030362079893, 0.02, 0.467233763, 0.940033043, 0.06051045543119839, 0.02, 0.5102, 0.911, 0.08068060724159785, 0.02000006, 0.546401494, 0.872669438, 0.10085075905199731, 0.02, 0.582600362, 0.83433295, 0.12102091086239677, 0.02, 0.6188, 0.796, 0.14119106267279624, 0.02000006, 0.652535156, 0.749802434, 0.1613612144831957, 0.02, 0.686267004, 0.703599538, 0.18153136629359515, 0.02, 0.72, 0.6574, 0.20170151810399461, 0.02000006, 0.757035456, 0.603735359, 0.2218716699143941, 0.02, 0.794067037, 0.55006613, 0.24204182172479355, 0.02, 0.8311, 0.4964, 0.26221197353519304, 0.021354336738172372, 0.8645368555261631, 0.4285579460761159, 0.2823821253455925, 0.023312914349117714, 0.897999359924484, 0.36073871343115577, 0.302552277155992, 0.015976108242848862, 0.9310479513349017, 0.2925631815088092, 0.3227224289663914, 0.27421074700988196, 0.952562960995083, 0.15356836602739213, 0.34289258077679086, 0.4933546281681699, 0.9619038625309482, 0.11119493614749336, 0.3630627325871903, 0.6439, 0.9773, 0.0469, 0.3832328843975898, 0.762401813, 0.984669591, 0.034600153, 0.40340303620798923, 0.880901185, 0.992033407, 0.022299877, 0.4235731880183887, 0.9995285432627147, 0.9995193706781492, 0.0134884641450013, 0.4437433398287882, 0.999402998, 0.955036376, 0.079066628, 0.4639134916391877, 0.9994, 0.910666223, 0.148134024, 0.4840836434495871, 0.9994, 0.8663, 0.2172, 0.5042537952599866, 0.999269665, 0.818035981, 0.217200652, 0.5244239470703861, 0.999133332, 0.769766184, 0.2172, 0.5445940988807856, 0.999, 0.7215, 0.2172, 0.564764250691185, 0.99913633, 0.673435546, 0.217200652, 0.5849344025015845, 0.999266668, 0.625366186, 0.2172, 0.605104554311984, 0.9994, 0.5773, 0.2172, 0.6252747061223833, 0.999402998, 0.521068455, 0.217200652, 0.6454448579327828, 0.9994, 0.464832771, 0.2172, 0.6656150097431822, 0.9994, 0.4086, 0.2172, 0.6857851615535817, 0.9947599917687346, 0.33177297300202935, 0.2112309638520206, 0.7059553133639812, 0.9867129505479589, 0.2595183410914934, 0.19012239549291934, 0.7261254651743806, 0.9912458875646419, 0.14799417507952672, 0.21078892136920357, 0.7462956169847801, 0.949903037, 0.116867171, 0.252900603, 0.7664657687951796, 0.903199533, 0.078432949, 0.291800389, 0.7866359206055791, 0.8565, 0.04, 0.3307, 0.8068060724159785, 0.798902627, 0.04333345, 0.358434298, 0.826976224226378, 0.741299424, 0.0466667, 0.386166944, 0.8471463760367774, 0.6837, 0.05, 0.4139]
# velocityMagnitudeLUT.ColorSpace = 'RGB'
# velocityMagnitudeLUT.NanColor = [1.0, 0.0, 0.0]
# velocityMagnitudeLUT.ScalarRangeInitialized = 1.0
velocityMagnitudeLUT.ApplyPreset('Rainbow Uniform', True)

# get opacity transfer function/opacity map for 'VelocityMagnitude'
velocityMagnitudePWF = GetOpacityTransferFunction('VelocityMagnitude')
velocityMagnitudePWF.Points = [0.0, 0.0, 0.5, 0.0, 0.8471463760367774, 1.0, 0.5, 0.0]
velocityMagnitudePWF.ScalarRangeInitialized = 1

# get color legend/bar for velocityMagnitudeLUT in view renderView1
velocityMagnitudeLUTColorBar = GetScalarBar(velocityMagnitudeLUT, renderView1)

velocityMagnitudeLUTColorBar.Title = 'Velocity'
velocityMagnitudeLUTColorBar.ComponentTitle = ''

# change scalar bar placement
velocityMagnitudeLUTColorBar.WindowLocation = 'AnyLocation'
velocityMagnitudeLUTColorBar.Position = [0.736753574432296, 0.33911882510013347]
velocityMagnitudeLUTColorBar.ScalarBarLength = 0.3300000000000002

velocityMagnitudeLUTColorBar.RangeLabelFormat = '%-#6.2f'

# Properties modified on velocityMagnitudeLUTColorBar
velocityMagnitudeLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
velocityMagnitudeLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

# set active source
SetActiveSource(None)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# layout/tab size in pixels
layout1.SetSize(1189, 749)

# current camera placement for renderView1
renderView1.CameraPosition = [1.2200000062584877, 1.2200000062584877, -8.72274266440093]
renderView1.CameraFocalPoint = [1.2200000062584877, 1.2200000062584877, 1.2200000286102295]
renderView1.CameraViewUp = [0.0, -1.0, 0.0]
renderView1.CameraParallelScale = 2.1131020347884015

# save screenshot
SaveScreenshot(pt+fn[0]+'.png', renderView1, ImageResolution=[1189, 749])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1189, 749)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [9.384399344554623, 1.2200000286102295, 1.2200000286102295]
renderView1.CameraFocalPoint = [1.2200000286102295, 1.2200000286102295, 1.2200000286102295]
renderView1.CameraViewUp = [0.0, -1.0, 0.0]
renderView1.CameraParallelScale = 2.1131020347884015

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).