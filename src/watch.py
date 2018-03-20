#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明: 导入公共模块
import time
import os
import sys
from watchdog.events import FileSystemEventHandler
import shopcart
# 说明: 导入其它模块

assestpath = os.path.abspath(os.path.join(__file__, '../..'))  # 工程根目录
sys.path.insert(0, assestpath)


class CustomerHandler(FileSystemEventHandler):

    xlsx_path = os.path.abspath(os.path.join(
        __file__, '..', 'docs', '订单明细目录.xls'))
    is_modified = False

    def dispatch(self, event):
        if 'docs' in event.src_path and '订单明细目录.xls' in event.src_path:
            print('event', event)
            if self.is_modified == True:
                self.is_modified = False
                self.on_modified(event)
                pass
            elif hasattr(event, 'dest_path') and len(event.dest_path) > 0:
                self.is_modified = True
            pass

    # 新增
    def on_created(self, event):
        pass

    # 删除
    def on_deleted(self, event):
        pass

    # 修改
    def on_modified(self, event):
        shopcart.do_shopcart(self.xlsx_path)
        print('on_modified', self, event)
        pass

    # 移动
    def on_moved(self, event):
        pass


def start_watching(event_handler, path='.', recursive=True):
    from watchdog.observers import Observer
    watcher = Observer()
    watcher.schedule(event_handler, path, recursive)
    watcher.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()


if __name__ == '__main__':
    event_handler = CustomerHandler()
    start_watching(event_handler, '..')
