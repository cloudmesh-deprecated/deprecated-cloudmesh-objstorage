###############################################################
<<<<<<< HEAD
# pip install .; pytest -v --capture=no -v --nocapture tests/test_objstorage_installer.py:Test_objstorage_installer.test_001
=======
>>>>>>> cb1529aa1c9c3f2d9c849e9b31adc72174d780ea
# pytest -v --capture=no tests/test_objstorage_installer.py
# pytest -v  tests/test_installer.py
###############################################################

from __future__ import print_function
import shutil

import os
import pytest
from cloudmesh_installer.install.test import readfile, run


<<<<<<< HEAD

=======
>>>>>>> cb1529aa1c9c3f2d9c849e9b31adc72174d780ea
@pytest.mark.incremental
class Test_objstorage_installer:

    def test_create_dir(self):
        path = "tmp"
        try:
            os.mkdir(path)
        except OSError:
            print(f"Creation of the directory {path} failed")
        else:
            print(f"Successfully created the directory {path}")

        assert True

    def test_info(self):
        cmd = "cloudmesh-installer info"
        result = run(cmd)
        print(result)
        assert "Package" in str(result)

    def test_clone_cloud(self):
        cmd = "cd tmp; cloudmesh-installer git clone storage"
        result = run(cmd)
        print(result)
        assert os.path.isdir("tmp/cloudmesh-cmd5")

    def test_install_cms(self):
        cmd = "cd tmp; cloudmesh-installer install objstorage-e"
        result = run(cmd)
        print(result)
        assert os.path.isdir("tmp/cloudmesh-cmd5/cloudmesh_cmd5.egg-info")
        assert os.path.isdir("tmp/cloudmesh-cloud/cloudmesh_cloud.egg-info")
<<<<<<< HEAD
        assert os.path.isdir("tmp/cloudmesh-objstorage/cloudmesh_objstorage.egg-info")
=======
        assert os.path.isdir(
            "tmp/cloudmesh-objstorage/cloudmesh_objstorage.egg-info")
>>>>>>> cb1529aa1c9c3f2d9c849e9b31adc72174d780ea

    def test_cms_help(self):
        cmd = "cms help"
        result = run(cmd)
        print(result)
        assert "quit" in result
        assert "objstorage" in result
        assert "vm" in result

    def test_cms_info(self):
        cmd = "cms info"
        result = run(cmd)
        print(result)
        assert "cloudmesh.common" in result
        assert "cloudmesh.cloud" in result
        assert "cloudmesh.objstorage" in result

    def test_cms_version(self):
        cmd = "cms version"
        result = run(cmd)
        print(result)
        assert "cloudmesh.common" in result
        assert "cloudmesh.cloud" in result
        assert "cloudmesh.objstorage" in result


<<<<<<< HEAD


=======
>>>>>>> cb1529aa1c9c3f2d9c849e9b31adc72174d780ea
class other:
    def test_delete_dir(self):
        path = "tmp"
        shutil.rmtree(path)
        assert True
