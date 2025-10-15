import os
import argparse
import numpy as np

def arg_parse(weight_name: str = 'q'):
    parser = argparse.ArgumentParser(description="")
    npy_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "npy_result", "weight")
    parser.add_argument("--npy_file_path", type=str, default=os.path.join(npy_dir, f"{weight_name}_proj_weight.npy"), help="numpy file path")
    return parser.parse_args()

def decimal_to_hex(num, bit_width=8):
    if num < 0:
        num = (1 << bit_width) + num
    return hex(num)[2:].zfill(2)

if __name__ == "__main__":
    weight_name = input("Enter weight name (q/k/v): ").strip().lower()
    args = arg_parse(weight_name=weight_name)
    weight = np.load(args.npy_file_path).astype(int)
    rows, cols = weight.shape
    print(f"Weight Shape: {weight.shape}")

    step = 8
    with open(f"W{weight_name}.dat", "w") as dat_file:
        for offset in range(step):
            for col in range(offset, cols, step):
                hex_values = []
                for row in range(rows):
                    hex_value = decimal_to_hex(weight[row][col])
                    hex_values.append(hex_value)
                    if (row + 1) % step == 0 or row == rows - 1:
                        dat_file.write("".join(hex_values) + f"  // col_{col}, row_{row-step+1}~row_{row}\n")
                        hex_values.clear()
                    else:
                        continue

    print(f"Transform W{weight_name}.npy to W{weight_name}.dat finish!")