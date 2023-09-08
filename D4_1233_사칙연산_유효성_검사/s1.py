"""
1
171
1 - 2 3
2 - 4 5
3 + 6 7
4 / 8 9
5 - 10 11
6 + 12 13
7 - 14 15
8 - 16 17
9 * 18 19
10 7 20 21
11 * 22 23
12 - 24 25
13 * 26 27
14 / 28 29
15 + 30 31
16 - 32 33
17 / 34 35
18 * 36 37
19 * 38 39
20 3 40 41
21 + 42 43
22 - 44 45
23 / 46 47
24 * 48 49
25 * 50 51
26 / 52 53
27 - 54 55
28 - 56 57
29 + 58 59
30 / 60 61
31 / 62 63
32 * 64 65
33 / 66 67
34 / 68 69
35 - 70 71
36 / 72 73
37 + 74 75
38 - 76 77
39 * 78 79
40 + 80 81
41 2 82 83
42 * 84 85
43 / 86 87
44 - 88 89
45 - 90 91
46 - 92 93
47 * 94 95
48 / 96 97
49 * 98 99
50 + 100 101
51 * 102 103
52 + 104 105
53 * 106 107
54 / 108 109
55 * 110 111
56 - 112 113
57 / 114 115
58 * 116 117
59 - 118 119
60 * 120 121
61 * 122 123
62 * 124 125
63 * 126 127
64 + 128 129
65 - 130 131
66 * 132 133
67 - 134 135
68 / 136 137
69 + 138 139
70 / 140 141
71 / 142 143
72 - 144 145
73 * 146 147
74 * 148 149
75 - 150 151
76 - 152 153
77 * 154 155
78 + 156 157
79 * 158 159
80 / 160 161
81 - 162 163
82 9 164 165
83 3 166 167
84 / 168 169
85 * 170 171
86 4
87 2
88 8
89 3
90 6
91 3
92 6
93 8
94 1
95 9
96 4
97 4
98 3
99 3
100 7
101 7
102 2
103 2
104 7
105 9
106 7
107 1
108 8
109 3
110 9
111 3
112 6
113 3
114 1
115 7
116 2
117 1
118 7
119 9
120 2
121 7
122 9
123 3
124 7
125 1
126 9
127 3
128 6
129 9
130 1
131 9
132 7
133 8
134 1
135 6
136 8
137 9
138 1
139 7
140 2
141 3
142 4
143 4
144 2
145 2
146 8
147 8
148 3
149 1
150 6
151 6
152 7
153 4
154 3
155 1
156 6
157 9
158 4
159 3
160 4
161 1
162 4
163 -
164 -
165 *
166 -
167 *
168 -
169 7
170 4
171 2
#1 0
"""


def order_tree(parent):
    global answer

    if node_f[parent]:
        order_tree(node_f[parent])
        order_tree(node_s[parent])

        if tree[parent] == '-':
            try:
                tree[parent] = str(int(tree[node_f[parent]]) - int(tree[node_s[parent]]))
            except ValueError:
                answer = 0
        elif tree[parent] == '+':
            try:
                tree[parent] = str(int(tree[node_f[parent]]) + int(tree[node_s[parent]]))
            except ValueError:
                answer = 0
        elif tree[parent] == '*':
            try:
                tree[parent] = str(int(tree[node_f[parent]]) * int(tree[node_s[parent]]))
            except ValueError:
                answer = 0
        elif tree[parent] == '/':
            try:
                tree[parent] = str(int(tree[node_f[parent]]) // int(tree[node_s[parent]]))
            except ZeroDivisionError:
                answer = 0
            except ValueError:
                answer = 0
        else:
            answer = 0


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = 1
    tree = [[] for _ in range(n + 1)]
    node_f = [[] for _ in range(n + 1)]
    node_s = [[] for _ in range(n + 1)]

    for _ in range(n):
        arr = list(map(str, input().split()))

        if len(arr) == 4:
            tree[int(arr[0])] = arr[1]
            node_f[int(arr[0])] = int(arr[2])
            node_s[int(arr[0])] = int(arr[3])
        else:
            tree[int(arr[0])] = arr[1]

    order_tree(1)

    print(f"#{tc} {answer}")
