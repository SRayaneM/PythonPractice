from pyxll import xl_func, xl_arg, xl_return
import pandas as pd
import os


@xl_func("string path: object")
def load_csv_data(path):
     if path.startswith("."):

        path = os.path.join(os.path.dirname(__file__), path)
        df = pd.read_csv(path)

        return df