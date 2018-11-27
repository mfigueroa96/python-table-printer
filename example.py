#=================== ABOUT ===================#
# python-table-printer/example.py
# A python table printer for a given dataset
# Author: Martín Figueroa Padilla
# Version = 1.0.0
#=============================================#

from printer import TablePrinter

table = TablePrinter()
table.add_row(['Hermione Granger', 'Harry Potter'])
table.add_row(['Simon Spier', 'Simon vs. the Homo Sapiens Agenda'])
table.add_row(['Ally', 'A Star is Born'])
table.add_row(['Katara', 'Avatar: The Legend of Aang'])
table.add_row(['Luke Skywalker', 'Star Wars'])
table.set_header(['Character', 'Storyline'])
table.print(cell_padding=4, header_upper=True, row_border=True, auto_id=True, show_header=True)

print('\n\nTable fed with a pre-created dataset of lists:\n')

dataset_list = [
    ['Hermione Granger', 'Harry Potter'],
    ['Simon Spier', 'Simon vs. the Homo Sapiens Agenda'],
    ['Ally', 'A Star is Born'],
    ['Katara', 'Avatar: The Legend of Aang'],
    ['Luke Skywalker', 'Star Wars']
]

table_list = TablePrinter()
table_list.set_header(['Character', 'Storyline'])
table_list.set_dataset(dataset_list)
table_list.print(auto_id=True, cell_padding=4, show_header=True, row_border=True)

print('\n\nTable fed with a pre-created dataset of dictionaries:\n')

dataset_dict = [
    {'id': 1, 'name': 'Hermione Granger', 'storyline': 'Harry Potter'},
    {'id': 5, 'name': 'Simon Spier', 'storyline': 'Simon vs. the Homo Sapiens Agenda'},
    {'id': 3, 'name': 'Ally', 'storyline': 'A Star is Born'},
    {'id': 18, 'name': 'Katara', 'storyline': 'Avatar: The Legend of Aang'},
    {'id': 11, 'name': 'Luke Skywalker', 'storyline': 'Star Wars'}
]

table_dict = TablePrinter()
table_dict.set_header(header=['Character', 'Storyline'])
table_dict.set_dataset(dataset_dict, ignore_keys=['id'])
table_dict.print(auto_id=True, cell_padding=4, show_header=True, row_border=True)

'''
OUTPUT EXAMPLE:

    ID    |    CHARACTER           |    STORYLINE
==========|========================|=========================================
    1     |    Hermione Granger    |    Harry Potter
----------|------------------------|-----------------------------------------
    2     |    Simon Spier         |    Simon vs. the Homo Sapiens Agenda
----------|------------------------|-----------------------------------------
    3     |    Ally                |    A Star is Born
----------|------------------------|-----------------------------------------
    4     |    Katara              |    Avatar: The Legend of Aang
----------|------------------------|-----------------------------------------
    5     |    Luke Skywalker      |    Star Wars
'''
