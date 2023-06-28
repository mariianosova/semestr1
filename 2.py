class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        licensePlate = ''.join(filter(str.isalpha, licensePlate.lower())) 
        shortest = ""
        min_length = 16

        for word in words:
            current_word = word.lower()
            for symbol in licensePlate:
                if symbol not in current_word:
                    break
                current_word = current_word.replace(symbol, '', 1)
            else:
                if len(word) < min_length:
                    min_length = len(word)
                    shortest = word

        return shortest

solution = Solution()

licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
print(solution.shortestCompletingWord(licensePlate, words))

licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print(solution.shortestCompletingWord(licensePlate, words))

