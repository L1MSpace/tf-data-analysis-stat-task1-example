import pandas as pd
import numpy as np

chat_id = 704471350

def solution(x: np.array) -> float:
    x = sum(x) / (len(x)+18)
    return x
