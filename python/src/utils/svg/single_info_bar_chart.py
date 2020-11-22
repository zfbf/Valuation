from .bar_chart import BarChart


#
# Esta classe foi inicialmente elaborada para barras verticais.
# Uma outra classe deverá ser desenvolvida para barras horizontais.
#
class SingleInfoBarChart(BarChart):

    def __init__(self):
        super().__init__()
        self.color = 'gray'

    def set_color(self, color):
        self.color = color

    def is_valid(self):
        state_valid = False

        if len(self.dados) > 0:
            if type(self.dados[0]) in [int or float]:
                state_valid = True
        else:
            state_valid = True

        return state_valid

    def get_errors(self):
        errors = []

        if len(self.dados) > 0:
            if not type(self.dados[0]) in [int or float]:
                errors.append('Tipo de dado incompatível')
        
        return errors

    #
    # Para este cálculo leva-se em consideração que haverá uma distância
    # equivalente à metade da largura da coluna entre o início da coluna
    # e o início do eixo dos x e que também haverá uma distância similar
    # entre o final da coluna e o final do eixo dos x.
    #
    def get_unit_width(self):
        qtd_bars = len(self.dados)
        qtd_units = (self.bar_width_units * (qtd_bars + 1) +
                self.inter_bar_width_units * (qtd_bars - 1))
        unit_width = self.axis_width / qtd_units
        return unit_width

    #
    # Para este cálculo leva-se em consideração uma margem de 10%
    # de espaço acima da maior columna para fins de título e
    # informações sobre o valor
    #
    def get_unit_height(self):
        max_value = max(self.dados)
        unit_height = self.axis_height * 0.9 / max_value
        return unit_height

    #
    # <g class="bar">
    #     <rect x="0" y="315" width="20" height="10"></rect>
    # </g>
    #
    def get_svg_bars(self):
        unit_width = self.get_unit_width()
        unit_height = self.get_unit_height()
        initial_x_offset = self.bar_width_units / 2 * unit_width
        column_width = unit_width * self.bar_width_units
        space_width = unit_width * self.inter_bar_width_units
        svg_lines = ['<g class="bars" fill="{}" {}>'.format(
                self.color, self.get_translate_expression())]

        for i, dado in enumerate(self.dados):
            x = round(initial_x_offset + (i * (column_width + space_width)))
            y = round(self.transform_to_plot_area(unit_height * dado))
            width = column_width
            height = round(unit_height * dado)
            svg_lines.append('<g class="bar">')
            svg_lines.append('\t<rect x="{}" y="{}" width="{}" height="{}"'.
                    format(x, y, width, height))
            svg_lines.append('<\g>')

        svg = '\n\t\t'.join(svg_lines)
        svg += '\n\t</g>'
        return svg

    def __str__(self):
        repr = super().__str__()
        repr += 'SingleInfoBarChart'
        repr += '\n\tcolor: {}'.format(self.color)
        return repr
