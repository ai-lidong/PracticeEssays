# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2019-08-06 16:33
# @Author  : lidong@immusician.com
# @Site    :
# @File    : abtesting.py
import ujson
from UnitTest.base import BaseRequest


class ABTestingTest(BaseRequest):
    def __init__(self):
        super().__init__()

    # def upload_event_data(self):
    #     data = {"data": [
    #         {
    #             "event_id": "5d494b8e191e7529d62b4add",
    #             "uid": 1,
    #             "create_time": 10,
    #             "item_id": '1',
    #             "item_type": 1
    #         },
    #         {
    #             "event_id": "5d494b8e191e7529d62b4add",
    #             "uid": 1,
    #             "create_time": 100,
    #             "item_id": '1',
    #             "item_type": 1
    #         },
    #         {
    #             "event_id": "5d494b8e191e7529d62b4ae1",
    #             "uid": 1,
    #             "create_time": 10,
    #             "item_id": '1',
    #             "item_type": 1,
    #             "duration": 1000
    #         },
    #     ]}
    #     # data = {"data": "a"}
    #     url = "/v1/upload/event/info"
    #     ret = self.get(url, json=data)
    #     return url, ret

    def get_all_event(self):
        url = "/v1/get/event"
        ret = self.get(url)
        return url, ret

    def get_course(self):
        url = "/v1/get_course"
        ret = self.get(url)
        self._show_data("get_course", url, ret)

    def create_course(self):
        url = "/v1/create_course"
        ret = self.post(url, json={"course_id": 14, "course_name": "未命名"})
        self._show_data("create_course", url, ret)

    def create_project(self):
        data = {
            "has_ratio": 0,
            "name": "完课率",
            "course_id": 120,
            "ratio_indicator_list": ujson.dumps([
                {
                    "dividend_id": 2,
                    "indicator_id": "5d41473b191e75ebb226bd23",
                    "divisor_id": 1
                }
            ]),
            "indicator_select_args_dict": ujson.dumps({
                "1": {
                    "course_id": 120,
                    "indicator_id": "5d41473b191e75ebb226bd22",
                    "completed": False,
                    "user_group": 5
                },
                "2": {
                    "course_id": 120,
                    "indicator_id": "5d41473b191e75ebb226bd22",
                    "completed": 1,
                    "user_group": 5
                }
            }),

            "course_name": "好玩的非洲鼓"
        }
        data2 = {
            "ratio_indicator_list": ujson.dumps([
                {
                    "dividend_id": 1,
                    "indicator_id": "5d41473b191e75ebb226bd23",
                    "divisor_id": 2
                }
            ]),
            "indicator_select_args_dict": ujson.dumps({
                "1": {
                    "course_id": 19,
                    "indicator_id": "5d414da8191e75edaf07adbc",
                    "user_group": 9
                },
                "2": {
                    "indicator_id": "5d414da8191e75edaf07adbd"
                }
            }),
            "name": "购课率",
            "course_id": 120,
            "has_ratio": 0
        }
        url = "/v1/create_project"
        ret = self.post(url, json=data)
        self._show_data("create_project", url, ret)

    def get_all_indicator(self):
        url = "/v1/get_all_indicator"
        ret = self.get(url)
        self._show_data("get_all_indicator", url, ret)

    def get_project_data(self):
        url = "/v1/get_project_data"
        ret = self.post(url, json={"project_id": "5d414f5b191e75ee50919d7b"})
        self._show_data("get_project_data", url, ret)


if __name__ == '__main__':
    # ABTestingTest().run()
    # ABTestingTest().get_all_indicator()
    # ABTestingTest().get_course()
    # ABTestingTest().create_course()
    ABTestingTest().create_project()
    # ABTestingTest().get_project_data()
