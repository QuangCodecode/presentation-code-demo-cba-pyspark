import numpy as np


class Params:
    def __init__(self) -> None:
        self.xx = np.array([2.,  2.26530612,  2.53061224,  2.79591837,  3.06122449,
                            3.32653061,  3.59183673,  3.85714286,  4.12244898,  4.3877551,
                            4.65306122,  4.91836735,  5.18367347,  5.44897959,  5.71428571,
                            5.97959184,  6.24489796,  6.51020408,  6.7755102,  7.04081633,
                            7.30612245,  7.57142857,  7.83673469,  8.10204082,  8.36734694,
                            8.63265306,  8.89795918,  9.16326531,  9.42857143,  9.69387755,
                            9.95918367, 10.2244898, 10.48979592, 10.75510204, 11.02040816,
                            11.28571429, 11.55102041, 11.81632653, 12.08163265, 12.34693878,
                            12.6122449, 12.87755102, 13.14285714, 13.40816327, 13.67346939,
                            13.93877551, 14.20408163, 14.46938776, 14.73469388, 15.])

        self.yy = np.array([29.54621157, 28.74403774, 27.9418639, 27.13969007, 26.33751623,
                            25.5353424, 24.73316856, 23.93099473, 23.12882089, 22.32664706,
                            21.52447322, 20.72229939, 19.92012556, 19.11795172, 18.31577789,
                            17.51360405, 16.71143022, 15.90925638, 15.10708255, 14.30490871,
                            13.50273488, 12.70056104, 11.89838721, 11.09621337, 10.29403954,
                            9.4918657,  8.68969187,  7.88751803,  7.0853442,  6.28317036,
                            5.48099653,  4.67882269,  3.87664886,  3.07447502,  2.27230119,
                            1.47012735,  0.66795352, -0.13422032, -0.93639415, -1.73856799,
                            -2.54074182, -3.34291565, -4.14508949, -4.94726332, -5.74943716,
                            -6.55161099, -7.35378483, -8.15595866, -8.9581325, -9.76030633])

        self.yy_down = np.array([26.84153217,  26.03935833,  25.2371845,  24.43501066,
                                 23.63283683,  22.83066299,  22.02848916,  21.22631533,
                                 20.42414149,  19.62196766,  18.81979382,  18.01761999,
                                 17.21544615,  16.41327232,  15.61109848,  14.80892465,
                                 14.00675081,  13.20457698,  12.40240314,  11.60022931,
                                 10.79805547,   9.99588164,   9.1937078,   8.39153397,
                                 7.58936013,   6.7871863,   5.98501246,   5.18283863,
                                 4.38066479,   3.57849096,   2.77631712,   1.97414329,
                                 1.17196945,   0.36979562,  -0.43237822,  -1.23455205,
                                 -2.03672588,  -2.83889972,  -3.64107355,  -4.44324739,
                                 -5.24542122,  -6.04759506,  -6.84976889,  -7.65194273,
                                 -8.45411656,  -9.2562904, -10.05846423, -10.86063807,
                                 -11.6628119, -12.46498574])

        self.yy_up = np.array([32.25089098, 31.44871714, 30.64654331, 29.84436947, 29.04219564,
                               28.2400218, 27.43784797, 26.63567413, 25.8335003, 25.03132646,
                               24.22915263, 23.42697879, 22.62480496, 21.82263112, 21.02045729,
                               20.21828345, 19.41610962, 18.61393579, 17.81176195, 17.00958812,
                               16.20741428, 15.40524045, 14.60306661, 13.80089278, 12.99871894,
                               12.19654511, 11.39437127, 10.59219744,  9.7900236,  8.98784977,
                               8.18567593,  7.3835021,  6.58132826,  5.77915443,  4.97698059,
                               4.17480676,  3.37263292,  2.57045909,  1.76828525,  0.96611142,
                               0.16393758, -0.63823625, -1.44041009, -2.24258392, -3.04475776,
                               -3.84693159, -4.64910542, -5.45127926, -6.25345309, -7.05562693])

        self.support_vectors0 = np.array([10.65658821,  9.04392612])

        self.support_vectors1 = np.array([6.07702479, 5.54366269])

    def params_loader(self):
        return self.xx, self.yy, self.yy_up, self.yy_down, self.support_vectors0, self.support_vectors1
