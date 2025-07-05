from manim import *

class QuadraticFormulaGeometric(Scene):
    def intro(self):
        squ1 = Square().scale(.75)
        squ2 = Square().scale(.75)
        self.play(Create(squ1), Create(squ2))
        self.play(Rotate(squ2, PI/4))
        oct = RegularPolygon(n=8, color=WHITE).scale(1.07)
        self.play(Create(oct))
        txt = Text("AlgeBro").scale(.5)
        self.play(Write(txt))
        self.wait(7)
        self.play(Uncreate(squ1), Uncreate(squ2), Uncreate(oct), Unwrite(txt))

    def RtoC(self):
        texR = Tex(r'$\mathbb{R}$', font_size=244)
        texC = Tex(r'$\mathbb{R}$ or $\mathbb{C}$', font_size=244)

        self.play(Write(texR))
        self.wait()
        self.play(Transform(texR, texC))
        self.wait(8)
        self.play(Unwrite(texR))

    def QP(self):
        return '$ax^2+bx+c$'

    def QF(self):
        return '$x = \\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$'

    def Poly(self):
        pos_list = [
            [2,0,0],
            [0,1,0],
            [0,0,0],
            [.5, -.5, 0],
        ]
        pos_list = [[x * 3 for x in row] for row in pos_list]
        poly = Polygon(*pos_list, color=PURPLE)
        return poly

    def construct(self):
        self.intro()

        self.RtoC()
        fs = 144
        QQPT = Text("What is the Quadratic Polynomial?")
        self.play(Write(QQPT))
        self.wait(2)
        self.play(Unwrite(QQPT, run_time=.75))

        QPT = Text("Quadratic Polynomial", font_size=fs-100)
        QP = Tex(self.QP(), font_size=fs)
        QP0 = Tex(self.QP() + r' $=0$', font_size=fs)
        QF = Tex(self.QF(), font_size=fs+50)
        QPT.next_to(QP, UP)
        self.play(Write(QPT, run_time=.7), Write(QP))
        self.wait(4)
        self.play(Transform(QP, QP0))
        self.wait(3.5)
        self.play(Unwrite(QPT), QP.animate.shift(UP * 3))
        QF.next_to(QP, DOWN*5)
        self.play(Write(QF))
        self.wait(2)
        self.play(Unwrite(QPT), Unwrite(QF))
        self.wait()

        self.play(QP[0][7].animate.set_color(RED))
        poly = self.Poly().set_fill(PURPLE, opacity=0.5).shift(LEFT+DOWN)
        self.play(Create(poly))
        c = Text('c', font_size=144, color=RED)
        self.play(Write(c))
        self.wait(5)
        self.play(Uncreate(poly), Unwrite(c), QP[0][7].animate.set_color(WHITE))
        self.wait()

        self.play(QP[0][4:6].animate.set_color(RED))
        self.wait(5)
        rec = Rectangle().set_fill(PURPLE, opacity=0.5).shift(LEFT+DOWN)
        self.play(Create(rec))
        b = Tex(r'$b$', font_size=fs).next_to(rec, LEFT)
        x = Tex(r'$x$', font_size=fs).next_to(rec, UP)
        self.play(Write(b), Write(x))
        self.wait(3)
        self.play(Unwrite(b), Unwrite(x), Uncreate(rec))
        self.play(QP[0][4:6].animate.set_color(WHITE))
        self.wait()
        
        self.play(QP[0][0:3].animate.set_color(RED))
        self.wait(7)
        QP_Sep = Tex(r'$(\sqrt{a}x)(\sqrt{a}x)$', r'$ + bx + c = 0$', font_size=fs-20).align_to(QP, UP)
        QP_Sep.set_color_by_tex('(\sqrt{a}x)(\sqrt{a}x)', RED)
        self.play(Transform(QP, QP_Sep))
        self.wait(9)
        squ = Square().set_fill(PURPLE, opacity=0.5).shift(DOWN*1.5).scale(2)
        self.play(Create(squ))
        ax1 = Tex(r'$\sqrt{a}x$', font_size=fs).next_to(squ, LEFT)
        ax2 = Tex(r'$\sqrt{a}x$', font_size=fs).next_to(squ, UP)
        self.play(Write(ax1), Write(ax2))
        self.wait(2)
        self.play(Unwrite(ax1), Unwrite(ax2), Uncreate(squ), Uncreate(QP))

        squ = Square().set_fill(PURPLE, opacity=0.5).shift(RIGHT+DOWN).scale(2)
        xk1 = Tex(r'$x+k$', font_size=fs-20).next_to(squ, LEFT)
        xk2 = Tex(r'$x+k$', font_size=fs-20).next_to(squ, UP)
        self.play(Write(xk1), Write(xk2), Create(squ))
        self.wait(4)
        var_squ1 = Tex(r'$(x+k)^2$', font_size=fs-50).to_edge(UL)
        self.play(Write(var_squ1))
        self.wait()
        x_squ = Square().set_fill(PURPLE).scale(1.5).align_to(squ, UL)
        xkrec1 = Rectangle(width=1, height=3).set_fill(PURPLE).align_to(squ, UR)
        xkrec2 = Rectangle(width=3, height=1).set_fill(PURPLE).align_to(squ, DL)
        k_squ = Square().set_fill(PURPLE).scale(0.5).align_to(squ, DR)
        x1 = Tex(r'$x$', font_size=fs-50).next_to(x_squ, UP)
        x2 = Tex(r'$x$', font_size=fs-50).next_to(x_squ, LEFT)
        x3 = Tex(r'$x$', font_size=fs-50).next_to(xkrec1, RIGHT)
        x4 = Tex(r'$x$', font_size=fs-50).next_to(xkrec2, DOWN)
        k1 = Tex(r'$k$', font_size=fs-50).next_to(k_squ, RIGHT)
        k2 = Tex(r'$k$', font_size=fs-50).next_to(k_squ, DOWN)
        k3 = Tex(r'$k$', font_size=fs-50).next_to(xkrec1, UP)
        k4 = Tex(r'$k$', font_size=fs-50).next_to(xkrec2, LEFT)
        self.play(Create(x_squ), Create(xkrec1), Create(xkrec2), Create(k_squ))
        self.wait()
        self.play(Unwrite(xk1), Unwrite(xk2))
        self.play(Write(x1), Write(x2), Write(x3), Write(x4), Write(k1), Write(k2), Write(k3), Write(k4))
        var_squ3 = Tex(r'$ = xx + (kx + kx) + kk$', font_size=fs-50).next_to(var_squ1)
        self.wait(7)
        self.play(Write(var_squ3))
        self.wait()
        var_squ4 = Tex(r'$= x^2 + 2kx + k^2$', font_size=fs-50).next_to(var_squ1)
        self.play(Transform(var_squ3, var_squ4))
        self.wait(4)
        self.play(Unwrite(x1), Unwrite(x2), Unwrite(x3), Unwrite(x4), Unwrite(k1), Unwrite(k2), Unwrite(k3), Unwrite(k4))
        self.play(Unwrite(var_squ1), Unwrite(var_squ3))
        self.play(Uncreate(squ), Uncreate(x_squ), Uncreate(xkrec1), Uncreate(xkrec2), Uncreate(k_squ))
        self.wait()

        QP = Tex(self.QP(), font_size=fs-50).to_edge(UP)
        self.play(Write(QP))
        self.wait()
        divByA = Tex(r'$\xrightarrow{\div a}$', font_size=fs-50).next_to(QP, RIGHT)
        self.play(Write(divByA))
        self.wait()
        QPDivA = Tex(r'$x^2 + \frac{b}{a}x + \frac{c}{a} = 0$', font_size=fs-50).next_to(QP, DOWN)
        self.play(Write(QPDivA))
        self.wait(4)
        subByC = Tex(r'$\xrightarrow{- \frac{c}{a}}$', font_size=fs-50).next_to(QPDivA, RIGHT)
        self.play(Write(subByC))
        QPSubByC = Tex(r'$x^2 + \frac{b}{a}x = - \frac{c}{a}$', font_size=fs-50).next_to(QPDivA, DOWN)
        self.play(Write(QPSubByC))
        self.wait(5)
        self.play(QPSubByC[0][3:6].animate.set_color(RED))
        self.wait(17)
        QPAdd2 = Tex(r'$x^2 + \frac{2b}{2a}x = - \frac{c}{a}$', font_size=fs-50).next_to(QPDivA, DOWN)
        self.play(Transform(QPSubByC, QPAdd2))
        self.wait()
        QPPar = Tex(r'$x^2 + 2\frac{b}{2a}x = - \frac{c}{a}$', font_size=fs-50).next_to(QPDivA, DOWN)
        self.play(Transform(QPSubByC, QPPar))
        self.wait()

        self.play(Unwrite(QP), Unwrite(divByA), Unwrite(QPDivA), Unwrite(subByC))
        self.play(QPSubByC.animate.to_edge(UP))

        squ = Square().set_fill(PURPLE, opacity=0.5).scale(1.5).to_edge(LEFT).shift(RIGHT*1.25)
        x_squ = Square().set_fill(PURPLE).scale(1.5).align_to(squ, UL)
        xkrec1 = Rectangle(width=1, height=3).set_fill(PURPLE).align_to(squ, UR)
        xkrec2 = Rectangle(width=3, height=1).set_fill(PURPLE).align_to(squ, DL)
        k_squ = Square().set_fill(PURPLE).scale(0.5).align_to(squ, DR)
        x1 = Tex(r'$x$', font_size=fs-50).next_to(x_squ, UP)
        x2 = Tex(r'$x$', font_size=fs-50).next_to(x_squ, LEFT)
        x3 = Tex(r'$x$', font_size=fs-50).next_to(xkrec1, RIGHT)
        x4 = Tex(r'$x$', font_size=fs-50).next_to(xkrec2, DOWN)
        k1 = Tex(r'$\frac{b}{2a}$', font_size=fs-80).next_to(k_squ, RIGHT)
        k2 = Tex(r'$\frac{b}{2a}$', font_size=fs-80).next_to(k_squ, DOWN)
        k3 = Tex(r'$\frac{b}{2a}$', font_size=fs-80).next_to(xkrec1, UP)
        k4 = Tex(r'$\frac{b}{2a}$', font_size=fs-80).next_to(xkrec2, LEFT)
        self.play(Create(squ), Create(x_squ), Create(xkrec1), Create(xkrec2))
        self.wait()
        self.play(Write(x1), Write(x2), Write(x3), Write(x4), Write(k3), Write(k4))
        self.wait(2)
        compSqu = Text("Completing the square", font_size=fs-90).to_edge(RIGHT)
        self.play(Create(k_squ), Write(k1), Write(k2))
        self.play(Write(compSqu))
        self.wait()
        self.play(Indicate(k_squ), Wiggle(k_squ))
        self.play(Unwrite(x1, run_time=.5), Unwrite(x2, run_time=.5), Unwrite(x3, run_time=.5), Unwrite(x4, run_time=.5), Unwrite(k1, run_time=.5), Unwrite(k2, run_time=.5), Unwrite(k3, run_time=.5), Unwrite(k4, run_time=.5),Unwrite(var_squ1, run_time=.5), Unwrite(var_squ3, run_time=.5), Uncreate(squ, run_time=.5), Uncreate(x_squ, run_time=.5), Uncreate(xkrec1, run_time=.5), Uncreate(xkrec2, run_time=.5), Uncreate(k_squ, run_time=.5), Unwrite(compSqu, run_time=.5))

        addK = Tex(r'$\xrightarrow{+ \left( \frac{b}{2a} \right)^2}$', font_size=fs-50).next_to(QPSubByC, RIGHT)
        self.play(Write(addK, run_time=.5))
        self.wait()

        QPNotCompl = Tex(r'$x^2 + 2\frac{b}{2a}x + \left( \frac{b}{2a} \right)^2 = - \frac{c}{a} + \left( \frac{b}{2a} \right)^2$', font_size=fs-50).next_to(QPSubByC, DOWN)
        self.play(Write(QPNotCompl))
        self.wait()

        self.play(Unwrite(QP), Unwrite(divByA), Unwrite(QPDivA), Unwrite(subByC), Unwrite(QPSubByC), Unwrite(addK))
        self.wait()
        self.play(QPNotCompl.animate.to_edge(UP))
        self.wait()
        QPCompl = Tex(r'$x^2 + 2\frac{b}{2a}x + \left( \frac{b}{2a} \right)^2 = \left( x + \frac{b}{2a} \right)^2 = - \frac{c}{a} + \left( \frac{b}{2a} \right)^2$', font_size=fs-80).to_edge(UP)
        self.play(Transform(QPNotCompl, QPCompl))
        self.wait()

        QPCompl1 = Tex(r'$\left( x + \frac{b}{2a} \right)^2 = - \frac{c}{a} + \left( \frac{b}{2a} \right)^2$', font_size=fs-80).to_edge(UP)
        QPCompl2 = Tex(r'$\left( x + \frac{b}{2a} \right)^2 = \frac{b^2 - 4ac}{4a^2}$', font_size=fs-50).next_to(QPCompl, DOWN)
        QPCompl3 = Tex(r'$x + \frac{b}{2a} = \pm \frac{\sqrt{ b^2 - 4ac }}{2a}$', font_size=fs-50).next_to(QPCompl2, DOWN)
        QPCompl4 = Tex(r'$x = \frac{-b \pm \sqrt{ b^2 - 4ac }}{2a}$', font_size=fs-50).next_to(QPCompl3, DOWN)
        self.play(Transform(QPNotCompl, QPCompl1))
        self.wait()
        self.play(Write(QPCompl2))
        self.wait()
        self.play(Write(QPCompl3))
        self.wait()
        self.play(Write(QPCompl4))
        self.wait()




        




        self.wait()
