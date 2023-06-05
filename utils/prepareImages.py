from PIL import Image

def resize_crop_avatar_image(image_path, size):
        #fit aspect ratio
        image = Image.open(image_path)
        original_width, original_height = image.size
        crop_size = min(original_width, original_height)
        left = (original_width - crop_size) // 2
        upper = (original_height - crop_size) // 2
        right = left + crop_size
        lower = upper + crop_size
        cropped_image = image.crop((left, upper, right, lower))

        #then resize
        resized_image = cropped_image.resize(size)
        return resized_image

def resize_crop_cover_image(image_path, size):
        aspect_ratio = (3, 1)
        img = Image.open(image_path)
        width, height = img.size

        target_aspect_ratio = aspect_ratio[0] / aspect_ratio[1]
        current_aspect_ratio = width / height

        if current_aspect_ratio > target_aspect_ratio:
        # Crop the width to match the target aspect ratio
                new_width = int(height * target_aspect_ratio)
                left = (width - new_width) // 2
                right = left + new_width
                img = img.crop((left, 0, right, height))
        elif current_aspect_ratio < target_aspect_ratio:
        # Crop the height to match the target aspect ratio
                new_height = int(width / target_aspect_ratio)
                top = (height - new_height) // 2
                bottom = top + new_height
                img = img.crop((0, top, width, bottom))

        resized_img = img.resize(size)

        return resized_img

