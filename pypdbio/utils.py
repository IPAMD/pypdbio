import os
from contextlib import contextmanager


@contextmanager
def open_pdb(source, mode):
    """Yield a text stream for a path or an already-open file.

    A path is opened and closed here. A file object is yielded as-is and
    left open for its owner to close.
    """
    if isinstance(source, (str, os.PathLike)):
        with open(source, mode, encoding="utf-8") as stream:
            yield stream
    elif hasattr(source, "read" if "r" in mode else "write"):
        yield source
    else:
        raise TypeError(
            f"expected a path or a text file object, got {type(source).__name__}"
        )


def next_chain_id(current_chain_id, occupied_chain_ids):
    if current_chain_id == "":
        return "A"
    stride = 1
    while chr(ord(current_chain_id) + stride) in occupied_chain_ids:
        stride += 1
    return chr(ord(current_chain_id) + stride)

def index_of_chain_id(target_chain_id, occupied_chain_ids):
    n_occupied = sum(1 for chain_id in occupied_chain_ids if chain_id <= target_chain_id)
    return ord(target_chain_id) - ord('A') - n_occupied

def chain_id_of_index(index, occupied_chain_ids):
    start = 'A'
    for _ in range(index):
        start = next_chain_id(start, occupied_chain_ids)
    return start
