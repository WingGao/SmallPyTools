# coding=utf-8
import traceback
import re
import json


def strip(x):
    if isinstance(x, list):
        return [i.strip() for i in x]
    return x.strip()


def proc(lines):
    for line_num, line in enumerate(lines):
        # print line
        spans = line.strip().split('\t')
        spans = [i.strip() for i in spans]
        # print spans
        try:
            print str.format('{{ id:{0}, name:"{1}", company:"{2}", title:"{3}" }},', line_num, *spans)
        except:
            traceback.print_exc()
            print 'Error Line', line_num + 1
            return


def proc_re(lines):
    points = []
    for line_num, line in enumerate(lines):
        spans = re.findall('\{.*?\}', line)
        for span in spans:
            s2 = strip(span.split(';'))
            point = {}
            for s3 in s2:
                if s3.startswith('left'):
                    point['x'] = int(s3.split(':')[1][:-2])
                elif s3.startswith('top'):
                    point['y'] = int(s3.split(':')[1][:-2])
                elif s3.startswith('width'):
                    point['w'] = int(s3.split(':')[1][:-2])
            points.append(point)

    print json.dumps(points)


if __name__ == '__main__':
    with open('t.txt', 'r') as f:
        lines = f.readlines()

    # proc(lines)
    proc_re(lines)
