from pathlib import Path
import os, yaml


def load_config(path="configs/base.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        cfg  = yaml.safe_load(f)
        data_dir  = os.getenv("DATA_DIR", cfg.get("data, {}").get("dir", "./data"))
    cfg["data"]["dir"] = data_dir
    cfg["paths"] = {
        "raw": str(Path(data_dir) / "raw"),
        "interim": str(Path(data_dir) / "interim"),
        "processed": str(Path(data_dir) / "processed"),
        "artifacts": "models/artifacts",
        "metrics": "models/metrics",
    }
    return cfg