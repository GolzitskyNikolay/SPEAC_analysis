import unittest

from Tests.speac_chapter_7_tests.chopin_33_3 import CHOPIN_33_3
from speac_chapter_7.pattern_match import *
from speacsettings import SpeacSettings

speac_settings = SpeacSettings()


class PatternMatchTest(unittest.TestCase):

    def test_all(self):
        self.test_my_count()
        self.test_get_ontimes_and_pitches()
        self.test_run_pattern_match()
        self.test_interval_translator()
        self.test_find_matchings()
        self.test_find_the_matches()
        self.test_simple_matcher()

    def test_my_count(self):
        self.assertEqual(True, pattern_match([2, 3], [1, 2], 1, speac_settings))
        self.assertEqual(False, pattern_match([3, 4], [1, 4], 1, speac_settings))

    def test_get_ontimes_and_pitches(self):
        events = [[0, 74, 1000, 1, 64], [0, 76, 1500, 1, 64], [1000, 74, 500, 1, 64], [3000, 72, 750, 1, 64]]
        result = [[0, 74], [0, 76], [1000, 74], [3000, 72]]
        self.assertEqual(result, get_ontimes_and_pitches(events))

    def test_run_pattern_match(self):
        pattern = [-2, -2]
        patterns = [-2, -2, -3, 2, 1, -1, 1, 0, 0, 0, 2, 3, 2, 2, -2, -2, -1, -2, 2,
                    3, 0, -3, 0, -2, 2, -7, 2, 1, 2, -3, -2, 2, 1, 2, 2, 1, 2, -2, -1]

        self.assertEqual(7, run_pattern_match(pattern, patterns, speac_settings))

    def test_interval_translator(self):
        self.assertEqual([2, 1, -62], interval_translator([60, 62, 63, 1]))

    def test_find_matchings(self):
        pattern = [[0, 74], [1000, 76]]
        patterns = [[0, 74], [1000, 76], [0, 74], [-1, -2]]
        result = 1
        self.assertEqual(result, find_matchings(pattern, patterns, speac_settings))

    def test_find_the_matches(self):
        speac_settings.set_pattern_size(2)
        work_1 = [[0, 74], [1000, 76], [2500, 74], [3000, 72], [3750, 71], [4000, 72], [5500, 73]]
        work_2 = [[0, 74], [1000, 76], [2500, 74], [3000, 72], [3750, 71], [4000, 72], [5500, 73]]
        result = [[3, 0, [2]], [3, 2500, [-2]], [3, 3750, [1]]]
        self.assertEqual(result, find_the_matches(work_1, work_2, speac_settings))

        work_1 = [[0, 74], [1000, 76], [2500, 74], [3000, 72], [3750, 71], [4000, 72], [5500, 73], [6000, 74],
                  [6750, 75], [7000, 76], [8500, 74], [9000, 72], [9750, 71], [10000, 72], [12000, 71], [13000, 72],
                  [14500, 71], [15000, 69], [15750, 68], [16000, 69], [17500, 71], [18000, 72], [18750, 73],
                  [19000, 76], [20500, 74], [21000, 73], [21750, 74], [22000, 79], [24000, 74], [25000, 76],
                  [26500, 74], [27000, 72], [27750, 71], [28000, 72], [29500, 73], [30000, 74], [30750, 75],
                  [31000, 76], [32500, 74], [33000, 72], [33750, 71], [34000, 72], [36000, 69], [37000, 71],
                  [38500, 69], [39000, 67], [39750, 66], [40000, 67], [41500, 69], [42000, 71], [42750, 72],
                  [43000, 76], [44500, 74], [45000, 71], [45750, 72], [46000, 84], [47000, 72], [48000, 76],
                  [48500, 74], [49000, 72], [50000, 68], [51000, 66], [51500, 67], [52000, 71], [53000, 72],
                  [54000, 73], [54500, 74], [55000, 76], [56000, 77], [57000, 78], [59000, 79], [60500, 80],
                  [61000, 81], [62500, 79], [63000, 77], [63500, 76], [64000, 77], [65500, 76], [66000, 75],
                  [66500, 76], [67000, 77], [68500, 76], [69000, 74], [69500, 72], [70000, 74], [71000, 72],
                  [72000, 76], [72500, 77], [73000, 69], [74000, 71], [75000, 66], [75500, 67], [76000, 71],
                  [77000, 72], [78000, 73], [78500, 74], [79000, 76], [80000, 77], [81000, 78], [83000, 79],
                  [84500, 80], [85000, 81], [86500, 79], [87000, 77], [87500, 76], [88000, 77], [89000, 76],
                  [90000, 75], [90500, 76], [91000, 77], [92500, 76], [93000, 74], [93500, 72], [94000, 74],
                  [95500, 72], [96000, 74], [97000, 76], [98500, 74], [99000, 72], [99750, 71], [100000, 72],
                  [101500, 73], [102000, 74], [102750, 75], [103000, 76], [104500, 74], [105000, 72], [105750, 71],
                  [106000, 72], [108000, 71], [109000, 72], [110500, 71], [111000, 69], [111750, 68], [112000, 69],
                  [113500, 71], [114000, 72], [114750, 73], [115000, 76], [116500, 74], [117000, 73], [117750, 74],
                  [118000, 79], [120000, 74], [121000, 76], [122500, 74], [123000, 72], [123750, 71], [124000, 72],
                  [125500, 73], [126000, 74], [126750, 75], [127000, 76], [128500, 74], [129000, 72], [129750, 71],
                  [130000, 72], [132000, 69], [133000, 71], [134500, 69], [135000, 67], [135750, 66], [136000, 67],
                  [137500, 69], [138000, 71], [138750, 72], [139000, 76], [140500, 74], [141000, 71], [141750, 72],
                  [142000, 84], [143000, 67]]
        work_2 = copy.deepcopy(work_1)

        speac_settings.set_pattern_size(12)
        result = [[4, 0, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]],
                  [4, 24000, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]],
                  [4, 96000, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]],
                  [4, 120000, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]]]
        self.assertEqual(result, find_the_matches(work_1, work_2, speac_settings))

    def test_simple_matcher(self):
        events = CHOPIN_33_3
        speac_settings.set_pattern_size(2)
        result = [[85, 0, [2]], [69, 2500, [-2]], [83, 3750, [1]], [83, 5500, [1]], [83, 6750, [1]], [69, 8500, [-2]],
                  [83, 9750, [1]], [83, 12000, [1]], [69, 14500, [-2]], [83, 15750, [1]], [83, 17500, [1]],
                  [26, 18750, [3]], [65, 20500, [-1]], [8, 21750, [5]], [85, 24000, [2]], [69, 26500, [-2]],
                  [83, 27750, [1]], [83, 29500, [1]], [83, 30750, [1]], [69, 32500, [-2]], [83, 33750, [1]],
                  [85, 36000, [2]], [69, 38500, [-2]], [83, 39750, [1]], [85, 41500, [2]], [10, 42750, [4]],
                  [44, 44500, [-3]], [10, 47000, [4]], [69, 48500, [-2]], [69, 50000, [-2]], [10, 51500, [4]],
                  [83, 53000, [1]], [85, 54500, [2]], [83, 56000, [1]], [83, 59000, [1]], [69, 61000, [-2]],
                  [65, 63000, [-1]], [65, 64000, [-1]], [83, 66000, [1]], [65, 67000, [-1]], [69, 69000, [-2]],
                  [69, 70000, [-2]], [83, 72000, [1]], [85, 73000, [2]], [83, 75000, [1]], [83, 76000, [1]],
                  [83, 78000, [1]], [83, 79000, [1]], [83, 81000, [1]], [83, 84500, [1]], [69, 86500, [-2]],
                  [83, 87500, [1]], [65, 89000, [-1]], [83, 90500, [1]], [69, 92500, [-2]], [85, 93500, [2]],
                  [85, 95500, [2]], [69, 97000, [-2]], [65, 99000, [-1]], [83, 100000, [1]], [83, 102000, [1]],
                  [69, 103000, [-2]], [65, 105000, [-1]], [65, 106000, [-1]], [65, 109000, [-1]], [65, 111000, [-1]],
                  [85, 112000, [2]], [83, 114000, [1]], [69, 115000, [-2]], [83, 117000, [1]], [4, 118000, [-5]],
                  [69, 121000, [-2]], [65, 123000, [-1]], [83, 124000, [1]], [83, 126000, [1]], [69, 127000, [-2]],
                  [65, 129000, [-1]], [44, 130000, [-3]], [69, 133000, [-2]], [65, 135000, [-1]], [85, 136000, [2]],
                  [83, 138000, [1]], [69, 139000, [-2]], [83, 141000, [1]]]
        self.assertEqual(result, simple_matcher(events, speac_settings))

        speac_settings.set_pattern_size(12)
        result = [[4, 0, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]],
                  [4, 24000, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]],
                  [4, 96000, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]],
                  [4, 120000, [2, -2, -2, -1, 1, 1, 1, 1, 1, -2, -2]]]
        self.assertEqual(result, simple_matcher(CHOPIN_33_3, speac_settings))
