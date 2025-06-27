#!/usr/bin/env python3
"""
Test script for napari-nifti-viewer plugin

This script generates test NIfTI files and demonstrates the plugin functionality.
Run this script to create sample data and test the plugin.

Usage:
    python test_plugin.py
"""

import numpy as np
import nibabel as nib
import tempfile
import os
from pathlib import Path

def create_test_nifti_data():
    """Create test NIfTI files for plugin testing
    
    Returns:
        tuple: (data_file_path, labels_file_path)
    """
    print("Creating test NIfTI files...")
    
    # Create test data (64x64x32 volume)
    data = np.random.randint(0, 1000, (64, 64, 32), dtype=np.uint16)
    
    # Add some structure to make it more realistic
    # Create a sphere in the center
    center = np.array([32, 32, 16])
    radius = 10
    
    for x in range(64):
        for y in range(64):
            for z in range(32):
                distance = np.sqrt((x - center[0])**2 + (y - center[1])**2 + (z - center[2])**2)
                if distance < radius:
                    data[x, y, z] = 2000 + int(100 * np.sin(distance))
    
    # Create test labels (simple segmentation)
    labels = np.zeros_like(data, dtype=np.uint8)
    
    # Background label (0)
    labels[data < 500] = 0
    
    # Tissue label (1)
    labels[(data >= 500) & (data < 1500)] = 1
    
    # High intensity structure (2)
    labels[(data >= 1500) & (data < 2200)] = 2
    
    # Special structure (3)
    labels[data >= 2200] = 3
    
    # Create NIfTI images with proper headers
    # Set voxel size to 0.5mm isotropic
    affine = np.eye(4) * 0.5
    affine[3, 3] = 1.0
    
    # Create data image
    data_img = nib.Nifti1Image(data, affine)
    data_img.header.set_xyzt_units('mm', 'sec')
    data_img.header['descrip'] = b'Test data for napari-nifti-viewer plugin'
    
    # Create labels image  
    labels_img = nib.Nifti1Image(labels, affine)
    labels_img.header.set_xyzt_units('mm', 'sec')
    labels_img.header['descrip'] = b'Test labels for napari-nifti-viewer plugin'
    
    # Save files
    data_file = "test_data.nii.gz"
    labels_file = "test_labels.nii.gz"
    
    nib.save(data_img, data_file)
    nib.save(labels_img, labels_file)
    
    print(f"✅ Created test data: {data_file}")
    print(f"✅ Created test labels: {labels_file}")
    print(f"   Data shape: {data.shape}")
    print(f"   Data type: {data.dtype}")
    print(f"   Data range: {data.min()} - {data.max()}")
    print(f"   Labels: {np.unique(labels)}")
    print(f"   Voxel size: 0.5mm isotropic")
    
    return data_file, labels_file

def test_plugin_loading():
    """Test if the plugin can be loaded properly"""
    try:
        from napari_nifti_viewer._nifti_loader import load_nifti_file
        print("✅ Plugin loading test: SUCCESS")
        return True
    except ImportError as e:
        print(f"❌ Plugin loading test: FAILED - {e}")
        return False

def test_nifti_loading(data_file):
    """Test NIfTI file loading functionality
    
    Args:
        data_file (str): Path to test data file
    """
    try:
        from napari_nifti_viewer._nifti_loader import load_nifti_file
        
        print(f"\nTesting NIfTI loading with: {data_file}")
        data, metadata = load_nifti_file(data_file)
        
        print("✅ NIfTI loading test: SUCCESS")
        print(f"   Loaded data shape: {data.shape}")
        print(f"   Metadata keys: {len(metadata)} items")
        print(f"   Has header info: {'nifti_header' in metadata}")
        print(f"   Has file info: {'file_info' in metadata}")
        
        return True
        
    except Exception as e:
        print(f"❌ NIfTI loading test: FAILED - {e}")
        return False

def test_label_detection(labels_file):
    """Test automatic label detection
    
    Args:
        labels_file (str): Path to test labels file  
    """
    try:
        from napari_nifti_viewer._nifti_loader import load_nifti_file
        
        print(f"\nTesting label detection with: {labels_file}")
        data, metadata = load_nifti_file(labels_file)
        
        is_labels = metadata.get('analysis', {}).get('is_labels', False)
        unique_values = metadata.get('analysis', {}).get('unique_values', [])
        
        print("✅ Label detection test: SUCCESS")
        print(f"   Detected as labels: {is_labels}")
        print(f"   Unique values: {unique_values}")
        
        return True
        
    except Exception as e:
        print(f"❌ Label detection test: FAILED - {e}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("napari-nifti-viewer Plugin Test Suite")
    print("=" * 60)
    
    # Test 1: Plugin loading
    if not test_plugin_loading():
        print("\n❌ Cannot proceed - plugin loading failed")
        return
    
    # Test 2: Create test data
    try:
        data_file, labels_file = create_test_nifti_data()
    except Exception as e:
        print(f"\n❌ Failed to create test data: {e}")
        return
    
    # Test 3: NIfTI loading
    test_nifti_loading(data_file)
    
    # Test 4: Label detection  
    test_label_detection(labels_file)
    
    print("\n" + "=" * 60)
    print("Test Summary:")
    print("- Test files created successfully")
    print("- You can now test the plugin in napari:")
    print("  1. Open napari")
    print("  2. Load the napari-nifti-viewer plugin")
    print("  3. Open the test files to verify functionality")
    print("=" * 60)
    
    # Cleanup instructions
    print("\nTo clean up test files:")
    print("rm test_data.nii.gz test_labels.nii.gz")

if __name__ == "__main__":
    main() 