from get_sort_data import sort,get_da
from commands import get_data
from read_write import read_file,write_file
from main import sort_data
from commands import get_operation


def start():
    return sort_data(get_operation,read_file,write_file,sort,get_da,get_data)