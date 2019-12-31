""" Store XFLR results into a dataframe """
import pandas as pd

def xflr_dat_to_dataframe(file_name : str) -> pd.DataFrame:
    lines = dat_clean(file_name)
    frame = pd.DataFrame(lines[1:], columns = lines[0])
    frame = frame.dropna()
    frame = frame.astype('float')
    return frame


def dat_clean(file_name : str, skip_lines : int = 5):
    with open(file_name) as file:
        lines = file.readlines()
        # Don't use the first 5 lines
        lines = lines[skip_lines:]
        # Split by white space then remove empty entries
        for index, line in enumerate(lines):
            line = line.replace("\n", "")
            lines[index] = list(filter(lambda a: a != '', line.split(" ")))
    return lines