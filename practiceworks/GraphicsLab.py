import tkinter as tk
from tkinter import ttk
import math
import random


class GraphicsApp:
    """Головний клас застосунку для виконання лабораторної роботи з графіки."""

    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторна робота: Графіка Tkinter")
        self.root.geometry("750x550")

        # --- ГЛОБАЛЬНІ ЗМІННІ ДЛЯ АНІМАЦІЇ (Розділ 6) ---
        self.H = 30
        self.Xpos = 2 * self.H
        self.Ypos = 200  # "Земля"
        self.Hmen = 30  # Висота тіла
        self.Rhead = 10
        self.Rhead2 = self.Rhead / 2
        self.revers = 1  # Напрямок руху
        self.L = self.H * 1.41
        self.num = 0  # Поза (0 або 1)
        self.timer_id = None
        self.timer_active = False

        # --- ЕКВІВАЛЕНТИ RG3 (Стилі кистей) для Розділу 7 ---
        self.BRUSH_STYLES = [
            '',  # 0: bsSolid (Не використовувати stipple)
            'gray25',  # 1: bsCross
            'half-tone',  # 2: bsDiagCross
            'gray12'  # 3: bsVertical
        ]

        # --- Змінні для керування (Розділ 7) ---
        self.action_var = tk.StringVar(value='0')
        self.brush_style_var = tk.StringVar(value='0')
        self.pen_mode_var = tk.StringVar(value='0')

        self.setup_ui()

    def setup_ui(self):
        """Створення інтерфейсу користувача з вкладками."""

        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # Створення вкладок
        tab_lines = ttk.Frame(notebook)
        notebook.add(tab_lines, text="Стилі ліній")

        tab_sinusoids = ttk.Frame(notebook)
        notebook.add(tab_sinusoids, text="Синусоїди")

        tab_animation = ttk.Frame(notebook)
        notebook.add(tab_animation, text="Мультиплікація")

        tab_penbrush = ttk.Frame(notebook)
        notebook.add(tab_penbrush, text="Перо і пензель")

        # Налаштування вкладок
        self.setup_lines_tab(tab_lines)
        self.setup_sinusoids_tab(tab_sinusoids)
        self.setup_animation_tab(tab_animation)
        self.setup_penbrush_tab(tab_penbrush)

    # ----------------------------------------------------------------------
    #                         РОЗДІЛ 3: СТИЛІ ЛІНІЙ
    # ----------------------------------------------------------------------

    def setup_lines_tab(self, tab):
        self.canvas_lines = tk.Canvas(tab, bg="white")
        self.canvas_lines.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        button_show = ttk.Button(tab, text="Показати", command=self.draw_line_styles)
        button_show.pack(pady=10)

    def draw_line_styles(self):
        self.canvas_lines.delete("all")

        # Оновлення розмірів перед отриманням width/height
        self.root.update_idletasks()
        widget_width = self.canvas_lines.winfo_width()

        y_start = 15

        styles = [
            None,  # 0: psSolid (None для суцільної лінії)
            (5, 5),  # 1: psDash
            (1, 4),  # 2: psDot
            (8, 3, 1, 3),  # 3: psDashDot
            (8, 3, 1, 3, 1, 3),  # 4: psDashDotDot
            (0, 0),  # 5: psClear
            None  # 6: psInsideFrame
        ]

        style_names = ["Solid (0)", "Dash (1)", "Dot (2)", "DashDot (3)", "DashDotDot (4)", "Clear (5)",
                       "InsideFrame (6)"]

        for i, style in enumerate(styles):
            y = (i + 1) * y_start * 2

            line_options = {
                "fill": "black",
                "width": 2,
                "tags": "line_style"
            }

            # Виключення параметра 'dash' для суцільних ліній
            if style is not None:
                line_options["dash"] = style

            # Робимо Clear-стиль невидимим
            if style == (0, 0):
                line_options["fill"] = ""

            self.canvas_lines.create_line(0, y, widget_width, y, **line_options)
            self.canvas_lines.create_text(widget_width - 150, y, text=style_names[i], anchor="w")

    # ----------------------------------------------------------------------
    #                         РОЗДІЛ 4: СИНУСОЇДИ
    # ----------------------------------------------------------------------

    def setup_sinusoids_tab(self, tab):
        canvas_frame = ttk.Frame(tab)
        canvas_frame.pack(pady=10, padx=10, expand=True, fill="both")

        self.canvas_pixels = tk.Canvas(canvas_frame, bg="white", highlightthickness=1)
        self.canvas_pixels.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)

        self.canvas_pen = tk.Canvas(canvas_frame, bg="white", highlightthickness=1)
        self.canvas_pen.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.BOTH)

        button_draw = ttk.Button(tab, text="Намалювати", command=self.draw_sinusoids)
        button_draw.pack(pady=10)

    def draw_sinusoids(self):
        self.canvas_pixels.delete("all")
        self.canvas_pen.delete("all")

        self.root.update_idletasks()
        width_pen = self.canvas_pen.winfo_width()
        height_pen = self.canvas_pen.winfo_height()

        width_pixels = self.canvas_pixels.winfo_width()
        height_pixels = self.canvas_pixels.winfo_height()

        points_pen = []
        Pi = 3.14159

        self.canvas_pen.create_line(0, height_pen / 2, width_pen, height_pen / 2, fill="gray")

        for px in range(width_pixels):
            X = px * 4.0 * Pi / width_pixels
            Y = math.sin(X) * 0.9
            PY = height_pixels - (Y + 1.0) * height_pixels / 2.0

            # Малювання пікселями (Image4)
            if 0 <= PY < height_pixels:
                self.canvas_pixels.create_rectangle(px, PY, px + 1, PY + 1, fill="black", outline="black")

            # Збір точок для малювання пером (Image5)
            points_pen.extend([px, PY])

        # Малювання на правому графіку (Пером)
        if points_pen:
            self.canvas_pen.create_line(points_pen, fill="blue", width=2, smooth=True)

    # ----------------------------------------------------------------------
    #                         РОЗДІЛ 6: МУЛЬТИПЛІКАЦІЯ
    # ----------------------------------------------------------------------

    def setup_animation_tab(self, tab):
        self.canvas_animation = tk.Canvas(tab, bg="white")
        self.canvas_animation.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.button_start_stop = ttk.Button(tab, text="Пуск", command=self.start_stop_animation)
        self.button_start_stop.pack(pady=10)

        # Малюємо початкове положення після невеликої затримки
        self.root.after(100, self.Draw)

    def Draw(self):
        self.canvas_animation.delete("figure")

        # Малювання "землі" (одноразово)
        if not self.canvas_animation.find_withtag("ground"):
            self.canvas_animation.create_line(0, self.Ypos + 3, self.canvas_animation.winfo_width(), self.Ypos + 3,
                                              width=4, fill="darkgreen", tags="ground")

        Yhead = self.Ypos - self.H - self.Hmen if self.num == 0 else self.Ypos - self.L - self.Hmen

        # --- Голова та Капелюх ---
        self.canvas_animation.create_oval(self.Xpos - self.Rhead, Yhead - 2 * self.Rhead, self.Xpos + self.Rhead, Yhead,
                                          fill="peachpuff", outline="black", tags="figure")
        self.canvas_animation.create_rectangle(self.Xpos - self.Rhead, Yhead - 2 * self.Rhead - 4,
                                               self.Xpos + self.Rhead, Yhead - 2 * self.Rhead - 1,
                                               fill="black", outline="black", tags="figure")

        # --- Тулуб ---
        self.canvas_animation.create_line(self.Xpos, self.Ypos - self.H, self.Xpos, Yhead, fill="black", tags="figure")

        if self.num == 0:
            # Рух 0: Ноги згинаються (V-форма)
            self.canvas_animation.create_line(self.Xpos - self.H, self.Ypos, self.Xpos, self.Ypos - self.H,
                                              fill="black", tags="figure")
            self.canvas_animation.create_line(self.Xpos + self.H, self.Ypos, self.Xpos, self.Ypos - self.H,
                                              fill="black", tags="figure")

            # Руки (зігнуті)
            self.canvas_animation.create_line(self.Xpos, Yhead + 4, self.Xpos + self.revers * self.H, Yhead - self.H,
                                              fill="black", tags="figure")
            self.canvas_animation.create_line(self.Xpos, Yhead + 4, self.Xpos + self.revers * self.H, Yhead + self.H,
                                              fill="black", tags="figure")

            # Кулаки
            self.canvas_animation.create_oval(self.Xpos + self.revers * self.H - self.Rhead2,
                                              Yhead - self.H - self.Rhead2,
                                              self.Xpos + self.revers * self.H + self.Rhead2,
                                              Yhead - self.H + self.Rhead2, fill="red", tags="figure")
            self.canvas_animation.create_oval(self.Xpos + self.revers * self.H - self.Rhead2,
                                              Yhead + self.H - self.Rhead2,
                                              self.Xpos + self.revers * self.H + self.Rhead2,
                                              Yhead + self.H + self.Rhead2, fill="red", tags="figure")

        elif self.num == 1:
            # Рух 1: Ноги прямі
            self.canvas_animation.create_line(self.Xpos, self.Ypos, self.Xpos, Yhead, fill="black", tags="figure")

            # Рука (простягнута)
            self.canvas_animation.create_line(self.Xpos, Yhead + 4, self.Xpos + self.revers * self.L, Yhead + 4,
                                              fill="black", tags="figure")

            # Кулак
            self.canvas_animation.create_oval(self.Xpos + self.revers * self.L - self.Rhead2, Yhead + 4 - self.Rhead2,
                                              self.Xpos + self.revers * self.L + self.Rhead2, Yhead + 4 + self.Rhead2,
                                              fill="red", tags="figure")

    def timer_tick(self):
        """Еквівалент Timer1Timer."""

        if (self.Xpos >= self.canvas_animation.winfo_width() - self.H) or (self.Xpos <= self.H):
            self.revers = -self.revers

        self.Xpos = self.Xpos + self.revers * self.H
        self.num = 1 - self.num

        self.Draw()

        if self.timer_active:
            self.timer_id = self.root.after(500, self.timer_tick)

    def start_stop_animation(self):
        """Обробник кнопки «Пуск/Стоп» (Button7Click)."""

        if self.timer_active:
            # Стоп
            self.root.after_cancel(self.timer_id)
            self.timer_active = False
            self.button_start_stop.config(text="Пуск")
        else:
            # Пуск
            self.Draw()
            self.timer_active = True
            self.button_start_stop.config(text="Стоп")
            self.timer_id = self.root.after(500, self.timer_tick)

    # ----------------------------------------------------------------------
    #                         РОЗДІЛ 7: ПЕРО І ПЕНЗЕЛЬ
    # ----------------------------------------------------------------------

    def setup_penbrush_tab(self, tab):
        control_frame = ttk.Frame(tab)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.canvas_draw = tk.Canvas(tab, bg="white", highlightthickness=1)
        self.canvas_draw.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # --- Елементи керування (RG2, RG3, RG4) ---

        # RG2: Дії
        gbox_actions = ttk.LabelFrame(control_frame, text="Дії (RG2)")
        gbox_actions.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        actions = ["Прямокутник", "Еліпс", "Текст", "Заливка (FloodFill)"]
        for i, text in enumerate(actions):
            ttk.Radiobutton(gbox_actions, text=text, variable=self.action_var, value=str(i)).pack(anchor=tk.W)

        # RG3: Стилі кистей
        gbox_brush = ttk.LabelFrame(control_frame, text="Стилі кистей (RG3)")
        gbox_brush.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        brush_styles = ["Solid", "Cross", "DiagCross", "Vertical"]
        for i, text in enumerate(brush_styles):
            ttk.Radiobutton(gbox_brush, text=text, variable=self.brush_style_var, value=str(i)).pack(anchor=tk.W)

        # RG4: Режими пера
        gbox_pen = ttk.LabelFrame(control_frame, text="Режими пера (RG4)")
        gbox_pen.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        pen_modes = ["pmCopy", "pmXor", "pmNotXor"]
        for i, text in enumerate(pen_modes):
            ttk.Radiobutton(gbox_pen, text=text, variable=self.pen_mode_var, value=str(i)).pack(anchor=tk.W)

        # Прив'язка обробника миші
        self.canvas_draw.bind("<Button-1>", self.image_mouse_down)

        button_clear = ttk.Button(tab, text="Очищення", command=self.button_clear_click)
        button_clear.pack(pady=10)

    def button_clear_click(self):
        """Обробник кнопки «Очищення» (Button8Click)."""
        self.canvas_draw.delete("all")

    def image_mouse_down(self, event):
        """Обробник натискання клавіші миші (Image7MouseDown)."""
        X, Y = event.x, event.y
        sx = random.randint(30, 100)
        sy = random.randint(30, 100)

        # Випадковий колір
        color_hex = '#%06x' % random.randint(0, 0xFFFFFF)

        style_index = int(self.brush_style_var.get())
        brush_stipple = self.BRUSH_STYLES[style_index]

        # Режими пера не мають прямого аналога XOR/NotXOR в Tkinter Canvas,
        # тому ми використовуємо просту логіку малювання.

        action_index = int(self.action_var.get())

        if action_index == 0:  # Прямокутник
            self.canvas_draw.create_rectangle(X, Y, X + sx, Y + sy,
                                              fill=color_hex,
                                              stipple=brush_stipple if brush_stipple else None,
                                              outline="black")
        elif action_index == 1:  # Еліпс
            self.canvas_draw.create_oval(X, Y, X + sx, Y + sy,
                                         fill=color_hex,
                                         stipple=brush_stipple if brush_stipple else None,
                                         outline="black")
        elif action_index == 2:  # Текст
            self.canvas_draw.create_text(X, Y, text="Графіка в Tkinter",
                                         fill=color_hex,
                                         anchor="nw")
        elif action_index == 3:  # Заливка (FloodFill) - Імітація
            fill_color_hex = '#%02x0000' % random.randint(100, 255)
            self.canvas_draw.create_rectangle(X - 50, Y - 50, X + 50, Y + 50,
                                              fill=fill_color_hex,
                                              outline="")


# --- ЗАПУСК ПРОГРАМИ ---
if __name__ == "__main__":
    main_root = tk.Tk()
    app = GraphicsApp(main_root)
    main_root.mainloop()