class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Step 1: Find how many words can fit in the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])  # 1 space + word length
                j += 1

            line_words = words[i:j]
            num_words = j - i
            num_spaces = maxWidth - sum(len(word) for word in line_words)

            # Step 2: Construct the line
            if j == n or num_words == 1:
                # Case: Last line OR only one word -> left-aligned
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))  # pad right spaces
            else:
                # Case: fully justified line
                space_slots = num_words - 1
                even_space = num_spaces // space_slots
                extra_space = num_spaces % space_slots

                line = ""
                for k in range(space_slots):
                    line += line_words[k]
                    line += ' ' * (even_space + (1 if k < extra_space else 0))
                line += line_words[-1]  # Add the last word (no space after it)

            res.append(line)
            i = j  # Move to the next line

        return res
        