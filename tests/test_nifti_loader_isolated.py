"""Tests for NiftiLoader class without Qt dependencies."""

import sys
from pathlib import Path

import numpy as np
import pytest

# Add the project root to the path to import modules directly
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_import_nifti_loader():
    """Test that we can import NiftiLoader without Qt dependencies."""
    # This import should not trigger Qt imports
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    loader = NiftiLoader()
    assert loader is not None


def test_nifti_file_detection():
    """Test NiftiLoader file format detection."""
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    loader = NiftiLoader()
    
    # Valid formats
    assert loader._is_nifti_file(Path("test.nii")) is True
    assert loader._is_nifti_file(Path("test.nii.gz")) is True
    assert loader._is_nifti_file(Path("data.NII")) is True
    assert loader._is_nifti_file(Path("brain.NII.GZ")) is True
    
    # Invalid formats
    assert loader._is_nifti_file(Path("test.txt")) is False
    assert loader._is_nifti_file(Path("test.nii.txt")) is False
    assert loader._is_nifti_file(Path("test.gz")) is False
    assert loader._is_nifti_file(Path("test")) is False


def test_data_info_extraction():
    """Test data information extraction with mock data."""
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    loader = NiftiLoader()
    
    # Create mock 3D data
    mock_data = np.random.rand(10, 20, 30)
    mock_data[0, 0, 0] = 0  # Ensure we have at least one zero
    
    class MockNiftiImage:
        def get_fdata(self):
            return mock_data
    
    loader.current_nii = MockNiftiImage()
    
    data_info = loader._extract_data_info()
    
    # Check basic properties
    assert data_info['shape'] == [10, 20, 30]
    assert data_info['ndim'] == 3
    assert 'min_value' in data_info
    assert 'max_value' in data_info
    assert 'mean_value' in data_info
    assert 'std_value' in data_info
    assert data_info['zero_count'] >= 1 