from .bar_chart import BarChart


#
# Esta classe foi elaborada para um único grupo de informações
#
class MultiInfoBarChart(BarChart):

    def __init__(self):
        super().__init__()
        self.colors = []
        self.set_inter_group_width_units(10)

    def set_colors(self, colors):
        self.colors = colors

    def set_inter_group_width_units(self, inter_group_width_units):
        self.inter_group_width_units = inter_group_width_units

    def is_valid(self):
        state_valid = False

        if len(self.dados) > 0:
            first_group = self.dados[0]

            if type(first_group) in [list]:
                if len(first_group) > 0:
                    first_item = first_group[0]

                    if type(first_item) in [int or float]:
                        state_valid = True

        return state_valid

    def get_errors(self):
        errors = []

        if len(self.dados) != len(self.colors):
            errors.append('Dimensão do array de dados incompatível')

        return errors

    def get_qtd_units_group(self):
        qtd_bars = len(self.dados[0])
        bar_units = self.bar_width_units
        inter_bar_units = self.inter_bar_width_units
        qtd_units_group = ((bar_units * qtd_bars) +
                (inter_bar_units * (qtd_bars - 1)))
        return qtd_units_group

    #
    # Para este cálculo leva-se em consideração que haverá uma distância
    # equivalente à metade da largura da coluna entre o início da coluna
    # e o início do eixo dos x e que também haverá uma distância similar
    # entre o final da coluna e o final do eixo dos x, ou seja, deverá
    # ser adicionado ao cálculo o equivalente à largura de uma coluna.
    #
    # Cada grupo de colunas ocupará o espaço do número de colunas adicionado
    # ao número de espaços entre elas.
    #
    def get_unit_width(self):
        bar_units = self.bar_width_units
        inter_bar_units = self.inter_bar_width_units
        inter_group_units = self.inter_group_width_units

        qtd_groups = len(self.dados)
        qtd_bars = len(self.dados[0])

        qtd_units_group = ((bar_units * qtd_bars) +
                (inter_bar_units * (qtd_bars - 1)))
        qtd_units_total = ((qtd_units_group * qtd_groups) + bar_units +
                (inter_group_units * (qtd_groups - 1)))

        unit_width = self.axis_width / qtd_units_total
        return unit_width

    #
    # Para este cálculo leva-se em consideração uma margem de 10%
    # de espaço acima da maior columna para fins de título e
    # informações sobre o valor
    #
    def get_unit_height(self):
        aux = [dado for dado in self.dados[0]]

        for aux2 in self.dados[1:]:
            aux += aux2

        max_value = max(aux)
        unit_height = self.axis_height * 0.9 / max_value
        return unit_height

    #
    # <g class="bar">
    #     <rect x="0" y="315" width="20" height="10"></rect>
    # </g>
    #
    def get_svg_bars(self):
        print('#get_svg_bars - len(self.dados): {}'.format(len(self.dados)))
        unit_width = self.get_unit_width()
        unit_height = self.get_unit_height()
        initial_x_offset = self.bar_width_units / 2 * unit_width
        column_width = unit_width * self.bar_width_units
        space_width = unit_width * self.inter_bar_width_units
        svg_lines = ['<g class="bars" {}>'.format(
                self.get_translate_expression())]
        qtd_bars_in_group = len(self.dados[0])
        qtd_units_in_group = self.get_qtd_units_group()

        print('qtd_bars_in_group: {}'.format(qtd_bars_in_group))

        for i, grupo_dados in enumerate(self.dados):
            group_offset = i * (unit_width * (qtd_units_in_group +
                    self.inter_group_width_units))
            for j, dado in enumerate(grupo_dados):
                x = round(initial_x_offset + group_offset +
                        (j * (column_width + space_width)))
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
        repr += '\n\tcolors: {}'.format(self.colors)
        return repr
