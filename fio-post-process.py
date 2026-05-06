#!/usr/bin/env python3
# -*- mode: python; indent-tabs-mode: nil; python-indent-level: 4 -*-
# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=python

import json
import os
import re
import sys
from pathlib import Path

TOOLBOX_HOME = os.environ.get("TOOLBOX_HOME")
if TOOLBOX_HOME:
    sys.path.append(str(Path(TOOLBOX_HOME) / "python"))

from toolbox.cdm_metrics import CDMMetrics
from toolbox.fileio import open_read_text_file


def main():
    metrics = CDMMetrics()
    type_map = {
        "iops": {"source": "fio", "class": "throughput", "type": "iops"},
        "bw": {"source": "fio", "class": "throughput", "type": "bw-KiBs"},
        "lat": {"source": "fio", "class": "count", "type": "latency-usec"},
        "clat": {"source": "fio", "class": "count", "type": "completion-latency-usec"},
        "slat": {"source": "fio", "class": "count", "type": "submission-latency-usec"},
    }
    io_oper_map = {"0": "Read", "1": "Write", "2": "Trim"}

    for log_file in sorted(os.listdir(".")):
        m = re.match(r'^fio_([a-z]+)\.(\d+)\.log(\.xz)?$', log_file)
        if not m:
            print(f"Not considering {log_file} for processing")
            continue

        fio_type = m.group(1)
        job_id = m.group(2)
        print(f"found file {log_file}")

        if fio_type not in type_map:
            print(f"fio log file {fio_type} not recognized, skipping")
            continue

        desc = type_map[fio_type].copy()
        names = {"job": job_id}

        try:
            fh, _ = open_read_text_file(log_file)
        except FileNotFoundError:
            print(f"ERROR: could not open file {log_file}")
            continue

        for line in fh:
            m = re.match(r'^(\d+),\s+(\d+),\s+(\d+),\s+(\d+)', line)
            if m:
                timestamp_ms = int(m.group(1))
                value = int(m.group(2))
                io_oper = m.group(3)
                if int(io_oper) > 2:
                    continue
                names["cmd"] = io_oper_map.get(io_oper, io_oper)
                sample = {"end": timestamp_ms, "value": value}
                metrics.log_sample("0", desc, names, sample)
        fh.close()

    metric_data_name = metrics.finish_samples()

    sample = {
        "rickshaw-bench-metric": {"schema": {"version": "2021.04.12"}},
        "benchmark": "fio",
        "primary-metric": "iops",
        "primary-period": "measurement",
        "periods": [
            {
                "name": "measurement",
                "metric-files": [metric_data_name],
            }
        ],
    }

    with open("post-process-data.json", "w") as f:
        json.dump(sample, f)


if __name__ == "__main__":
    main()
