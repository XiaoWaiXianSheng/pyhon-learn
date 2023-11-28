from typing import Union

my_list: list[Union[str, int]] = [1, 3, "itheima"]

my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 13}


def func(data: Union[int, str]) -> Union[int, str]:
    return data
