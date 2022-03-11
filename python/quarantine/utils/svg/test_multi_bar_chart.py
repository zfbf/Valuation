import unittest
import pdb

from .multi_info_bar_chart import MultiInfoBarChart

class MultiBarChartTest(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.bar_chart = MultiInfoBarChart()
        self.bar_chart.set_dados([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        self.bar_chart.set_colors(['red', 'orangered', 'orange'])

    def test_set_axis(self):
        self.bar_chart.set_axis(width=1000, height=500)
        self.assertEqual(self.bar_chart.axis_width, 1000)
        self.assertEqual(self.bar_chart.axis_height, 500)

    def test_set_box_width(self):
        self.assertEqual(self.bar_chart.box_width, 1600)
        self.bar_chart.set_box_width(1000)
        self.assertEqual(self.bar_chart.box_width, 1000)

    def test_set_box_height(self):
        self.assertEqual(self.bar_chart.box_height, 900)
        self.bar_chart.set_box_height(600)
        self.assertEqual(self.bar_chart.box_height, 600)

    def test_set_colors(self):
        self.bar_chart.set_colors(['red', 'orangered', 'orange', 'blue'])
        self.assertEqual(len(self.bar_chart.colors), 4)

    def test_get_unit_width(self):
        unit_width = self.bar_chart.get_unit_width()
        self.assertTrue(unit_width > 0)

    def test_get_unit_height(self):
        unit_height = self.bar_chart.get_unit_height()
        self.assertTrue(unit_height > 0)
        print('unit_height: {}'.format(unit_height))

    def test_get_qtd_units_group(self):
        qtd_units_group = self.bar_chart.get_qtd_units_group()
        self.assertTrue(qtd_units_group > 0)
        print('qtd_units_group: {}'.format(qtd_units_group))

    def test_is_valid(self):
        #pdb.set_trace()
        self.assertTrue(self.bar_chart.is_valid())

    def test_get_svg_axis(self):
        #Todo: Testar Exception
        svg_axis = self.bar_chart.get_svg_axis()
        self.assertIsNotNone(svg_axis)

        if self.print_to_stdout:
            print('svg_axis: \n{}'.format(svg_axis))

    def test_to_svg(self):
        #Todo: Testar Exception
        svg = self.bar_chart.to_svg()
        self.assertIsNotNone(svg)

        if self.print_to_stdout:
            print(svg)

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.bar_chart)
