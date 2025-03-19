import numpy as np

array = np.load('k_proj.scale.npy')

array_col = array.astype(int)  # 確保數據為整數
min_value = np.min(array_col)
max_value = np.max(array_col)
print(array_col.shape)
input()
print("min:", min_value)
print("max:", max_value)
print(array_col[0, 1])

def decimal_to_hex(num, bit_width=8):
    """將十進制數字轉換為 8-bit 兩補數的 16 進制字串"""
    if num < 0:
        num = (1 << bit_width) + num  # 轉換為 8-bit 補數格式
    return hex(num)[2:].zfill(2)  # 確保 8-bit (2 位元 16 進制) 格式

with open("qk_kt.dat", "w") as bias_fp:
    for col in range(array_col.shape[1]):
        hex_values = []
        for row in range(array_col.shape[0]):
            hex_str = decimal_to_hex(array_col[row][col])
            hex_values.append(hex_str)
            # 每 8 筆數據寫入一行
            if (row + 1) % 8 == 0 or row == array_col.shape[0] - 1:
                bias_fp.write("".join(hex_values) + f"  // col{col} row{row - len(hex_values) + 1}~row{row}\n")
                hex_values = []

print("finish bias pattern")
