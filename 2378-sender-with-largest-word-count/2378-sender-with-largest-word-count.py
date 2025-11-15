class Solution(object):
    def largestWordCount(self, messages, senders):
        freq = {}

        for i in range(len(messages)):
            msg = messages[i]
            snd = senders[i]

            word_count = len(msg.split(" "))
            freq[snd] = freq.get(snd,0) + word_count

        sorted_msg = sorted(freq.items(),key = lambda x: (x[1],x[0]),reverse = True)

        return sorted_msg[0][0]



       