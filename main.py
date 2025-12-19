"""
Image Processing Studio - Ultimate Control Version
Individual controls for EVERY parameter in EVERY filter
"""

import cv2
import numpy as np
from skimage.color import rgb2gray
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading
import time


class UltimateControlGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing Studio - Ultimate Control")
        self.root.geometry("1700x900")
        self.root.configure(bg='#2b2b2b')

        # Camera and state
        self.cap = None
        self.running = False
        self.current_frame = None
        self.processed_frame = None
        self.current_mode = None

        # ALL PARAMETERS FOR ALL FILTERS
        self.params = {
            # Edge Detection - Sobel
            'sobel_kernel': 3,

            # Canny Edge Detection
            'canny_kernel': 3,
            'canny_sigma': 0,
            'canny_low_ratio': 30,  # Now direct threshold value (0-255)
            'canny_high_ratio': 60,  # Now direct threshold value (0-255)

            # Frequency - ILPF
            'ilpf_radius': 30,

            # Frequency - GLPF
            'glpf_radius': 30,

            # Frequency - BLPF
            'blpf_radius': 30,
            'blpf_order': 2,

            # Frequency - IHPF
            'ihpf_radius': 30,

            # Frequency - GHPF
            'ghpf_radius': 30,

            # Frequency - BHPF
            'bhpf_radius': 30,
            'bhpf_order': 2,

            # Arithmetic Mean
            'arith_kernel': 3,

            # Geometric Mean
            'geo_kernel': 3,

            # Harmonic Mean
            'harm_kernel': 3,

            # Contraharmonic Mean
            'contra_kernel': 3,
            'contra_Q': 1.5,

            # Median Filter
            'median_kernel': 3,

            # Min Filter
            'min_kernel': 3,

            # Max Filter
            'max_kernel': 3,

            # Midpoint Filter
            'midpoint_kernel': 3,
        }

        self.create_gui()

    def create_gui(self):
        """Create GUI with ultimate control"""

        # ========== TOP BAR ==========
        top_bar = tk.Frame(self.root, bg='#1e1e1e', height=70)
        top_bar.pack(fill='x')
        top_bar.pack_propagate(False)

        tk.Label(top_bar, text="📷 Image Processing Studio - Ultimate Control",
                 bg='#1e1e1e', fg='#ffffff',
                 font=('Arial', 18, 'bold')).pack(side='left', padx=20)

        # Main buttons
        btn_frame = tk.Frame(top_bar, bg='#1e1e1e')
        btn_frame.pack(side='right', padx=20)

        self.camera_btn = tk.Button(btn_frame, text="▶ Camera",
                                    command=self.toggle_camera,
                                    bg='#4CAF50', fg='white',
                                    font=('Arial', 11, 'bold'),
                                    width=10, height=2, relief='flat')
        self.camera_btn.pack(side='left', padx=5)

        tk.Button(btn_frame, text="📁 Load",
                  command=self.load_image,
                  bg='#2196F3', fg='white',
                  font=('Arial', 11, 'bold'),
                  width=10, height=2, relief='flat').pack(side='left', padx=5)

        tk.Button(btn_frame, text="💾 Save",
                  command=self.save_image,
                  bg='#FF9800', fg='white',
                  font=('Arial', 11, 'bold'),
                  width=10, height=2, relief='flat').pack(side='left', padx=5)

        # ========== MAIN CONTAINER ==========
        main = tk.Frame(self.root, bg='#2b2b2b')
        main.pack(fill='both', expand=True, padx=10, pady=10)

        # LEFT: Image display
        left = tk.Frame(main, bg='#1e1e1e')
        left.pack(side='left', fill='both', expand=True, padx=(0, 5))

        # Status
        status_frame = tk.Frame(left, bg='#1e1e1e', height=50)
        status_frame.pack(fill='x', padx=10, pady=5)
        status_frame.pack_propagate(False)

        self.status = tk.Label(status_frame, text="Ready | Select a filter to see its controls",
                               bg='#1e1e1e', fg='#00ff00',
                               font=('Arial', 11, 'bold'), anchor='w')
        self.status.pack(side='left', fill='x', expand=True)

        self.fps = tk.Label(status_frame, text="",
                            bg='#1e1e1e', fg='#ffffff',
                            font=('Arial', 11))
        self.fps.pack(side='right')

        # Canvas
        self.canvas = tk.Canvas(left, bg='#000000', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True, padx=10, pady=10)

        # RIGHT: Controls
        right = tk.Frame(main, bg='#1e1e1e', width=600)
        right.pack(side='right', fill='y')
        right.pack_propagate(False)

        self.create_controls(right)

        # Bind keys
        self.root.bind('<Key>', self.key_press)

    def create_controls(self, parent):
        """Create ultimate control panel"""

        tk.Label(parent, text="⚙️ ULTIMATE CONTROLS",
                 bg='#1e1e1e', fg='#ffffff',
                 font=('Arial', 14, 'bold')).pack(pady=(10, 5))

        tk.Label(parent, text="Every filter has its own dedicated controls below",
                 bg='#1e1e1e', fg='#ffd54f',
                 font=('Arial', 9, 'italic')).pack(pady=(0, 10))

        # Scrollable area
        canvas = tk.Canvas(parent, bg='#1e1e1e', highlightthickness=0)
        scrollbar = tk.Scrollbar(parent, orient='vertical', command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg='#1e1e1e')

        scroll_frame.bind("<Configure>",
                          lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scroll_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side='left', fill='both', expand=True, padx=(10, 0))
        scrollbar.pack(side='right', fill='y')

        # ========== EDGE DETECTION ==========
        self.add_section(scroll_frame, "🔍 EDGE DETECTION")

        # Sobel X
        self.add_filter_with_controls(scroll_frame, "X", "Sobel X", 'sobelx', [
            ('sobel_kernel', "Kernel Size", 1, 31, 2, "3-7 optimal"),
        ])

        # Sobel Y
        self.add_filter_with_controls(scroll_frame, "Y", "Sobel Y", 'sobely', [
            ('sobel_kernel', "Kernel Size", 1, 31, 2, "3-7 optimal"),
        ])

        # Gradient
        self.add_filter_with_controls(scroll_frame, "S", "Gradient Magnitude", 'gradient', [
            ('sobel_kernel', "Kernel Size", 1, 31, 2, "3-7 optimal"),
        ])

        # Canny
        self.add_filter_with_controls(scroll_frame, "C", "Canny Edge", 'canny', [
            ('canny_kernel', "Kernel Size", 1, 31, 2, "3-7 optimal"),
            ('canny_sigma', "Gaussian Sigma", 0, 10, 1, "0=auto, 1-3 typical"),
            ('canny_low_ratio', "Low Threshold", 0, 255, 5, "30-100 typical"),
            ('canny_high_ratio', "High Threshold", 0, 255, 5, "60-200 typical"),
        ])

        # ========== FREQUENCY FILTERS ==========
        self.add_section(scroll_frame, "🌊 LOW-PASS FILTERS (Smoothing)")

        self.add_filter_with_controls(scroll_frame, "1", "Ideal LPF", 'ilpf', [
            ('ilpf_radius', "Cutoff Radius", 1, 200, 5, "10-50 typical"),
        ])

        self.add_filter_with_controls(scroll_frame, "2", "Gaussian LPF", 'glpf', [
            ('glpf_radius', "Cutoff Radius", 1, 200, 5, "20-80 optimal"),
        ])

        self.add_filter_with_controls(scroll_frame, "3", "Butterworth LPF", 'blpf', [
            ('blpf_radius', "Cutoff Radius", 1, 200, 5, "20-80 optimal"),
            ('blpf_order', "Order (n)", 1, 10, 1, "2-4 typical"),
        ])

        self.add_section(scroll_frame, "⚡ HIGH-PASS FILTERS (Sharpening)")

        self.add_filter_with_controls(scroll_frame, "4", "Ideal HPF", 'ihpf', [
            ('ihpf_radius', "Cutoff Radius", 1, 200, 5, "10-50 typical"),
        ])

        self.add_filter_with_controls(scroll_frame, "5", "Gaussian HPF", 'ghpf', [
            ('ghpf_radius', "Cutoff Radius", 1, 200, 5, "20-80 optimal"),
        ])

        self.add_filter_with_controls(scroll_frame, "6", "Butterworth HPF", 'bhpf', [
            ('bhpf_radius', "Cutoff Radius", 1, 200, 5, "20-80 optimal"),
            ('bhpf_order', "Order (n)", 1, 10, 1, "2-4 typical"),
        ])

        # ========== MEAN FILTERS ==========
        self.add_section(scroll_frame, "📊 MEAN FILTERS (Noise Reduction)")

        self.add_filter_with_controls(scroll_frame, "A", "Arithmetic Mean", 'arith_mean', [
            ('arith_kernel', "Kernel Size", 1, 31, 2, "3-9 optimal"),
        ])

        self.add_filter_with_controls(scroll_frame, "G", "Geometric Mean", 'geo_mean', [
            ('geo_kernel', "Kernel Size", 1, 31, 2, "3-7 for Gaussian noise"),
        ])

        self.add_filter_with_controls(scroll_frame, "H", "Harmonic Mean", 'harm_mean', [
            ('harm_kernel', "Kernel Size", 1, 31, 2, "3-7 for salt noise"),
        ])

        self.add_filter_with_controls(scroll_frame, "M", "Contraharmonic Mean", 'contra_mean', [
            ('contra_kernel', "Kernel Size", 1, 31, 2, "3-7 optimal"),
            ('contra_Q', "Q Order", -5.0, 5.0, 0.2, "Q>0: pepper | Q<0: salt"),
        ])

        # ========== ORDER STATISTIC ==========
        self.add_section(scroll_frame, "📈 ORDER STATISTIC FILTERS")

        self.add_filter_with_controls(scroll_frame, "D", "Median Filter", 'median', [
            ('median_kernel', "Kernel Size", 1, 31, 2, "3-9 for salt & pepper"),
        ])

        self.add_filter_with_controls(scroll_frame, "I", "Min Filter (Erosion)", 'min', [
            ('min_kernel', "Kernel Size", 1, 31, 2, "3-7 removes white"),
        ])

        self.add_filter_with_controls(scroll_frame, "O", "Max Filter (Dilation)", 'max', [
            ('max_kernel', "Kernel Size", 1, 31, 2, "3-7 removes black"),
        ])

        self.add_filter_with_controls(scroll_frame, "P", "Midpoint Filter", 'midpoint', [
            ('midpoint_kernel', "Kernel Size", 1, 31, 2, "3-7 optimal"),
        ])

        # ========== RESET ==========
        self.add_section(scroll_frame, "🔄 RESET")
        tk.Button(scroll_frame, text="N - No Filter (Original)",
                  command=lambda: self.set_filter(None),
                  bg='#f44336', fg='white',
                  font=('Arial', 10, 'bold'),
                  height=2, relief='flat').pack(fill='x', padx=10, pady=5)

        # Info
        tk.Label(scroll_frame,
                 text="💡 Every filter has its own controls\n"
                      "✏️ Click any value to type manually\n"
                      "⌨️ Keyboard shortcuts still work",
                 bg='#1e1e1e', fg='#888888',
                 font=('Arial', 9, 'italic'),
                 justify='center').pack(pady=20)

    def add_section(self, parent, title):
        frame = tk.Frame(parent, bg='#0d47a1', height=35)
        frame.pack(fill='x', padx=10, pady=(15, 5))
        frame.pack_propagate(False)
        tk.Label(frame, text=title, bg='#0d47a1', fg='#ffffff',
                 font=('Arial', 10, 'bold')).pack(anchor='w', padx=10, pady=8)

    def add_filter_with_controls(self, parent, key, name, mode, controls):
        """Add filter button with its dedicated controls"""
        main_frame = tk.Frame(parent, bg='#2d2d2d', relief='solid', borderwidth=1)
        main_frame.pack(fill='x', padx=10, pady=5)

        # Filter button
        btn_frame = tk.Frame(main_frame, bg='#2d2d2d')
        btn_frame.pack(fill='x', padx=5, pady=5)

        tk.Label(btn_frame, text=key, bg='#000000', fg='#00ff00',
                 font=('Consolas', 11, 'bold'),
                 width=4).pack(side='left', padx=5)

        tk.Button(btn_frame, text=name,
                  command=lambda: self.set_filter(mode),
                  bg='#424242', fg='#ffffff',
                  font=('Arial', 10, 'bold'),
                  relief='flat', anchor='w').pack(side='left', fill='x', expand=True, padx=5)

        # Controls for this filter
        if controls:
            ctrl_container = tk.Frame(main_frame, bg='#363636')
            ctrl_container.pack(fill='x', padx=5, pady=(0, 5))

            for param_key, label, min_val, max_val, step, tip in controls:
                self.add_inline_param(ctrl_container, label, param_key, min_val, max_val, step, tip)

    def add_inline_param(self, parent, label, param_key, min_val, max_val, step, tip):
        """Add inline parameter control"""
        frame = tk.Frame(parent, bg='#363636')
        frame.pack(fill='x', padx=5, pady=3)

        # Label
        label_frame = tk.Frame(frame, bg='#363636')
        label_frame.pack(side='left', fill='x', expand=True)

        tk.Label(label_frame, text=label + ":", bg='#363636', fg='#ffffff',
                 font=('Arial', 8, 'bold'), anchor='w').pack(side='left')

        tk.Label(label_frame, text=f"💡 {tip}",
                 bg='#363636', fg='#ffd54f',
                 font=('Arial', 7, 'italic'), anchor='w').pack(side='left', padx=5)

        # Controls
        ctrl = tk.Frame(frame, bg='#363636')
        ctrl.pack(side='right')

        # Minus
        tk.Button(ctrl, text="−",
                  command=lambda: self.adjust_param(param_key, -step, min_val, max_val),
                  bg='#d32f2f', fg='white',
                  font=('Arial', 9, 'bold'),
                  width=2, relief='flat').pack(side='left', padx=1)

        # Entry
        entry = tk.Entry(ctrl,
                         bg='#000000', fg='#00ff00',
                         font=('Consolas', 9, 'bold'),
                         width=7, justify='center',
                         relief='flat', insertbackground='#00ff00')
        entry.pack(side='left', padx=3)
        entry.insert(0, str(self.params[param_key]))

        entry.bind('<Return>', lambda e: self.manual_entry(param_key, entry, min_val, max_val))
        entry.bind('<FocusOut>', lambda e: self.manual_entry(param_key, entry, min_val, max_val))

        setattr(self, f'entry_{param_key}', entry)

        # Plus
        tk.Button(ctrl, text="+",
                  command=lambda: self.adjust_param(param_key, step, min_val, max_val),
                  bg='#388e3c', fg='white',
                  font=('Arial', 9, 'bold'),
                  width=2, relief='flat').pack(side='left', padx=1)

    def manual_entry(self, param_key, entry, min_val, max_val):
        try:
            value = entry.get()

            if isinstance(self.params[param_key], float):
                new_val = float(value)
            else:
                new_val = int(float(value))
                if 'kernel' in param_key and new_val % 2 == 0:
                    new_val += 1

            new_val = max(min_val, min(new_val, max_val))
            self.params[param_key] = new_val

            if isinstance(new_val, float):
                entry.delete(0, tk.END)
                entry.insert(0, f"{new_val:.2f}")
            else:
                entry.delete(0, tk.END)
                entry.insert(0, str(new_val))

        except ValueError:
            current = self.params[param_key]
            entry.delete(0, tk.END)
            if isinstance(current, float):
                entry.insert(0, f"{current:.2f}")
            else:
                entry.insert(0, str(current))
            messagebox.showwarning("Invalid", f"Enter number between {min_val} and {max_val}")

    def adjust_param(self, key, change, min_val, max_val):
        current = self.params[key]
        new_val = current + change

        if 'kernel' in key and isinstance(new_val, int) and new_val % 2 == 0:
            new_val += 1 if change > 0 else -1

        new_val = max(min_val, min(new_val, max_val))
        self.params[key] = new_val

        entry = getattr(self, f'entry_{key}')
        entry.delete(0, tk.END)
        if isinstance(new_val, float):
            entry.insert(0, f"{new_val:.2f}")
        else:
            entry.insert(0, str(new_val))

    def set_filter(self, mode):
        self.current_mode = mode
        if mode:
            self.status.config(text=f"Active: {mode.replace('_', ' ').title()} | Adjust its controls above")
        else:
            self.status.config(text="Ready | Select a filter to see its controls")

        # If there's a loaded image (not camera running), update it immediately
        if self.current_frame is not None and not self.running:
            processed = self.apply_filter(self.current_frame)
            self.processed_frame = processed
            self.update_canvas(processed)

    def update_static_image(self):
        """Continuously update loaded image when parameters change"""
        if self.current_frame is not None and not self.running:
            processed = self.apply_filter(self.current_frame)
            self.processed_frame = processed
            self.update_canvas(processed)
            # Schedule next update
            self.root.after(100, self.update_static_image)

    def key_press(self, event):
        key = event.char.lower()

        filter_map = {
            'x': 'sobelx', 'y': 'sobely', 's': 'gradient', 'c': 'canny',
            '1': 'ilpf', '2': 'glpf', '3': 'blpf',
            '4': 'ihpf', '5': 'ghpf', '6': 'bhpf',
            'a': 'arith_mean', 'g': 'geo_mean', 'h': 'harm_mean', 'm': 'contra_mean',
            'd': 'median', 'i': 'min', 'o': 'max', 'p': 'midpoint',
            'n': None
        }

        if key in filter_map:
            self.set_filter(filter_map[key])
        elif key == 'q':
            self.root.quit()

    def toggle_camera(self):
        if not self.running:
            self.start_camera()
        else:
            self.stop_camera()

    def start_camera(self):
        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Cannot open camera")
                return

            self.running = True
            self.camera_btn.config(text="⏹ Stop", bg='#f44336')
            threading.Thread(target=self.camera_loop, daemon=True).start()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def stop_camera(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.camera_btn.config(text="▶ Camera", bg='#4CAF50')
        # Note: update_static_image will naturally stop when camera starts

    def camera_loop(self):
        fps_time = time.time()
        fps_count = 0

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break

            self.current_frame = frame
            processed = self.apply_filter(frame)
            self.processed_frame = processed
            self.update_canvas(processed)

            fps_count += 1
            if fps_count % 10 == 0:
                fps_val = 10 / (time.time() - fps_time)
                self.fps.config(text=f"FPS: {fps_val:.1f}")
                fps_time = time.time()

    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp"), ("All", "*.*")])

        if path:
            self.stop_camera()
            img = cv2.imread(path)
            if img is not None:
                self.current_frame = img
                processed = self.apply_filter(img)
                self.processed_frame = processed
                self.update_canvas(processed)
                # Start a timer to continuously update the image when filter changes
                self.update_static_image()

    def save_image(self):
        if self.processed_frame is None:
            messagebox.showwarning("Warning", "No image to save")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])

        if path:
            cv2.imwrite(path, self.processed_frame)
            messagebox.showinfo("Success", "Saved!")

    def apply_filter(self, frame):
        """Apply filter with individual parameters"""
        if frame is None or self.current_mode is None:
            return frame

        try:
            mode = self.current_mode

            # Edge detection
            if mode == 'sobelx':
                k = self.params['sobel_kernel']
                result = self.sobelx_func(frame, k)
                return cv2.cvtColor(result.astype(np.uint8), cv2.COLOR_GRAY2BGR)

            elif mode == 'sobely':
                k = self.params['sobel_kernel']
                result = self.sobely_func(frame, k)
                return cv2.cvtColor(result.astype(np.uint8), cv2.COLOR_GRAY2BGR)

            elif mode == 'gradient':
                k = self.params['sobel_kernel']
                sx = self.sobelx_func(frame, k)
                sy = self.sobely_func(frame, k)
                result = self.gradient_magnitude_func(sx, sy)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'canny':
                k = self.params['canny_kernel']
                result = self.Canny_edge_detection(frame, k)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            # Frequency filters
            elif mode == 'ilpf':
                r = self.params['ilpf_radius']
                result, _ = self.ILPF(frame, r)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'glpf':
                r = self.params['glpf_radius']
                result, _ = self.GLPF(frame, r)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'blpf':
                r = self.params['blpf_radius']
                n = self.params['blpf_order']
                result, _ = self.BLPF(frame, r, n)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'ihpf':
                r = self.params['ihpf_radius']
                result, _ = self.IHPF(frame, r)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'ghpf':
                r = self.params['ghpf_radius']
                result, _ = self.GHPF(frame, r)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'bhpf':
                r = self.params['bhpf_radius']
                n = self.params['bhpf_order']
                result, _ = self.BHPF(frame, r, n)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            # Mean filters
            elif mode == 'arith_mean':
                k = self.params['arith_kernel']
                result = self.arithmetic_mean_filter(frame, k)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'geo_mean':
                k = self.params['geo_kernel']
                result = self.geometric_mean_filter(frame, k)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'harm_mean':
                k = self.params['harm_kernel']
                result = self.harmonic_mean_filter(frame, k)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'contra_mean':
                k = self.params['contra_kernel']
                q = self.params['contra_Q']
                result = self.contraharmonic_mean_filter(frame, k, q)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            # Order statistic
            elif mode == 'median':
                k = self.params['median_kernel']
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                k = k if k % 2 == 1 else k + 1
                result = cv2.medianBlur(gray, k)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'min':
                k = self.params['min_kernel']
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                kernel = np.ones((k, k), np.uint8)
                result = cv2.erode(gray, kernel)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'max':
                k = self.params['max_kernel']
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                kernel = np.ones((k, k), np.uint8)
                result = cv2.dilate(gray, kernel)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

            elif mode == 'midpoint':
                k = self.params['midpoint_kernel']
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                kernel = np.ones((k, k), np.uint8)
                min_f = cv2.erode(gray, kernel)
                max_f = cv2.dilate(gray, kernel)
                result = ((min_f.astype(np.int16) + max_f.astype(np.int16)) // 2).astype(np.uint8)
                return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

        except Exception as e:
            print(f"Error: {e}")
            return frame

        return frame

    def update_canvas(self, frame):
        if frame is None:
            return

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        if w <= 1 or h <= 1:
            self.root.after(100, lambda: self.update_canvas(frame))
            return

        fh, fw = frame.shape[:2]
        scale = min(w / fw, h / fh) * 0.95
        nw, nh = int(fw * scale), int(fh * scale)

        resized = cv2.resize(frame, (nw, nh))
        rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        photo = ImageTk.PhotoImage(image=img)

        self.canvas.delete('all')
        x, y = (w - nw) // 2, (h - nh) // 2
        self.canvas.create_image(x, y, anchor='nw', image=photo)
        self.canvas.image = photo

    # ========== EXACT METHODS FROM NOTEBOOK ==========

    def sobelx_func(self, frame, ksize):
        gray = rgb2gray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
        return sobelx

    def sobely_func(self, frame, ksize):
        gray = rgb2gray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
        return sobely

    def gradient_magnitude_func(self, sobelx, sobely):
        gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)
        gradient_magnitude *= 255.0 / gradient_magnitude.max()
        return gradient_magnitude.astype(np.uint8)

    def Canny_edge_detection(self, frame, ksize):
        # Use the improved Canny implementation with direct threshold values
        low_threshold = self.params['canny_low_ratio']  # Direct threshold value (0-255)
        high_threshold = self.params['canny_high_ratio']  # Direct threshold value (0-255)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (ksize, ksize), 0)
        gx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=ksize)
        gy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=ksize)
        mag = np.hypot(gx, gy)
        mag = (mag / mag.max()) * 255
        ang = np.degrees(np.arctan2(gy, gx))
        ang[ang < 0] += 180
        M, N = mag.shape
        Z = np.zeros((M, N), dtype=np.float32)

        # Non-Max Suppression
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                angle = ang[i, j]
                if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                    q, r = mag[i, j + 1], mag[i, j - 1]
                elif 22.5 <= angle < 67.5:
                    q, r = mag[i + 1, j - 1], mag[i - 1, j + 1]
                elif 67.5 <= angle < 112.5:
                    q, r = mag[i + 1, j], mag[i - 1, j]
                else:
                    q, r = mag[i - 1, j - 1], mag[i + 1, j + 1]
                if mag[i, j] >= q and mag[i, j] >= r:
                    Z[i, j] = mag[i, j]

        # Double Threshold using direct threshold values
        strong, weak = 255, 75
        res = np.zeros_like(Z, dtype=np.uint8)
        res[Z >= high_threshold] = strong
        res[(Z < high_threshold) & (Z >= low_threshold)] = weak

        # Hysteresis
        result = res.copy()
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if result[i, j] == weak:
                    if strong in result[i - 1:i + 2, j - 1:j + 2]:
                        result[i, j] = strong
                    else:
                        result[i, j] = 0

        return result

    def DFT_and_reconstruct(self, gray_img, filter_mask=None):
        img = np.float32(gray_img)
        dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])
        c = 255.0 / (np.log(1 + np.max(magnitude)) + 1e-9)
        magnitude_spectrum = c * np.log(magnitude + 1)

        if filter_mask is not None:
            fshift = dft_shift * filter_mask
        else:
            fshift = dft_shift

        f_ishift = np.fft.ifftshift(fshift)
        img_back = cv2.idft(f_ishift)
        img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
        if img_back.max() != 0:
            img_back = img_back / img_back.max() * 255
        img_back = img_back.astype(np.uint8)
        mag_display = np.uint8(np.clip(magnitude_spectrum, 0, 255))
        return img_back, mag_display, dft_shift

    def ILPF(self, frame, r):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        mask = np.zeros((rows, cols, 2), np.float32)
        crow, ccol = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        mask_area = (x - ccol) ** 2 + (y - crow) ** 2 <= r * r
        mask[mask_area] = 1
        img_back, mag_display, _ = self.DFT_and_reconstruct(gray, filter_mask=mask)
        return img_back, mag_display

    def GLPF(self, frame, r):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        D0 = float(r) if r > 0 else 1.0
        mask = np.zeros((rows, cols, 2), np.float32)
        crow, ccol = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        D = np.sqrt((x - ccol) ** 2 + (y - crow) ** 2)
        H = np.exp(-(D ** 2) / (2 * (D0 ** 2)))
        mask[:, :, 0] = H
        mask[:, :, 1] = H
        img_back, mag_display, _ = self.DFT_and_reconstruct(gray, filter_mask=mask)
        return img_back, mag_display

    def BLPF(self, frame, r, n=2):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        D0 = float(r) if r > 0 else 1.0
        mask = np.zeros((rows, cols, 2), np.float32)
        crow, ccol = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        D = np.sqrt((x - ccol) ** 2 + (y - crow) ** 2)
        H = 1.0 / (1.0 + (D / (D0 + 1e-9)) ** (2 * n))
        mask[:, :, 0] = H
        mask[:, :, 1] = H
        img_back, mag_display, _ = self.DFT_and_reconstruct(gray, filter_mask=mask)
        return img_back, mag_display

    def IHPF(self, frame, r):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        mask = np.ones((rows, cols, 2), np.float32)
        crow, ccol = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        mask_area = (x - ccol) ** 2 + (y - crow) ** 2 <= r * r
        mask[mask_area] = 0
        img_back, mag_display, _ = self.DFT_and_reconstruct(gray, filter_mask=mask)
        return img_back, mag_display

    def GHPF(self, frame, r):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        D0 = float(r) if r > 0 else 1.0
        mask = np.zeros((rows, cols, 2), np.float32)
        crow, ccol = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        D = np.sqrt((x - ccol) ** 2 + (y - crow) ** 2)
        H = 1.0 - np.exp(-(D ** 2) / (2 * (D0 ** 2)))
        mask[:, :, 0] = H
        mask[:, :, 1] = H
        img_back, mag_display, _ = self.DFT_and_reconstruct(gray, filter_mask=mask)
        return img_back, mag_display

    def BHPF(self, frame, r, n=2):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        D0 = float(r) if r > 0 else 1.0
        mask = np.zeros((rows, cols, 2), np.float32)
        crow, ccol = rows // 2, cols // 2
        y, x = np.ogrid[:rows, :cols]
        D = np.sqrt((x - ccol) ** 2 + (y - crow) ** 2)
        H_low = 1.0 / (1.0 + (D / (D0 + 1e-9)) ** (2 * n))
        H = 1.0 - H_low
        mask[:, :, 0] = H
        mask[:, :, 1] = H
        img_back, mag_display, _ = self.DFT_and_reconstruct(gray, filter_mask=mask)
        return img_back, mag_display

    def arithmetic_mean_filter(self, frame, ksize):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
        filtered = cv2.filter2D(gray, -1, kernel)
        return filtered

    def geometric_mean_filter(self, frame, ksize):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = gray.astype(np.float32) + 1.0
        log_img = np.log(gray)
        kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
        log_mean = cv2.filter2D(log_img, -1, kernel)
        geo_mean = np.exp(log_mean)
        geo_mean = np.clip(geo_mean, 0, 255)
        return geo_mean.astype(np.uint8)

    def harmonic_mean_filter(self, frame, ksize):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = gray.astype(np.float32) + 1.0
        inv = 1.0 / gray
        kernel = np.ones((ksize, ksize), np.float32)
        inv_sum = cv2.filter2D(inv, -1, kernel)
        h_mean = (ksize * ksize) / inv_sum
        h_mean = np.clip(h_mean, 0, 255)
        return h_mean.astype(np.uint8)

    def contraharmonic_mean_filter(self, frame, ksize, Q=1.5):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = gray.astype(np.float32)
        numerator = cv2.filter2D(np.power(gray, Q + 1), -1, np.ones((ksize, ksize)))
        denominator = cv2.filter2D(np.power(gray, Q), -1, np.ones((ksize, ksize))) + 1e-9
        ch_mean = numerator / denominator
        ch_mean = np.clip(ch_mean, 0, 255)
        return ch_mean.astype(np.uint8)


def main():
    root = tk.Tk()
    app = UltimateControlGUI(root)

    def on_close():
        app.running = False
        if app.cap:
            app.cap.release()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()


if __name__ == "__main__":
    main()