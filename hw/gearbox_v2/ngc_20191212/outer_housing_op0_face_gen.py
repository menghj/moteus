#!/usr/bin/python3

PREFIX = """
%
(AXIS,stop)
(MK2_OUTER_HOUSING_OP0_PART)
N10 G21
N15 G90 G94 G40 G17 G91.1
N20 G53 G0 Z0.
(OD FINISH)
N25 G49
N30 M5
N35 G53 G0 X63.5 Y63.5
N40 M0
N45 T10 M6
N50 S47000 M3
N55 G54 G0
N60 G43 Z66.799 H10

N100 G0 A0. B{bstart}
N200 G1 X0 Y{y:.3f} F10000.

N400 X0 Z53 F10000.

N500 Z43 F750.
N550 G93
"""

POSTFIX = """
N5000 G94
N5010 F10000.
N5020 Z53

N5820 X46.788 Z68.284 F10000.
N5825 G49
N5830 G53 G0 Z0.
N5835 G49
N5840 G53 G0 X63.5 Y63.5
N5845 M5
N5855 M30
(AXIS,stop)
%
"""

MOVE = """
N{line1} B{b1} Y{y:.3f} F20
N{line2} B{b2} F2
"""

def main():
    REF_TO_STOCK_BOTTOM = 24.717
    STOCK_HEIGHT = 33.5
    MODEL_TOP = 26.8
    TOOL_DIAMETER = 4

    YSTART = REF_TO_STOCK_BOTTOM + STOCK_HEIGHT + 0.5 * TOOL_DIAMETER
    YEND = REF_TO_STOCK_BOTTOM + MODEL_TOP + 0.5 * TOOL_DIAMETER
    YSTEP = 0.15

    y = YSTART
    b = 7000
    line = 1000

    print(PREFIX.format(y=y, bstart=b))

    while True:
        y = max(y - YSTEP, YEND)

        print(MOVE.format(y=y, b1=b-20, b2=b-360, line1=line, line2 = line +5))

        b -= 360
        line += 10

        if y == YEND:
            break

    print("N{line} B{b} F2".format(line=line, b=b-360))

    print(POSTFIX)

if __name__ == '__main__':
    main()
