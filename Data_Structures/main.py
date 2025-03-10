from manim import *
from manim.opengl import *


class LinearSearch(Scene):

    def construct(self):
        
        announcement = Text("Linear Search")
        square1 = Square(side_length=1,color=WHITE)
        square2 = Square(side_length=1,color=WHITE)
        square3 = Square(side_length=1,color=WHITE)
        square4 = Square(side_length=1,color=WHITE)
        square5 = Square(side_length=1,color=WHITE)
        square6 = Square(side_length=1,color=WHITE)
        square7 = Square(side_length=1,color=WHITE)
        square8 = Square(side_length=1,color=WHITE)
        square9 = Square(side_length=1,color=WHITE)
        square10 = Square(side_length=1,color=WHITE)

        
        num1 = Integer(4)
        num2 = Integer(2)
        num3 = Integer(3)
        num4 = Integer(5)
        num5 = Integer(7)
        num6 = Integer(6)
        num7 = Integer(8)
        num8 = Integer(5)
        num9 = Integer(6)
        num10 = Integer(4)

        arrow = Arrow(start=DOWN,end=UP)
        

        All_numbers = Group(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
        All_numbers.arrange(
            RIGHT,
            aligned_edge =RIGHT,
            buff=1
        )

        

        All_Squares=Group(square1,square2,square3,square4,square5,square6,square7,square8,square9,square10)
        All_Squares.arrange(
            RIGHT,
            aligned_edge = RIGHT,
            buff = 0.6
        )
        arrow.next_to(square1,DOWN,buff=0.5)
        self.play(AddTextLetterByLetter(announcement,rum_time=5))
        self.play(RemoveTextLetterByLetter(announcement),rum_time = 3)
        self.play(Create(All_Squares,run_time=4))
        self.play(Create(All_numbers,run_time=3))
        self.play(Create(arrow))
        self.wait()
        self.play(arrow.animate.next_to(square2,DOWN,buff=0.5))
        self.play(arrow.animate.next_to(square3,DOWN,buff=0.5))
        self.play(arrow.animate.next_to(square4,DOWN,buff=0.5))
        self.play(arrow.animate.next_to(square5,DOWN,buff=0.5))
        self.play(Circumscribe(square5,Circle))
        self.wait(1)
        self.interactive_embed()


class BinarySearch(Scene):

    def construct(self):
        announcement = Text("Binary Search")
        searchingFor = Text("Searching For: 8")
        square1 = Square(side_length=1,color=WHITE)
        square2 = Square(side_length=1,color=WHITE)
        square3 = Square(side_length=1,color=WHITE)
        square4 = Square(side_length=1,color=WHITE)
        square5 = Square(side_length=1,color=WHITE)
        square6 = Square(side_length=1,color=WHITE)
        square7 = Square(side_length=1,color=WHITE)
        square8 = Square(side_length=1,color=WHITE)
        square9 = Square(side_length=1,color=WHITE)
        square10 = Square(side_length=1,color=WHITE)

        
        num1 = Integer(1)
        num2 = Integer(2)
        num3 = Integer(3)
        num4 = Integer(4)
        num5 = Integer(5)
        num6 = Integer(6)
        num7 = Integer(7)
        num8 = Integer(8)
        num9 = Integer(9)
        num10 = Integer(10)

        arrowLeft = Arrow(start=DOWN,end=UP)
        arrowRight = Arrow(start=UP,end=DOWN)
        arrowMiddle = Arrow(start=DOWN,end=UP,color=GOLD)

        All_numbers = Group(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
        All_numbers.arrange(
            RIGHT,
            aligned_edge =RIGHT,
            buff=1
        )

        

        All_Squares=Group(square1,square2,square3,square4,square5,square6,square7,square8,square9,square10)
        All_Squares.arrange(
            RIGHT,
            aligned_edge = RIGHT,
            buff = 0.6
        )
        arrowLeft.next_to(square1,DOWN,buff=0.5)
        arrowRight.next_to(square10,UP,buff=0.5)
        arrowMiddle.next_to(square5,DOWN,buff=0.5)

        searchingFor.align_on_border(UP)
        self.play(AddTextLetterByLetter(announcement,rum_time=5))
        self.play(RemoveTextLetterByLetter(announcement),rum_time = 3)
        self.play(Create(All_Squares,run_time=4))
        self.play(Create(All_numbers,run_time=3),FadeIn(searchingFor))
        self.play(Create(arrowLeft),Create(arrowRight),Create(arrowMiddle))
        self.play(arrowLeft.animate.next_to(square6,DOWN,buff=0.5))
        self.play(arrowMiddle.animate.next_to(square8,DOWN,buff=0.5))
        squareRem1=Group(square1,num1,square2,num2,square3,num3,square4,num4,square5,num5)
        self.play(FadeOut(squareRem1,run_time=2))
        squareRem2 =Group(square6,num6,square7,num7,square8,num8,square9,num9,square10,num10,arrowLeft,arrowRight,arrowMiddle)
        self.play(squareRem2.animate.shift(LEFT*2.5))

        self.interactive_embed()