from manim import *

class LineAdder:
    def __init__(self, scene: Scene, next_to_obj: Mobject, gap = DOWN*2, font_size = 36):
        """
        Handles adding and editing MathTex lines below a given object.
        """
        self.scene = scene
        self.font_size = font_size
        self.next_to_obj = next_to_obj
        self.gap = gap
        self.lines: list[MathTex] = []
        self.prev_line: MathTex | None = None

    def add_line(self, line: str, font_size = None, color=WHITE, **kwargs):
        """
        Adds a MathTex line below the previous one (or reference object).

        kwargs: Any additional MathTex parameters (e.g., tex_template, substrings_to_isolate)
        """
        target = self.prev_line if self.prev_line else self.next_to_obj
        
        if font_size:
            new_line = MathTex(line, color=color, font_size=font_size, **kwargs).next_to(target, self.gap)
        else:
            new_line = MathTex(line, color=color, font_size=self.font_size, **kwargs).next_to(target, self.gap)
        self.lines.append(new_line)
        self.prev_line = new_line
        self.scene.play(Write(new_line))

    def edit_line(self, line_num: int, new_line: str, color=WHITE, font_size=None, time_transform=1.5, **kwargs):
        """
        Replaces the content of a line with a new expression.
        The old line fades out, and the new one writes on top.
        
        font_size: Optional, overrides the old line's font size.
        kwargs: Any additional MathTex parameters.
        """
        if line_num < 0 or line_num >= len(self.lines):
            raise ValueError("Invalid line number")

        old_line = self.lines[line_num]
        fs = font_size if font_size else old_line.font_size
        updated_line = MathTex(new_line, color=color, font_size=fs, **kwargs).move_to(old_line.get_center())
        self.lines[line_num] = updated_line

        # Update prev_line if editing the last line
        if line_num == len(self.lines) - 1:
            self.prev_line = updated_line

        # Play animations: fade out old, write new
        self.scene.play(FadeOut(old_line), run_time=time_transform)
        self.scene.play(Write(updated_line), run_time=time_transform)

