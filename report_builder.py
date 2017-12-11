#!/usr/bin/env python
import sqlite3
import csv
import yaml
import os.path

REPORTS_DIR='reports'

def main(conf):
    conn = sqlite3.connect(conf['database_path'])
    if not os.path.exists('reports'):
        os.mkdir(REPORTS_DIR)
    for report in conf['reports']:
        cursor = conn.execute(report['query'])
        table = prepare_table(cursor)
        save(os.path.join(REPORTS_DIR, report['name']), table)


def prepare_table(cursor):
    colnames = cursor.description
    results = []
    header = []
    for row in colnames:
        header.append(row[0])

    results.append(tuple(header))
    for row in cursor:
        results.append(row)

    return results


def save(out_file, table):
    with open(out_file, 'w') as f:
        wr = csv.writer(f)
        for row in table:
            wr.writerow(row)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('usage: script <conf.yml>')
        exit(1)
    else:
        conf = sys.argv[1]
        if not os.path.exists(conf):
            print('file not found: ' + conf)
            exit(1)
        with open('conf.yml', 'r') as f:
            conf = yaml.load(f)
            main(conf)
        exit(0)
