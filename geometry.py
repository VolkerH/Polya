from point import point
import math
#EPS = 1e-4;

def intersection(p1,p2,p3,p4):
	# Determine line equations
	# |A1 B1| |x|   |C1|
	# |A2 B2| |y| = |C2|
	A1 = p1.y - p2.y;
	B1 = p2.x - p1.x;
	C1 = A1*p1.x + B1*p1.y;
	A2 = p3.y - p4.y;
	B2 = p4.x - p3.x;
	C2 = A2*p3.x + B2*p3.y;
	# Solve for intersection
	# Parallel lines:
	if (A1*B2 == B1*A2):
		return null;
		
	# Inverse of matri'x':
	# | B2 -B1|
	# |-A2  A1|/D
	D = A1*B2 - B1*A2;
	x = (B2*C1 - B1*C2)/D;
	y = (A1*C2 - A2*C1)/D;
	return point( x,y );

# Calculates the circumcenter of the triangle with vertices p1, p2, p3
# Calculates the intersection of perpendicular bisectors
def circumcenter(p1, p2, p3):
	m1 = point( (p1.x+p2.x)/2, (p1.y+p2.y)/2 );
	m2 = point( (p3.x+p2.x)/2, (p3.y+p2.y)/2 );
	pv1 = point( (p1.y-p2.y), (p2.x-p1.x) );
	pv2 = point( (p3.y-p2.y), (p2.x-p3.x) );
	a = point( m1.x+pv1.x, m1.y+pv1.y );
	b = point( m2.x+pv2.x, m2.y+pv2.y );
	return intersection(m1,a,m2,b);

def dist2(p1,p2):
	return (p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y);
	
def dist(p1,p2):
	return math.sqrt(dist2(p1,p2));

# Calculates the circumradius of the triangle with vertices p1, p2, p3
# Formula from Wikipedia (http:#en.wikipedia.org/wiki/Circumscribed_circle)
def circumradius(p1, p2, p3):
	l1 = dist(p1,p2);
	l2 = dist(p1,p3);
	l3 = dist(p3,p2);
	return l1*l2*l3/math.sqrt((l1+l2+l3)*(-l1+l2+l3)*(l1-l2+l3)*(l1+l2-l3));

# Calculates the center of a circle tangent to a horizontal line y = yl
# that goes through p1 and p2
def tangentCircle(p1, p2, yl):
	# Can't have both points on the line
	#if (p1.x == p2.x and p2.x == xl) {
		#return null;
	#}
	# Also can't have one point on either side of the line
	#if ((p1.x < xl and p2.x > xl) or (p1.x > xl and p2.x < xl)) {
		#return null;
	#}
	# Calculate equation of perpendicular bisector
	pp1 = point( (p1.x+p2.x)/2, (p1.y+p2.y)/2 );
	pv = point( (p1.y-p2.y), (p2.x-p1.x) );
	pp2 = point( pp1.x+pv.x, pp1.y+pv.y );
	A = pp2.y - pp1.y;
	B = pp1.x - pp2.x;
	C = A*pp1.x + B*pp1.y;

	if (p1.y == yl):
		return intersection( pp1, pp2, p1, point(p1.x, p1.y-100) );
	if (p2.y == yl):
		return intersection( pp1, pp2, p2, point(p2.x, p2.y-100) );

	# Algebraically, the distance to the line is equal to the distance to p1.
	# (x-xl)^2 = (y-y1)^2 + (x-x1)^2
	# x = (y^2 - 2yy1 + y1^2 + x1^2 - xl^2)/(2*(x1-xl))
	# Plug into line equation and solve quadratic in y
	d = 2*(p1.y - yl);
	a = A/d;
	b = B - A*(2*p1.x)/d;
	c = A*(p1.y*p1.y + p1.x*p1.x - yl*yl)/d - C;
	if (A == 0):
	   x = C/B;
	   y = x*x - 2*x*p1.x + (p1.y*p1.y + p1.x*p1.x - yl*yl);
	   y /= d;
	else:
		x = math.sqrt(abs(b*b - 4*a*c)) - b;
		x /= 2*a;
		y = (C - B*x)/A;
		x1 = -math.sqrt(abs(b*b - 4*a*c)) - b;
		x1 /= 2*a;
		y1 = (C - B*x1)/A;
		if ((x1 < x and p1.y < p2.y) or (x1 > x and p1.y > p2.y)):
			y = y1;
			x = x1;
	return point( x, y );







"""
# Calculates the center of a circle tangent to a vertical line x = xl
# that goes through p1 and p2
def tangentCircle(p1, p2, xl):
	# Can't have both points on the line
	#if (p1.x == p2.x and p2.x == xl) {
		#return null;
	#}
	# Also can't have one point on either side of the line
	#if ((p1.x < xl and p2.x > xl) or (p1.x > xl and p2.x < xl)) {
		#return null;
	#}
	# Calculate equation of perpendicular bisector
	pp1 = point( (p1.x+p2.x)/2, (p1.y+p2.y)/2 );
	pv = point( (p1.y-p2.y), (p2.x-p1.x) );
	pp2 = point( pp1.x+pv.x, pp1.y+pv.y );
	A = pp1.y - pp2.y;
	B = pp2.x - pp1.x;
	C = A*pp1.x + B*pp1.y;

	if (p1.x == xl):
		return intersection( pp1, pp2, p1, point(p1.x-100, p1.y) );
	if (p2.x == xl):
		return intersection( pp1, pp2, p2, point(p2.x-100, p2.y) );

	# Algebraically, the distance to the line is equal to the distance to p1.
	# (x-xl)^2 = (y-y1)^2 + (x-x1)^2
	# x = (y^2 - 2yy1 + y1^2 + x1^2 - xl^2)/(2*(x1-xl))
	# Plug into line equation and solve quadratic in y
	d = 2*(p1.x - xl);
	a = A/d;
	b = B - A*(2*p1.y)/d;
	c = A*(p1.y*p1.y + p1.x*p1.x - xl*xl)/d - C;
	if (A == 0):
	   y = C/B;
	   x = y*y - 2*y*p1.y + (p1.y*p1.y + p1.x*p1.x - xl*xl);
	   x /= d;
	else:
		y = math.sqrt(abs(b*b - 4*a*c)) - b;
		y /= 2*a;
		x = (C - B*y)/A;
		y1 = -math.sqrt(abs(b*b - 4*a*c)) - b;
		y1 /= 2*a;
		x1 = (C - B*y1)/A;
		if ((y1 < y and p1.x < p2.x) or (y1 > y and p1.x > p2.x)):
			y = y1;
			x = x1;
	return point( x, y );
"""