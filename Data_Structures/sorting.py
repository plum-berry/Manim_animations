from manim import *
from manim.opengl import *

def makeArrayBox(index,element):
    result = VGroup()
    arrayIndex = Integer(index,font_size=40)
    arrayBox=Square(side_length=1,color=WHITE,fill_opacity=0)
    arrayElement = Integer(element)
    arrayElement.move_to(arrayBox.get_center())
    arrayIndex.next_to(arrayBox,UP,buff=0.1)
    result.add(arrayBox,arrayIndex,arrayElement)
    return result

# void BubbleSort(int a[], int size)
# {
#     int i, j,temp;
#     for ( i = 0 ; i < size ; i ++)
#     {
#         for (j = 0 ; j < size - 1 ; j++)
#         {
#             if (a[j] > a[j+1])
#             {
#                 temp = a[j];
#                 a[j] = a[j+1];
#                 a[j+1] = temp;
#             }
#         }
#     }
# }


class BubbleSort(Scene):
    def construct(self):
        text = Text("BubbleSort")
        self.play(Write(text),run_time=3)
        self.play(text.animate.shift(UP*3))

        elements = [2,5,3,6,8,9,1,0,-4]
        indexes = [0,1,2,3,4,5,6,7,8]
        allElements = VGroup()
        for ele,idx in zip(elements,indexes):
            temp = makeArrayBox(idx,ele)
            allElements.add(temp)

        allElements.arrange(RIGHT,aligned_edge = LEFT,buff=0.5)
        self.play(FadeIn(allElements))
        arrow1 = Arrow(start=UP,end=DOWN)
        arrow2 = Arrow(start=UP,end=DOWN)
        arrow1.next_to(allElements[0],UP,buff=0.1)
        arrow2.next_to(allElements[0],UP,buff=0.1)
        for i in range(0,9):
            for j in range(0,8):
                self.play(arrow1.animate.next_to(allElements[j],UP,buff=0.1),arrow2.animate.next_to(allElements[j+1],UP,buff=0.1))
                if allElements[j][2].get_value() > allElements[j+1][2].get_value():
                    self.play(Swap(allElements[j][2],allElements[j+1][2]))
                    temp = allElements[j][2]
                    allElements[j][2] = allElements[j+1][2]
                    allElements[j+1][2] = temp

        #self.interactive_embed()