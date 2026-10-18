# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 401 (the final check needs at least 200)
- Words: 628,353
- Estimated tokens (words times 1.4): 879,694 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `598us1r10_febh__p001-005` | 1,768 | 2296 | - | 5 running line(s) removed |
| `598us1r10_febh__p006-010` | 1,753 | 2150 | - | 5 running line(s) removed |
| `598us1r10_febh__p011-015` | 1,637 | 2042 | - | 5 running line(s) removed |
| `598us1r10_febh__p016-020` | 1,676 | 2085 | - | 5 running line(s) removed |
| `598us1r10_febh__p021-025` | 1,605 | 2054 | - | 5 running line(s) removed |
| `598us1r10_febh__p026-030` | 1,692 | 2114 | - | 5 running line(s) removed |
| `598us1r10_febh__p031-035` | 1,742 | 2077 | - | 5 running line(s) removed |
| `598us1r10_febh__p036-040` | 1,868 | 2205 | - | 5 running line(s) removed |
| `598us1r10_febh__p041-045` | 1,263 | 1498 | - | 5 running line(s) removed |
| `598us1r11_ca7d__p001-005` | 1,505 | 1923 | - | 4 running line(s) removed |
| `598us1r11_ca7d__p006-010` | 1,615 | 1987 | - | 4 running line(s) removed |
| `598us1r11_ca7d__p011-014` | 743 | 1179 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p001-005` | 1,552 | 1933 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p006-010` | 1,578 | 1977 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p011-015` | 1,720 | 2101 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p016-020` | 1,821 | 2257 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p021-025` | 1,776 | 2206 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p026-030` | 1,794 | 2132 | - | 4 running line(s) removed |
| `598us1r12_l5gm__p031-036` | 1,608 | 1584 | - | 4 running line(s) removed |
| `598us1r13_3e04__p001-005` | 1,634 | 2076 | - | 5 running line(s) removed |
| `598us1r13_3e04__p006-010` | 1,566 | 1982 | - | 5 running line(s) removed |
| `598us1r13_3e04__p011-015` | 1,540 | 1967 | - | 5 running line(s) removed |
| `598us1r13_3e04__p016-020` | 1,603 | 2002 | - | 5 running line(s) removed |
| `598us1r13_3e04__p021-026` | 1,773 | 1784 | - | 5 running line(s) removed |
| `598us1r14_3e04__p001-005` | 1,695 | 2123 | - | 4 running line(s) removed |
| `598us1r14_3e04__p006-010` | 1,657 | 2030 | - | 4 running line(s) removed |
| `598us1r14_3e04__p011-015` | 1,640 | 2037 | - | 4 running line(s) removed |
| `598us1r14_3e04__p016-020` | 1,154 | 1444 | - | 4 running line(s) removed |
| `598us1r1_3e04__p001-005` | 1,495 | 1900 | - | 4 running line(s) removed |
| `598us1r1_3e04__p006-010` | 1,612 | 2024 | - | 4 running line(s) removed |
| `598us1r1_3e04__p011-016` | 1,631 | 1754 | - | 4 running line(s) removed |
| `598us1r2_d18e` | 537 | 819 | - | 1 running line(s) removed |
| `598us1r3_j4ek__p001-005` | 1,703 | 2079 | - | 4 running line(s) removed |
| `598us1r3_j4ek__p006-010` | 1,619 | 1940 | - | 4 running line(s) removed |
| `598us1r3_j4ek__p011-015` | 1,718 | 2065 | - | 4 running line(s) removed |
| `598us1r3_j4ek__p016-020` | 1,711 | 2095 | - | 4 running line(s) removed |
| `598us1r3_j4ek__p021-024` | 969 | 1442 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p001-005` | 1,839 | 2221 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p006-010` | 1,653 | 2008 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p011-015` | 1,814 | 2117 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p016-020` | 1,874 | 2174 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p021-025` | 1,626 | 1979 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p026-030` | 1,670 | 2011 | - | 4 running line(s) removed |
| `598us1r4_1a7d__p031-032` | 176 | 546 | - | 4 running line(s) removed |
| `598us1r5_1b72__p001-005` | 1,605 | 2005 | - | 4 running line(s) removed |
| `598us1r5_1b72__p006-010` | 1,651 | 2000 | - | 4 running line(s) removed |
| `598us1r5_1b72__p011-015` | 1,607 | 2012 | - | 4 running line(s) removed |
| `598us1r5_1b72__p016-018` | 477 | 985 | - | 4 running line(s) removed |
| `598us1r6_0813__p001-005` | 1,750 | 2254 | - | 5 running line(s) removed |
| `598us1r6_0813__p006-010` | 1,625 | 1951 | - | 5 running line(s) removed |
| `598us1r6_0813__p011-015` | 1,788 | 2168 | - | 5 running line(s) removed |
| `598us1r6_0813__p016-020` | 1,676 | 2061 | - | 5 running line(s) removed |
| `598us1r6_0813__p021-025` | 1,654 | 2066 | - | 5 running line(s) removed |
| `598us1r6_0813__p026-030` | 1,612 | 2001 | - | 5 running line(s) removed |
| `598us1r6_0813__p031-032` | 387 | 1204 | - | 5 running line(s) removed |
| `598us1r7_3dq4__p001-005` | 1,683 | 2148 | - | 5 running line(s) removed |
| `598us1r7_3dq4__p006-010` | 1,566 | 1968 | - | 5 running line(s) removed |
| `598us1r7_3dq4__p011-015` | 1,608 | 2033 | - | 5 running line(s) removed |
| `598us1r7_3dq4__p016-020` | 1,632 | 2080 | - | 5 running line(s) removed |
| `598us1r7_3dq4__p021-025` | 1,738 | 2120 | - | 5 running line(s) removed |
| `598us1r7_3dq4__p026-029` | 830 | 1292 | - | 5 running line(s) removed |
| `598us1r8_limq__p001-005` | 1,534 | 1932 | - | 3 running line(s) removed |
| `598us1r8_limq__p006-010` | 1,711 | 2038 | - | 3 running line(s) removed |
| `598us1r8_limq__p011-012` | 229 | 694 | - | 3 running line(s) removed |
| `598us1r9_8mjp__p001-005` | 1,590 | 2031 | - | 5 running line(s) removed |
| `598us1r9_8mjp__p006-010` | 1,744 | 2148 | - | 5 running line(s) removed |
| `598us1r9_8mjp__p011-015` | 1,695 | 2089 | - | 5 running line(s) removed |
| `598us1r9_8mjp__p016-020` | 1,613 | 1985 | - | 5 running line(s) removed |
| `598us1r9_8mjp__p021-025` | 1,445 | 1737 | - | 5 running line(s) removed |
| `598us2r15_d1o2__p001-005` | 1,515 | 1955 | - | 5 running line(s) removed |
| `598us2r15_d1o2__p006-010` | 1,648 | 2084 | - | 5 running line(s) removed |
| `598us2r15_d1o2__p011-015` | 1,092 | 1419 | - | 5 running line(s) removed |
| `598us2r16_4gdj__p001-005` | 1,656 | 2052 | - | 4 running line(s) removed |
| `598us2r16_4gdj__p006-010` | 1,654 | 2030 | - | 4 running line(s) removed |
| `598us2r16_4gdj__p011-015` | 1,602 | 1956 | - | 4 running line(s) removed |
| `598us2r16_4gdj__p016-020` | 1,690 | 2020 | - | 4 running line(s) removed |
| `598us2r16_4gdj__p021-022` | 162 | 508 | - | 4 running line(s) removed |
| `598us2r17_c0nd__p001-005` | 1,565 | 1998 | - | 6 running line(s) removed |
| `598us2r17_c0nd__p006-010` | 1,611 | 2033 | - | 6 running line(s) removed |
| `598us2r17_c0nd__p011-015` | 1,595 | 2023 | - | 6 running line(s) removed |
| `598us2r17_c0nd__p016-019` | 1,000 | 1486 | - | 6 running line(s) removed |
| `598us2r18_g2bh__p001-005` | 1,839 | 2366 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p006-010` | 2,037 | 2536 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p011-015` | 1,609 | 2059 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p016-020` | 1,566 | 2019 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p021-025` | 1,804 | 2211 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p026-030` | 1,646 | 2069 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p031-035` | 1,731 | 2172 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p036-040` | 1,589 | 1975 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p041-045` | 1,634 | 2034 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p046-050` | 1,535 | 1957 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p051-055` | 1,623 | 2074 | - | 4 running line(s) removed |
| `598us2r18_g2bh__p056-057` | 315 | 991 | - | 4 running line(s) removed |
| `598us2r19_dc8f__p001-005` | 1,507 | 1998 | - | 5 running line(s) removed |
| `598us2r19_dc8f__p006-010` | 1,648 | 2108 | - | 5 running line(s) removed |
| `598us2r19_dc8f__p011-015` | 1,608 | 2009 | - | 5 running line(s) removed |
| `598us2r19_dc8f__p016-020` | 1,593 | 1992 | - | 5 running line(s) removed |
| `598us2r19_dc8f__p021-023` | 602 | 1301 | - | 5 running line(s) removed |
| `598us2r20_b07d__p001-005` | 1,461 | 1776 | - | 5 running line(s) removed |
| `598us2r20_b07d__p006-010` | 1,629 | 2009 | - | 5 running line(s) removed |
| `598us2r20_b07d__p011-015` | 1,689 | 2051 | - | 5 running line(s) removed |
| `598us2r20_b07d__p016-019` | 1,073 | 1692 | - | 5 running line(s) removed |
| `598us2r21_5425__p001-005` | 1,521 | 1981 | - | 5 running line(s) removed |
| `598us2r21_5425__p006-010` | 1,600 | 2036 | - | 5 running line(s) removed |
| `598us2r21_5425__p011-015` | 1,578 | 1998 | - | 5 running line(s) removed |
| `598us2r21_5425__p016-020` | 1,605 | 1980 | - | 5 running line(s) removed |
| `598us2r21_5425__p021-024` | 848 | 1331 | - | 5 running line(s) removed |
| `598us2r22_hejm__p001-005` | 1,839 | 2348 | - | 5 running line(s) removed |
| `598us2r22_hejm__p006-010` | 1,868 | 2349 | - | 5 running line(s) removed |
| `598us2r22_hejm__p011-015` | 1,553 | 1991 | - | 5 running line(s) removed |
| `598us2r22_hejm__p016-020` | 1,640 | 2033 | - | 5 running line(s) removed |
| `598us2r22_hejm__p021-025` | 1,731 | 2068 | - | 5 running line(s) removed |
| `598us2r22_hejm__p026-030` | 1,619 | 2061 | - | 5 running line(s) removed |
| `598us2r22_hejm__p031-035` | 1,629 | 2066 | - | 5 running line(s) removed |
| `598us2r22_hejm__p036-039` | 888 | 1437 | - | 5 running line(s) removed |
| `598us2r24_m6hn__p001-005` | 1,806 | 2241 | - | 5 running line(s) removed |
| `598us2r24_m6hn__p006-010` | 1,736 | 2104 | - | 5 running line(s) removed |
| `598us2r24_m6hn__p011-015` | 1,731 | 2036 | - | 5 running line(s) removed |
| `598us2r24_m6hn__p016-020` | 1,742 | 2083 | - | 5 running line(s) removed |
| `598us2r24_m6hn__p021-025` | 1,392 | 1675 | - | 5 running line(s) removed |
| `598us2r25_i32j__p001-005` | 1,929 | 2318 | - | 2 running line(s) removed |
| `598us2r25_i32j__p006-008` | 897 | 1819 | - | 2 running line(s) removed |
| `598us2r26_feag__p001-005` | 1,433 | 1825 | - | 5 running line(s) removed |
| `598us2r26_feag__p006-010` | 1,343 | 1624 | - | 5 running line(s) removed |
| `598us2r27_aplc__p001-005` | 1,743 | 2109 | - | 4 running line(s) removed |
| `598us2r27_aplc__p006-010` | 1,704 | 1969 | - | 4 running line(s) removed |
| `598us2r27_aplc__p011-015` | 1,876 | 2076 | - | 4 running line(s) removed |
| `598us2r27_aplc__p016-020` | 1,605 | 1916 | - | 4 running line(s) removed |
| `598us2r27_aplc__p021-022` | 213 | 633 | - | 4 running line(s) removed |
| `598us2r28_hgcj__p001-005` | 1,846 | 2356 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p006-010` | 1,967 | 2447 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p011-015` | 1,593 | 1985 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p016-020` | 1,599 | 2028 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p021-025` | 1,781 | 2111 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p026-030` | 1,681 | 2060 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p031-035` | 1,545 | 1904 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p036-040` | 1,680 | 2034 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p041-045` | 1,739 | 2094 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p046-050` | 1,683 | 2055 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p051-055` | 1,850 | 2316 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p056-060` | 1,576 | 2016 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p061-065` | 1,665 | 2066 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p066-070` | 1,636 | 2029 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p071-075` | 1,528 | 1942 | - | 5 running line(s) removed |
| `598us2r28_hgcj__p076-080` | 1,404 | 1731 | - | 5 running line(s) removed |
| `598us2r29_k5fm__p001-005` | 1,571 | 1911 | - | 3 running line(s) removed |
| `598us2r29_k5fm__p006-010` | 1,740 | 2107 | - | 3 running line(s) removed |
| `598us2r29_k5fm__p011-012` | 441 | 1297 | - | 3 running line(s) removed |
| `598us2r30_g2bh__p001-005` | 1,718 | 2181 | - | 4 running line(s) removed |
| `598us2r30_g2bh__p006-010` | 1,460 | 1919 | - | 4 running line(s) removed |
| `598us2r30_g2bh__p011-015` | 1,663 | 2054 | - | 4 running line(s) removed |
| `598us2r30_g2bh__p016-020` | 1,621 | 1982 | - | 4 running line(s) removed |
| `598us2r30_g2bh__p021-022` | 163 | 504 | - | 4 running line(s) removed |
| `598us2r31_5h26__p001-005` | 1,703 | 2096 | - | 3 running line(s) removed |
| `598us2r31_5h26__p006-010` | 1,677 | 2048 | - | 3 running line(s) removed |
| `598us2r31_5h26__p011-014` | 1,252 | 1848 | - | 3 running line(s) removed |
| `598us2r32_ca7d__p001-005` | 1,692 | 2117 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p006-010` | 1,651 | 1996 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p011-015` | 1,808 | 2155 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p016-020` | 1,673 | 2058 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p021-025` | 1,594 | 1985 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p026-030` | 1,633 | 2041 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p031-035` | 1,617 | 2019 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p036-040` | 1,638 | 1989 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p041-045` | 1,707 | 2114 | - | 4 running line(s) removed |
| `598us2r32_ca7d__p046-047` | 199 | 618 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p001-005` | 1,672 | 2159 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p006-010` | 2,197 | 2756 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p011-015` | 1,630 | 1972 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p016-020` | 1,610 | 1999 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p021-025` | 1,570 | 1998 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p026-030` | 1,670 | 2114 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p031-035` | 1,708 | 2132 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p036-040` | 1,750 | 2154 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p041-045` | 1,704 | 2087 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p046-050` | 1,713 | 2116 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p051-055` | 1,737 | 2151 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p056-060` | 1,664 | 2148 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p061-065` | 1,841 | 2340 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p066-070` | 1,605 | 2096 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p071-075` | 1,550 | 2024 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p076-080` | 1,724 | 2182 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p081-085` | 1,638 | 2087 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p086-090` | 1,692 | 2135 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p091-095` | 579 | 723 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p096-100` | 1,544 | 1915 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p101-105` | 1,633 | 1981 | - | 4 running line(s) removed |
| `599us1r33_dc8f__p106-111` | 1,730 | 1788 | - | 4 running line(s) removed |
| `599us1r34_p86b__p001-005` | 1,767 | 2280 | - | 4 running line(s) removed |
| `599us1r34_p86b__p006-010` | 1,585 | 1983 | - | 4 running line(s) removed |
| `599us1r34_p86b__p011-015` | 1,742 | 2133 | - | 4 running line(s) removed |
| `599us1r34_p86b__p016-020` | 1,633 | 2051 | - | 4 running line(s) removed |
| `599us1r34_p86b__p021-025` | 1,747 | 2134 | - | 4 running line(s) removed |
| `599us1r34_p86b__p026-030` | 1,721 | 2100 | - | 4 running line(s) removed |
| `599us1r34_p86b__p031-032` | 367 | 1101 | - | 4 running line(s) removed |
| `599us1r35_3f14__p001-005` | 1,701 | 2129 | - | 4 running line(s) removed |
| `599us1r35_3f14__p006-010` | 1,530 | 1856 | - | 4 running line(s) removed |
| `599us1r35_3f14__p011-015` | 1,379 | 1654 | - | 4 running line(s) removed |
| `599us1r35_3f14__p016-020` | 1,602 | 1942 | - | 4 running line(s) removed |
| `599us1r35_3f14__p021-025` | 1,641 | 2000 | - | 4 running line(s) removed |
| `599us1r35_3f14__p026-028` | 680 | 1387 | - | 4 running line(s) removed |
| `599us1r36_feah__p001-005` | 1,768 | 2294 | - | 5 running line(s) removed |
| `599us1r36_feah__p006-010` | 1,713 | 2135 | - | 5 running line(s) removed |
| `599us1r36_feah__p011-015` | 1,757 | 2119 | - | 5 running line(s) removed |
| `599us1r36_feah__p016-020` | 1,579 | 2051 | - | 5 running line(s) removed |
| `599us1r36_feah__p021-025` | 1,628 | 2088 | - | 5 running line(s) removed |
| `599us1r36_feah__p026-030` | 1,670 | 2072 | - | 5 running line(s) removed |
| `599us1r36_feah__p031-035` | 1,620 | 2124 | - | 5 running line(s) removed |
| `599us1r36_feah__p036-040` | 1,667 | 2116 | - | 5 running line(s) removed |
| `599us1r36_feah__p041-045` | 1,721 | 2121 | - | 5 running line(s) removed |
| `599us1r36_feah__p046-050` | 1,620 | 2031 | - | 5 running line(s) removed |
| `599us1r36_feah__p051-055` | 1,606 | 2017 | - | 5 running line(s) removed |
| `599us1r36_feah__p056-060` | 1,639 | 2017 | - | 5 running line(s) removed |
| `599us1r36_feah__p061-065` | 1,751 | 2247 | - | 5 running line(s) removed |
| `599us1r36_feah__p066-070` | 1,579 | 1983 | - | 5 running line(s) removed |
| `599us1r36_feah__p071-072` | 384 | 1146 | - | 5 running line(s) removed |
| `599us1r37_8m59__p001-005` | 1,759 | 2128 | - | 4 running line(s) removed |
| `599us1r37_8m59__p006-010` | 1,754 | 2039 | - | 4 running line(s) removed |
| `599us1r37_8m59__p011-015` | 1,786 | 2115 | - | 4 running line(s) removed |
| `599us1r37_8m59__p016-021` | 1,654 | 1624 | - | 4 running line(s) removed |
| `599us1r39_3204__p001-005` | 1,486 | 1930 | - | 6 running line(s) removed |
| `599us1r39_3204__p006-010` | 1,489 | 1886 | - | 6 running line(s) removed |
| `599us1r39_3204__p011-015` | 1,549 | 2044 | - | 6 running line(s) removed |
| `599us1r39_3204__p016-020` | 1,591 | 2052 | - | 6 running line(s) removed |
| `599us1r39_3204__p021-025` | 1,604 | 2001 | - | 6 running line(s) removed |
| `599us1r39_3204__p026-030` | 1,644 | 2055 | - | 6 running line(s) removed |
| `599us1r39_3204__p031-035` | 1,633 | 2012 | - | 6 running line(s) removed |
| `599us1r39_3204__p036-039` | 869 | 1350 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p001-005` | 1,778 | 2219 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p006-010` | 1,625 | 1993 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p011-015` | 1,567 | 1951 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p016-020` | 1,733 | 2099 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p021-025` | 1,526 | 1841 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p026-030` | 1,680 | 2100 | - | 6 running line(s) removed |
| `599us1r40_q8l1__p031-036` | 1,870 | 1902 | - | 6 running line(s) removed |
| `599us1r41_2bo2__p001-005` | 1,400 | 1803 | - | 5 running line(s) removed |
| `599us1r41_2bo2__p006-010` | 1,464 | 1891 | - | 5 running line(s) removed |
| `599us1r41_2bo2__p011-014` | 809 | 1338 | - | 5 running line(s) removed |
| `599us1r42_2b35__p001-005` | 1,811 | 2258 | - | 5 running line(s) removed |
| `599us1r42_2b35__p006-010` | 1,690 | 1995 | - | 5 running line(s) removed |
| `599us1r42_2b35__p011-015` | 1,666 | 2070 | - | 5 running line(s) removed |
| `599us1r42_2b35__p016-020` | 1,746 | 2134 | - | 5 running line(s) removed |
| `599us1r42_2b35__p021-025` | 1,908 | 2291 | - | 5 running line(s) removed |
| `599us1r42_2b35__p026-030` | 1,698 | 2133 | - | 5 running line(s) removed |
| `599us1r42_2b35__p031-035` | 1,591 | 1947 | - | 5 running line(s) removed |
| `599us1r42_2b35__p036-040` | 1,681 | 2082 | - | 5 running line(s) removed |
| `599us1r42_2b35__p041-045` | 1,694 | 2080 | - | 5 running line(s) removed |
| `599us1r42_2b35__p046-050` | 1,630 | 2052 | - | 5 running line(s) removed |
| `599us1r42_2b35__p051-055` | 1,674 | 2070 | - | 5 running line(s) removed |
| `599us1r42_2b35__p056-060` | 1,698 | 2155 | - | 5 running line(s) removed |
| `599us1r42_2b35__p061-065` | 1,892 | 2319 | - | 5 running line(s) removed |
| `599us1r42_2b35__p066-070` | 1,281 | 1598 | - | 5 running line(s) removed |
| `599us1r43_jhek__p001-005` | 1,698 | 2221 | - | 4 running line(s) removed |
| `599us1r43_jhek__p006-010` | 1,524 | 1949 | - | 4 running line(s) removed |
| `599us1r43_jhek__p011-015` | 1,575 | 1995 | - | 4 running line(s) removed |
| `599us1r43_jhek__p016-020` | 1,689 | 2094 | - | 4 running line(s) removed |
| `599us1r43_jhek__p021-024` | 848 | 1279 | - | 4 running line(s) removed |
| `599us1r44_54l8__p001-005` | 1,690 | 2066 | - | 4 running line(s) removed |
| `599us1r44_54l8__p006-010` | 1,645 | 2007 | - | 4 running line(s) removed |
| `599us1r44_54l8__p011-015` | 1,776 | 2127 | - | 4 running line(s) removed |
| `599us1r44_54l8__p016-020` | 1,730 | 2091 | - | 4 running line(s) removed |
| `599us1r44_54l8__p021-025` | 1,597 | 1923 | - | 4 running line(s) removed |
| `599us1r44_54l8__p026-030` | 1,680 | 2032 | - | 4 running line(s) removed |
| `599us1r44_54l8__p031-035` | 1,660 | 2020 | - | 4 running line(s) removed |
| `599us1r44_54l8__p036-040` | 1,651 | 1964 | - | 4 running line(s) removed |
| `599us1r44_54l8__p041-045` | 1,725 | 2047 | - | 4 running line(s) removed |
| `599us1r44_54l8__p046-047` | 448 | 1328 | - | 4 running line(s) removed |
| `599us1r45_6537__p001-005` | 1,447 | 1854 | - | 4 running line(s) removed |
| `599us1r45_6537__p006-010` | 1,709 | 2178 | - | 4 running line(s) removed |
| `599us1r45_6537__p011-015` | 1,599 | 2033 | - | 4 running line(s) removed |
| `599us1r45_6537__p016-020` | 1,681 | 2106 | - | 4 running line(s) removed |
| `599us1r45_6537__p021-025` | 1,842 | 2261 | - | 4 running line(s) removed |
| `599us1r45_6537__p026-030` | 1,704 | 2147 | - | 4 running line(s) removed |
| `599us1r45_6537__p031-035` | 1,666 | 2092 | - | 4 running line(s) removed |
| `599us1r45_6537__p036-037` | 386 | 1223 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p001-005` | 1,805 | 2272 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p006-010` | 1,627 | 2060 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p011-015` | 1,549 | 1956 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p016-020` | 1,566 | 1989 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p021-025` | 1,614 | 1988 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p026-030` | 1,673 | 2065 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p031-035` | 1,650 | 2110 | - | 4 running line(s) removed |
| `599us1r46_dc8f__p036-037` | 412 | 1298 | - | 4 running line(s) removed |
| `599us1r47_8m58__p001-005` | 1,704 | 2192 | - | 4 running line(s) removed |
| `599us1r47_8m58__p006-010` | 1,665 | 2031 | - | 4 running line(s) removed |
| `599us1r47_8m58__p011-015` | 1,697 | 2145 | - | 4 running line(s) removed |
| `599us1r47_8m58__p016-020` | 1,671 | 2086 | - | 4 running line(s) removed |
| `599us1r47_8m58__p021-025` | 1,726 | 2083 | - | 4 running line(s) removed |
| `599us1r47_8m58__p026-030` | 1,691 | 2083 | - | 4 running line(s) removed |
| `599us1r47_8m58__p031-035` | 1,711 | 2078 | - | 4 running line(s) removed |
| `599us1r47_8m58__p036-040` | 1,684 | 2069 | - | 4 running line(s) removed |
| `599us1r47_8m58__p041-045` | 1,587 | 1980 | - | 4 running line(s) removed |
| `599us1r47_8m58__p046-050` | 1,602 | 1964 | - | 4 running line(s) removed |
| `599us1r47_8m58__p051-055` | 1,671 | 2047 | - | 4 running line(s) removed |
| `599us1r47_8m58__p056-060` | 1,642 | 2029 | - | 4 running line(s) removed |
| `599us1r47_8m58__p061-065` | 1,742 | 2177 | - | 4 running line(s) removed |
| `599us1r47_8m58__p066-068` | 689 | 1375 | - | 4 running line(s) removed |
| `599us1r48_986b__p001-005` | 1,541 | 1978 | - | 5 running line(s) removed |
| `599us1r48_986b__p006-010` | 1,758 | 2153 | - | 5 running line(s) removed |
| `599us1r48_986b__p011-015` | 1,589 | 2032 | - | 5 running line(s) removed |
| `599us1r48_986b__p016-020` | 1,718 | 2112 | - | 5 running line(s) removed |
| `599us1r48_986b__p021-025` | 1,703 | 2126 | - | 5 running line(s) removed |
| `599us1r48_986b__p026-028` | 637 | 1387 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p001-005` | 1,738 | 2272 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p006-010` | 1,625 | 2033 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p011-015` | 1,610 | 2045 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p016-020` | 1,660 | 2084 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p021-025` | 1,668 | 2087 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p026-030` | 1,725 | 2132 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p031-035` | 1,583 | 2034 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p036-040` | 1,563 | 2006 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p041-045` | 1,720 | 2178 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p046-050` | 1,600 | 2038 | - | 5 running line(s) removed |
| `599us1r49_jgkn__p051-053` | 499 | 1074 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p001-005` | 1,679 | 2139 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p006-010` | 2,085 | 2581 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p011-015` | 1,603 | 1971 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p016-020` | 1,673 | 2032 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p021-025` | 1,593 | 1990 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p026-030` | 1,523 | 2012 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p031-035` | 1,579 | 1988 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p036-040` | 1,639 | 2058 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p041-045` | 1,604 | 1988 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p046-050` | 1,795 | 2178 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p051-055` | 1,865 | 2263 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p056-060` | 1,788 | 2196 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p061-065` | 1,739 | 2180 | - | 5 running line(s) removed |
| `600us1r50_h3ci__p066-067` | 450 | 1405 | - | 5 running line(s) removed |
| `600us1r51_g3bi__p001-005` | 1,699 | 2124 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p006-010` | 1,681 | 2052 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p011-015` | 1,760 | 2191 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p016-020` | 1,604 | 2009 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p021-025` | 1,614 | 2042 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p026-030` | 1,735 | 2134 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p031-035` | 1,688 | 2023 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p036-040` | 1,691 | 2085 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p041-045` | 1,585 | 1988 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p046-050` | 1,703 | 2101 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p051-055` | 1,621 | 2003 | - | 4 running line(s) removed |
| `600us1r51_g3bi__p056-058` | 492 | 973 | - | 4 running line(s) removed |
| `600us1r52_7l48__p001-005` | 1,676 | 2087 | - | 3 running line(s) removed |
| `600us1r52_7l48__p006-010` | 1,670 | 2026 | - | 3 running line(s) removed |
| `600us1r52_7l48__p011-015` | 1,697 | 2037 | - | 3 running line(s) removed |
| `600us1r52_7l48__p016-020` | 1,680 | 2081 | - | 3 running line(s) removed |
| `600us1r52_7l48__p021-025` | 1,489 | 1854 | - | 3 running line(s) removed |
| `600us1r52_7l48__p026-030` | 1,594 | 2045 | - | 3 running line(s) removed |
| `600us1r52_7l48__p031-035` | 1,686 | 2068 | - | 3 running line(s) removed |
| `600us1r52_7l48__p036-040` | 1,750 | 2127 | - | 3 running line(s) removed |
| `600us1r52_7l48__p041-045` | 1,615 | 2010 | - | 3 running line(s) removed |
| `600us1r52_7l48__p046-050` | 1,643 | 2065 | - | 3 running line(s) removed |
| `600us1r52_7l48__p051-055` | 1,804 | 2208 | - | 3 running line(s) removed |
| `600us1r52_7l48__p056-061` | 1,817 | 1837 | - | 3 running line(s) removed |
| `600us1r54_g3bi__p001-005` | 1,623 | 2105 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p006-010` | 1,604 | 2015 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p011-015` | 1,690 | 2069 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p016-020` | 1,642 | 1987 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p021-025` | 1,663 | 2050 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p026-030` | 1,628 | 2027 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p031-035` | 1,837 | 2319 | - | 5 running line(s) removed |
| `600us1r54_g3bi__p036-037` | 427 | 1323 | - | 5 running line(s) removed |
| `600us1r55_3dq4__p001-005` | 1,832 | 2297 | - | 4 running line(s) removed |
| `600us1r55_3dq4__p006-010` | 1,981 | 2444 | - | 4 running line(s) removed |
| `600us1r55_3dq4__p011-015` | 1,628 | 2008 | - | 4 running line(s) removed |
| `600us1r55_3dq4__p016-020` | 1,753 | 2154 | - | 4 running line(s) removed |
| `600us1r55_3dq4__p021-025` | 1,668 | 2068 | - | 4 running line(s) removed |
| `600us1r55_3dq4__p026-030` | 1,616 | 1985 | - | 4 running line(s) removed |
| `600us1r55_3dq4__p031-032` | 252 | 782 | - | 4 running line(s) removed |
| `600us1r56_1o13__p001-005` | 1,843 | 2302 | - | 5 running line(s) removed |
| `600us1r56_1o13__p006-010` | 1,830 | 2298 | - | 5 running line(s) removed |
| `600us1r56_1o13__p011-015` | 1,570 | 1996 | - | 5 running line(s) removed |
| `600us1r56_1o13__p016-020` | 1,672 | 2048 | - | 5 running line(s) removed |
| `600us1r56_1o13__p021-025` | 1,656 | 2077 | - | 5 running line(s) removed |
| `600us1r56_1o13__p026-030` | 1,700 | 2087 | - | 5 running line(s) removed |
| `600us1r56_1o13__p031-035` | 1,649 | 2123 | - | 5 running line(s) removed |
| `600us1r56_1o13__p036-040` | 1,710 | 2109 | - | 5 running line(s) removed |
| `600us1r56_1o13__p041-045` | 1,726 | 2126 | - | 5 running line(s) removed |
| `600us1r56_1o13__p046-050` | 1,625 | 2003 | - | 5 running line(s) removed |
| `600us1r56_1o13__p051-055` | 1,732 | 2094 | - | 5 running line(s) removed |
| `600us1r56_1o13__p056-060` | 1,715 | 2128 | - | 5 running line(s) removed |
| `600us1r56_1o13__p061-065` | 1,738 | 2156 | - | 5 running line(s) removed |
| `600us1r56_1o13__p066-070` | 1,603 | 1993 | - | 5 running line(s) removed |
| `600us1r56_1o13__p071-076` | 1,543 | 1620 | - | 5 running line(s) removed |
| `600us1r57_o7kq__p001-005` | 1,768 | 2251 | - | 4 running line(s) removed |
| `600us1r57_o7kq__p006-010` | 1,602 | 2051 | - | 4 running line(s) removed |
| `600us1r57_o7kq__p011-015` | 1,546 | 1925 | - | 4 running line(s) removed |
| `600us1r57_o7kq__p016-021` | 1,432 | 1457 | - | 4 running line(s) removed |
| `600us1r58_7khn__p001-005` | 1,823 | 2309 | - | 5 running line(s) removed |
| `600us1r58_7khn__p006-010` | 2,240 | 2691 | - | 5 running line(s) removed |
| `600us1r58_7khn__p011-015` | 1,563 | 1930 | - | 5 running line(s) removed |
| `600us1r58_7khn__p016-020` | 1,655 | 1998 | - | 5 running line(s) removed |
| `600us1r58_7khn__p021-025` | 1,735 | 2103 | - | 5 running line(s) removed |
| `600us1r58_7khn__p026-030` | 1,772 | 2137 | - | 5 running line(s) removed |
| `600us1r58_7khn__p031-035` | 1,754 | 2149 | - | 5 running line(s) removed |
| `600us1r58_7khn__p036-040` | 1,835 | 2181 | - | 5 running line(s) removed |
| `600us1r58_7khn__p041-045` | 1,776 | 2079 | - | 5 running line(s) removed |
| `600us1r58_7khn__p046-050` | 1,695 | 2037 | - | 5 running line(s) removed |
| `600us1r58_7khn__p051-055` | 1,616 | 1968 | - | 5 running line(s) removed |
| `600us1r58_7khn__p056-060` | 1,645 | 2000 | - | 5 running line(s) removed |
| `600us1r58_7khn__p061-065` | 1,659 | 2039 | - | 5 running line(s) removed |
| `600us1r58_7khn__p066-070` | 1,779 | 2084 | - | 5 running line(s) removed |
| `600us1r58_7khn__p071-073` | 671 | 1308 | - | 5 running line(s) removed |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
