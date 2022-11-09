"""
Description: This class will implement a simplified LZW compression
algorithm to compress text files.  The characters include all uppercase
letters, comma and period as a beginning table.  The algorithm will use
text patterns to build the rest of the table for the input file.  The
output will be stored in another textfile 'mslzw.txt'.
"""


class Lzw:
    def __init__(self, text1):
        self.compress(text1)

    def compress(self, file1):
        """
        This method will implement the LZW compression of a text file.
        :param file1: takes text file as input.
        :return: result: returns a list of lzw compression result
        values.
        """
        letter_string = ''
        with open(file1) as file:
            for letter in file.read():
                letter_string += letter.upper()

        # build initial table (letter_dict: dict) for text.
        letter_dict = {chr(i): (i - 65) for i in range(65, 91, 1)}
        letter_dict[' '] = 26
        letter_dict[','] = 27
        letter_dict['.'] = 28

        # instantiate useful variables for algorithm
        dict_size = len(letter_dict)
        check_str = ""
        result = []

        for letter in letter_string:
            str_letter = check_str + letter
            if str_letter in letter_dict:
                check_str = str_letter
            else:
                result.append(letter_dict[check_str])
                letter_dict[str_letter] = dict_size
                dict_size += 1
                check_str = letter
                # prints code table
                print(str_letter, dict_size)

        self.write_file(result)
        return result

    def write_file(self, result_list):
        """
        Method will create a text file of LZW algorithm table values.
        :param result_list: list output from compression algorithm
        :return: None
        """
        with open('mslzw.txt', 'w') as f:
            for item in result_list:
                f.writelines(f"{str(item)}\n")
        print(f"File: {f.name} has been written successfully.")

    def decode(self):
        pass


def main():
    lzw1 = Lzw('tt.txt')


if __name__ == "__main__":
    main()

"""    --- SAMPLE RUN & CODE TABLE ---
TH 30
HE 31
E  32
 T 33
TI 34
IM 35
ME 36
E T 37
TR 38
RA 39
AV 40
VE 41
EL 42
LL 43
LE 44
ER 45
R, 46
,  47
 F 48
FO 49
OR 50
R  51
 S 52
SO 53
O  54
 I 55
IT 56
T  57
 W 58
WI 59
IL 60
LL  61
 B 62
BE 63
E C 64
CO 65
ON 66
NV 67
VEN 68
NI 69
IE 70
EN 71
NT 72
T T 73
TO 74
O S 75
SP 76
PE 77
EA 78
AK 79
K  80
 O 81
OF 82
F  83
 H 84
HI 85
IM, 86
, W 87
WA 88
AS 89
S  90
 E 91
EX 92
XP 93
PO 94
OU 95
UN 96
ND 97
DI 98
IN 99
NG 100
G  101
 A 102
A  103
 R 104
RE 105
EC 106
CON 107
NDI 108
ITE 109
E M 110
MA 111
AT 112
TT 113
TE 114
ER  115
 TO 116
O U 117
US 118
S. 119
.  120
 HI 121
IS 122
S G 123
GR 124
REY 125
Y  126
 EY 127
YE 128
ES 129
S S 130
SH 131
HO 132
ONE 133
E A 134
AN 135
ND  136
 TW 137
WIN 138
NK 139
KL 140
LED 141
D, 142
, A 143
AND 144
D  145
 HIS 146
S U 147
USU 148
UA 149
AL 150
LLY 151
Y P 152
PA 153
ALE 154
E F 155
FA 156
AC 157
CE 158
E W 159
WAS 160
S F 161
FL 162
LU 163
USH 164
HED 165
D A 166
AND  167
 AN 168
NIM 169
MAT 170
TED 171
D. 172
. T 173
THE 174
E FI 175
IR 176
RE  177
 BU 178
UR 179
RN 180
NE 181
ED 182
D B 183
BR 184
RI 185
IG 186
GH 187
HT 188
TL 189
LY 190
Y A 191
AND T 192
THE  193
 SO 194
OFT 195
T R 196
RAD 197
DIA 198
ANC 199
CE  200
 OF 201
F T 202
THE I 203
INC 204
CA 205
ANDE 206
ESC 207
CEN 208
NT  209
 L 210
LI 211
IGH 212
HTS 213
S I 214
IN  215
 TH 216
HE  217
 LI 218
ILI 219
IES 220
S O 221
OF  222
 SI 223
ILV 224
VER 225
R C 226
CAU 227
UG 228
GHT 229
T TH 230
HE B 231
BU 232
UB 233
BB 234
BL 235
LES 236
S T 237
THA 238
AT  239
 FL 240
LA 241
ASH 242
HED  243
 AND 244
D P 245
PAS 246
SS 247
SE 248
ED  249
 IN 250
N  251
 OU 252
UR  253
 G 254
GL 255
LAS 256
SSE 257
ES. 258
File: mslzw.txt has been written successfully.

Process finished with exit code 0

"""

