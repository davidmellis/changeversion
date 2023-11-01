import sys
import unittest
sys.path.append("/mnt/c/Users/dellis/workspace/changeversion/src")
sys.path.append("/mnt/c/Users/dellis/workspace/changeversion/tests")
from changeversion.versh import VersionHolder

class TestVersionHolder(unittest.TestCase):
    def test_reps_correct_string(self):
        vh = VersionHolder("0.0.1")
        assert "0.0.1" == vh.rep()

    def test_bumps_correct_number(self):
        print(sys.path)
        vh = VersionHolder("0.0.1").bump('minor')
        assert "0.1.1" == vh.rep()

    def test_bumps_correct_number_major(self):
        print(sys.path)
        vh = VersionHolder("0.0.1").bump('major')
        assert "1.0.1" == vh.rep()

    def test_bumps_correct_number_major(self):
        print(sys.path)
        vh = VersionHolder("0.0.1").bump('micro')
        assert "0.0.2" == vh.rep()

    def test_sets_correct_part(self):
        print(sys.path)
        vh = VersionHolder("0.0.1").set('micro', '999')
        assert "0.0.999" == vh.rep()


if __name__ == '__main__':
    unittest.main()
