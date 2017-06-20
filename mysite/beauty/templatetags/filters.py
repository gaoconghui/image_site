# coding=utf-8 #coding:utf-8


from django import template

from beauty.view_counter import view_counter

register = template.Library()


@register.filter(name='calculate_page')
def calculate_page(current_page, total_page):
    """
    计算页码，-1为省略号
    :param current_page: 当前页
    :param total_page: 总页数
    :return:
    """
    if total_page <= 10:
        return range(1, total_page + 1)
    result = [1]
    if current_page > 5:
        result.append(-1)

    num_start = current_page - 3
    num_end = current_page + 3
    if num_start < 2:
        num_start = 2
        num_end = num_end - num_start + 2
    if num_end > total_page - 1:
        num_end = total_page - 1
        num_start -= num_end - total_page + 1
    result += range(num_start, num_end + 1)
    if current_page < total_page - 4:
        result.append(-1)
    result.append(total_page)
    return result

