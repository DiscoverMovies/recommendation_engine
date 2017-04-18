"""
    Copyright (C) 2017 Sidhin S Thomas

    This file is part of discovermovie.

    discovermovies is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    discovermovie is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with discovermovie.  If not, see <http://www.gnu.org/licenses/>.
"""

from collections import defaultdict


def partition(data, min_num):
    """
    This methods divides the entire list to a subset where the content have apears greater than a specified value.


    data contains the list of IDs
    min_num is the threshold used to partition it into sets.

    :param data: list
    :param min_num: integer
    :return: list
    """
    count = defaultdict(int)
    for i in data:
        count[i] += 1
    final_set = []
    for i in count.keys():
        if count[i] > min_num:
            final_set.append(i)
    return final_set


def min_max_normalize(data, min, max):
    r = []
    for i in data:
        value = i - min
        value = value / (max - min)
        r.append(value)
    return r
