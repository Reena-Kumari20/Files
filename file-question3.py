def main(banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] ):
    f=open("file-question3.txt","r")
    a=f.read()
    i=0
    while i<len(banks_list):
        print(banks_list[i])
        i=i+1
    f.close()
main()