from manim import *

config.pixel_height = 1280
config.pixel_width = 720

class Thales(Scene):
    def construct(self):
        # Define points
        A = UP * 3
        B = DOWN * 3 + RIGHT * 3
        C = DOWN * 3 + LEFT * 3
        D = LEFT*1.5 + UP*7
        E = RIGHT*1.5 + UP*7
        F = RIGHT*0.65 + UP*8.6
        G = LEFT*0.65 + UP*8.6
        
        # Defining Shapes
        ABC = Polygon(A, B, C, color=BLUE)
        DE = Line(D, E, color=GREEN)
        DF = Line(D, F, color=PINK)
        EG = Line(E, G, color=PINK)
        DB = DashedLine(D, B+UP*7, color=YELLOW, dashed_ratio=0.2)
        EC = DashedLine(E, C+UP*7, color=YELLOW, dashed_ratio=0.2)
        
        # Define Right Angles
        ang1 = RightAngle(EG, Line(G, D), length=0.3, quadrant=(-1, 1))
        ang2 = RightAngle(DF, Line(F, E), length=0.3, quadrant=(-1, 1))
        
        # Add Labels
        labels = [
            ("A", A, UP),
            ("B", B, RIGHT),
            ("C", C, LEFT),
            ("D", D, LEFT),
            ("E", E, RIGHT),
            ("F", F, RIGHT),
            ("G", G, LEFT),
        ]
        
        label_objs = [MathTex(label_text).next_to(label_point, label_pos) for label_text, label_point, label_pos in labels]
        
        # Lines logic
        lines: list[MathTex] = []
        prev_line: MathTex | None = None
        def add_line(line: str, color=WHITE):
            """_summary_
                Adds an expression at the bottom
            
            Args:
                line (str): The text to add
            """
            nonlocal prev_line
            if prev_line:
                lines.append(MathTex(line, color=color).next_to(prev_line, DOWN))
            else:
                lines.append(MathTex(line, color=color).next_to(triangle_main_group, DOWN))
            prev_line = lines[-1]
            self.play(Write(prev_line))
        def add_labels(begin, end):
            for label in label_objs[begin:end+1]:
                self.play(Write(label, run_time=0.5))
        
        # Main triangle
        triangle_main_group = VGroup(ABC, label_objs[:3])
        # Define title
        heading = Text("Proof Of Thales Theorem", font_size=60, color=YELLOW).next_to(triangle_main_group, UP*5)
        # Play the animations
        self.play(Create(ABC), Create(heading))
        add_labels(0, 2)
        self.play(triangle_main_group.animate.shift(UP*7), heading.animate.shift(UP*6))
        self.play(Create(DE))
        add_labels(3, 4)
        # Given Section
        add_line(r"\text{Given:} DE \parallel BC")
        # Prove Section
        add_line(r"\text{Prove:} \frac{AD}{DC} = \frac{AE}{BE}")
        self.play(Create(DF), Create(EG))
        self.play(Create(ang1), Create(ang2))
        add_labels(5, 6)
        # Construction section
        add_line(r"\text{Construction: Draw } EG \perp AD \text{ and } DF \perp AE")
        self.play(Create(DB), Create(EC))
        add_line(r"\text{Join } DB \text{ and } EC")
        # Marking Triangle ADE
        self.play(Create(Polygon(A+UP*7, D, E, color=RED)))
        add_line(line=r"\text{Area(}\triangle\text{ADE)} = \frac{1}{2} \times EG \times AD", color=RED)
        # Marking Triangle EDC
        self.play(Create(Polygon(C+UP*7, D, E, color=PURE_GREEN)))
        add_line(line=r"\text{Area(}\triangle\text{EDC)} = \frac{1}{2} \times EG \times DC", color=PURE_GREEN)
        add_line(r"\frac{\text{Area(}\triangle\text{ADE)}}{\text{Area(}\triangle\text{EDC)}} = \frac{\frac{1}{2}\times EG \times AD}{\frac{1}{2}\times EG \times DC} = \frac{AD}{DC}")
        add_line(line=r"\text{Area(}\triangle\text{ADE)} = \frac{1}{2} \times DF \times AE", color=RED)
        # Marking Triangle EDB
        self.play(Create(Polygon(B+UP*7, D, E, color=YELLOW)))
        add_line(line=r"\text{Area(}\triangle\text{EDB)} = \frac{1}{2} \times DF \times EB", color=YELLOW)
        add_line(r"\frac{\text{Area(}\triangle\text{ADE)}}{\text{Area(}\triangle\text{EDB)}} = \frac{\frac{1}{2}\times DF \times AE}{\frac{1}{2}\times DF \times BE} = \frac{AE}{BE}")
        # Since Area of triangles between parallel lines is equal, hence we can write Ar(EDC) = Ar(EDB)
        add_line(r"\text{Area(}\triangle\text{EDC)} = \text{Area(}\triangle\text{EDB)} [\triangle\text{'s b/w} \parallel \text{lines have equal area}]")
        # Therefore Ar(ADE)/Ar(EDC) = Ar(ADE)/Ar(EDB)
        add_line(r"\therefore \frac{\text{Area(}\triangle\text{ADE)}}{\text{Area(}\triangle\text{EDC)}} = \frac{\text{Area(}\triangle\text{ADE)}}{\text{Area(}\triangle\text{EDB)}")
        # Therefore Ar(ADE)/Ar(EDC) = Ar(ADE)/Ar(EDB) => AD/DE = AE/BE
        add_line(r"\frac{AD}{DC} = \frac{AE}{BE}")
        final_rect = SurroundingRectangle(lines[-1], color=YELLOW, buff=0.2)
        self.play(Create(final_rect))
        self.wait()
