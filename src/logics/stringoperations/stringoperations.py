sachin_history=""""Tendulkar" redirects here. For other people with the same surname, see Tendulkar (surname).
Sachin Tendulkar
Sachin at Castrol Golden Spanner Awards.jpg
Tendulkar at a promotional event
Personal information
Sachin Ramesh Tendulkar AO BR (/ˌsʌtʃɪn tɛnˈduːlkər/ (listen); pronounced [sət͡ʃin t̪eːɳɖulkəɾ]; born 24 April 1973) is an Indian former international cricketer who captained the Indian national team. He is regarded as one of the greatest batsmen in the history of cricket.[4]
Tendulkar took up cricket at the age of eleven, made his Test match debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. In 2002, halfway through his career, Wisden ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[5] Later in his career, Tendulkar was part of the Indian team that won the 2011 Cricket World Cup, his first win in six World Cup appearances for India.[6] He had previously been named "Player of the Tournament" at the 2003 edition of the tournament."""

noOfCharacters=len(sachin_history);
print(f"No of characters in sachin history is--{noOfCharacters}")

splitWords=sachin_history.split()
print(splitWords)
print(len(splitWords))

testword="a b c a d a b e g"
testword_split=testword.split()
print(testword_split)
#iterate
a=0;
for splittedWords in testword_split:
    a=a+1
    print(f"Position of splitted words--{a}-{splittedWords}")
