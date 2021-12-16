import math;

def isIncreasing(lis):
    prevElem = lis[0];
    for i in range(1, len(lis)):
        currElem = lis[i];
        if currElem > prevElem:
            pass;
        else:
            return False;
    return True;

def NumConvert(lis):
    result = "";
    for elem in lis:
        result = result + str(elem);
    return int(result);

def BinConvert(binStr):
    """
    brainstorming
    first determine how many digits in binary number
    do a backwards iteration, adding 2^exponent to the sum if the curr element is "1"
    after each iteration, increment the exponent by 1
    return the sum
    """
    numDigits = len(binStr);
    pointer = numDigits - 1;
    currExponent = 0
    result = 0;
    while pointer >= 0:
        currElem = binStr[pointer];
        if currElem == "1":
            # print("adding",math.pow(2,currExponent),"to",result);
            result = result + math.pow(2,currExponent);
        pointer = pointer - 1;
        currExponent = currExponent + 1;
    return int(result);

def main():
    print("------------------- Question 1 ----------------");
    print("Function isIncreasing returns whether the list is strictly increasing");
    print("isIncreasing([4,5,6,7,8]) returns",isIncreasing([4,5,6,7,8]));
    print("isIncreasing([1,3,3,7,-5]) returns",isIncreasing([1,3,3,7,-5]));
    print("isIncreasing([9,8,7,6,5]) returns",isIncreasing([9,8,7,6,5]));
    print("isIncreasing([2,200,1421,9999,420142]) returns",isIncreasing([2,200,1421,9999,420142]));
    print("isIncreasing([45,20,65,80,91]) returns",isIncreasing([45,20,65,80,91]));
    print("------------------- Question 2 ----------------");
    print("Function NumConvert takes a int list with single digits and returns the combined number");
    print("NumConvert([4,5,6,7,8]) returns",NumConvert([4,5,6,7,8]));
    print("NumConvert([2,0,2,1]) returns",NumConvert([2,0,2,1]));
    print("NumConvert([4,2,5,9,1,0,1,7]) returns",NumConvert([4,2,5,9,1,0,1,7]));
    print("NumConvert([4,2,1]) returns",NumConvert([4,2,1]));
    print("NumConvert([6,7,1,2,5,9,3]) returns",NumConvert([6,7,1,2,5,9,3]));
    print("------------------- Question 3 ----------------");
    print("Function BinConvert takes in a string representing a binary number and returns its decimal form as an integer. (convert from binary to decimal)");
    print("BinConvert('1010100111') returns",BinConvert('1010100111'));
    print("BinConvert('101') returns",BinConvert('101'));
    print("BinConvert('10110011') returns",BinConvert('10110011'));
    print("BinConvert('1011') returns",BinConvert('1011'));
    print("BinConvert('110101') returns",BinConvert('110101'));

if __name__ == "__main__":
    main();
