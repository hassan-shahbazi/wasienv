import os

from wasienv.wasiswiftc import run
from wasienv.tools import is_exe, is_wasm

EXAMPLES_DIR = os.path.join(os.path.dirname(__file__), '../examples/')
os.chdir(EXAMPLES_DIR)

def test_wasiswift():
    return_code = run(["wasiswiftc", "swift/example-wasi.swift", "-o", "swift/example-wasi"])
    assert return_code == 0
    assert is_exe("swift/example-wasi")
    assert is_wasm("swift/example-wasi.wasm")
