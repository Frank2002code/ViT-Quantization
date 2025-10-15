import numpy as np

array = np.load('out_proj.scale.npy')

array_row = array.astype(int)  # 確保數據為整數
min_value = np.min(array_row)
max_value = np.max(array_row)
print(array_row.shape)
input()
print("min:", min_value)
print("max:", max_value)
print(array_row[0, 1])

def decimal_to_hex(num, bit_width=8):
    """將十進制數字轉換為 8-bit 兩補數的 16 進制字串"""
    if num < 0:
        num = (1 << bit_width) + num  # 轉換為 8-bit 補數格式
    return hex(num)[2:].zfill(2)  # 確保 8-bit (2 位元 16 進制) 格式

with open("qk_out.dat", "w") as bias_fp:
    for row in range(array_row.shape[0]):
        hex_values = []
        for col in range(array_row.shape[1]):
            hex_str = decimal_to_hex(array_row[row][col])
            hex_values.append(hex_str)
            # 每 8 筆數據寫入一行
            if (col + 1) % 8 == 0 or col == array_row.shape[1] - 1:
                bias_fp.write("".join(hex_values) + f"  // row{row} col{col - len(hex_values) + 1}~col{col}\n")
                hex_values = []

print("finish bias pattern")
