# mygraphicsV1.py: Various graphics functions to
# augment Zelle's graphics.py

from graphics import *
from random import randint
# For tracing function calls:
trace = True

def RandColor():
  """Returns a random color string"""
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  color = color_rgb( r, g, b )
  return color

def MyRectangle( xcent, ycent, w2, h2 ):
    """Rectangle centered on (xcent,ycent), with 'radii' half-width w2 and half-height h2.
    Returns rectangle object."""
    # Construct p1 & p2
    # Construct p1 & p2, LL, UR
    p1 = Point( xcent-w2, ycent-h2 )
    p2 = Point( xcent+w2, ycent+h2 )
    rect = Rectangle( p1, p2 )
    return rect

def MyOval( xcent, ycent, w2, h2 ):
    """Oval centered on (xcent,ycent), with 'radii'
    half-width w2 and half-height h2.
    Returns oval object."""
    # Construct p1 & p2, LL, UR
    p1 = Point( xcent-w2, ycent-h2 )
    p2 = Point( xcent+w2, ycent+h2 )
    oval = Oval( p1, p2 )
    return oval

def IsInRect( p, rect ):
    """Is point p inside the rectangle?
       Both p and rect are graphics objects.
    """
    # Extract the pt coords:
    x,y = p.getX(),p.getY()

    # Extract the rect corners:
    p1 = rect.getP1()
    x1,y1 = p1.getX(),p1.getY()
    p2 = rect.getP2()
    x2,y2 = p2.getX(),p2.getY()

    # Inside the rect when between both x&y.
    # Make no assumption about p1 & p2, so need to 
    # check several between possibilities.
    if ((x1 <= x <= x2) or (x1 >= x >= x2)) and ((y1 <= y <= y2) or (y1 >= y >= y2)):
        if trace:
          print('IsInRect')
        return True
    else:
        return False

def IsInCirc( p, circ ):
    """Is point p inside the circle?
       Both p and circ are graphics objects.
    """
    # Extract the pt coords:
    x,y = p.getX(),p.getY()

    # Extract the circ data:
    r = circ.getRadius()
    pcent = circ.getCenter()
    xc,yc = pcent.getX(),pcent.getY()
    
    # Pythagorean Theorem:
    if (xc-x)**2 + (yc-y)**2 <= r*r:
        if trace:
            print('IsInCirc')
        return True
    else:
        return False
