

import PySpin
from clases_VM import *


system = PySpin.System.GetInstance()

cam_list = system.GetCameras()

num_cameras = cam_list.GetSize()

print('Number of cameras detected: %d' % num_cameras)

# Run example on each camera
camara = Camera_PySpin(cam_list[0])

print(camara.Get_Device_Info())

camara.Set_Exposure_Auto(True)
camara.Set_Gain_Auto(True)
camara.Set_Sharpness_Auto(True)

camara.Set_Buffer_Mode('MultiFrame')

#camara.Reset()
del  camara 


cam_list.Clear()

# Release system instance
system.ReleaseInstance()
