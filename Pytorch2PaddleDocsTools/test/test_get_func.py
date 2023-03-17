import unittest

import requests

from Pytorch2PaddleDocsTools import utils

class GetFuncTestCase(unittest.TestCase):
    def test_get_torch_func(self):
        torch_url = "https://pytorch.org/docs/1.13/generated/torch.abs.html?highlight=abs#torch.abs"
        torch_page = requests.get(torch_url).text
        torch_func = utils.get_torch_func(torch_page)
        torch_abs_func = '''torch.abs(input,*,out=None)'''
        self.assertEqual(torch_func, torch_abs_func)

    def test_get_paddle_func(self):
        paddle_url = "https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/abs_cn.html#abs"
        paddle_page = requests.get(paddle_url).text
        paddle_func = utils.get_paddle_func(paddle_page)
        paddle_abs_func = '''paddle.abs(x,name=None)'''
        self.assertEqual(paddle_func, paddle_abs_func)


if __name__ == '__main__':
    unittest.main()
