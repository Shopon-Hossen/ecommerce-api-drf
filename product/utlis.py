def product_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"image/product/{instance.name_slug}.{ext}"
