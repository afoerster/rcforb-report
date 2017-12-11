#!/usr/bin/env python
import sqlite3
import csv
import yaml
import os.path

REPORTS_DIR='reports'
DATABASE_PATH='database_path'
QUERY='query'
NAME='name'

def main(conf):
    conn = sqlite3.connect(conf[DATABASE_PATH])
    if not os.path.exists(REPORTS_DIR):
        os.mkdir(REPORTS_DIR)
    for report in conf[REPORTS_DIR]:
        cursor = conn.execute(report[QUERY])
        table = prepare_table(cursor)
        save(os.path.join(REPORTS_DIR, report[NAME]), table)


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
    with open('conf.yml', 'r') as f:
        conf = yaml.load(f)
        main(conf)
