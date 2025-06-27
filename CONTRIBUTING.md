# Contributing to napari-nifti-viewer

Thank you for your interest in contributing to napari-nifti-viewer! We welcome contributions from everyone.

## Ways to Contribute

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find that the issue has already been reported. When you create a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots if possible**

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain which behavior you expected to see instead**
- **Explain why this enhancement would be useful**

### 🔧 Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for your changes
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git

### Setting Up Your Development Environment

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yohanchiu/napari-nifti-viewer.git
   cd napari-nifti-viewer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package in development mode**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## Testing

### Running Tests

```bash
# Run basic functionality tests
python test_plugin.py

# Run with napari interface (requires display)
python test_plugin.py --napari

# Run pytest (if available)
pytest tests/
```

### Adding Tests

- Add unit tests for new functionality
- Ensure tests cover edge cases
- Test with different NIfTI file types
- Include tests for error handling

## Code Style

We follow Python PEP 8 style guidelines. Please ensure your code:

- Uses 4 spaces for indentation
- Has line lengths of 88 characters or less
- Includes docstrings for all public functions and classes
- Uses type hints where appropriate

### Code Formatting

We use `black` for code formatting:

```bash
black napari_nifti_viewer/
```

### Import Sorting

We use `isort` for import sorting:

```bash
isort napari_nifti_viewer/
```

## Documentation

- Update docstrings for any new or modified functions
- Update the README if you change functionality
- Add comments for complex logic
- Update type hints

## Commit Messages

Please write clear and meaningful commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add support for 4D NIfTI files

- Implement time series data handling
- Add 4D visualization options
- Update tests for temporal data
- Fixes #123
```

## Release Process

Releases are handled by maintainers. The process includes:

1. Update version numbers
2. Update CHANGELOG.md
3. Create a git tag
4. Build and upload to PyPI
5. Create GitHub release

## Questions?

If you have questions about contributing, please:

1. Check the existing issues and discussions
2. Open a new discussion on GitHub
3. Contact the maintainers

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you are expected to uphold this code.

## License

By contributing to napari-nifti-viewer, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to napari-nifti-viewer! 🎉 