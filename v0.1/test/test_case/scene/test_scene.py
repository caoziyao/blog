# coding:utf-8
import os
import json
import logging
import base64, requests, time
import unittest
from test_case.base import Base
from pyquery import PyQuery as pq
from test.config.config import path_test_data, host
from test_case.base_vars import vars
from share.request_headers import headers
from functools import wraps

logger = logging.getLogger('testlog')  # 获取dblog的日志配置


class TestScene(Base):
    def __init__(self, *args, **kwargs):
        super(TestScene, self).__init__(*args, **kwargs)

    def data(self):
        """
        todo
        测试数据
        :return:
        """
        pass

    def test_struct_view(self):
        """
        加载场景结构
        请求参数
        node_id
        返回参数
        {
          "status": 1,
          "msg": "success",
          "data": {
            "1": {
                "Name": "",  // 节点名称
                  "level": 1,  // 层次
                  "ProjectId": 1,  // 项目id
                  "RelateEffectIdList": // 被关联场景id
                  "chlid": []  // 子节点列表
            }
        }
        """
        api = '/scenewordview/api/struct_view'
        args = '?node_id=1'
        url = host + api + args
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_struct_view.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '加载场景结构.txt',
            'api': api,
            'method': 'get',
            'req': args,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_latest_scene_list(self):
        """
        加载场景最新关联数据
        请求参数:
        无
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": [
            {
              "Id":   // 被关联节点id
              "Name":  // 被关联节点名称
            },
          ],
          "result": 1
        }
        """
        api = '/scenewordview/api/latest_scene_list'
        url = host + api
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_latest_scene_list.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '加载场景最新关联数据.txt',
            'api': api,
            'method': 'get',
            'req': '',
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_check_import_scenes(self):
        """
        检测场景
        请求参数:
        无
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": {
          "del_json": [],  // 删除的被关联节点
          "new_json": [],  // 新增的被关联节点
            "latest_scene": [  // 全部被关联节点
                {
                  "Id":   // 被关联节点id
                  "Name":  // 被关联节点名称
                },
            ]
          },
          "result": 1
        }
        """
        api = '/scenewordview/api/check_import_scenes'
        url = host + api
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_check_import_scenes.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '检测场景.txt',
            'api': api,
            'method': 'get',
            'req': '',
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_all_import_scenes(self):
        """
        加载场景已经导入的数据
        请求参数:
        无
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": [
            {
              "Id":   // 被关联节点id
              "Name":  // 被关联节点名称
            },
          ],
          "result": 1
        }
        """
        api = '/scenewordview/api/all_import_scenes'
        url = host + api
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_all_import_scenes.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '加载场景已经导入的数据.txt',
            'api': api,
            'method': 'get',
            'req': '',
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_related_scene(self):
        """
        加载场景已关联的数据
        请求参数:
        node_id: int 必须 // 节点Id
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": [
            {
              "Id":   // 被关联节点id
              "Name":  // 被关联节点名称
            },
          ],
          "result": 1
        }
        """
        api = '/scenewordview/api/related_scene'
        args = '?node_id=2'
        url = host + api + args
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_related_scene.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '加载场景已关联的数据.txt',
            'api': api,
            'method': 'get',
            'req': args,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_update_path(self):
        """
        更新图片地址
        请求参数：
        {
          "path": str 必须 // 图片地址
          "node_id": int 必须 // 节点Id
        }
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": {
            "Name": ,
            "level": 2,
            "ProjectId": 1,
            "RelateEffectIdList": // 被关联节点id列表
            "PicUrl": // 图片地址
            "Path": "/1/2",
            "Id": 2
          },
          "result": 1
        }
        """
        data = vars.payload
        api = '/scenewordview/api/update_path'
        url = host + api
        d = {
            'node_id': 2,
            'path': 'media/word_view/struct/20171106/7b17f803-1b4c-4868-9a9a-1473c4c820de.png'
        }

        data.update(d)
        r = vars.session.post(url, data=json.dumps(d))
        docstring = self.format_doc(self.test_update_path.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        d = json.dumps(d, indent=2)

        res = {
            'filename': '更新图片地址.txt',
            'api': api,
            'method': 'post',
            'req': d,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_edit_node(self):
        """
        测试编辑节点， 编辑子节点, node_id 不存在则新增
        请求参数：
        {
          "parent_id": int 必须 // 父亲节点id
          "node_id": int 必须 // 节点id
          "name": str 必须 // 节点名称
        }
        返回参数：
            {
          "status": 1,
          "msg": "success",
          "data": {
            "Name": ,
            "level": 2,
            "ProjectId": 1,
            "RelateEffectIdList": // 被关联节点id列表
            "PicUrl": // 图片地址
            "Path": "/1/2",
            "Id": 2
          },
          "result": 1
        }
        """
        data = vars.payload
        api = '/scenewordview/api/edit_node'
        url = host + api
        d = {
            'node_id': 2,
            'parent_id': 1,
            'name': '深圳的'
        }

        data.update(d)
        r = vars.session.post(url, data=json.dumps(d))
        docstring = self.format_doc(self.test_edit_node.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        format_d = json.dumps(d, indent=2, ensure_ascii=False)

        res = {
            'filename': '编辑子节点.txt',
            'api': api,
            'method': 'post',
            'req': format_d,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_directly_chlid_node(self):
        """
        测试查找节点直属子节点
        请求参数：
        node_id: int 必须 // 节点id
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": [
            {
              "Id":    int // 子节点id
              "Name":   str // 子节点名称
            }
          ],
          "result": 1
        }
        """
        api = '/scenewordview/api/directly_chlid_node'
        args = '?node_id=2'
        url = host + api + args
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_directly_chlid_node.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '查找节点直属子节点.txt',
            'api': api,
            'method': 'get',
            'req': args,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_update_coordinate(self):
        """
        更新字节点座标
        请求参数：
        {
          "chlid_id": int 必须 // 子节点id,
          "node_id": int 必须 // 节点id
          "x": int 必须// x 座标
          "y": int 必须// y 座标
        }
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": [
            {
              "WorldViewCId": // 即 chlid_id
              "WorldViewId": // 即 node_id
              "PictureCoordinate": "100,14"  // 座标点 (x,y)
            }
          ],
          "result": 1
        }
        """
        data = vars.payload
        api = '/scenewordview/api/update_coordinate'
        url = host + api
        d = {
            'node_id': 2,
            'chlid_id': 3,
            'x': 100,
            'y': 14,
        }

        data.update(d)
        r = vars.session.post(url, data=json.dumps(d))
        docstring = self.format_doc(self.test_update_coordinate.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        format_d = json.dumps(d, indent=2, ensure_ascii=False)

        res = {
            'filename': '更新字节点座标.txt',
            'api': api,
            'method': 'post',
            'req': format_d,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200

    def test_add_related_scene(self):
        """
        添加关联场景
        请求参数：
        {
          "relate_id": // 被关联的场景id,
          "node_id": //节点id
        }
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": {
            "Name":
            "level":
            "ProjectId":
            "RelateEffectIdList": // 被关联的场景id列表,
            "PicUrl":
            "Path":
            "Id":
          },
          "result": 1
        }
        """
        data = vars.payload
        api = '/scenewordview/api/add_related_scene'
        url = host + api
        d = {
            'node_id': 2,
            'relate_id': 12,
        }

        data.update(d)
        r = vars.session.post(url, data=json.dumps(d))
        docstring = self.format_doc(self.test_add_related_scene.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        d = json.dumps(d, indent=2)

        res = {
            'filename': '添加关联场景.txt',
            'api': api,
            'method': 'post',
            'req': d,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200


    def test_load_map(self):
        """
        加载地图地址
        请求参数：
        node_id:  int //节点Id 必须
        返回参数：
        {
          "status": 1,
          "msg": "success",
          "data": {
            "path": str //文件路径
          },
          "result": 1
        }
        """
        api = '/scenewordview/api/load_map'
        args = '?node_id=2'
        url = host + api + args
        r = vars.session.get(url)
        docstring = self.format_doc(self.test_load_map.__doc__.strip())

        content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
        res = {
            'filename': '加载图片.txt',
            'api': api,
            'method': 'get',
            'req': args,
            'response': content,
            'folder': 'scene',
            'rewrite': False,
            'remark': docstring,
        }
        self.output_text(**res)
        assert r.status_code == 200
