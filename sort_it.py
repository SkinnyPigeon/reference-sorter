from typing import List


def sort_references(filename: str) -> List:
    with open(filename, "r") as ref:
        ref_list = ref.read().splitlines()
        ref_list = [item for item in ref_list if item not in ("\\\\")]
        return sorted(ref_list)


def save_sorted_references(filename: str, sorted_list: List) -> None:
    with open(filename, "w") as ref:
        for item in sorted_list:
            ref.write(item)
            ref.write("\n")
            ref.write("\\\\")
            ref.write("\n")
            ref.write("\\\\")
            ref.write("\n")


sorted_list = sort_references("./references.txt")
save_sorted_references("./sorted_references.txt", sorted_list)
