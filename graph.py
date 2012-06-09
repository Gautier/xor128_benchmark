import sys

import numpy as np
import matplotlib.pyplot as plt

def parse_results(results_file):
    with open(results_file) as f:
        lines = f.read().splitlines()

    header = lines[0].split(',')
    content = [map(int, line.split(',')) for line in lines[1:]]
    ns = [int(line.split(',')[0]) for line in lines[1:]]

    results = dict()

    for i, test_type in enumerate(header[1:]):
        results[test_type] = [result[i+1] for result in content]

    return ns, results

def plot_results(ns, results, output_file):
    N = len(results.values()[0])
    ind = np.arange(N)

    width = .1

    plt.subplot(111)

    palette = ((  0,   0,   0), 
               (255, 255, 255),
               (250,  60,  60),
               (  0, 220,   0),
               ( 30,  60, 255),
               (  0, 200, 200),
               (240,   0, 130),
               (230, 220,  50),
               (240, 130,  40),
               (160,   0, 200),
               (160, 230,  50),
               (  0, 160, 255),
               (230, 175,  45),
               (  0, 210, 140),
               (130,   0, 220),
               (170, 170, 170))
    palette = [map(lambda x: x / 255., p) for p in palette]

    plt.ylabel('N')
    plt.yticks(ind+width, ["%.4g" % n for n in ns])
    plt.xlabel('time in ms')
    plt.xscale('log')

    rects = []
    legends = []
    for i, (legend, result) in enumerate(results.items()):
        color = palette[i]
        rects.append(plt.barh(ind + (i * width),
                              result,
                              width,
                              color=color))
        legends.append(legend)

    plt.legend((rect[0] for rect in rects), legends, loc='lower right')

    plt.savefig(output_file, format='png')
    plt.show()

def main():
    if len(sys.argv) < 3:
        print "usage: python graph.py RESULT_CSV OUTPUT"
        return

    arguments = sys.argv[1:]

    results_file, output_file = arguments[0], arguments[1]
    ns, results = parse_results(results_file)
    plot_results(ns, results, output_file)

if __name__  == "__main__":
    main()
