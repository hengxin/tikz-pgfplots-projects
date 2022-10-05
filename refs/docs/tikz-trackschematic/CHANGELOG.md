# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Categories: Added, Changed, Deprecated, Removed, Fixed, and Security.

## [Unreleased]

### Added

  * i18n option

## Version [0.7.0] - 2022-04-02

### Added
 
 * unified build script for development

### Changed
  
  * revised symbol and syntax for balises
  * the track loop was separated from the balises
  * replaced "\gettikzxy" with "\path let" syntax
  * label placement for derailers

### Fixed

  * wrong option for labels in vehicles
  * foreground of sidetrack (alias)
  * PackageWarning Error in development mode

## Version [0.6.3] - 2022-02-15

### Added

  * anchor for SVG export
  * automated testing and releasing
  * separate changelog

### Fixed

  * documented (slip-)turnout option: points=moving
  * spelling error in documentation
  * URL to signalschablone


## Version [0.6.2] - 2021-10-15

### Fixed

  * runaway argument
  * developer mode always on 


## Version [0.6.1] - 2021-09-30

### Added

  * added citation information

### Removed
  
  * removed package requirement lmodern

### Fixed

  * minor correction in manual


## Version [0.6] - 2021-01-02

### Added

  * created an encapsulating package for future flexibility
  * added symbols for direction control, track marking, pylons and electric wiring

### Changed

  * changed symbol for friction bufferstop;
  * changed load command to \usepackage{tikz-trackschematic}


## Version [0.5.1] - 2020-02-10
  
### Added

  * added symbols "braking point" and "danger point"

### Changed
 
  * modified symbol "end of movement authority"


## Version [0.5] - 2020-01-14

### Added

  * documentation

### Changed

  * new improved syntax for topology


## Version [0.4] - 2019-07-21

### Added

  * added document for symbology

### Changed

  * renamed overview to snippets
  * reworked library for common tikz library layout


## Version [0.3] - 2019-04-04

### Added

  * added shunting movements
  * added points to turnouts
  * added moving trains
  * defined and used color foreground and background

### Changed

  * moved snippet folder to root folder


## Version [0.2] - 2018-12-19

### Added

  * added transmitters

### Changed

  * reorganized src library
  * minor improvements


## Version [0.1] - 2018-09-14

### Added

  Basic concept of a library with railway topology symbols and some examples.


[Unreleased]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.7.0...master
[0.7.0]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.6.3...v0.7.0
[0.6.3]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.6.2...v0.6.3
[0.6.2]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.6.1...v0.6.2
[0.6.1]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.6...v0.6.1
[0.6]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.5.1...v0.6
[0.5.1]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.5...v0.5.1
[0.5]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.4...v0.5
[0.4]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.3...v0.4
[0.3]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.2...v0.3
[0.2]: https://github.com/railtoolkit/tikz-trackschematic/compare/v0.1...v0.2
[0.1]: https://github.com/railtoolkit/tikz-trackschematic/releases/tag/v0.1