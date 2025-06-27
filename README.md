# napari-nifti-viewer

A powerful napari plugin for comprehensive NIfTI file analysis and visualization.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-nifti-viewer)](https://napari-hub.org/plugins/napari-nifti-viewer)

## Overview

napari-nifti-viewer is a comprehensive napari plugin specifically designed for reading, analyzing, and visualizing NIfTI (.nii/.nii.gz) files. It provides detailed metadata extraction, intelligent label detection, and seamless integration with napari's visualization capabilities.

## Features

### 🔍 **Complete NIfTI Support**
- Read .nii and .nii.gz format files
- Support for NIfTI-1 standard
- Compatible with both image and label data

### 📊 **Comprehensive Metadata Analysis**
- Extract complete NIfTI header information (40+ fields)
- Display affine transformation matrices
- Show coordinate system information
- Analyze voxel spacing and orientation

### 🏷️ **Intelligent Label Detection**
- Automatic label image detection
- Statistical analysis of label distributions
- Label value counting and percentage calculations

### 📈 **Data Statistics**
- Complete data shape and type information
- Statistical measures (min, max, mean, std)
- Non-zero voxel counting
- Unique value analysis

### 💾 **Export Capabilities**
- Export complete metadata as JSON
- Preserve all numerical precision
- Human-readable format

### 🎨 **User-Friendly Interface**
- Clean, organized tabbed interface
- Real-time data loading
- Seamless napari integration

## Screenshots

### File Overview Tab
![File Overview](assets/file_overview.png)
*Displays basic file information and data statistics*

### Detailed Information Tab
![Detailed Info](assets/detailed_info.png)
*Shows complete NIfTI header fields and metadata*

### Label Analysis Tab
![Label Analysis](assets/label_analysis.png)
*Intelligent label detection and statistical analysis*

## Installation

### From PyPI (Recommended)
```bash
pip install napari-nifti-viewer
```

### From Source
```bash
git clone https://github.com/qyhohh/napari-nifti-viewer.git
cd napari-nifti-viewer
pip install -e .
```

## Quick Start

1. **Launch napari** with the plugin installed
2. **Open the plugin** from the Plugins menu → napari-nifti-viewer
3. **Load a file** by clicking "Browse..." and selecting a .nii/.nii.gz file
4. **Explore the data** across three informative tabs:
   - **File Overview**: Basic information and statistics
   - **Detailed Info**: Complete NIfTI headers and metadata
   - **Label Analysis**: Label detection and analysis
5. **Visualize in napari** by clicking "Load to Napari"

## Usage Examples

### Loading a Medical Image
```python
import napari
from napari_nifti_viewer import NiftiViewerWidget

# Create napari viewer
viewer = napari.Viewer()

# The plugin will be available in the Plugins menu
# Or you can add it programmatically:
widget = NiftiViewerWidget(viewer)
viewer.window.add_dock_widget(widget, name="NIfTI Viewer")
```

### Exporting Metadata
The plugin allows you to export complete metadata including:
- File information (size, format, version)
- NIfTI header fields (all 40+ standard fields)
- Data statistics (shape, type, value ranges)
- Coordinate system information
- Affine transformation matrices

## Requirements

- **napari** >= 0.4.18
- **nibabel** >= 5.2.1
- **numpy** >= 1.21.0
- **qtpy** >= 2.0.0
- **magicgui** >= 0.7.0
- **Python** >= 3.8

## Supported File Formats

- `.nii` - Uncompressed NIfTI files
- `.nii.gz` - Compressed NIfTI files
- Compatible with NIfTI-1 standard
- Support for both neuroimaging and medical imaging data

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/qyhohh/napari-nifti-viewer.git
cd napari-nifti-viewer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest
```

### Running Tests

```bash
# Basic functionality test
python test_plugin.py

# Test with napari interface
python test_plugin.py --napari
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use this plugin in your research, please consider citing:

```bibtex
@software{napari_nifti_viewer,
  title={napari-nifti-viewer: Comprehensive NIfTI Analysis for napari},
  author={Your Name},
  year={2024},
  url={https://github.com/qyhohh/napari-nifti-viewer}
}
```

## Acknowledgments

- Built with [napari](https://napari.org/) - a fast, interactive, multi-dimensional image viewer
- Uses [nibabel](https://nipy.org/nibabel/) for NIfTI file handling
- Inspired by the neuroimaging and medical imaging communities

## Support

- 📖 [Documentation](https://github.com/qyhohh/napari-nifti-viewer/wiki)
- 🐛 [Issue Tracker](https://github.com/qyhohh/napari-nifti-viewer/issues)
- 💬 [Discussions](https://github.com/qyhohh/napari-nifti-viewer/discussions)

---

Made with ❤️ for the napari and neuroimaging communities 