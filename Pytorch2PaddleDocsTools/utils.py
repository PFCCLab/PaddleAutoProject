import re
from bs4 import BeautifulSoup

def torch_html2dict(torch_page=""):
    torch_dict = {}
    torch_dict['torch_func'] = get_torch_func(torch_page)
    torch_dict['torch_example'] = get_torch_example(torch_page)
    torch_dict['torch_parames'] = get_func_param(torch_dict['torch_func'])
    return torch_dict

def paddle_html2dict(paddle_page=""):
    paddle_dict = {}
    paddle_dict['paddle_func'] = get_paddle_func(paddle_page)
    paddle_dict['paddle_example'] = get_paddle_example(paddle_page)
    paddle_dict['paddle_parames'] = get_func_param(paddle_dict['paddle_func'])
    return paddle_dict

def get_func_param(input_str):
    result = re.search("\((.*?)\)", input_str)
    if result:
        content = result.group(1)
    else:
        print("自动匹配参数填充表格失败",input_str)

    params = content.split(',')
    for number, i in enumerate(params):
        if '=' in i:
            params[number] = i.split('=')[0]

    return params

def get_torch_func(torch_page=""):
    soup = BeautifulSoup(torch_page, 'html.parser')

    function_name = ''

    for link in soup.find_all("span", attrs={"class": "sig-prename descclassname"}):
        function_name += link.string
    for link in soup.find_all("span", attrs={"class": "sig-name descname"}):
        function_name += link.string

    function_str = ''
    for link in soup.find_all("dt", attrs={"class": "sig sig-object py"}):
        for sub_link in link.find_all("em", attrs={"class": "sig-param"}):
            for sub_sub_link in sub_link.find_all("span", attrs={"class": "pre"}):
                function_str += sub_sub_link.string
            function_str += ','
    function_str = function_str[:len(function_str) - 1]

    function_torch = f'{function_name}({function_str})'
    return function_torch


def get_paddle_func(paddle_page=""):
    soup = BeautifulSoup(paddle_page, 'html.parser')

    for link in soup.find_all("dt", attrs={"class": "sig sig-object py"}):
        function_name = link.get('id')

    function_str = ''
    for link in soup.find_all("em", attrs={"class": "sig-param"}):
        for ll in link.find_all("span", attrs={"class": "pre"}):
            function_str += ll.string
        function_str += ','

    # 去除最后多余的','
    function_str = function_str[:len(function_str) - 1]
    function_paddle = f'{function_name}({function_str})'
    return function_paddle


def get_torch_example(torch_page=''):
    # 正则匹配内容
    example_content = str(re.findall(
        r'<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>(.*)</pre></div>',
        torch_page, re.DOTALL)[0])

    # 去除无用的标签
    example_content = example_content.replace('<span class="gp">', "").replace('<span class="n">', '').replace(
        '<span class="o">', '').replace('<span class="mi">', '').replace('<span class="p">', '').replace('</span>',
                                                                                                         '').replace(
        '<span class="go">', '')

    # 替换一些符号
    example_content = example_content.replace('&gt;&gt;&gt;', '>>>')

    return example_content


def get_paddle_example(paddle_page=''):
    # 正则匹配内容
    example_content = str(re.findall(
        r'<h2>代码示例<a class="headerlink" href="#daimashili" title="永久链接至标题">¶</a></h2>(.*)</pre>',
        paddle_page, re.DOTALL)[0])

    # 去除无用的标签
    example_content = example_content.replace('<span class="nn">', "").replace('<span class="n">', '').replace(
        '<span class="o">', '').replace('<span class="mi">', '').replace('<span class="p">', '').replace(
        '<div class="highlight-python notranslate">\n', '').replace('<div class="highlight">\n', '').replace(
        '<span class="kn">', '').replace('</span>', '').replace('<span class="go">', '').replace('<pre>', '').replace(
        '<span>', '').replace('<span class="nb">', '').replace('<span class="c1">', '').replace('<span class="mf">', '')\
        .replace('<span class="k">', '').replace('<span class="kc">', '')

    # 去除一些奇奇怪怪的空格
    example_content = example_content.replace('                           ', '')

    return example_content
