from abc import ABC, abstractmethod


class BarChart():
    def __init__(self):
        super().__init__()
        self.set_box_width(1600)
        self.set_box_height(900)
        self.set_dados([])
        self.set_bar_width_units(8)
        self.set_inter_bar_width_units(2)
        self.set_axis(1400, 600)
        self.set_offset(100, 100)

    def set_box_width(self, box_width):
        self.box_width = box_width

    def set_box_height(self, box_height):
        self.box_height = box_height

    def set_bar_width_units(self, bar_width_units):
        self.bar_width_units = bar_width_units

    def set_inter_bar_width_units(self, inter_bar_width_units):
        self.inter_bar_width_units = inter_bar_width_units

    @abstractmethod
    def get_unit_width(self):
        pass

    @abstractmethod
    def get_unit_height(self):
        pass

    def set_axis(self, width, height):
        self.axis_width = width
        self.axis_height = height

    def set_offset(self, x, y):
        self.offset = {
            'x': x,
            'y': y
        }

    def get_translate_expression(self):
        return 'transform="translate({}, {})"'.format(self.offset['x'],
                self.offset['y'])

    def set_dados(self, dados):
        self.dados = dados

    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def get_errors(self):
        pass

    def transform_to_plot_area(self, y):
        return self.axis_height - y

    def to_svg(self):
        if not self.is_valid():
            errors = self.get_errors()
            raise Exception(errors)

        svg = '\n\t'.join([
            '<g class="bars">',
            self.get_svg_axis(),
            '',
            self.get_svg_bars()
        ])
        svg += '\n</g>'
        return svg

    def get_svg_axis(self):
        x1 = 0
        x2 = self.axis_width
        y1 = 0
        y2 = self.axis_height
        svg_lines = [
            '<g class="eixos" style="stroke:darkslategray;stroke-width:2"',
            '\t' + self.get_translate_expression() + '>',
            '<g class="eixo">',
            '\t<line x1="{0}" x2="{1}" y1="{3}" y2="{3}"></line>',
            '</g>',
            '',
            '<g class="eixo">',
            '\t<line x1="{0}" x2="{0}" y1="{2}" y2="{3}"></line>',
            '</g>'
        ]

        svg = '\n\t'.join(svg_lines).format(x1, x2, y1, y2)
        svg += '\n</g>'
        return svg

    @abstractmethod
    def get_svg_bars(self):
        pass

    def __str__(self):
        repr = '\nBarChart'
        repr += '\n\tbox size: {} w x {} h'.format(self.box_width,
                self.box_height)
        repr += '\n\taxis_width: {}'.format(self.axis_width)
        repr += '\n\taxisx_height: {}'.format(self.axis_height)
        repr += '\n\tbar_width_units: {}'.format(self.bar_width_units)
        repr += '\n\tinter_bar_width_units: {}'.format(
                self.inter_bar_width_units)
        return repr
