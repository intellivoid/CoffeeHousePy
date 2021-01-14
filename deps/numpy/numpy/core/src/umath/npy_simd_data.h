#ifndef __NPY_SIMD_DATA_H_
#define __NPY_SIMD_DATA_H_
#if defined HAVE_ATTRIBUTE_TARGET_AVX512F_WITH_INTRINSICS && defined  NPY_HAVE_SSE2_INTRINSICS
/*
 * Constants used in vector implementation of float64 exp(x)
 */
#define NPY_RINT_CVT_MAGIC 0x1.8p52
#define NPY_INV_LN2_MUL_32 0x1.71547652b82fep+5
#define NPY_TANG_NEG_L1 -0x1.62e42fefp-6
#define NPY_TANG_NEG_L2 -0x1.473de6af278edp-39
#define NPY_TANG_A1 0x1p-1
#define NPY_TANG_A2 0x1.5555555548f7cp-3
#define NPY_TANG_A3 0x1.5555555545d4ep-5
#define NPY_TANG_A4 0x1.11115b7aa905ep-7
#define NPY_TANG_A5 0x1.6c1728d739765p-10

/* Lookup table for 2^(j/32) */
static npy_uint64 EXP_Table_top[32] = {
    0x3FF0000000000000,
    0x3FF059B0D3158540,
    0x3FF0B5586CF98900,
    0x3FF11301D0125B40,
    0x3FF172B83C7D5140,
    0x3FF1D4873168B980,
    0x3FF2387A6E756200,
    0x3FF29E9DF51FDEC0,
    0x3FF306FE0A31B700,
    0x3FF371A7373AA9C0,
    0x3FF3DEA64C123400,
    0x3FF44E0860618900,
    0x3FF4BFDAD5362A00,
    0x3FF5342B569D4F80,
    0x3FF5AB07DD485400,
    0x3FF6247EB03A5580,
    0x3FF6A09E667F3BC0,
    0x3FF71F75E8EC5F40,
    0x3FF7A11473EB0180,
    0x3FF82589994CCE00,
    0x3FF8ACE5422AA0C0,
    0x3FF93737B0CDC5C0,
    0x3FF9C49182A3F080,
    0x3FFA5503B23E2540,
    0x3FFAE89F995AD380,
    0x3FFB7F76F2FB5E40,
    0x3FFC199BDD855280,
    0x3FFCB720DCEF9040,
    0x3FFD5818DCFBA480,
    0x3FFDFC97337B9B40,
    0x3FFEA4AFA2A490C0,
    0x3FFF50765B6E4540,
};

static npy_uint64 EXP_Table_tail[32] = {
    0x0000000000000000,
    0x3D0A1D73E2A475B4,
    0x3CEEC5317256E308,
    0x3CF0A4EBBF1AED93,
    0x3D0D6E6FBE462876,
    0x3D053C02DC0144C8,
    0x3D0C3360FD6D8E0B,
    0x3D009612E8AFAD12,
    0x3CF52DE8D5A46306,
    0x3CE54E28AA05E8A9,
    0x3D011ADA0911F09F,
    0x3D068189B7A04EF8,
    0x3D038EA1CBD7F621,
    0x3CBDF0A83C49D86A,
    0x3D04AC64980A8C8F,
    0x3CD2C7C3E81BF4B7,
    0x3CE921165F626CDD,
    0x3D09EE91B8797785,
    0x3CDB5F54408FDB37,
    0x3CF28ACF88AFAB35,
    0x3CFB5BA7C55A192D,
    0x3D027A280E1F92A0,
    0x3CF01C7C46B071F3,
    0x3CFC8B424491CAF8,
    0x3D06AF439A68BB99,
    0x3CDBAA9EC206AD4F,
    0x3CFC2220CB12A092,
    0x3D048A81E5E8F4A5,
    0x3CDC976816BAD9B8,
    0x3CFEB968CAC39ED3,
    0x3CF9858F73A18F5E,
    0x3C99D3E12DD8A18B,
};
#endif

/*
 * Constants used in vector implementation of exp(x)
 */
#define NPY_RINT_CVT_MAGICf 0x1.800000p+23f
#define NPY_CODY_WAITE_LOGE_2_HIGHf -6.93145752e-1f
#define NPY_CODY_WAITE_LOGE_2_LOWf -1.42860677e-6f
#define NPY_COEFF_P0_EXPf 9.999999999980870924916e-01f
#define NPY_COEFF_P1_EXPf 7.257664613233124478488e-01f
#define NPY_COEFF_P2_EXPf 2.473615434895520810817e-01f
#define NPY_COEFF_P3_EXPf 5.114512081637298353406e-02f
#define NPY_COEFF_P4_EXPf 6.757896990527504603057e-03f
#define NPY_COEFF_P5_EXPf 5.082762527590693718096e-04f
#define NPY_COEFF_Q0_EXPf 1.000000000000000000000e+00f
#define NPY_COEFF_Q1_EXPf -2.742335390411667452936e-01f
#define NPY_COEFF_Q2_EXPf 2.159509375685829852307e-02f

/*
 * Constants used in vector implementation of log(x)
 */
#define NPY_COEFF_P0_LOGf 0.000000000000000000000e+00f
#define NPY_COEFF_P1_LOGf 9.999999999999998702752e-01f
#define NPY_COEFF_P2_LOGf 2.112677543073053063722e+00f
#define NPY_COEFF_P3_LOGf 1.480000633576506585156e+00f
#define NPY_COEFF_P4_LOGf 3.808837741388407920751e-01f
#define NPY_COEFF_P5_LOGf 2.589979117907922693523e-02f
#define NPY_COEFF_Q0_LOGf 1.000000000000000000000e+00f
#define NPY_COEFF_Q1_LOGf 2.612677543073109236779e+00f
#define NPY_COEFF_Q2_LOGf 2.453006071784736363091e+00f
#define NPY_COEFF_Q3_LOGf 9.864942958519418960339e-01f
#define NPY_COEFF_Q4_LOGf 1.546476374983906719538e-01f
#define NPY_COEFF_Q5_LOGf 5.875095403124574342950e-03f
/*
 * Constants used in vector implementation of sinf/cosf(x)
 */
#define NPY_TWO_O_PIf 0x1.45f306p-1f
#define NPY_CODY_WAITE_PI_O_2_HIGHf -0x1.921fb0p+00f
#define NPY_CODY_WAITE_PI_O_2_MEDf -0x1.5110b4p-22f
#define NPY_CODY_WAITE_PI_O_2_LOWf -0x1.846988p-48f
#define NPY_COEFF_INVF0_COSINEf 0x1.000000p+00f
#define NPY_COEFF_INVF2_COSINEf -0x1.000000p-01f
#define NPY_COEFF_INVF4_COSINEf 0x1.55553cp-05f
#define NPY_COEFF_INVF6_COSINEf -0x1.6c06dcp-10f
#define NPY_COEFF_INVF8_COSINEf 0x1.98e616p-16f
#define NPY_COEFF_INVF3_SINEf -0x1.555556p-03f
#define NPY_COEFF_INVF5_SINEf 0x1.11119ap-07f
#define NPY_COEFF_INVF7_SINEf -0x1.a06bbap-13f
#define NPY_COEFF_INVF9_SINEf 0x1.7d3bbcp-19f

#endif
