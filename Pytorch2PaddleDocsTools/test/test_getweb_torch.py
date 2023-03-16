import requests
from bs4 import BeautifulSoup


def get_torch_func(url = "https://pytorch.org/docs/1.13/generated/torch.ones_like.html#torch.ones_like"
):
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


if __name__ == '__main__':
    function_torch = get_torch_func()
    print("解析的结果为:",function_torch)