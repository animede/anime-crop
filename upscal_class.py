import cv2
from realesrgan import RealESRGANer
from realesrgan.archs.srvgg_arch import SRVGGNetCompact

class  Up_Scale():
    #+++++++++++++++++++  init  +++++++++++++++++++
    def __init__(self):
        model_name = 'realesr-animevideov3'
        model = SRVGGNetCompact(num_in_ch=3, num_out_ch=3, num_feat=64, num_conv=16, upscale=4, act_type='prelu')
        netscale = 4
        model_path = "./weights/" + model_name +".pth"
        print(model_path )
        dni_weight = None

        self.upsampler = RealESRGANer(
                scale=netscale,
                model_path=model_path,
                dni_weight=dni_weight,
                model=model,
                tile=0,
                tile_pad=10,
                pre_pad=0,
                half=True,
                gpu_id=0)        

    # ++++++++++++++  up scale ++++++++++++++++ img=OpenCV ndarrey BGR or BGRA
    def  upscale(self,img , scale):
        try:
                output, _ = self.upsampler.enhance(img , outscale=scale)
        except RuntimeError as error:
                print('Error', error)
                print('If you encounter CUDA out of memory, try to set --tile with a smaller number.')
        return output



