from django.db import IntegrityError
from Crypto import Random
import base64
from models import Cell
from forms import Cell_Create

CELL_ID_SIZE = 20

#read all cell
def read_allCell(cell_ids):
    try:
        cells = Cell.objects.filter(cell_ud__in=cell_ids)
        return cells
    except Exception as e:
        return e


#read select cell
def read_selectCell(cell_id):
    pass

#create new cell
def create_Cell(cell: Cell_Create):
    try:
        cell_id_bytes = Random.new().read(CELL_ID_SIZE)
        cell_id = base64.b64encode(cell_id_bytes).decode('utf-8')
        cell_id = cell_id[:CELL_ID_SIZE].replace('/', '@')

    except Exception as e:
        return e

#update cell

#delete cell