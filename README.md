# bench-fio
[![CI Actions Status](https://github.com/perftool-incubator/bench-fio/workflows/crucible-ci/badge.svg)](https://github.com/perftool-incubator/bench-fio/actions)

Scripts and configuration to run the [fio](https://github.com/axboe/fio) I/O benchmark within the [crucible](https://github.com/perftool-incubator/crucible) performance testing framework. This does not include the actual fio benchmark.

## Key Files

| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: defines how to run and post-process fio |
| `multiplex.json` | Parameter validation and expansion requirements for multiplex |
| `fio-prepare-jobfile` | Pre-benchmark script: copies the fio job file to the working directory |
| `fio-post-process` | Post-benchmark script: parses fio log files (iops, bw, lat, clat, slat) into crucible metrics |
| `fio-get-runtime` | Extracts runtime from command-line options |
| `workshop.json` | Engine image build requirements |
| `params` | Default multiplex parameters |

## Path Variables

- `%bench-dir%` — Directory where this fio repo is installed (on the controller host)
- `%run-dir%` — Run directory for rickshaw, set with `--run-dir`
