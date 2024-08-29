def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

radius_list = [5, 10, 15, "twenty", 25] 

if __name__ == "__main__":
    for r in radius_list:
        print(f"The area of a circle with radius {r} is {calculate_area(r):.2f}")
