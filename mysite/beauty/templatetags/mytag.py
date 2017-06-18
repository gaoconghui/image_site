# coding=utf-8 #coding:utf-8
import datetime
import random

from django import template

image_list = [
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/43/2BAXH021A9Q5.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/57/4EQCZY6K3ZUD.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/052/48/42O8UEM211O0_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/13/R3BOLYL40D79.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/17/9XX992QF07X5.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/052/16/PI9D9Y91Z99C_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/57/L4TX3O72D38T.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/09/2IM8874N8UW1.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/50/K5UG17R130MX.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/38/3J3M56I30D7D.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/32/6GP49GZXR25P.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/57/KNAM69152MSE.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/13/DU2IF50A8Z1O.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/13/2052D8FWI66I.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/38/9I0A309G9P04.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/00/PD51VVZ08UXV.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/52/9G18AZ6TDF6B.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/59/OW4DS5XO71TR.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/30/57I78EX09R35.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/56/45VGTPKYG8E8.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/28/C64CMKUIB2LW.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/58/GTXZ02IL0K44.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/342/07/K1A91LJ24JTD.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/29/B5PX2CUV6067.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/151/54/PQ7C0J6XIC75_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/15/TPOQX3E6E805.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/12/JSFE67P4JRVP.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/34/XCYJJ6Y1WTZ8.jpg",
    "http://image.tianjimedia.com/uploadImages/2016/335/07/J6373OCDKH0F.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/25/PPN0IRKB8YFY.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/36/99K61E9ZB7B6.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/23/QOR8E94UJ0CH.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/56/45VGTPKYG8E8.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/27/C25PJUL32KOZ.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/053/54/W39S7AIZ3N87_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/50/P4AC9IDNA8J2.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/068/23/962DOOXEY7E5_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/067/26/PZ7I9371SCJ1_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/152/22/6MD0MYG2Y3ZE_800x1200.jpg",
    "http://image.tianjimedia.com/uploadImages/2016/323/50/W835A5A422A5.jpg",
    "http://image.tianjimedia.com/uploadImages/2016/327/30/AAG07XOSLB7L.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/136/23/R563592998Q5_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/136/37/WZEE3N10D9G1_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/052/44/AW9WI9N9A49W_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/066/37/R49ERFC40091_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/052/22/2S35LYQ053FQ_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/154/02/V9R4AHXV858A_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/068/09/3L7D9LR8ZPAM_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/069/03/463M7HS2VBH5_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/151/45/648TB6134L1U_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/066/38/UWFN7KI3D115_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/156/03/DCFMFY033458_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/068/52/5O0XG0W97963_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/57/323V2C16J564.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/01/6K0W0Q5W7L5I.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/49/NO486P11Z942.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/049/59/DOZE6AF1C516_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/57/996F4VZE2X26.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/30/6VHV5IJO900U.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/38/T793DK5CQ3BX.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/10/D511N2B5OSSC.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/06/93TJ1SP10ND1.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/51/V033407920R1.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/35/9IEX1BQQ0991.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/342/05/S90AMDDT6TF0.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/049/47/HH228GNOWJ3I_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/38/X6UO24K73574.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/151/02/322D356QIU0I_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/37/OPL31VKHVRO0.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/28/4FCNIYSFL6C0.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/36/P1P8RC28GP74.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/55/9A3QNT85OLWO.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/15/C474042H5EWK.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/51/1L4MT15ZFK8Z.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/39/X75ECV4V9EEZ.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/12/NRT1UAC5JP33.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/19/N3E9C87WT1D1.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/14/90Y8J2S585RF.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/335/07/SCSL41T4X881.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/58/8OD1H1OA7364.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/02/363D7S5UO4Q5.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/12/ET8YH1CXI60Q.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/57/DP965V9S04UJ.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/52/GTXM2J88K1HH.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/38/T793DK5CQ3BX.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/51/ECU15E5L5I4Z.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/337/53/92068I4OHI57.JPG",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/049/57/22CX8C6B869W_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2016/340/50/CAM2UW0YOMJ0.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/049/17/9P3PJ3YC32PH_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/048/43/MR2H086XO183_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/152/20/FB86J74126UL_800x1200.jpg",
    "http://image.tianjimedia.com/uploadImages/2016/330/40/WJ7CL78JC13Y.jpg",
    "http://image.tianjimedia.com/uploadImages/2016/327/48/T926083N36K6.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/125/05/I0ZJ915B0953_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/158/27/8ITQ06H8IIYN_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/133/05/6871RUO8FGE3_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/049/24/4TLV9UUD1UYX_800x1200.jpg",
    "http://dynamic-image.yesky.com/740x-/uploadImages/2017/048/05/5H81C176IYWE_800x1200.jpg"
]

register = template.Library()


@register.simple_tag(name="image")
def get_image_url(image_id):
    """
    根据imageid 返回url
    在内容没有传云端时，先采取随机返回image的方式
    :param image_id: 
    :return: 
    """
    url = "http://beauty07.b0.upaiyun.com/{image_id}".format(image_id=image_id)
    return url

@register.simple_tag(name="thumb")
def get_thumb_url(image_id):
    """
    根据imageid 返回url
    在内容没有传云端时，先采取随机返回image的方式
    :param image_id: 
    :return: 
    """
    url = "http://beauty07.b0.upaiyun.com/{image_id}!home".format(image_id=image_id)
    return url


@register.simple_tag(name="time")
def time_format(t):
    return datetime.datetime.fromtimestamp(int(t)).strftime('%Y-%m-%d')
