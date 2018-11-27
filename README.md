# Python: TablePrinter
A python table printer for a given dataset.<br>
Actual version: 1.0.0

## Files
The files included in this project:
* example.py: an example on how to use TablePrinter.
* printer.py: the TablePrinter file.

## Functions
#### add_row(row, times)
Add a row to the table's dataset.<br>
* row: input must be a list.
* times (optional): how many times the row must be added; default=1.

#### set_dataset(dataset, ignore_keys)
Set the dataset of the row giving a list of lists or a list of dictionaries.<br>
* dataset: input must be a list of lists or list of dictionaries.
* ignore_keys (optional): if the dataset given is a dictionary, state which keys to ignore in case you don't want to add all of the values.

#### set_header(header)
Set the header of the table. If not provided, the header will keep empty.

#### print(show_header, header_upper, cell_padding, cell_min_width, row_border, auto_id)
Print the table.<br>
* show_header (optional): if the header must be printed; default=True.
* header_upper (optional): if the header must be printed in upper case; default=True.
* cell_padding (optional): left and right padding of all the cells; default=0.
* cell_min_width (optional): minimum with the rows must have; default=0.
* row_border (optional): if each row must be printed with a bottom separator; default=False.
* auto_id (optional): print each row with an automatic id at the first column; default=False.
