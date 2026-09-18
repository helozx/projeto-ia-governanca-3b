import json
import os
import sys
from pathlib import Path


def display(value):
    data = getattr(value, "data", None)
    if data is not None:
        print(data)
    else:
        print(value)


notebook_path = Path(sys.argv[1]).resolve()
project_dir = notebook_path.parent.parent
os.chdir(project_dir)

notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
namespace = {"display": display}

executed = 0
for index, cell in enumerate(notebook["cells"], start=1):
    if cell.get("cell_type") != "code":
        continue
    source = "".join(cell.get("source", []))
    print(f"Executando célula de código {index}...")
    exec(compile(source, f"celula_{index}", "exec"), namespace)
    executed += 1

print(f"Validação concluída: {executed} células de código executadas sem erro.")

