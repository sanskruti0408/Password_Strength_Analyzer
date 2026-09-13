import tkinter as tk

from core.analyzer import analyze_password


class PasswordAnalyzerGUI:

    def __init__(self, root):
        self.root = root

        self.root.title("Password Strength Analyzer")
        self.root.geometry("1100x720")
        self.root.minsize(950, 650)
        self.root.configure(bg="#0B0F14")

        self.colors = {
            "background": "#0B0F14",
            "panel": "#121923",
            "panel_dark": "#0D131B",
            "border": "#263241",
            "cyan": "#00D9FF",
            "green": "#00E5A0",
            "yellow": "#FFC857",
            "orange": "#FF8C42",
            "red": "#FF4D67",
            "white": "#F4F7FA",
            "muted": "#8F9BAA",
            "secondary": "#647184"
        }

        self.password_visible = False

        self.create_layout()


    def run_analysis(self):

        password = self.password_entry.get()

        if not password:
            self.reset_display()
            self.status_label.config(
                text="⚠ Enter a password to begin analysis.",
                fg=self.colors["yellow"]
            )
            return

        result = analyze_password(password)

        score = result["score"]

        strength = self.get_strength(score)
        score_color = self.get_score_color(score)

        self.score_label.config(
            text=str(score),
            fg=score_color
        )

        self.strength_label.config(
            text=strength,
            fg=score_color
        )

        self.status_label.config(
            text="● ANALYSIS COMPLETE",
            fg=score_color
        )

        self.draw_score_ring(score, score_color)

        entropy = result.get("entropy", 0)

        self.entropy_label.config(
            text=f"Entropy: {entropy:.2f} bits"
        )

        complexity = result["complexity"]

        checks = [
            (
                "📏",
                "Password Length",
                result["length"],
                result["length"] in ("Strong", "Very Strong")
            ),
            (
                "🔠",
                "Uppercase Letters",
                "PASS" if complexity["uppercase"] else "MISSING",
                complexity["uppercase"]
            ),
            (
                "🔡",
                "Lowercase Letters",
                "PASS" if complexity["lowercase"] else "MISSING",
                complexity["lowercase"]
            ),
            (
                "🔢",
                "Numbers",
                "PASS" if complexity["digit"] else "MISSING",
                complexity["digit"]
            ),
            (
                "🔣",
                "Special Characters",
                "PASS" if complexity["symbol"] else "MISSING",
                complexity["symbol"]
            ),
            (
                "🚫",
                "Common Password",
                "DETECTED" if result["common_password"] else "SAFE",
                not result["common_password"]
            ),
            (
                "🧠",
                "Predictability",
                "DETECTED" if result["predictability"] else "LOW",
                not result["predictability"]
            ),
            (
                "⌨",
                "Keyboard Pattern",
                "DETECTED" if result["keyboard_pattern"] else "SAFE",
                not result["keyboard_pattern"]
            ),
            (
                "🔗",
                "Sequence Pattern",
                "DETECTED" if result["sequence"] else "SAFE",
                not result["sequence"]
            ),
            (
                "🔁",
                "Character Repetition",
                "DETECTED" if result["repetition"] else "SAFE",
                not result["repetition"]
            )
        ]

        for index, check in enumerate(checks):
            self.update_check_row(
                index,
                check[0],
                check[1],
                check[2],
                check[3]
            )

        suggestions = result["suggestions"]

        suggestion_text = "\n".join(
            f"• {suggestion}"
            for suggestion in suggestions
        )

        self.suggestions_text.config(
            text=suggestion_text
        )


    def get_strength(self, score):

        if score < 20:
            return "VERY WEAK"

        elif score < 40:
            return "WEAK"

        elif score < 60:
            return "FAIR"

        elif score < 80:
            return "STRONG"

        else:
            return "VERY STRONG"

    def get_score_color(self, score):

        if score < 20:
            return self.colors["red"]

        elif score < 40:
            return self.colors["orange"]

        elif score < 60:
            return self.colors["yellow"]

        elif score < 80:
            return self.colors["green"]

        else:
            return self.colors["cyan"]


    def toggle_password(self):

        self.password_visible = not self.password_visible

        if self.password_visible:
            self.password_entry.config(show="")
            self.visibility_button.config(text="🙈")
        else:
            self.password_entry.config(show="•")
            self.visibility_button.config(text="👁")


    def draw_score_ring(self, score, color):

        self.score_canvas.delete("all")

        center = 105
        radius = 82

        self.score_canvas.create_oval(
            center - radius,
            center - radius,
            center + radius,
            center + radius,
            outline=self.colors["border"],
            width=12
        )

        extent = score * 3.6

        if score > 0:
            self.score_canvas.create_arc(
                center - radius,
                center - radius,
                center + radius,
                center + radius,
                start=90,
                extent=-extent,
                style="arc",
                outline=color,
                width=12
            )

        self.score_canvas.create_text(
            center,
            center - 5,
            text=str(score),
            fill=color,
            font=("Segoe UI", 30, "bold")
        )

        self.score_canvas.create_text(
            center,
            center + 28,
            text="/ 100",
            fill=self.colors["muted"],
            font=("Segoe UI", 9)
        )


    def update_check_row(
        self,
        index,
        icon,
        name,
        value,
        passed
    ):

        row = self.check_rows[index]

        row["icon"].config(
            text=icon
        )

        row["name"].config(
            text=name
        )

        row["value"].config(
            text=value,
            fg=self.colors["green"]
            if passed
            else self.colors["red"]
        )


    def reset_display(self):

        self.score_label.config(
            text="--",
            fg=self.colors["muted"]
        )

        self.strength_label.config(
            text="WAITING FOR ANALYSIS",
            fg=self.colors["muted"]
        )

        self.entropy_label.config(
            text="Entropy: --"
        )

        self.status_label.config(
            text="● READY FOR ANALYSIS",
            fg=self.colors["cyan"]
        )

        self.score_canvas.delete("all")

        self.draw_empty_ring()

        for row in self.check_rows:

            row["icon"].config(
                text="•"
            )

            row["name"].config(
                text="Waiting..."
            )

            row["value"].config(
                text="--",
                fg=self.colors["muted"]
            )

        self.suggestions_text.config(
            text="Enter a password and click ANALYZE."
        )

    def draw_empty_ring(self):

        center = 105
        radius = 82

        self.score_canvas.create_oval(
            center - radius,
            center - radius,
            center + radius,
            center + radius,
            outline=self.colors["border"],
            width=12
        )

        self.score_canvas.create_text(
            center,
            center,
            text="?",
            fill=self.colors["secondary"],
            font=("Segoe UI", 28, "bold")
        )


    def create_layout(self):

        header = tk.Frame(
            self.root,
            bg=self.colors["panel"],
            height=82
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        title_frame = tk.Frame(
            header,
            bg=self.colors["panel"]
        )

        title_frame.pack(
            side="left",
            padx=28
        )

        tk.Label(
            title_frame,
            text="🔐  PASSWORD STRENGTH ANALYZER",
            bg=self.colors["panel"],
            fg=self.colors["white"],
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            pady=(15, 0)
        )

        tk.Label(
            title_frame,
            text="Cybersecurity Password Assessment Tool",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        self.status_label = tk.Label(
            header,
            text="● READY FOR ANALYSIS",
            bg=self.colors["panel"],
            fg=self.colors["cyan"],
            font=("Segoe UI", 9, "bold")
        )

        self.status_label.pack(
            side="right",
            padx=30
        )


        main = tk.Frame(
            self.root,
            bg=self.colors["background"]
        )

        main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        left_panel = tk.Frame(
            main,
            bg=self.colors["panel"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )

        left_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )


        tk.Label(
            left_panel,
            text="🔐  PASSWORD INPUT",
            bg=self.colors["panel"],
            fg=self.colors["cyan"],
            font=("Segoe UI", 11, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(28, 5)
        )

        tk.Label(
            left_panel,
            text="Enter a password to evaluate its security.",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=28,
            pady=(0, 20)
        )


        input_frame = tk.Frame(
            left_panel,
            bg=self.colors["panel_dark"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )

        input_frame.pack(
            fill="x",
            padx=28
        )

        self.password_entry = tk.Entry(
            input_frame,
            bg=self.colors["panel_dark"],
            fg=self.colors["white"],
            insertbackground=self.colors["cyan"],
            selectbackground=self.colors["cyan"],
            selectforeground=self.colors["background"],
            font=("Segoe UI", 13),
            relief="flat",
            show="•",
            bd=0
        )

        self.password_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 5),
            pady=14
        )

        self.visibility_button = tk.Button(
            input_frame,
            text="👁",
            command=self.toggle_password,
            bg=self.colors["panel_dark"],
            fg=self.colors["muted"],
            activebackground=self.colors["panel_dark"],
            activeforeground=self.colors["white"],
            relief="flat",
            bd=0,
            font=("Segoe UI Emoji", 11),
            cursor="hand2"
        )

        self.visibility_button.pack(
            side="right",
            padx=10
        )

        self.analyze_button = tk.Button(
            left_panel,
            text="⚡  ANALYZE PASSWORD",
            command=self.run_analysis,
            bg=self.colors["cyan"],
            fg=self.colors["background"],
            activebackground="#33E1FF",
            activeforeground=self.colors["background"],
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        self.analyze_button.pack(
            fill="x",
            padx=28,
            pady=20,
            ipady=10
        )

        tk.Label(
            left_panel,
            text="🛡️  WHAT WE CHECK",
            bg=self.colors["panel"],
            fg=self.colors["white"],
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(15, 12)
        )

        requirements = [
            "📏  Password length",
            "🔠  Character complexity",
            "🚫  Common password usage",
            "🧠  Predictable patterns",
            "⌨  Keyboard patterns",
            "🔗  Sequential characters",
            "🔁  Repeated characters"
        ]

        for requirement in requirements:

            tk.Label(
                left_panel,
                text=requirement,
                bg=self.colors["panel"],
                fg=self.colors["muted"],
                font=("Segoe UI", 9)
            ).pack(
                anchor="w",
                padx=35,
                pady=3
            )


        tk.Label(
            left_panel,
            text="🔒 Passwords are evaluated locally by the analyzer.",
            bg=self.colors["panel"],
            fg=self.colors["secondary"],
            font=("Segoe UI", 8)
        ).pack(
            anchor="w",
            padx=28,
            side="bottom",
            pady=22
        )


        right_panel = tk.Frame(
            main,
            bg=self.colors["panel"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )

        right_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        tk.Label(
            right_panel,
            text="🛡️  SECURITY ANALYSIS",
            bg=self.colors["panel"],
            fg=self.colors["cyan"],
            font=("Segoe UI", 11, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(28, 8)
        )


        score_frame = tk.Frame(
            right_panel,
            bg=self.colors["panel"]
        )

        score_frame.pack(
            fill="x",
            pady=(5, 5)
        )

        self.score_canvas = tk.Canvas(
            score_frame,
            width=210,
            height=210,
            bg=self.colors["panel"],
            highlightthickness=0
        )

        self.score_canvas.pack(
            side="left",
            padx=(35, 10)
        )

        score_info = tk.Frame(
            score_frame,
            bg=self.colors["panel"]
        )

        score_info.pack(
            side="left",
            padx=10
        )

        tk.Label(
            score_info,
            text="SECURITY SCORE",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9, "bold")
        ).pack(
            anchor="w"
        )

        self.score_label = tk.Label(
            score_info,
            text="--",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 30, "bold")
        )

        self.score_label.pack(
            anchor="w"
        )

        self.strength_label = tk.Label(
            score_info,
            text="WAITING FOR ANALYSIS",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 11, "bold")
        )

        self.strength_label.pack(
            anchor="w",
            pady=(0, 10)
        )

        self.entropy_label = tk.Label(
            score_info,
            text="Entropy: --",
            bg=self.colors["panel"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9)
        )

        self.entropy_label.pack(
            anchor="w"
        )


        tk.Label(
            right_panel,
            text="🔎  SECURITY CHECKS",
            bg=self.colors["panel"],
            fg=self.colors["white"],
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(5, 10)
        )

        checks_container = tk.Frame(
            right_panel,
            bg=self.colors["panel_dark"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )

        checks_container.pack(
            fill="x",
            padx=28
        )

        self.check_rows = []

        for index in range(10):

            row = tk.Frame(
                checks_container,
                bg=self.colors["panel_dark"]
            )

            row.pack(
                fill="x",
                padx=12,
                pady=2
            )

            icon_label = tk.Label(
                row,
                text="•",
                bg=self.colors["panel_dark"],
                fg=self.colors["muted"],
                font=("Segoe UI Emoji", 10),
                width=3
            )

            icon_label.pack(
                side="left"
            )

            name_label = tk.Label(
                row,
                text="Waiting...",
                bg=self.colors["panel_dark"],
                fg=self.colors["muted"],
                font=("Segoe UI", 9)
            )

            name_label.pack(
                side="left"
            )

            value_label = tk.Label(
                row,
                text="--",
                bg=self.colors["panel_dark"],
                fg=self.colors["muted"],
                font=("Segoe UI", 9, "bold")
            )

            value_label.pack(
                side="right"
            )

            self.check_rows.append({
                "icon": icon_label,
                "name": name_label,
                "value": value_label
            })


        tk.Label(
            right_panel,
            text="💡  SECURITY RECOMMENDATIONS",
            bg=self.colors["panel"],
            fg=self.colors["white"],
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(16, 8)
        )

        self.suggestions_text = tk.Label(
            right_panel,
            text="Enter a password and click ANALYZE.",
            bg=self.colors["panel_dark"],
            fg=self.colors["muted"],
            font=("Segoe UI", 9),
            justify="left",
            anchor="w",
            wraplength=450,
            padx=15,
            pady=10
        )

        self.suggestions_text.pack(
            fill="x",
            padx=28
        )


        self.draw_empty_ring()


