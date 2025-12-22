# 📷 Image Processing Studio

A comprehensive real-time image processing application with an intuitive GUI, featuring 20+ filters for edge detection, frequency domain filtering, and noise reduction. Perfect for computer vision learning, experimentation, and practical image enhancement tasks.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/license-MIT-purple)

## ✨ Features


### 🎯 Real-Time Processing
- **Live Camera Feed**: Process webcam input in real-time with instant filter application
- **Static Image Processing**: Load and process images from disk with live parameter adjustment
- **Dynamic Updates**: All filter parameters update in real-time as you adjust them

### 🔧 20+ Professional Filters

#### Edge Detection (4 filters)
- **Sobel X & Y**: Directional edge detection with adjustable kernel size
- **Gradient Magnitude**: Combined edge strength visualization
- **Canny Edge Detection**: Advanced multi-stage edge detection with full parameter control

#### Frequency Domain Filters (6 filters)
**Low-Pass Filters (Smoothing)**
- Ideal Low-Pass Filter (ILPF)
- Gaussian Low-Pass Filter (GLPF)
- Butterworth Low-Pass Filter (BLPF)

**High-Pass Filters (Sharpening)**
- Ideal High-Pass Filter (IHPF)
- Gaussian High-Pass Filter (GHPF)
- Butterworth High-Pass Filter (BHPF)

#### Mean Filters (4 filters)
- **Arithmetic Mean**: Standard averaging for noise reduction
- **Geometric Mean**: Effective against Gaussian noise
- **Harmonic Mean**: Specialized for salt noise removal
- **Contraharmonic Mean**: Adjustable for salt or pepper noise

#### Order Statistic Filters (4 filters)
- **Median Filter**: Excellent for salt & pepper noise
- **Min Filter**: Morphological erosion (removes white noise)
- **Max Filter**: Morphological dilation (removes black noise)
- **Midpoint Filter**: Average of min and max values

### 🎮 Intuitive Controls
- **Individual Filter Controls**: Each filter has its own dedicated parameter panel
- **Multiple Input Methods**: 
  - Slider-style +/- buttons
  - Direct numerical entry (click value to type)
  - Keyboard shortcuts for quick filter switching
- **Smart Constraints**: Automatic validation and constraints (e.g., odd kernel sizes)
- **Helpful Tips**: Context-sensitive guidance for each parameter

## 🚀 Installation

### Prerequisites
```bash
Python 3.7 or higher
```

### Required Libraries
```bash
pip install opencv-python numpy scikit-image pillow
```

Or install all dependencies at once:
```bash
pip install -r requirements.txt
```

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/image-processing-studio.git
cd image-processing-studio

# Install dependencies
pip install -r requirements.txt

# Run the application
python image_processing_studio.py
```

## 📖 Usage Guide

### Getting Started

1. **Launch the Application**
   ```bash
   python image_processing_studio.py
   ```

2. **Choose Your Input Source**
   - Click **"▶ Camera"** to use your webcam
   - Click **"📁 Load"** to open an image file

3. **Apply Filters**
   - Click any filter button or use keyboard shortcuts
   - Adjust parameters using +/- buttons or click values to type directly
   - See results update in real-time

4. **Save Your Work**
   - Click **"💾 Save"** to export the processed image

### Keyboard Shortcuts

#### Edge Detection
- `X` - Sobel X (vertical edges)
- `Y` - Sobel Y (horizontal edges)
- `S` - Gradient Magnitude
- `C` - Canny Edge Detection

#### Frequency Filters
**Low-Pass (Smoothing)**
- `1` - Ideal LPF
- `2` - Gaussian LPF
- `3` - Butterworth LPF

**High-Pass (Sharpening)**
- `4` - Ideal HPF
- `5` - Gaussian HPF
- `6` - Butterworth HPF

#### Mean Filters
- `A` - Arithmetic Mean
- `G` - Geometric Mean
- `H` - Harmonic Mean
- `M` - Contraharmonic Mean

#### Order Statistic Filters
- `D` - Median Filter
- `I` - Min Filter (Erosion)
- `O` - Max Filter (Dilation)
- `P` - Midpoint Filter

#### General Controls
- `N` - Remove all filters (show original)
- `Q` - Quit application

## 🔬 Filter Details & Use Cases

### Edge Detection Filters

#### Sobel Filters (X, Y, Gradient)
**Purpose**: Detect edges by computing image derivatives

**Parameters**:
- `Kernel Size` (3-31, odd): Larger kernels = smoother edges but less detail
  - 3-5: Fine details, high sensitivity
  - 7-9: Smoother edges, noise reduction
  - 11+: Very smooth, best for noisy images

**Use Cases**:
- Object boundary detection
- Feature extraction
- Computer vision preprocessing

#### Canny Edge Detection
**Purpose**: Multi-stage algorithm for optimal edge detection

**Parameters**:
- `Kernel Size` (3-31, odd): Gaussian blur before detection
- `Gaussian Sigma` (0-10): Blur strength (0 = auto)
- `Low Threshold` (0-255): Minimum edge strength (30-100 typical)
- `High Threshold` (0-255): Strong edge threshold (60-200 typical)

**Guidelines**:
- High/Low ratio should be 2:1 or 3:1
- Lower thresholds = more edges detected
- Higher thresholds = only strong edges

**Use Cases**:
- Precise object detection
- Image segmentation
- Lane detection in autonomous vehicles

### Frequency Domain Filters

All frequency filters work in the Fourier domain, manipulating image frequencies.

#### Low-Pass Filters (Smoothing)
**Purpose**: Remove high-frequency noise, blur images

**Common Parameters**:
- `Cutoff Radius` (1-200): Larger radius = more detail preserved
  - 10-30: Strong smoothing
  - 40-80: Moderate smoothing
  - 100+: Gentle smoothing

**Comparison**:
- **ILPF**: Sharp cutoff, may cause ringing artifacts
- **GLPF**: Smooth transition, no ringing, best general-purpose
- **BLPF**: Adjustable transition sharpness via order parameter
  - Order 1: Similar to GLPF
  - Order 2-4: Balanced (typical)
  - Order 5+: Approaches ILPF

**Use Cases**:
- Noise reduction
- Image compression preprocessing
- Anti-aliasing

#### High-Pass Filters (Sharpening)
**Purpose**: Enhance edges and fine details

**Common Parameters**:
- `Cutoff Radius` (1-200): Larger radius = more smoothing of details
  - 10-30: Aggressive sharpening
  - 40-80: Moderate enhancement
  - 100+: Subtle detail preservation

**Use Cases**:
- Image sharpening
- Detail enhancement
- Edge emphasis

### Mean Filters

#### Arithmetic Mean
**Purpose**: Simple averaging for noise reduction

**Parameters**:
- `Kernel Size` (3-31, odd): Size of averaging window
  - 3-5: Minimal blur, some noise reduction
  - 7-9: Balanced
  - 11+: Heavy blur, strong noise reduction

**Use Cases**:
- General noise reduction
- Image smoothing
- Preprocessing for other algorithms

#### Geometric Mean
**Purpose**: Better preserves edges than arithmetic mean

**Parameters**:
- `Kernel Size` (3-7 recommended)

**Best For**:
- Gaussian noise
- Preserving image details while smoothing

#### Harmonic Mean
**Purpose**: Specialized for salt noise (bright pixels)

**Parameters**:
- `Kernel Size` (3-7 recommended)

**Best For**:
- Salt noise removal
- Bright outlier suppression

#### Contraharmonic Mean
**Purpose**: Adjustable for salt or pepper noise

**Parameters**:
- `Kernel Size` (3-7 recommended)
- `Q Order` (-5.0 to 5.0):
  - **Q > 0**: Removes pepper noise (dark pixels)
  - **Q < 0**: Removes salt noise (bright pixels)
  - **Q = 0**: Equivalent to arithmetic mean
  - Typical values: ±1.5 to ±2.5

**Use Cases**:
- Targeted noise removal
- Impulse noise suppression

### Order Statistic Filters

#### Median Filter
**Purpose**: Excellent for salt & pepper noise without blurring

**Parameters**:
- `Kernel Size` (3-31, odd):
  - 3-5: Preserves details, removes isolated noise
  - 7-9: Stronger noise removal, slight blur
  - 11+: Heavy filtering

**Use Cases**:
- Salt & pepper noise removal
- Image restoration
- Preprocessing for OCR

#### Min Filter (Erosion)
**Purpose**: Morphological erosion - removes bright pixels

**Parameters**:
- `Kernel Size` (3-7 recommended)

**Effects**:
- Shrinks bright regions
- Removes small bright objects
- Darkens image

**Use Cases**:
- Removing bright noise
- Separating connected objects
- Morphological operations

#### Max Filter (Dilation)
**Purpose**: Morphological dilation - removes dark pixels

**Parameters**:
- `Kernel Size` (3-7 recommended)

**Effects**:
- Expands bright regions
- Removes small dark objects
- Brightens image

**Use Cases**:
- Removing dark noise
- Connecting nearby objects
- Morphological operations

#### Midpoint Filter
**Purpose**: Average of minimum and maximum values

**Parameters**:
- `Kernel Size` (3-7 recommended)

**Use Cases**:
- Random noise reduction
- Combines effects of min and max filters

## 🏗️ Architecture & Implementation

### Class Structure

```python
UltimateControlGUI
├── GUI Components
│   ├── Top Bar (controls)
│   ├── Canvas (image display)
│   └── Control Panel (filter parameters)
├── State Management
│   ├── Camera feed
│   ├── Current frame
│   ├── Processed frame
│   └── Filter parameters
└── Processing Methods
    ├── Edge detection
    ├── Frequency filters
    ├── Mean filters
    └── Order statistic filters
```

### Key Components

#### 1. GUI Initialization (`__init__`, `create_gui`)
- Sets up the main window with dark theme
- Creates responsive layout with canvas and control panel
- Initializes all filter parameters with sensible defaults

#### 2. Control Panel (`create_controls`, `add_filter_with_controls`)
- Scrollable interface for all filters
- Organized into logical sections
- Each filter has dedicated parameter controls
- Real-time parameter adjustment

#### 3. Parameter Management
```python
self.params = {
    'sobel_kernel': 3,
    'canny_low_ratio': 30,
    # ... all filter parameters
}
```
- Centralized parameter storage
- Type-aware (int vs float)
- Automatic constraint enforcement

#### 4. Real-Time Processing Pipeline
```python
Input Source → apply_filter() → update_canvas() → Display
     ↓              ↓                   ↓
  Camera/File   Processing         Resize/Display
```

#### 5. Threading Model
- **Main Thread**: GUI updates and user interaction
- **Camera Thread**: Continuous frame capture and processing
- **Update Loop**: Parameter changes trigger re-processing

### Technical Implementation Details

#### Frequency Domain Processing
```python
def DFT_and_reconstruct(self, gray_img, filter_mask):
    # 1. Convert to frequency domain
    dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    
    # 2. Apply filter mask
    fshift = dft_shift * filter_mask
    
    # 3. Convert back to spatial domain
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    
    return processed_image
```

#### Canny Edge Detection
Custom implementation following the standard algorithm:
1. Gaussian blur for noise reduction
2. Sobel operators for gradient computation
3. Non-maximum suppression
4. Double thresholding
5. Edge tracking by hysteresis

#### Contraharmonic Mean
Mathematical formulation:
```
f̂(x,y) = Σ g(s,t)^(Q+1) / Σ g(s,t)^Q
```
where the sum is over the kernel window.

## 🎨 GUI Features

### Visual Design
- **Dark Theme**: Reduces eye strain during long sessions
- **Color Coding**: 
  - Green: Active/positive actions
  - Red: Stop/destructive actions
  - Blue: Information
  - Orange: Save/export
- **Responsive Layout**: Adapts to window resizing
- **Status Feedback**: Real-time FPS and filter status

### User Experience
- **No Learning Curve**: Intuitive button layout and tooltips
- **Visual Feedback**: 
  - Current filter highlighted in status bar
  - FPS counter for performance monitoring
  - Helpful parameter tips
- **Flexible Input**: Mouse, keyboard, or direct value entry
- **Undo-Friendly**: Switch filters instantly to compare results

## 📊 Performance

### Optimization Features
- **Threaded Camera Capture**: Prevents GUI freezing
- **Efficient Frame Processing**: Optimized OpenCV operations
- **Smart Canvas Updates**: Only redraws when necessary
- **FPS Monitoring**: Real-time performance feedback

### Typical Performance
- **720p Camera**: 15-30 FPS (depending on filter complexity)
- **Static Images**: Instant parameter updates
- **Large Images**: Automatic scaling for display

### Performance Tips
- Simpler filters (median, arithmetic mean) run fastest
- Frequency domain filters are computationally intensive
- Large kernel sizes reduce performance
- Lower camera resolution improves FPS

## 🛠️ Customization & Extension

### Adding New Filters

1. **Add parameters** to `self.params` dictionary:
```python
self.params = {
    # ... existing params
    'my_filter_param': 10,
}
```

2. **Create filter section** in `create_controls()`:
```python
self.add_filter_with_controls(scroll_frame, "K", "My Filter", 'my_filter', [
    ('my_filter_param', "Parameter Name", 1, 100, 5, "Helpful tip"),
])
```

3. **Implement processing** in `apply_filter()`:
```python
elif mode == 'my_filter':
    param = self.params['my_filter_param']
    result = self.my_filter_function(frame, param)
    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
```

4. **Add keyboard shortcut** in `key_press()`:
```python
filter_map = {
    # ... existing shortcuts
    'k': 'my_filter',
}
```

### Modifying Existing Filters

All filter implementations are self-contained methods:
- `sobelx_func()`, `sobely_func()`
- `Canny_edge_detection()`
- `ILPF()`, `GLPF()`, `BLPF()`, etc.
- `arithmetic_mean_filter()`, `geometric_mean_filter()`, etc.

Simply modify the respective method to change behavior.

## 🐛 Troubleshooting

### Camera Issues
**Problem**: "Cannot open camera" error
**Solution**: 
- Ensure no other application is using the camera
- Check camera permissions in system settings
- Try changing camera index: `cv2.VideoCapture(1)` or `(2)`

### Performance Issues
**Problem**: Low FPS or lag
**Solution**:
- Use smaller kernel sizes
- Reduce camera resolution
- Close other applications
- Try simpler filters first

### Import Errors
**Problem**: Module not found
**Solution**:
```bash
pip install --upgrade opencv-python numpy scikit-image pillow
```

### Display Issues
**Problem**: Image doesn't fit or appears distorted
**Solution**:
- Resize the window
- Application auto-scales to fit canvas
- Check if image loaded correctly

## 📚 Educational Value

This project is excellent for:
- **Learning Computer Vision**: Practical implementation of classic algorithms
- **Understanding Image Processing**: See immediate results of parameter changes
- **Algorithm Comparison**: Switch between filters to understand differences
- **Parameter Tuning**: Learn optimal settings for different scenarios

### Recommended Learning Path
1. Start with **Sobel filters** to understand edge detection basics
2. Experiment with **Canny** to see multi-stage processing
3. Compare **Low-Pass filters** to understand frequency domain
4. Test **Mean filters** on noisy images
5. Use **Order Statistic** filters for specific noise types

## 🤝 Contributing

Contributions are welcome! Here are some ideas:
- Additional filters (Laplacian, Prewitt, etc.)
- Batch processing mode
- Filter presets/favorites
- Image comparison view (before/after)
- Export filter settings
- Video file processing

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV**: Computer vision library
- **scikit-image**: Image processing algorithms
- **Tkinter**: GUI framework
- **NumPy**: Numerical computations

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐
