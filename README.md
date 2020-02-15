# fio
A collection of scripts and configuration files to help run the Fio benchmark.  This does not include the actual fio benchmark.

### config files
- config.json: This configuration is used by the rickshaw project, so it knows how to run fio.  A few notable items in this file:
  - \%bench-dir\% refers to the directory where this fio repo is installed (on the same host as rickshaw)
  - \%run-dir\% refers to the run directory for rickshaw, which is set with --run-dir for the rickshaw command line

### scripts
- fio-prepare-jobfile: This is a script used by the rickshaw project and is referenced in the config.json, controler.pre-script, and is executed before the benchmark is run in order to copy the fio job file to tright location


