"""Basic tests for napari-nifti-viewer."""

import pytest
from pathlib import Path

from napari_nifti_viewer._nifti_loader import NiftiLoader


def test_nifti_loader_init():
    """Test NiftiLoader initialization."""
    loader = NiftiLoader()
    assert loader.supported_formats == {'.nii', '.nii.gz'}
    assert loader.current_file is None
    assert loader.current_nii is None


def test_is_nifti_file_valid_formats():
    """Test _is_nifti_file with valid formats."""
    loader = NiftiLoader()
    
    # Test .nii.gz format
    nii_gz_path = Path("test.nii.gz")
    assert loader._is_nifti_file(nii_gz_path) is True
    
    # Test .nii format
    nii_path = Path("test.nii")
    assert loader._is_nifti_file(nii_path) is True


def test_is_nifti_file_invalid_formats():
    """Test _is_nifti_file with invalid formats."""
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