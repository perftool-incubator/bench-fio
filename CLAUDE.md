# Bench-FIO

## Purpose
Scripts and configuration to run the fio I/O benchmark within the crucible framework. Handles job file preparation, benchmark execution, and post-processing of fio log files into crucible metrics.

## Languages
- Bash: `fio-prepare-jobfile`, `fio-get-runtime`
- Perl: `fio-post-process`

## Key Files
| File | Purpose |
|------|---------|
| `rickshaw.json` | Rickshaw integration: pre/post scripts, client command, parameter transformations |
| `multiplex.json` | Parameter validation rules, unit conversions, and presets for multiplex |
| `fio-prepare-jobfile` | Copies fio job file to working directory before benchmark starts |
| `fio-post-process` | Parses fio log files (iops, bw, lat, clat, slat), generates metrics, identifies primary period |
| `fio-get-runtime` | Extracts `--runtime` value from command-line options |
| `workshop.json` | Engine image build: installs fio |
| `params` | Default multiplex parameters |

## Post-Processing
- Parses 5 log types: iops, bw, lat, clat, slat
- Primary metric: iops (used to determine measurement periods)
- Uses `toolbox::metrics` and `toolbox::json` from `$TOOLBOX_HOME/perl`
- Outputs `post-process-data.json` with period information

## Conventions
- Primary branch is `master`
- Standard Bash/Perl modelines and 4-space indentation
- Path variables: `%bench-dir%` (benchmark repo location), `%run-dir%` (rickshaw run directory)
