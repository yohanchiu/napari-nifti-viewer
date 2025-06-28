"""Basic tests for napari-nifti-viewer."""

import sys
from pathlib import Path
from unittest.mock import Mock

import pytest


def test_nifti_loader_init():
    """Test NiftiLoader initialization."""
    # Import NiftiLoader directly to avoid Qt dependencies
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    loader = NiftiLoader()
    assert loader.supported_formats == {'.nii', '.nii.gz'}
    assert loader.current_file is None
    assert loader.current_nii is None


def test_is_nifti_file_valid_formats():
    """Test _is_nifti_file with valid formats."""
    # Import NiftiLoader directly to avoid Qt dependencies
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    loader = NiftiLoader()
    
    # Test .nii.gz format
    nii_gz_path = Path("test.nii.gz")
    assert loader._is_nifti_file(nii_gz_path) is True
    
    # Test .nii format
    nii_path = Path("test.nii")
    assert loader._is_nifti_file(nii_path) is True


def test_is_nifti_file_invalid_formats():
    """Test _is_nifti_file with invalid formats."""
    # Import NiftiLoader directly to avoid Qt dependencies
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    loader = NiftiLoader()
    
    # Test invalid formats
    invalid_paths = [
        Path("test.txt"),
        Path("test.nii.txt"),
        Path("test.gz"),
        Path("test"),
    ]
    
    for path in invalid_paths:
        assert loader._is_nifti_file(path) is False


def test_extract_data_info_mock():
    """Test _extract_data_info method with mock data."""
    # Import NiftiLoader directly to avoid Qt dependencies
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from napari_nifti_viewer._nifti_loader import NiftiLoader
    
    import numpy as np
    
    loader = NiftiLoader()
    
    # Create mock data
    mock_data = np.array([[1, 2, 3], [4, 5, 6]])
    
    # Mock the current_nii attribute
    class MockNii:
        def get_fdata(self):
            return mock_data
    
    loader.current_nii = MockNii()
    
    # Test data info extraction
    data_info = loader._extract_data_info()
    
    assert data_info['shape'] == [2, 3]
    assert data_info['ndim'] == 2
    assert data_info['min_value'] == 1.0
    assert data_info['max_value'] == 6.0
    assert data_info['mean_value'] == 3.5
    assert data_info['unique_values_count'] == 6
    assert data_info['non_zero_count'] == 6
    assert data_info['zero_count'] == 0 