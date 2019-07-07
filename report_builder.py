#!/usr/bin/env python
import sqlite3
import csv
import yaml
import os.path
import datetime

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
        save(report[NAME], table)
    conn.close
    print("Finished")


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


def save(report_name, table):
    print("creating report '{}'.".format(report_name))
    now = datetime.datetime.now()
    date = "{}-{}-{}".format(now.year, now.month, now.day)
    date_dir = os.path.join(REPORTS_DIR, date)
    if not os.path.exists(date_dir):
        os.mkdir(date_dir)

    out_file = os.path.join(date_dir, report_name)
    print("saving report to '{}'.".format(out_file))

    with open(out_file, 'w') as f:
        wr = csv.writer(f)
        for row in table:
            wr.writerow(row)
    


if __name__ == '__main__':
    with open('conf.yml', 'r') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        main(conf)
