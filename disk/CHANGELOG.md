# CHANGELOG - disk

<!-- towncrier release notes start -->

## 5.0.0 / 2023-08-10 / Agent 7.48.0

***Changed***:

* Bump the minimum base check version ([#15427](https://github.com/DataDog/integrations-core/pull/15427))

***Added***:

* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 4.10.0 / 2023-07-10 / Agent 7.47.0

***Added***:

* Add percentage-based utilization metrics ([#15138](https://github.com/DataDog/integrations-core/pull/15138))

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))
* Added debug logs ([#14650](https://github.com/DataDog/integrations-core/pull/14650))

## 4.9.0 / 2023-01-20 / Agent 7.43.0

***Added***:

* Exclude tracefs by default from disk checks ([#13530](https://github.com/DataDog/integrations-core/pull/13530)) Thanks [DaveWK](https://github.com/DaveWK).

## 4.8.0 / 2022-12-09 / Agent 7.42.0

***Added***:

* Allow device-specific tags for all device-specific metrics ([#13233](https://github.com/DataDog/integrations-core/pull/13233))

## 4.7.1 / 2022-08-05 / Agent 7.39.0

***Fixed***:

* Dependency updates ([#12653](https://github.com/DataDog/integrations-core/pull/12653))

## 4.7.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

***Fixed***:

* Support newer versions of `click` ([#11746](https://github.com/DataDog/integrations-core/pull/11746))

## 4.6.0 / 2022-02-19 / Agent 7.35.0

***Added***:

* Add `pyproject.toml` file ([#11338](https://github.com/DataDog/integrations-core/pull/11338))
* Upgrade psutil to 5.9.0 ([#11139](https://github.com/DataDog/integrations-core/pull/11139))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))

## 4.5.2 / 2022-01-08 / Agent 7.34.0

***Fixed***:

* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 4.5.1 / 2021-11-16 / Agent 7.33.0

***Fixed***:

* Fix use_mount required field ([#10657](https://github.com/DataDog/integrations-core/pull/10657))

## 4.5.0 / 2021-11-13

***Added***:

* Add runtime configuration validation ([#8905](https://github.com/DataDog/integrations-core/pull/8905))

***Fixed***:

* Fix `tag_by_label` when used together with `use_mount` ([#10418](https://github.com/DataDog/integrations-core/pull/10418))

## 4.4.0 / 2021-08-05 / Agent 7.31.0

***Added***:

* Add option to use `lsblk` command for labeling ([#9827](https://github.com/DataDog/integrations-core/pull/9827))

## 4.3.0 / 2021-03-24 / Agent 7.28.0

***Added***:

* Log something if a disk is excluded ([#8829](https://github.com/DataDog/integrations-core/pull/8829))

## 4.2.0 / 2021-03-07 / Agent 7.27.0

***Added***:

* Report read_time and write_time as a count of millis ([#7323](https://github.com/DataDog/integrations-core/pull/7323))

***Fixed***:

* Rename config spec example consumer option `default` to `display_default` ([#8593](https://github.com/DataDog/integrations-core/pull/8593))
* Bump minimum base package version ([#8443](https://github.com/DataDog/integrations-core/pull/8443))

## 4.1.1 / 2021-01-28 / Agent 7.26.0

***Fixed***:

* Fix example config for `create_mounts` ([#8480](https://github.com/DataDog/integrations-core/pull/8480))

## 4.1.0 / 2021-01-25

***Added***:

* Support network drives on Windows ([#8273](https://github.com/DataDog/integrations-core/pull/8273))
* Add device_label tag in addition to label tag ([#8306](https://github.com/DataDog/integrations-core/pull/8306))

***Fixed***:

* Correct default template usage ([#8233](https://github.com/DataDog/integrations-core/pull/8233))

## 4.0.0 / 2020-10-31 / Agent 7.24.0

***Changed***:

* Rename whitelist/blacklist to include/exclude ([#7627](https://github.com/DataDog/integrations-core/pull/7627))

## 3.0.0 / 2020-09-24 / Agent 7.23.0

***Changed***:

* Ignore `/proc/sys/fs/binfmt_misc` by default ([#7650](https://github.com/DataDog/integrations-core/pull/7650))

***Added***:

* Add options for global exclusion patterns ([#7648](https://github.com/DataDog/integrations-core/pull/7648))

## 2.11.0 / 2020-09-21

***Added***:

* [disk] Add `include_all_devices` option and improve error logs ([#7378](https://github.com/DataDog/integrations-core/pull/7378))
* Upgrade psutil to 5.7.2 ([#7395](https://github.com/DataDog/integrations-core/pull/7395))

***Fixed***:

* Upgrade isort ([#7539](https://github.com/DataDog/integrations-core/pull/7539))

## 2.10.1 / 2020-06-11 / Agent 7.21.0

***Fixed***:

* Rename disk check example config back to .default suffix ([#6880](https://github.com/DataDog/integrations-core/pull/6880))

## 2.10.0 / 2020-06-09

***Added***:

* Add disk timeout configuration option ([#6826](https://github.com/DataDog/integrations-core/pull/6826))

## 2.9.1 / 2020-06-11 / Agent 7.20.1

***Fixed***:

* Rename disk check example config back to .default suffix ([#6880](https://github.com/DataDog/integrations-core/pull/6880))

## 2.9.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))
* Add config spec ([#6553](https://github.com/DataDog/integrations-core/pull/6553))
* Add device_name tag ([#6332](https://github.com/DataDog/integrations-core/pull/6332))

## 2.8.0 / 2020-04-04 / Agent 7.19.0

***Added***:

* Upgrade psutil to 5.7.0 ([#6243](https://github.com/DataDog/integrations-core/pull/6243))

## 2.7.0 / 2020-02-22 / Agent 7.18.0

***Added***:

* Read udev disk labels from the blkid cache file ([#5515](https://github.com/DataDog/integrations-core/pull/5515))

## 2.6.0 / 2020-01-13 / Agent 7.17.0

***Added***:

* Use lazy logging format ([#5398](https://github.com/DataDog/integrations-core/pull/5398))
* Use lazy logging format ([#5377](https://github.com/DataDog/integrations-core/pull/5377))

## 2.5.3 / 2019-12-13 / Agent 7.16.0

***Fixed***:

* Bump psutil to 5.6.7 ([#5210](https://github.com/DataDog/integrations-core/pull/5210))

## 2.5.2 / 2019-12-02

***Fixed***:

* Upgrade psutil dependency to 5.6.5 ([#5059](https://github.com/DataDog/integrations-core/pull/5059))

## 2.5.1 / 2019-10-11 / Agent 6.15.0

***Fixed***:

* Upgrade psutil dependency to 5.6.3 ([#4442](https://github.com/DataDog/integrations-core/pull/4442))

## 2.5.0 / 2019-08-24 / Agent 6.14.0

***Added***:

* Remove legacy collection method ([#4417](https://github.com/DataDog/integrations-core/pull/4417))
* Add `min_disk_size` option ([#4317](https://github.com/DataDog/integrations-core/pull/4317))

## 2.4.0 / 2019-07-12 / Agent 6.13.0

***Added***:

* Remove legacy code ([#4103](https://github.com/DataDog/integrations-core/pull/4103))

## 2.3.0 / 2019-07-04

***Added***:

* Add disk label ([#3953](https://github.com/DataDog/integrations-core/pull/3953))

## 2.2.0 / 2019-05-14 / Agent 6.12.0

***Added***:

* Upgrade psutil dependency to 5.6.2 ([#3684](https://github.com/DataDog/integrations-core/pull/3684))
* Adhere to code style ([#3500](https://github.com/DataDog/integrations-core/pull/3500))

## 2.1.0 / 2019-02-18 / Agent 6.10.0

***Added***:

* Upgrade psutil ([#3019](https://github.com/DataDog/integrations-core/pull/3019))

***Fixed***:

* Use `device` tag instead of the deprecated `device_name` parameter ([#2946](https://github.com/DataDog/integrations-core/pull/2946)) Thanks [aerostitch](https://github.com/aerostitch).

## 2.0.1 / 2019-01-04 / Agent 6.9.0

***Fixed***:

* Fix regression on agent 5 only ([#2848](https://github.com/DataDog/integrations-core/pull/2848))

## 2.0.0 / 2018-11-30 / Agent 6.8.0

***Changed***:

* Removed deprecated agentConfig option locations ([#2488](https://github.com/DataDog/integrations-core/pull/2488))

***Added***:

* Update psutil ([#2576](https://github.com/DataDog/integrations-core/pull/2576))
* Add new filtering options, continue deprecations ([#2483](https://github.com/DataDog/integrations-core/pull/2483))
* Support Python 3 ([#2468](https://github.com/DataDog/integrations-core/pull/2468))

***Fixed***:

* Use raw string literals when \ is present ([#2465](https://github.com/DataDog/integrations-core/pull/2465))

## 1.4.0 / 2018-10-12 / Agent 6.6.0

***Added***:

* Upgrade psutil ([#2190](https://github.com/DataDog/integrations-core/pull/2190))

## 1.3.0 / 2018-09-04 / Agent 6.5.0

***Added***:

* Adding optional service_check_rw parameter to check for read-only filesystem ([#2086](https://github.com/DataDog/integrations-core/pull/2086)) Thanks [bberezov](https://github.com/bberezov).

***Fixed***:

* Add data files to the wheel package ([#1727](https://github.com/DataDog/integrations-core/pull/1727))

## 1.2.0 / 2018-03-23

***Added***:

* Adds custom tag support

## 1.1.0 / 2018-02-13

***Added***:

* Adds additional device/mount tagging based on regex
* Allows disk latency metrics to be collected for non-Windows ([#1018](https://github.com/DataDog/integrations-core/issues/1018))

## 1.0.2 / 2017-10-10

***Fixed***:

* Skip now works with NFS secure mounts too ([#470](https://github.com/DataDog/integrations-core/issues/470))

## 1.0.1 / 2017-07-18

***Fixed***:

* Import `Platform` helper from `utils.platform` instead of deprecated `util` ([#484](https://github)com/DataDog/integrations-core/issues/484)

## 1.0.0 / 2017-03-22

***Added***:

* adds disk integration.