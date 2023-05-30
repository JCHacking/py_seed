# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2023-03-20
### Changed
- GPHQACLOUD-1358 - @jmencianaranjo - All dependencies versions specification is now min version
- GPHQACLOUD-1358 - @jmencianaranjo - Updaed dependencies
### Removed
- GPHQACLOUD-1358 - @jmencianaranjo - Removed fixed version specification from setuptools, pip, wheel and poetry.

## [1.0.5] - 2023-03-09
### Changed
- GPHQACLOUD-1066 - @jmencianaranjo - Modification of the documentation to integrate with the seed.
- GPHQACLOUD-1066 - @jmencianaranjo - Updaed dependencies
### Removed
- GPHQACLOUD-1066 - @jmencianaranjo - Coverage extra toml (Python 3.11 add native library for read TOML files)

## [1.0.4] - 2023-02-18
### Changed
- GPHQACLOUD-1066 - @jmencianaranjo - Updated dependencies

## [1.0.3] - 2023-02-13
### Changed
- GPHQACLOUD-1066 - @jmencianaranjo - cyclonedx-bom changed for cyclonedx-py command
- GPHQACLOUD-1066 - @jmencianaranjo - Updated dependencies
- GPHQACLOUD-1066 - @jmencianaranjo - Updated Python from 3.11.1 to 3.11.2

## [1.0.2] - 2023-02-07
### Fixed
- GPHQACLOUD-1066 - @jmencianaranjo - CHANGELOG links of the fixed versions to see the changes added in one version with respect to the previous one
### Changed
- GPHQACLOUD-1066 - @jmencianaranjo - Updated dependencies
- GPHQACLOUD-1066 - @jmencianaranjo - Last step of the integration, now also tells how to update the packages with poetry
### Added
- GPHQACLOUD-1066 - @jmencianaranjo - Added dependencies from requirements_base to pyproject.toml so that these are not updated unless we want them to be

## [1.0.1] - 2023-01-26
### Changed
- GPHQACLOUD-1066 - @jmencianaranjo - Updated dependencies

## [1.0.0] - 2022-12-16
### Added
- GPHQACLOUD-1114 - @jmencianaranjo - Folder structure created
- GPHQACLOUD-1114 - @jmencianaranjo - Configured exclude files and directories to be managed with `git`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured formatting standard with `EditorConfig`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured changelog linter with `python-kacl`
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for test changelog format
- GPHQACLOUD-1114 - @jmencianaranjo - Configured documentation generator with `sphinx`
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for documentation generation
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for export dependencies `cyclonedx`
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for list dependencies outdated
- GPHQACLOUD-1114 - @jmencianaranjo - Configured linter with `falke8`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured typing linter with `mypy`
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for check formatting, cyclomatic complexity, code safety, etc.
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for test typing
- GPHQACLOUD-1114 - @jmencianaranjo - Configured code coverage generator with `coverage` and `nose2`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured test execution with `unittest` and `nose2`
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for tests execution
- GPHQACLOUD-1114 - @jmencianaranjo - Created script for build generation
- GPHQACLOUD-1114 - @jmencianaranjo - Configured dependency manager with `poetry`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured dependency for poetry with `requirements.txt`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured development scripts with `poethepoet`
- GPHQACLOUD-1114 - @jmencianaranjo - Configured jenkins pipeline for CI
- GPHQACLOUD-1114 - @jmencianaranjo - Seed documented in `README.md`

[1.1.0]: https://www.google.es
[1.0.5]: https://www.google.es
[1.0.4]: https://www.google.es
[1.0.3]: https://www.google.es
[1.0.2]: https://www.google.es
[1.0.1]: https://www.google.es
[1.0.0]: https://www.google.es
