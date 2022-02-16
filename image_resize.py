import os
import glob
from tqdm import tqdm
from PIL import Image, ImageFile
from joblib import Parallel, delayed

#func to resize 1 image

def resize_image(image_path,output_folder,resize):
    base_name = os.path.basename(image_path)  #basename is something.jpg has been extracted
    outpath = os.path.join(output_folder,base_name) 
    img = Image.open(image_path)
    img = img.resize(
        (resize[1],resize[0]),resample= Image.BILINEAR
    )                   # image resized
    img.save(outpath)   #image saved in outpath


#parallel thread

input_folder = ""
output_folder = ""

images = glob.glob(os.pat.join(input_folder,"*.jpg"))

Parallel(n_jobs=12)(
    delayed(resize_image)(            #calling resize_image func with diff arguments
        i,
        output_folder,
        (512,512)
    )for i in tqdm(images)
)