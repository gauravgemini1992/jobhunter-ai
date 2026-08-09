import customtkinter as ctk

# -----------------------------
# Application Configuration
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class JobHunterAI(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window
        self.title("JobHunter AI • AI Career Copilot")
        self.geometry("1440x900")
        self.minsize(1200, 750)

        self.configure(fg_color="#0F172A")

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.create_sidebar()
        self.create_topbar()
        self.create_dashboard()

    # -----------------------------
    # Sidebar
    # -----------------------------
    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=240,
            corner_radius=0,
            fg_color="#111827"
        )

        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")

        title = ctk.CTkLabel(
            self.sidebar,
            text="JobHunter AI",
            font=("Inter", 26, "bold")
        )

        title.pack(pady=(30, 5))

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="AI Career Copilot",
            text_color="#94A3B8"
        )

        subtitle.pack(pady=(0, 30))

        menu = [
            "🏠 Dashboard",
            "📄 Resume Intelligence",
            "🎯 ATS Analysis",
            "💼 Smart Job Match",
            "🏢 Company Intelligence",
            "🤖 AI Career Coach",
            "📊 Reports",
            "⚙ Settings"
        ]

        for item in menu:
            button = ctk.CTkButton(
                self.sidebar,
                text=item,
                height=45,
                corner_radius=10,
                anchor="w",
                fg_color="transparent",
                hover_color="#1E293B"
            )

            button.pack(fill="x", padx=15, pady=4)

    # -----------------------------
    # Top Bar
    # -----------------------------
    def create_topbar(self):

        topbar = ctk.CTkFrame(
            self,
            height=70,
            corner_radius=0,
            fg_color="#111827"
        )

        topbar.grid(
            row=0,
            column=1,
            sticky="ew"
        )

        topbar.grid_columnconfigure(0, weight=1)

        search = ctk.CTkEntry(
            topbar,
            width=350,
            placeholder_text="Search jobs, companies..."
        )

        search.grid(
            row=0,
            column=0,
            padx=30,
            pady=18,
            sticky="w"
        )

        version = ctk.CTkLabel(
            topbar,
            text="Version 2.0",
            text_color="#94A3B8"
        )

        version.grid(
            row=0,
            column=1,
            padx=30
        )

    # -----------------------------
    # Dashboard
    # -----------------------------
    def create_dashboard(self):

        body = ctk.CTkFrame(
            self,
            fg_color="#0F172A"
        )

        body.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        heading = ctk.CTkLabel(
            body,
            text="Career Command Center",
            font=("Inter", 32, "bold")
        )

        heading.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            body,
            text="Welcome back! Here's your career overview.",
            text_color="#94A3B8"
        )

        subtitle.pack(anchor="w", pady=(0, 25))

        cards = ctk.CTkFrame(
            body,
            fg_color="transparent"
        )

        cards.pack(fill="x")

        stats = [
            ("ATS Score", "92%"),
            ("Job Matches", "147"),
            ("Companies", "58"),
            ("Reports", "18")
        ]

        for title, value in stats:

            card = ctk.CTkFrame(
                cards,
                width=220,
                height=140,
                fg_color="#1E293B",
                corner_radius=15
            )

            card.pack(side="left", padx=10)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Inter", 15)
            ).pack(pady=(20, 5))

            ctk.CTkLabel(
                card,
                text=value,
                font=("Inter", 30, "bold")
            ).pack()

            ctk.CTkLabel(
                card,
                text="Updated Today",
                text_color="#94A3B8"
            ).pack(pady=(10, 0))


if __name__ == "__main__":
    app = JobHunterAI()
    app.mainloop()