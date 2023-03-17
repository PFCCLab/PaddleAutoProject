import unittest

import requests

from Pytorch2PaddleDocsTools import utils


class GetExampleTestCase(unittest.TestCase):
    def test_get_torch_example(self):
        torch_url = "https://pytorch.org/docs/1.13/generated/torch.abs.html?highlight=abs#torch.abs"
        torch_page = requests.get(torch_url).text
        torch_example = utils.get_torch_example(torch_page)
        torch_abs_page = '''>>> torch.abs(torch.tensor([-1, -2, 3]))
tensor([ 1,  2,  3])
'''
        self.assertEqual(torch_abs_page, torch_example)

    def test_get_paddle_example(self):
        paddle_url = "https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/abs_cn.html#abs"
        paddle_page = requests.get(paddle_url).text
        paddle_example = utils.get_paddle_example(paddle_page)
        paddle_abs_page = ''' 
import paddle

x = paddle.to_tensor([-0.4, -0.2, 0.1, 0.3])
out = paddle.abs(x)
print(out)
# [0.4 0.2 0.1 0.3]
'''
        self.assertEqual(paddle_abs_page, paddle_example)


if __name__ == '__main__':
    unittest.main()
