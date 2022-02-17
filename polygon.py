from base64 import b16decode
import math
class Polygon:
    """ 
    A class to represent a polygon.
    Polygon is a finite set of vertices in the plane.
    The vertices are stored in a list, each element of the list is a pair of coordinates (x, y).
    attributes:
        vertices: a list of vertices
    methods:
        area: calculate the area of the polygon
        distance: calculate the distance between two points
        sides: get all sides of the polygon
        angles: get all angles of the polygon        
        perimeter: calculate the perimeter of the polygon
        is_valid: validate the polygon
        centroid: calculate the centroid of the polygon
    """
    # Constructor with vertices
    def __init__(self, vertices: list):
        """
        Constructor with vertices.
        vertices: a list of vertices each element of the list is a pair of coordinates (x, y)
        """
        self.vertices = vertices

    #7 Define the method to validate the polygon
    def is_valid(self) -> bool:
        """
        Validate the polygon.
        Returns:
            True if the polygon is valid
            False if the polygon is invalid
        """
        #if len(self.vertices) == 3:
            #if p1[2]==p2[1] and p2[2]==p3[1] and p3[3]==p1[1]
                #print(True)
        #elif len(self.vertices) == 4:
            #if p1[2]==p2[1] and p2[2]==p3[1] and p3[2]==p4[1] and p4[2]==p1[1]
                #print(True)
        #elif len(self.vertices) == 5:
            #if p1[2]==p2[1] and p2[2]==p3[1] and p3[2]==p4[1] and p4[2]==p5[1] and p5[2]==p1[1]
                #print(True)
        #else:
            #print(False)
    
    #4 Calculate the area of the polygon
    def area(self) -> float:
        """
        Calculate the area of the polygon.
        """
        if len(self.vertices) < 3:
            r=self.distance
            aylana=math.pi*(pow(r))
            return aylana
        elif len(self.vertices) == 3:
            a, b, c =self.sides
            
            s = self.perimeter / 2
            uchburchak = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return round(uchburchak, 2)
        elif len(self.vertices) == 4:
            a, b, c, d = self.sides
           
            s = self.perimeter / 2
            tortburchak = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d))
            return round(tortburchak, 2)
        elif len(self.vertices) == 5:
            a, b, c, d, e = self.sides
            
            s = self.perimeter / 2
            beshburchak = math.sqrt(s * (s - a) * (s - b) * (s - c) * (s - d) * (s - e))
            return round(beshburchak, 2)

    #1 Distance between two points
    def distance(self, p1: tuple, p2: tuple) -> float:
        """
        Calculate the distance between two points.
        Args:
            p1: a pair of coordinates (x, y)
            p2: a pair of coordinates (x, y)
        Returns:
            the distance between p1 and p2
        """
        x1,y1=p1
        x2,y2=p2
        return math.sqrt( pow(x2 - x1, 2) + pow(y2 - y1, 2))

    #2 Define the method to get all sides of the length of the polygon
    def sides(self) -> list:
        """
        Get all sides of the polygon.
        Returns:
            a list of all sides of the polygon
        """
        sides = [self.distance(self.vertices[-1], self.vertices[0])] + [self.distance(self.vertices[i], self.vertices[i+1]) for i in range(len(self.vertices)-1)]
        return sides
     
     #3 Define the method to calculate the perimeter of the polygon
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the polygon.
        Returns:
            the perimeter of the polygon
        """
        return (sum(self.sides()))

    #5 Define the method to calculate the angle between two sides
    def angles(self) -> list:
        """
        Calculate the angles of the polygon.
        Returns:
            a list of all angles of the polygon
        """
        pass
        
    # 6 Define the method to calculate the centroid of the polygon
    def centroid(self) -> tuple:
        """
        Calculate the centroid of the polygon.
        Returns:
            a pair of coordinates (x, y)
        """
        pass

vert = Polygon([(4,5), (1.5,2), (7,2), ])
print(vert.area())