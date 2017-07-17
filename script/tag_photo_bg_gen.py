# -*- coding: utf-8 -*-
"""
生成tag page 的背景图
"""

from PIL import Image

template_image = "/tmp/test.png"
template = Image.open(template_image)
a_band = template.split()[-1]
template_size = (550, 350)


def resize_and_crop(ori_image, target_size):
    """
    输入的必须是宽图，切除target_size大小的图片，先resize，然后取中间
    :param ori_image: 
    :param target_size: 
    :return: 
    """
    ori_width, ori_height = ori_image.size
    result_width = target_size[0]
    result_height = result_width * ori_height / ori_width
    crop_top = (result_height - target_size[1]) / 2
    crop_bottom = crop_top + target_size[1]
    return ori_image.resize((result_width, result_height)).crop((0, crop_top, result_width, crop_bottom))


def append_band(image, band):
    return Image.merge("RGBA", image.split() + (band,))


if __name__ == '__main__':
    path = "/tmp/pt.jpg"
    image = Image.open(path)
    image_result = append_band(resize_and_crop(image, template_size), a_band)
    image_result.save("/tmp/result.png")
