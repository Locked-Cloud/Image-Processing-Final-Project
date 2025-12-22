# Contributing to Image Processing Studio

Thank you for your interest in contributing to Image Processing Studio! This document provides guidelines and instructions for contributing.

## 🎯 Ways to Contribute

### 1. Bug Reports
If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version)
- Screenshots if applicable

### 2. Feature Requests
We welcome feature suggestions! Please include:
- Clear description of the feature
- Use case and benefits
- Potential implementation approach (optional)

### 3. Code Contributions
We accept pull requests for:
- New filters
- Performance improvements
- Bug fixes
- Documentation improvements
- UI/UX enhancements

## 🔧 Development Setup

1. **Fork and Clone**
```bash
git clone https://github.com/yourusername/image-processing-studio.git
cd image-processing-studio
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

## 📝 Coding Guidelines

### Python Style
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and modular

### Example Filter Implementation
```python
def my_custom_filter(self, frame, parameter1, parameter2):
    """
    Brief description of what the filter does.
    
    Args:
        frame: Input image (BGR format)
        parameter1: Description of parameter1
        parameter2: Description of parameter2
    
    Returns:
        Processed image (grayscale)
    """
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply processing
    result = some_processing(gray, parameter1, parameter2)
    
    return result
```

### Adding a New Filter Checklist
- [ ] Add parameters to `self.params` dictionary
- [ ] Implement filter method
- [ ] Add to `apply_filter()` method
- [ ] Create UI controls in `create_controls()`
- [ ] Add keyboard shortcut in `key_press()`
- [ ] Add documentation to README
- [ ] Test with various parameter values
- [ ] Test with camera and static images

## 🧪 Testing

Before submitting a PR:
1. Test your changes with:
   - Camera input
   - Static image input
   - Different parameter values
   - Edge cases (min/max values)
2. Ensure no errors in console
3. Check performance (should maintain reasonable FPS)
4. Test on different image types (color, grayscale, different sizes)

## 📋 Pull Request Process

1. **Update Documentation**
   - Add your filter to README
   - Include parameter descriptions and use cases
   - Update CHANGELOG if applicable

2. **Create Pull Request**
   - Use descriptive title
   - Explain what changes were made and why
   - Reference any related issues
   - Include screenshots/examples if UI changes

3. **PR Template**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Performance improvement
- [ ] Documentation update

## Testing
- [ ] Tested with camera input
- [ ] Tested with static images
- [ ] Tested edge cases
- [ ] No console errors

## Screenshots (if applicable)
Add screenshots here
```

## 🎨 UI/UX Guidelines

When adding UI elements:
- Maintain dark theme color scheme
- Use consistent spacing (padx=5, pady=5)
- Add tooltips for parameters
- Ensure responsive layout
- Test with different window sizes

### Color Scheme
```python
Background: '#2b2b2b'
Dark sections: '#1e1e1e'
Controls: '#363636'
Success/Active: '#4CAF50'
Stop/Delete: '#f44336'
Info: '#2196F3'
Warning: '#FF9800'
Text: '#ffffff'
Accent: '#00ff00'
```

## 📖 Documentation Standards

### Code Comments
- Explain complex algorithms
- Document parameter ranges and units
- Add references for algorithms (papers, articles)

### README Updates
When adding a filter, include:
- Description and purpose
- Parameter explanations with typical ranges
- Use cases and when to use it
- Example parameter combinations
- Performance considerations

## 🐛 Known Issues

Check existing issues before working on something. Common areas needing improvement:
- Performance optimization for large images
- More robust error handling
- Additional file format support
- Batch processing mode
- Parameter presets

## 💡 Feature Ideas

Looking for something to work on? Consider:
- Histogram equalization
- Color space conversions
- Morphological operations (opening, closing)
- Adaptive thresholding
- Image enhancement filters
- Batch processing mode
- Save/load parameter presets
- Before/after comparison view
- Video file processing
- Export processing history

## 🤔 Questions?

- Open an issue for discussion
- Check existing issues and PRs
- Read the main README thoroughly

## 📜 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn
- Focus on the code, not the person

## 🙏 Recognition

Contributors will be acknowledged in:
- README contributors section
- Release notes
- Project documentation

Thank you for contributing to Image Processing Studio! 🎉
