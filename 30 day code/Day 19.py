Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Calculator implements AdvancedArithmetic{

    public int divisorSum(int n){
        int divisorSum=n;
        for(int i=1;i<n;i++)
        {
            if(n%i==0)
                divisorSum += i;
        }
        return divisorSum;
    }
} 
