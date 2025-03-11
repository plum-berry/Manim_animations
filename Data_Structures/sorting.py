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
        elements = [2,5,3,6,8,9,1]
        indexes = [0,1,2,3,4,5,6]
        allElements = VGroup()
        for ele,idx in zip(elements,indexes):
            temp = makeArrayBox(idx,ele)
            allElements.add(temp)

        allElements.arrange(RIGHT,aligned_edge = LEFT,buff=0.5)
        self.play(FadeIn(allElements))

        for i in range(0,7):
            for j in range(0,6):
                if allElements[j][2].get_value() > allElements[j+1][2].get_value():
                    temp = allElements[j+1][2].get_value()
                    allElements[j+1][2].set_value(allElements[j][2].get_value())
                    allElements[j][2].set_value(temp)
        self.interactive_embed()