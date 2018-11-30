#! /usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import os

from wx.tools.img2py import img2py

if __name__ == '__main__':
    _basePath = os.path.abspath(os.path.join(__file__, '../images'))

    # img2py(os.path.abspath(os.path.join(
    #     _basePath, 'robot-nothing.png')), os.path.abspath(os.path.join(_basePath, 'imageRobotNothing.py')))

    # img2py(os.path.abspath(os.path.join(
    #     _basePath, 'robot-text.png')), os.path.abspath(os.path.join(_basePath, 'imageRobotText.py')))

    img2py(os.path.abspath(os.path.join(
        _basePath, 'logo.png')), os.path.abspath(os.path.join(_basePath, 'logo.py')))
