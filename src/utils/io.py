from pathlib import Path
import pandas as pd

def ensure_dirs(paths: dict):
     for p in oaths.values():
        Path(p).mkdir(parents=True, exist_ok=True)
        def save_csv(df: pd.DataFrame, path: str):
            Path(path).parentmkdir(parents=True, exist_ok=True)
            df.to_csv(path, index=False)
            