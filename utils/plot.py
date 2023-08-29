import matplotlib.pyplot as plt
import numpy as np

# Data
data_005 = [
    [2, 20.649, [19.47044414292179, 21.827555857078213]],
    [3, 50.181, [48.40768610858602, 51.954313891413975]],
    [4, 79.348, [77.08682929939394, 81.60917070060606]],
    [5, 96.214, [93.98898227252454, 98.43901772747546]],
    [6, 121.244, [118.6355607672284, 123.8524392327716]],
    [7, 142.02, [139.14810924182657, 144.89189075817345]],
    [8, 157.166, [154.2499605752137, 160.0820394247863]],
    [9, 175.986, [172.80773978083906, 179.16426021916092]],
    [10, 194.135, [190.97887931597484, 197.29112068402515]],
    [11, 209.884, [206.51682263475638, 213.2511773652436]],
    [12, 229.017, [225.66765224062112, 232.36634775937887]],
    [13, 245.75, [242.15271288952655, 249.34728711047345]],
    [14, 259.426, [255.6967388077749, 263.1552611922251]],
    [15, 276.193, [272.59270153597635, 279.7932984640236]],
    [16, 290.671, [287.103255664328, 294.238744335672]],
    [17, 312.029, [308.2138757767751, 315.84412422322487]],
    [18, 324.315, [320.3941873172672, 328.2358126827328]],
    [19, 341.885, [338.00146117794316, 345.7685388220568]],
    [20, 353.093, [349.1663099357907, 357.0196900642093]],
    [25, 428.781, [424.2997014512748, 433.2622985487252]],
    [30, 503.771, [499.13905954879675, 508.4029404512033]],
    [35, 573.506, [568.7034323091298, 578.3085676908702]],
    [40, 643.264, [638.0925904369669, 648.4354095630331]]
]

data_01 = [
    [2, 10.543, [9.96819849486058, 11.117801505139418]],
    [3, 25.245, [24.405368780190678, 26.084631219809324]],
    [4, 39.213, [38.18286479869605, 40.24313520130395]],
    [5, 51.893, [50.729835184113696, 53.056164815886305]],
    [6, 61.809, [60.548701217543055, 63.06929878245694]],
    [7, 72.137, [70.89670321258302, 73.37729678741698]],
    [8, 82.115, [80.72962877688624, 83.50037122311375]],
    [9, 89.094, [87.59493225598686, 90.59306774401313]],
    [10, 98.986, [97.5202171093335, 100.45178289066651]],
    [11, 109.758, [108.22550688523904, 111.29049311476095]],
    [12, 116.036, [114.49216695726145, 117.57983304273856]],
    [13, 123.538, [121.93138588109173, 125.14461411890827]],
    [14, 134.487, [132.7508636911865, 136.22313630881348]],
    [15, 141.91, [140.1596041282331, 143.6603958717669]],
    [16, 149.812, [148.12745381964123, 151.4965461803588]],
    [17, 157.317, [155.6116347727822, 159.02236522721782]],
    [18, 167.324, [165.51841353739846, 169.12958646260157]],
    [19, 176.091, [174.20605186049855, 177.97594813950147]],
    [20, 181.624, [179.75471562568873, 183.49328437431126]]
]

data_015 = [
    [2, 7.422, [7.05048513792178, 7.7935148620782195]],
    [3, 17.624, [17.07776881847187, 18.170231181528127]],
    [4, 27.182, [26.531082782308253, 27.832917217691744]],
    [5, 34.756, [34.05034092967766, 35.46165907032234]],
    [6, 42.75, [41.975108712442, 43.524891287558]],
    [7, 49.217, [48.391052686763885, 50.04294731323611]],
    [8, 55.047, [54.24466631509666, 55.849333684903335]],
    [9, 62.879, [62.047997553887704, 63.71000244611229]],
    [10, 68.529, [67.63450207145132, 69.42349792854867]],
    [11, 75.225, [74.34666848532471, 76.10333151467528]],
    [12, 81.308, [80.37508774565147, 82.24091225434854]],
    [13, 88.217, [87.22872732489762, 89.20527267510238]],
    [14, 94.557, [93.52183327910402, 95.59216672089599]],
    [15, 100.756, [99.71800621210325, 101.79399378789675]],
    [16, 106.181, [105.098215703336, 107.263784296664]],
    [17, 112.472, [111.41651760078601, 113.52748239921398]],
    [18, 118.889, [117.7755564165378, 120.0024435834622]],
    [19, 124.267, [123.1304140108226, 125.40358598917739]],
    [20, 130.951, [129.81604613627292, 132.08595386372707]]
]

sim_005 = [item[1] for item in data_005]
sim_01 = [item[1] for item in data_01]
sim_015 = [item[1] for item in data_015]

err_lower_01 = [row[1] - row[2][0] for row in data_01]
err_upper_01 = [row[2][1] - row[1] for row in data_01]

err_lower_015 = [row[1] - row[2][0] for row in data_015]
err_upper_015 = [row[2][1] - row[1] for row in data_015]

ana_005 = [20, 58.0696, 85.7344, 105.8186, 132.1876, 149.9606, 175.6066, 196.1002, 219.0824, 237.0068, 261.7016, 280.0756, 305.3478, 322.51, 346.166, 365.8616, 386.3986, 405.742, 429.207, 530.6136, 612.732, 737.0668, 813.759]
ana_01 = [10, 27.499, 41.2396, 49.7252, 62.0668, 71.528, 83.8324, 93.1614, 104.254, 113.623, 123.694, 133.5258, 144.9734, 154.287, 164.4344, 173.857, 185.3106, 193.641, 204.3456]
ana_015 = [8.67, 19.3658, 27.835, 33.6866, 41.4238, 47.5808, 55.2112, 60.7952, 67.785, 74.0276, 80.3514, 86.4256, 93.7568, 99.0962, 105.4492, 112.1368, 118.31, 124.2532, 130.9994]

sim_005_intervals = [[19.47044414292179, 21.827555857078213], [48.40768610858602, 51.954313891413975], [77.08682929939394, 81.60917070060606], [93.98898227252454, 98.43901772747546], [118.6355607672284, 123.8524392327716], [139.14810924182657, 144.89189075817345], [154.2499605752137, 160.0820394247863], [172.80773978083906, 179.16426021916092], [190.97887931597484, 197.29112068402515], [206.51682263475638, 213.2511773652436], [225.66765224062112, 232.36634775937887], [242.15271288952655, 249.34728711047345], [255.6967388077749, 263.1552611922251], [272.59270153597635, 279.7932984640236], [287.103255664328, 294.238744335672], [308.2138757767751, 315.84412422322487], [320.3941873172672, 328.2358126827328], [338.00146117794316, 345.7685388220568], [349.1663099357907, 357.0196900642093], [424.2997014512748, 433.2622985487252], [499.13905954879675, 508.4029404512033], [568.7034323091298, 578.3085676908702], [638.0925904369669, 648.4354095630331]]
y_errors = [(mean - lower, upper - mean) for mean, (lower, upper) in zip(sim_005, sim_005_intervals)]
lower_errors_005 = [err[0] for err in y_errors]
upper_errors_005 = [err[1] for err in y_errors]

x1 = list(range(2, 21))
x1.append(25)
x1.append(30)
x1.append(35)
x1.append(40)
x2 = list(range(2, 21))



# # Figure 1
# plt.figure(figsize=(10, 6))
# plt.errorbar(x1, sim_005, yerr=[lower_errors_005, upper_errors_005], fmt='-o', markersize=3, capsize=5, capthick=2, color='blue', ecolor='red', label='Simulation')
# plt.plot(x1, ana_005, linestyle='--', markersize=3, color='orange',label='Bound')
# plt.xticks(fontsize=18)
# plt.yticks(fontsize=18)
# plt.tick_params(bottom=False, top=False, left=False, right=False)
# plt.xlabel('Network Size', fontsize=18)
# plt.ylabel('Time', fontsize=18)
# plt.legend(fontsize=25)
# # plt.grid(True)
# plt.show()

# # Figure 3
# plt.figure(figsize=(20, 6))
# plt.errorbar(x2, sim_005[:19], yerr=[lower_errors_005[:19], upper_errors_005[:19]], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='$p_{con}$=0.05(Simulation)', color='orange')
# plt.plot(x2, ana_005[:19], linestyle='--', markersize=3,label='$p_{con}$=0.05(Bound)', color='orange')
# plt.errorbar(x2, sim_01, yerr=[err_lower_01, err_upper_01], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='$p_{con}$=0.1(Simulation)', color='green')
# plt.plot(x2, ana_01, linestyle='--', markersize=3, label='$p_{con}$=0.1(Bound)', color='green')
# plt.errorbar(x2, sim_015, yerr=[err_lower_015, err_upper_015], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='$p_{con}$=0.15(Simulation)', color='blue')
# plt.plot(x2, ana_015, linestyle='--', markersize=3, label='$p_{con}$=0.15(Bound)', color='blue')
# plt.xticks(x2,fontsize=18)
# plt.yticks(fontsize=18)
# plt.tick_params(bottom=False, top=False, left=False, right=False)
# plt.xlabel('Network Size', fontsize=18)
# plt.ylabel('Time', fontsize=18)
# plt.legend(fontsize=17)
# # plt.grid(True)
# plt.show()

# # 创建一个 Figure 和两个子图
# fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# # 第一个子图的内容
# axes[0].errorbar(x1, sim_005, yerr=[lower_errors_005, upper_errors_005], fmt='-o', markersize=3, capsize=5, capthick=2, color='blue', ecolor='red', label='Simulation')
# axes[0].plot(x1, ana_005, marker='o', markersize=3, color='orange',label='Bound')
# axes[0].set_xlabel('Network Size', fontsize=18)
# axes[0].set_ylabel('Time Cost', fontsize=18)
# axes[0].legend(fontsize=23)
# axes[0].tick_params(bottom=False, top=False, left=False, right=False)
# axes[0].set_title('(a)', fontsize=16, y=-0.2) 

# # 第二个子图的内容
# axes[1].errorbar(x2, sim_005[:19], yerr=[lower_errors_005[:19], upper_errors_005[:19]], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='P=0.05(Simulation)')
# axes[1].plot(x2, ana_005[:19], marker='o', markersize=3,label='P=0.05(Bound)')
# axes[1].errorbar(x2, sim_01, yerr=[err_lower_01, err_upper_01], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='P=0.1(Simulation)')
# axes[1].plot(x2, ana_01, marker='o', markersize=3, label='P=0.1(Bound)')
# axes[1].errorbar(x2, sim_015, yerr=[err_lower_015, err_upper_015], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='P=0.15(Simulation)')
# axes[1].plot(x2, ana_015, marker='o', markersize=3, label='P=0.15(Bound)')
# axes[1].set_xticks(x2)
# axes[1].set_xlabel('Network Size', fontsize=18)
# axes[1].set_ylabel('Time Cost', fontsize=18)
# axes[1].legend(fontsize=15)
# axes[1].tick_params(bottom=False, top=False, left=False, right=False) 
# axes[1].set_title('(b)', fontsize=16, y=-0.2) 

# # 调整子图之间的间距
# plt.tight_layout()

# # 显示图形
# plt.show()

data_graph = [
    [2, 134, 4, 22.332, [21.136509084970868, 23.527490915029134]],
    [3, 197, 6, 50.526, [48.79106392227285, 52.26093607772716]],
    [4, 221, 14, 75.567, [73.36169514565005, 77.77230485434994]],
    [5, 269, 24, 92.75, [90.59948137568998, 94.90051862431002]],
    [6, 310, 31, 110.563, [108.03300910519036, 113.09299089480965]],
    [7, 327, 44, 122.886, [120.25539025046427, 125.51660974953572]],
    [8, 379, 52, 137.575, [134.869097846395, 140.28090215360498]],
    [9, 346, 61, 147.233, [144.55295531613206, 149.91304468386795]],
    [10, 384, 53, 158.892, [156.0512877170478, 161.73271228295218]],
    [11, 385, 77, 173.543, [170.68229297274112, 176.4037070272589]],
    [12, 447, 73, 183.128, [180.01470618202086, 186.2412938179791]],
    [13, 387, 91, 191.841, [188.93302387402747, 194.74897612597255]],
    [14, 440, 91, 202.235, [199.28458048560992, 205.1854195143901]],
    [15, 457, 99, 208.329, [205.25394532705806, 211.40405467294195]],
    [16, 468, 110, 220.877, [217.69124275930642, 224.0627572406936]],
    [17, 519, 109, 228.449, [225.09887661294314, 231.79912338705688]],
    [18, 657, 118, 235.792, [232.4483458256286, 239.1356541743714]],
    [19, 557, 125, 242.644, [239.44378915735075, 245.84421084264926]],
    [20, 515, 130, 252.75, [249.55352436734935, 255.94647563265065]]
]

sim_graph = [item[3] for item in data_graph]

err_lower_graph = [row[3] - row[4][0] for row in data_graph]
err_upper_graph = [row[4][1] - row[3] for row in data_graph]

ana_graph = [150.26968, 237.34934, 323.58298, 407.76978, 489.96714, 572.85688, 654.37382, 736.53224, 818.478, 898.2258, 979.6407, 1059.06004, 1139.70134, 1219.18074, 1301.51014, 1380.41296, 1458.63818, 1538.95568, 1618.19488]

# Figure 1
plt.figure(figsize=(10, 6))
plt.errorbar(x2, sim_graph, yerr=[err_lower_graph, err_upper_graph], fmt='-o', markersize=3, capsize=5, capthick=2, color='green', ecolor='red', label='Simulation(graph)')
plt.errorbar(x2, sim_005[:19], yerr=[lower_errors_005[:19], upper_errors_005[:19]], fmt='-o', markersize=3, capsize=5, capthick=2, ecolor='red', label='Simulation(line)', color='orange')
plt.plot(x2, ana_005[:19], linestyle='--', markersize=3, label='Bound', color='blue')
plt.xticks(x2, fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel('Network Size',fontsize=18)
plt.ylabel('Time',fontsize=18)
plt.legend(fontsize=23)
# plt.grid(True)
plt.show()