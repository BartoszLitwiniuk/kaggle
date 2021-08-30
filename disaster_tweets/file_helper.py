import pandas as pd
import time
from config import SUBMISSION_BASE_FILE_NAME, SUBMISSION_EXTENSION_FILE_NAME, SUBMISSION_FILE_NAME_DATE_FORMAT


def save_df(df: pd.DataFrame, x_col, y_col):
    now_time = time.strftime(SUBMISSION_FILE_NAME_DATE_FORMAT)
    submission = pd.DataFrame({x_col: df[x_col], y_col: df[y_col]})
    submission.to_csv(f'{SUBMISSION_BASE_FILE_NAME}_{now_time}.{SUBMISSION_EXTENSION_FILE_NAME}', index=False)