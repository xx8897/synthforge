
import unittest
import sys
import os
from pathlib import Path

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

try:
    from devtools.structure_optimizer import StructureOptimizer
    IMPORT_SUCCESS = True
except ImportError as e:
    IMPORT_SUCCESS = False
    IMPORT_ERROR = str(e)

class TestOptimizerImport(unittest.TestCase):
    def test_import_success(self):
        """Test that structure_optimizer can be imported successfully"""
        if not IMPORT_SUCCESS:
            self.fail(f"Failed to import StructureOptimizer: {IMPORT_ERROR}")
        self.assertTrue(IMPORT_SUCCESS)

if __name__ == '__main__':
    unittest.main()
