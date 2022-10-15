from PIL import Image, ImageTk
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image

def read_images(img_dict, img_dict_name_location, img_directory, img_filetype):
    imgs_dict = {}

    for key in img_dict.keys():
        image = Image.open(img_directory + img_dict[key][img_dict_name_location] + img_filetype)
        image = image.resize((500, 500), Image.Resampling.LANCZOS)
        imgs_dict[key] = ImageTk.PhotoImage(image)
    
    return imgs_dict