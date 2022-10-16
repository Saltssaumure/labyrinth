from PIL import Image, ImageTk
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image

def overlay_images(bg_name, mob_name):
    mob_img = Image.open("images/monsters/" + mob_name + "_transparent.png").convert("RGBA")
    bg_img = Image.open("images/rooms/" + bg_name + ".jpg")
    bg_img = bg_img.resize((500, 500), Image.Resampling.LANCZOS)
    bg_img.paste(mob_img, (0,0), mob_img)
    
    return ImageTk.PhotoImage(image=bg_img)
