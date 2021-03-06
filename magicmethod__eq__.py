class ComplexNumber:
    # TODO: write your code here
    def __init__(self, real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
    def __eq__(self,other):
        return  bool(self.real_part == other.real_part and self.imaginary_part == other.imaginary_part)
            

if __name__ == "__main__":
    import json
    input_args = list(json.loads(input()))

    complex_number1 = ComplexNumber(*input_args[0])
    complex_number2 = ComplexNumber(*input_args[1])

    is_complex_numbers_equal = complex_number1 == complex_number2

    print(is_complex_numbers_equal)
    '''
    [[1,2],[1,2]]
    
    True
    '''
