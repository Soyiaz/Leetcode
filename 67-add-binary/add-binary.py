class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0

        a = a[::-1]
        b = b[::-1]
        max_len = max(len(a), len(b))

        for i in range(max_len):
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0

            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        return ''.join(result[::-1])
