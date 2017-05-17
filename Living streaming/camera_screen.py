from PIL import ImageGrab
import ctypes
import io

windowsize = 500//2
user32 = ctypes.windll.user32

class _point_t(ctypes.Structure):
    _fields_ = [
                ('x',  ctypes.c_long),
                ('y',  ctypes.c_long),
               ]

def get_cursor_position():
    point = _point_t()
    result = user32.GetCursorPos(ctypes.pointer(point))
    if result:  return (point.x, point.y)
    else:       return None

class Camera(object):
    
    def get_frame(self):
        pos = get_cursor_position()

        img_obj = ImageGrab.grab(bbox=(pos[0]-windowsize, pos[1]-windowsize, pos[0]+windowsize, pos[1]+windowsize))
        #img_obj = ImageGrab.grab()
        b = io.BytesIO()
        img_obj.save(b, 'jpeg')
        img_data = b.getvalue()
        return img_data
