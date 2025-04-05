# utlis.py
def product_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"image/product/{instance.slug}_{instance.id}.{ext}"
