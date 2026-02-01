
import unittest
import shutil
import tempfile
from pathlib import Path
import os
import sys

# 確保可以導入 core_lib (假設從根目錄執行)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from core_lib.utils.files import ensure_dir_exists, batch_create_dirs, batch_move_files, list_directory_tree

class TestCoreUtils(unittest.TestCase):
    """測試 core_lib.utils.files 中的工具函數"""

    def setUp(self):
        # 建立臨時目錄進行測試
        self.test_dir = Path(tempfile.mkdtemp())
        
    def tearDown(self):
        # 測試結束後清理臨時目錄
        shutil.rmtree(self.test_dir)
        
    def test_ensure_dir_exists(self):
        """測試目錄確保存在功能"""
        target = self.test_dir / "new_subdir"
        ensure_dir_exists(target)
        self.assertTrue(target.exists())
        self.assertTrue(target.is_dir())
        
    def test_batch_create_dirs(self):
        """測試批量創建目錄功能"""
        dirs = ['sub1', 'sub2/nested']
        batch_create_dirs(dirs, self.test_dir)
        self.assertTrue((self.test_dir / 'sub1').exists())
        self.assertTrue((self.test_dir / 'sub2' / 'nested').exists())
        
    def test_batch_move_files(self):
        """測試批量移動檔案功能"""
        # 設置測試環境
        src_file = self.test_dir / 'source.txt'
        src_file.write_text('hello world')
        dest_filename = 'moved.txt'
        
        # 執行移動
        batch_move_files([('source.txt', dest_filename)], self.test_dir)
        
        # 驗證
        self.assertFalse(src_file.exists())
        self.assertTrue((self.test_dir / dest_filename).exists())
        self.assertEqual((self.test_dir / dest_filename).read_text(), 'hello world')
        
    def test_list_directory_tree(self):
        """測試目錄樹列出功能"""
        # 建立一些結構
        (self.test_dir / 'f1.txt').touch()
        (self.test_dir / 'dir1').mkdir()
        (self.test_dir / 'dir1' / 'f2.txt').touch()
        
        # 執行並檢查輸出
        tree_output = list_directory_tree(self.test_dir)
        self.assertIn('f1.txt', tree_output)
        self.assertIn('dir1', tree_output)
        self.assertIn('f2.txt', tree_output)

if __name__ == '__main__':
    unittest.main()
