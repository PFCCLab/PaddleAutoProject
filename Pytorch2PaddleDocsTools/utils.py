import requests
from bs4 import BeautifulSoup

def get_torch_func(url = "https://pytorch.org/docs/1.13/generated/torch.ones_like.html#torch.ones_like"
):
    if 'pytorch' not in url:
        print("输入pytorch网址错误，请重新输入！")

    torch_page = requests.get(url).text

    soup = BeautifulSoup(torch_page, 'html.parser')

    function_name=''

    for link in soup.find_all("span", attrs={"class" :"sig-prename descclassname"}):
        function_name+=link.string
    for link in soup.find_all("span", attrs={"class" :"sig-name descname"}):
        function_name+=link.string

    function_str = ''
    for link in soup.find_all("dt", attrs={"class" :"sig sig-object py"}):
        for sub_link in link.find_all("em", attrs={"class" :"sig-param"}):
            for sub_sub_link in sub_link.find_all("span", attrs={"class" :"pre"}):
                function_str+=sub_sub_link.string
            function_str+=','
    function_str = function_str[:len(function_str)-1]

    function_torch = f'{function_name}({function_str})'
    return function_torch

def get_paddle_func(url = "https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/amax_cn.html"
):
    if 'paddlepaddle' not in url:
        print("输入paddlepaddle网址错误，请重新输入！")

    paddle_page = requests.get(url).text
    soup = BeautifulSoup(paddle_page, 'html.parser')

    for link in soup.find_all("dt", attrs={"class" :"sig sig-object py"}):
        function_name = link.get('id')

    function_str = ''
    for link in soup.find_all("em", attrs={"class" :"sig-param"}):
        for ll in link.find_all("span", attrs={"class" :"pre"}):
            function_str+=ll.string
        function_str+=','

    # 去除最后多余的','
    function_str = function_str[:len(function_str)-1]
    function_paddle = f'{function_name}({function_str})'
    return function_paddle
