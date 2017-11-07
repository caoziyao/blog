# coding: utf-8

from .test_scene import TestScene


cases = [
    TestScene("test_load_map"),
    TestScene("test_struct_view"),
    TestScene("test_add_related_scene"),
    TestScene("test_update_path"),
    TestScene("test_edit_node"),
    TestScene("test_directly_chlid_node"),
    TestScene("test_update_coordinate"),
    TestScene("test_latest_scene_list"),
    TestScene("test_check_import_scenes"),
    TestScene("test_all_import_scenes"),
    TestScene("test_related_scene"),
    TestScene("test_struct_view"),
]

__all__ = [
    cases,
]

