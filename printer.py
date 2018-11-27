#=================== ABOUT ===================#
# python-table-printer/printer.py
# A python table printer for a given dataset
# Author: Martín Figueroa Padilla
# Version = 1.0.0
#=============================================#

class TablePrinter:
    def __init__(self):
        self.__dataset = []
        self.__header = []

    def add_row(self, row=[], times=1):
        if isinstance(row, list):
            for i in range(times):
                self.__dataset.append(row)

    def set_dataset(self, dataset, ignore_keys=[]):
        if isinstance(dataset, list):
            if isinstance(dataset[0], dict):
                self.__dataset = []
                for row in dataset:
                    temp = []
                    for key in row.keys():
                        if key not in ignore_keys:
                            temp.append(row[key])
                    self.__dataset.append(temp)
            else:
                self.__dataset = dataset

    def set_header(self, header):
        if isinstance(header, list):
            self.__header = header

    def print(self, show_header=True, header_upper=True, cell_padding=0, cell_min_width=0, row_border=False, auto_id=False):
        # Initial setup
        if len(self.__header) == 0:
            show_header = False
        dataset = self.__dataset.copy()
        header = self.__header.copy() if not header_upper else [text.upper() for text in self.__header]
        header = header if not auto_id else ['ID'] + header

        # Calculate table columns
        cols = 0 if not show_header else len(header)
        for row in dataset:
            if len(row) > cols:
                cols = len(row)
        if auto_id and not show_header: cols += 1

        # Standarize columns on every row and header
        if show_header and len(header) < cols:
            header = header + [''] * (cols - len(header))
        row_id = 1
        for i in range(0, len(dataset)):
            if auto_id:
                dataset[i] = [row_id] + dataset[i]
                row_id += 1
            if len(dataset[i]) < cols:
                dataset[i] = dataset[i] + [''] * (cols - len(dataset[i]))

        # Calculate columns widths
        cols_width = [0] * cols if not show_header else [len(text) for text in header]
        for row in dataset:
            for i in range(0, cols):
                if len(str(row[i])) > cols_width[i]:
                    cols_width[i] = len(str(row[i]))
                if cols_width[i] < cell_min_width:
                    cols_width[i] = cell_min_width

        # Print header of table
        if show_header:
            header_repr = ''
            header_div = ''
            for i in range(0, len(header)):
                text = header[i]
                space = cols_width[i] - len(text)
                header_repr += '%s%s%s%s%s' \
                    %(' ' * cell_padding, text, ' ' * space, ' ' * cell_padding, '|' if i < len(header) - 1 else '')
                header_div += '%s%s' %('=' * (2 * cell_padding + space + len(text)), '|' if i < len(header) - 1 else '')
            print(header_repr)
            print(header_div)

        # Print dataset of table
        row_count = 0
        for row in dataset:
            row_repr = ''
            row_div = ''
            for i in range(0, len(row)):
                space = cols_width[i] - len(str(row[i]))
                row_repr += '%s%s%s%s%s' \
                    %(' ' * cell_padding, row[i], ' ' * space, ' ' * cell_padding, '|' if i < len(row) - 1 else '')
                if row_border:
                    row_div += '%s%s' %('-' * (2 * cell_padding + len(str(row[i])) + space), '|' if i < len(row) - 1 else '')
            print(row_repr + ('\n%s' %row_div if row_border and row_count < len(dataset) - 1 else ''))
            row_count += 1
