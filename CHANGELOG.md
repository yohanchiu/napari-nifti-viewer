# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2024-12-19

### Fixed
- **CI/CD Issues**: Complete resolution of GitHub Actions test failures
  - Fixed Qt dependency issues in testing environment
  - Added proper headless testing support with xvfb
  - Resolved pytest command not found errors
  - Fixed Ubuntu package installation issues
- **Code Quality**: Major improvements to code standards
  - Removed unused imports (F401 errors)
  - Fixed bare except clauses with specific exception handling
  - Applied black code formatting consistently
  - Reduced flake8 errors from 50+ to minor style issues
- **Testing Infrastructure**: Enhanced test coverage and reliability
  - Created Qt-independent test suite
  - Added comprehensive core functionality tests
  - Implemented isolated testing without external dependencies
  - All tests now pass on all platforms (Ubuntu, Windows, macOS)

### Changed
- **Test Architecture**: Redesigned testing approach for better CI compatibility
- **Error Handling**: Improved exception handling in extension data parsing
- **Import Organization**: Cleaned up module imports following best practices
- **Code Style**: Applied consistent formatting across all Python files

### Technical Improvements
- Added xvfb support for headless Qt testing in Linux CI
- Implemented platform-specific test execution strategies
- Enhanced pytest configuration for better test discovery
- Improved GitHub Actions workflow reliability

## [0.1.1] - 2024-06-28

### Changed
- Updated author information in pyproject.toml
- Fixed configuration for PyPI publication
- Improved package metadata

## [0.1.0] - 2024-01-XX

### Added
- Initial release of napari-nifti-viewer
- Complete NIfTI file support (.nii and .nii.gz)
- Comprehensive metadata extraction and display
- Intelligent label detection and analysis
- Three-tab user interface:
  - File Overview: Basic information and statistics
  - Detailed Info: Complete NIfTI headers and metadata
  - Label Analysis: Label detection and statistical analysis
- Export functionality for complete metadata as JSON
- Seamless napari integration for data visualization
- Support for both image and label data types
- Automatic coordinate system and affine transformation analysis
- Real-time data statistics calculation
- Professional English user interface

### Features
- **File Support**: Read .nii and .nii.gz format files
- **Metadata Analysis**: Extract 40+ NIfTI header fields
- **Label Detection**: Automatic detection of label images
- **Statistics**: Complete data shape, type, and statistical measures
- **Export**: JSON export of all metadata with proper type handling
- **Visualization**: Direct loading into napari viewer
- **User Interface**: Clean, organized tabbed interface

### Technical Details
- Built with napari plugin framework
- Uses nibabel for NIfTI file handling
- Qt-based user interface with QtPy
- Comprehensive error handling and user feedback
- Memory-efficient data loading
- Cross-platform compatibility (Windows, macOS, Linux)

### Dependencies
- napari >= 0.4.18
- nibabel >= 5.2.1
- numpy >= 1.21.0
- qtpy >= 2.0.0
- magicgui >= 0.7.0
- Python >= 3.8

---

## Release Notes

### Version 0.1.0 Highlights

This is the initial release of napari-nifti-viewer, a comprehensive solution for NIfTI file analysis in napari. The plugin provides:

1. **Complete File Support**: Full compatibility with NIfTI-1 standard
2. **Intelligent Analysis**: Automatic detection of image vs. label data
3. **Comprehensive Metadata**: All header fields and transformation matrices
4. **User-Friendly Interface**: Organized, professional interface design
5. **Export Capabilities**: Complete metadata export functionality

The plugin is designed for researchers, medical professionals, and anyone working with neuroimaging or medical imaging data who needs detailed insight into their NIfTI files.

---

For older versions and detailed technical changes, see the [Git commit history](https://github.com/yohanchiu/napari-nifti-viewer/commits). 