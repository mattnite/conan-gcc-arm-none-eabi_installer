# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class TestPackageConan(ConanFile):

    def test(self):
        pass
        #if not tools.cross_building(self.settings):
           # self.run("some_tool --version")
