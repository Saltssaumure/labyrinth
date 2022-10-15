from PIL import Image, ImageTk
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image

def read_images(img_dict, img_dict_name_location, img_directory, img_filetype, crop_type="none"):
    imgs_dict = {}

    for key in img_dict.keys():
        image = Image.open(img_directory + img_dict[key][img_dict_name_location] + img_filetype)
        image = image.resize((500, 500), Image.Resampling.LANCZOS)
        if crop_type == "left":
            image = image.crop([400,0,500,500])
        if crop_type == "right":
            image = image.crop([0,0,100,500])
        imgs_dict[key] = ImageTk.PhotoImage(image)
    
    return imgs_dict