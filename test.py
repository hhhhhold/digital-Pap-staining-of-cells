import numpy as np
from scipy import stats

# =========================
# 读取数据
# =========================
ssim_values = np.loadtxt("ssim_list.txt")
psnr_values = np.loadtxt("psnr_list.txt")

# =========================
# 设置参考基准（很关键）
# =========================
ssim_baseline = 0.80
psnr_baseline = 22.0

# =========================
# t-test
# =========================
t_ssim, p_ssim = stats.ttest_1samp(ssim_values, ssim_baseline)
t_psnr, p_psnr = stats.ttest_1samp(psnr_values, psnr_baseline)

# =========================
# 输出结果
# =========================
print("====== SSIM ======")
print("mean =", np.mean(ssim_values))
print("t =", t_ssim)
print("p =", p_ssim)

print("\n====== PSNR ======")
print("mean =", np.mean(psnr_values))
print("t =", t_psnr)
print("p =", p_psnr)