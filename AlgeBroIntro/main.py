from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        squ1 = Square().scale(.75)
        squ2 = Square().scale(.75)
        self.play(Create(squ1), Create(squ2))
        self.play(Rotate(squ2, PI/4))
        oct = RegularPolygon(n=8, color=WHITE).scale(1.07)
        self.play(Create(oct))
        txt = Text("AlgeBro").scale(.5)
        self.play(Write(txt))
        self.wait()
        self.play(Uncreate(squ1), Uncreate(squ2), Uncreate(oct), Unwrite(txt))
        self.wait()
