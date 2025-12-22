# Quick Reference Guide

## 🎮 Keyboard Shortcuts

### Edge Detection
| Key | Filter | Description |
|-----|--------|-------------|
| `X` | Sobel X | Detects vertical edges |
| `Y` | Sobel Y | Detects horizontal edges |
| `S` | Gradient | Combined edge magnitude |
| `C` | Canny | Advanced multi-stage edge detection |

### Low-Pass Filters (Smoothing)
| Key | Filter | Best For |
|-----|--------|----------|
| `1` | Ideal LPF | Sharp cutoff (may cause ringing) |
| `2` | Gaussian LPF | Smooth transition, no ringing |
| `3` | Butterworth LPF | Adjustable transition sharpness |

### High-Pass Filters (Sharpening)
| Key | Filter | Best For |
|-----|--------|----------|
| `4` | Ideal HPF | Sharp edge enhancement |
| `5` | Gaussian HPF | Smooth detail preservation |
| `6` | Butterworth HPF | Adjustable sharpening strength |

### Mean Filters (Noise Reduction)
| Key | Filter | Removes |
|-----|--------|---------|
| `A` | Arithmetic Mean | General noise |
| `G` | Geometric Mean | Gaussian noise |
| `H` | Harmonic Mean | Salt noise (bright pixels) |
| `M` | Contraharmonic Mean | Salt or Pepper (adjustable) |

### Order Statistic Filters
| Key | Filter | Effect |
|-----|--------|--------|
| `D` | Median | Salt & pepper noise |
| `I` | Min (Erosion) | Removes white noise, shrinks bright areas |
| `O` | Max (Dilation) | Removes black noise, expands bright areas |
| `P` | Midpoint | Random noise, combines min & max |

### General
| Key | Action |
|-----|--------|
| `N` | Remove all filters (show original) |
| `Q` | Quit application |

## 📊 Parameter Quick Reference

### Kernel Size
**Range**: 1-31 (odd numbers only)
- **3-5**: Fine details, minimal smoothing
- **7-9**: Balanced smoothing
- **11+**: Heavy smoothing, best for noisy images

### Canny Thresholds
**Low Threshold**: 0-255 (typically 30-100)
**High Threshold**: 0-255 (typically 60-200)
- Keep ratio 2:1 or 3:1 (high:low)
- Lower values = more edges detected

### Frequency Filter Radius
**Range**: 1-200
- **10-30**: Strong effect
- **40-80**: Moderate effect
- **100+**: Gentle effect

### Butterworth Order
**Range**: 1-10 (typically 2-4)
- **1**: Similar to Gaussian
- **2-4**: Balanced
- **5+**: Approaches Ideal filter

### Contraharmonic Q
**Range**: -5.0 to 5.0
- **Q > 0**: Removes pepper noise (dark pixels)
- **Q < 0**: Removes salt noise (bright pixels)
- **Q = 0**: Same as arithmetic mean
- **Typical**: ±1.5 to ±2.5

## 🎯 Common Use Cases

### Removing Noise

| Noise Type | Best Filter | Settings |
|------------|-------------|----------|
| Salt & Pepper | Median Filter (`D`) | Kernel: 3-5 |
| Gaussian | Geometric Mean (`G`) | Kernel: 3-7 |
| Salt (bright) | Harmonic Mean (`H`) | Kernel: 3-7 |
| Pepper (dark) | Contraharmonic (`M`) | Q > 0, Kernel: 3-7 |
| Random | Gaussian LPF (`2`) | Radius: 40-80 |

### Enhancing Images

| Goal | Best Filter | Settings |
|------|-------------|----------|
| Find edges | Canny (`C`) | Low: 50, High: 150 |
| Sharpen details | Gaussian HPF (`5`) | Radius: 30-50 |
| Smooth while preserving edges | Median (`D`) | Kernel: 3-5 |
| Blur background | Gaussian LPF (`2`) | Radius: 60-100 |

### Computer Vision Tasks

| Task | Recommended Approach |
|------|---------------------|
| Object Detection | Canny + appropriate thresholds |
| Feature Extraction | Sobel Gradient + Threshold |
| Noise Reduction | Median or Gaussian LPF |
| Edge Enhancement | Butterworth HPF (order 2-3) |
| Image Smoothing | Gaussian LPF or Arithmetic Mean |

## 💡 Tips & Tricks

### Performance
- Start with smaller kernel sizes
- Simpler filters run faster
- Frequency filters are most CPU-intensive
- Lower camera resolution for better FPS

### Getting Best Results
1. Always remove noise first (if present)
2. Then apply edge detection or sharpening
3. Try multiple filters to compare
4. Use keyboard shortcuts for quick switching

### Parameter Tuning
1. Start with default values
2. Adjust one parameter at a time
3. See real-time effects
4. Click values to type exact numbers

### Common Mistakes
- ❌ Using even kernel sizes (auto-corrected to odd)
- ❌ High threshold lower than low threshold in Canny
- ❌ Excessive kernel sizes causing over-smoothing
- ❌ Wrong Q sign in Contraharmonic for noise type

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Low FPS | Reduce kernel size or use simpler filter |
| Too blurry | Decrease kernel size or radius |
| Not enough smoothing | Increase kernel size or radius |
| Edges too thin | Increase Canny low threshold |
| Edges too thick | Decrease Canny low threshold |
| Ringing artifacts | Switch from Ideal to Gaussian/Butterworth |

## 📸 Workflow Examples

### Example 1: Cleaning Noisy Photo
1. Load image (`📁 Load`)
2. Apply Median Filter (`D`, kernel: 5)
3. Apply Gaussian LPF (`2`, radius: 50)
4. Save result (`💾 Save`)

### Example 2: Edge Detection for Object Recognition
1. Start camera (`▶ Camera`)
2. Apply Gaussian LPF (`2`, radius: 30) to reduce noise
3. Apply Canny (`C`, low: 50, high: 150)
4. Adjust thresholds until edges are clear
5. Save best result (`💾 Save`)

### Example 3: Sharpening Blurry Image
1. Load image (`📁 Load`)
2. Apply Butterworth HPF (`6`)
3. Set radius: 40, order: 2
4. Fine-tune for desired sharpness
5. Save (`💾 Save`)

## 📚 Learn More

For detailed explanations:
- See main [README.md](README.md)
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for customization
- Read inline tooltips in the application

---

**Quick Start**: Load image → Press `C` for Canny edges → Adjust parameters → Save! 🎉
